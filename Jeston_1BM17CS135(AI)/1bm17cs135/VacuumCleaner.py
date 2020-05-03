import random

class Environment(object):
    def __init__(self):
        self.locationCondition = {'A': '0', 'B': '0'}

        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)


class SimpleReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        print (Environment.locationCondition)
        Score = 0
        vacuumLocation = random.randint(0, 1)
        if vacuumLocation == 0:
            print ("Vacuum is randomly placed at Location A.")
            if Environment.locationCondition['A'] == 1:
                print ("Location A is Dirty.")
                Environment.locationCondition['A'] = 0;
                Score += 1
                print ("Location A has been Cleaned.")
                print ("Moving to Location B...")
                Score -= 1
                if Environment.locationCondition['B'] == 1:
                    print ("Location B is Dirty.")
                    # suck and mark clean
                    Environment.locationCondition['B'] = 0;
                    Score += 1
                    print ("Location B has been Cleaned.")
            else:
                # move to B
                Score -= 1
                print ("Moving to Location B...")
                # if B is Dirty
                if Environment.locationCondition['B'] == 1:
                    print ("Location B is Dirty.")
                    # suck and mark clean
                    Environment.locationCondition['B'] = 0;
                    Score += 1
                    print ("Location B has been Cleaned.")

        elif vacuumLocation == 1:
            print ("Vacuum cleaner randomly placed at Location B.")
            if Environment.locationCondition['B'] == 1:
                print ("Location B is Dirty.")
                Environment.locationCondition['B'] = 0;
                Score += 1
                print ("Location B has been Cleaned.")
                Score -= 1
                print ("Moving to Location A...")
                if Environment.locationCondition['A'] == 1:
                    print ("Location A is Dirty.")
                    Environment.locationCondition['A'] = 0;
                    Score += 1
                    print ("Location A has been Cleaned.")
            else:
                print ("Moving to Location A...")
                Score -= 1
                if Environment.locationCondition['A'] == 1:
                    print ("Location A is Dirty.")
                    Environment.locationCondition['A'] = 0;
                    Score += 1
                    print ("Location A has been Cleaned.")
        print (Environment.locationCondition)
        print ("Performance Measurement: " + str(Score))


theEnvironment = Environment()
theVacuum = SimpleReflexVacuumAgent(theEnvironment)
