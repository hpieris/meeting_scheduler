# architecture.py

from adk.workflow import Workflow
from adk.agent import Agent

class IntentParser(Agent):
    def run(self, state):
        print("🔍 Parsing intent...")
        state["intent"] = {"time": "3pm", "participants": ["Alex"], "topic": "Design Review"}
        return state

class AvailabilityChecker(Agent):
    def run(self, state):
        print("📅 Checking availability...")
        state["available"] = True
        return state

class Scheduler(Agent):
    def run(self, state):
        print("✅ Scheduling meeting...")
        state["status"] = f"Meeting scheduled with {state['intent']['participants'][0]} at {state['intent']['time']}"
        return state

def get_workflow():
    workflow = Workflow()
    workflow.add_agent("intent_parser", IntentParser())
    workflow.add_agent("availability_checker", AvailabilityChecker())
    workflow.add_agent("scheduler", Scheduler())

    workflow.set_start("intent_parser")
    workflow.add_edge("intent_parser", "availability_checker")
    workflow.add_edge("availability_checker", "scheduler")
    workflow.set_end("scheduler")

    return workflow

# Run the flow
if __name__ == "__main__":
    wf = get_workflow()
    result = wf.run({"user_input": "Schedule a design review with Alex at 3pm"})
    print("✅ Final Result:\n", result)
