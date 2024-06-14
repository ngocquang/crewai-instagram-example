from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.search import SearchTools

# Uncomment the following line to use an example of a custom tool
# from instagram.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool


@CrewBase
class ContentPlanningCrew:
    """Facebook crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def content_planner(self) -> Agent:
        return Agent(config=self.agents_config["content_planner"], verbose=True)

    @agent
    def content_creator(self) -> Agent:
        return Agent(config=self.agents_config["content_creator"], verbose=True)

    @task
    def content_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config["content_planning"],
            agent=self.content_planner(),
        )

    @task
    def content_create_task(self) -> Task:
        return Task(
            config=self.tasks_config["content_create"],
            agent=self.content_creator(),
            allow_delegation=False,
        )


    @crew
    def crew(self) -> Crew:
        """Creates the ContentPlanning crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
