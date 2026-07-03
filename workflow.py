from langgraph.graph import StateGraph, START, END

from state import TravelState

from agents import (
    TravelResearchAgent,
    ItineraryPlannerAgent,
    TravelWriterAgent
)


research_agent = TravelResearchAgent()
planner_agent = ItineraryPlannerAgent()
writer_agent = TravelWriterAgent()


def research_node(state: TravelState):

    research = research_agent.run(
        state["destination"],
        state["duration"],
        state["budget"],
        state["interests"]
    )

    return {"research": research}


def planner_node(state: TravelState):

    itinerary = planner_agent.run(
        state["research"][:1200]
    )

    return {"itinerary": itinerary}


def writer_node(state: TravelState):

    guide = writer_agent.run(
        state["research"],
        state["itinerary"]
    )

    return {"guide": guide}

graph = StateGraph(TravelState)

graph.add_node("research", research_node)
graph.add_node("planner", planner_node)
graph.add_node("writer", writer_node)

graph.add_edge(START, "research")
graph.add_edge("research", "planner")
graph.add_edge("planner", "writer")
graph.add_edge("writer", END)

travel_graph = graph.compile()