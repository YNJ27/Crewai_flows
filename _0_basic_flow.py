from crewai.flow.flow import Flow, start, listen

class BasicFlow(Flow):
    @start()
    def firstfn(self):
        return "Hello"
    
    @listen(firstfn)
    def secondfn(self, string):
        return f"I got the string: {string}"
    
flow = BasicFlow()
result = flow.kickoff()

print("final result: ", result)
