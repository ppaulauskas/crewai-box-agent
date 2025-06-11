from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from box_ai_agent_toolkit.tools.custom_tool import BoxSearch, BoxAIFile

@CrewBase
class BoxAiAgentToolkit():

    agents: List[BaseAgent]
    tasks: List[Task]

    search_tool = BoxSearch()
    box_ai_file_ask_tool = BoxAIFile()

    @agent
    def box_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['box_expert'],
            verbose=False,
            tools=[self.search_tool, self.box_ai_file_ask_tool],
        )

    @task
    def box_expert_task(self) -> Task:
        return Task(
            config=self.tasks_config['box_expert_task'],
        )

    @crew
    def crew(self) -> Crew:

        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )
