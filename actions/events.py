import sys
from st2common.runners.base_action import Action

class MyAction(Action):
    def run(self, a):
        for num in range(0,a):
            for j in range(0,num+1):
                print("* "),
            print("\r")
        return(True,a)