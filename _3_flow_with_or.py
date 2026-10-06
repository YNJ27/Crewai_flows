###Doesn't works as expected, the logger is only triggered by firstfn and not secondfn. 
### This is a bug reported by some users too

from crewai.flow.flow import Flow, start, listen, or_

class BasicFlow(Flow):
    @start()
    def firstfn(self):
        return "Avengers Assemble"
    
    @listen(firstfn)
    def secondfn(self):
        print("Executing secondfn")
        return "Avengers Akraman"

    @listen(or_(firstfn, secondfn))
    def logger(self, message):
        print("Logging message: ", message)
    
flow = BasicFlow()
result = flow.kickoff()
