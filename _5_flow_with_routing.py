from crewai.flow.flow import Flow, start, listen, router
from pydantic import BaseModel

class FlowState(BaseModel):
    boolean: bool = False


class BasicFlow(Flow[FlowState]):
    input: str = ""
    
    @start()
    def firstfn(self):
        self.input = input("Want to continue: yes/no\n")
        if self.input.lower() == "yes":
            self.state.boolean = True
        else:
            self.state.boolean = False
    
    @router(firstfn)
    def secondfn(self):
        if self.state.boolean:
            return "branch1"
        
        else:
            return "branch2"

    @listen("branch1")
    def branch1fn(self, message):
        print("Running branch 1")

    @listen("branch2")
    def branch2fn(self, message):
        print("Running branch 2")
    
flow = BasicFlow()
result = flow.kickoff()