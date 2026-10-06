from crewai.flow.flow import Flow, start, listen, and_

class BasicFlow(Flow):
    @start()
    def firstfn(self):
        print("Executing firstfn")
        self.state["message"] = "Avengers Assemble"
        # return "Avengers Assemble"
    
    @listen(firstfn)
    def secondfn(self):
        print("Executing secondfn")
        self.state["message"] += ", Avengers Akraman"
        # return "Avengers Akraman"

    @listen(and_(firstfn, secondfn))
    def logger(self):
        print("Logging message only after both the fns ran successfully")
        print("Message till now: ", self.state["message"])
    
flow = BasicFlow()
result = flow.kickoff()