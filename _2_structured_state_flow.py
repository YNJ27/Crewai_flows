from crewai.flow.flow import Flow, start, listen
from pydantic import BaseModel

class FlowState(BaseModel):
    message: str = ""
    counter: int = 0

class BasicFlow(Flow[FlowState]):
    @start()
    def firstfn(self):
        print("Printing the initial state")
        print("state: ", self.state)
        self.state.message += "Kisiki Muskurahto pe ho nisad, Kisika dard le sake toh le udhar, "
        self.state.counter += 1
    
    @listen(firstfn)
    def secondfn(self):
        print("Before second fn")
        print("message: ", self.state.message)
        print("counter: ", self.state.counter)
        self.state.message += "Kiske vaaste tumhare dilme ho pyaar. jina isika naam hai"
        self.state.counter += 1
        
    
flow = BasicFlow()
result = flow.kickoff()

print("final state:")
print("message: ", flow.state.message)
print("counter: ", flow.state.counter)