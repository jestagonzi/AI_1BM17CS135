from collections import deque
from itertools import chain, tee
from math import sqrt
from random import choice

class Puzzle:
    HOLE = 0

    def __init__(self, board, hole_location=None, width=None):
        # Use a flattened representation of the board (if it isn't already)
        self.board = list(chain.from_iterable(board)) if hasattr(board[0], '__iter__') else board
        self.hole = hole_location if hole_location is not None else self.board.index(Puzzle.HOLE)
        self.width = width or int(sqrt(len(self.board)))

    @property
    def solved(self):
        
        return self.board == list(range(1, self.width * self.width)) + [Puzzle.HOLE]

    @property 
    def possible_moves(self):
        
        for dest in (self.hole - self.width, self.hole + self.width):
            if 0 <= dest < len(self.board):
                yield dest
        
        for dest in (self.hole - 1, self.hole + 1):
            if dest // self.width == self.hole // self.width:
                yield dest

    def move(self, destination):
        board = self.board[:]
        board[self.hole], board[destination] = board[destination], board[self.hole]
        return Puzzle(board, destination, self.width)

    def shuffle(self, moves=1000):
        p = self
        for _ in range(moves):
            p = p.move(choice(list(p.possible_moves)))
        return p

    @staticmethod
    def direction(a, b):
        if a is None:
            return None
        return {
                     -a.width: 'U',
            -1: 'L',    0: None,    +1: 'R',
                     +a.width: 'D',
        }[b.hole - a.hole]

    def __str__(self):
        return "\n".join(str(self.board[start : start + self.width])
                         for start in range(0, len(self.board), self.width))

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        h = 0
        for value, i in enumerate(self.board):
            h ^= value << i
        return h

class MoveSequence:
    def __init__(self, last, prev_holes=None):
        self.last = last
        self.prev_holes = prev_holes or []

    def branch(self, destination):
        return MoveSequence(self.last.move(destination),
                            self.prev_holes + [self.last.hole])

    def __iter__(self):
        states = [self.last]
        for hole in reversed(self.prev_holes):
            states.append(states[-1].move(hole))
        yield from reversed(states)

class Solver:
    def __init__(self, start):
        self.start = start

    def solve(self):
        queue = deque([MoveSequence(self.start)])
        seen  = set([self.start])
        if self.start.solved:
            return queue.pop()

        for seq in iter(queue.pop, None):
            for destination in seq.last.possible_moves:
                attempt = seq.branch(destination)
                if attempt.last not in seen:
                    seen.add(attempt.last)
                    queue.appendleft(attempt)
                    if attempt.last.solved:
                        return attempt


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

if __name__ == '__main__':
    board = [[1,2,3],
             [4,0,6],
             [7,5,8]]

    puzzle = Puzzle(board).shuffle()
    print(puzzle)
    move_seq = iter(Solver(puzzle).solve())
    for from_state, to_state in pairwise(move_seq):
        print()
        print(Puzzle.direction(from_state, to_state))
        print(to_state)
