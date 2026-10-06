from crewai.flow.flow import Flow, start, listen

class BasicFlow(Flow):
    @start()
    def firstfn(self):
        print("Printing the initial state")
        print("state: ", self.state)
        self.state["message"] = "Jindagi Kaisi Hai Paheli Hay "
        self.state["counter"] = 0
    
    @listen(firstfn)
    def secondfn(self):
        print("Before second fn")
        print("message: ", self.state["message"])
        print("counter: ", self.state["counter"])
        self.state["message"] += "Kabhi toh hasae , kabhi yeh rulae"
        self.state["counter"] += 1
        
    
flow = BasicFlow()
result = flow.kickoff()

print("final state:")
print("message: ", flow.state["message"])
print("counter: ", flow.state["counter"])