from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool

@CrewBase
class Debate():
    

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], # type: ignore[index]
            verbose=True
        )

    @task
    def nyse_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['nyse_research_task'], # type: ignore[index]
            output_file='output/nyse_research_task.md'
        )
    
    @task
    def nasdaq_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['nasdaq_research_task'], # type: ignore[index]
            output_file='output/nasdaq_research_task.md'
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], # type: ignore[index]
            context=[self.nyse_research_task(), self.nasdaq_research_task()], # type: ignore[list-item]
            output_file='output/report.md'
        )

    @crew
    def crew(self) -> Crew:
      
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True           
        )
