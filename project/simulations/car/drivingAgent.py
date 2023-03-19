#!/usr/bin/env python

class DrivingAgent:
    
    def __init__(self, **kwargs):
        self.name = kwargs['name']

    def main():  
        agent = DrivingAgent(name="Toyota")
        print("The agent is driving")
            
    if __name__ == "main":
        main()
    
DrivingAgent.main()