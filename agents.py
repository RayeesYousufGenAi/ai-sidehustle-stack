from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

def create_hustle_crew(goal):
    """Creates a crew of agents to plan and launch an AI side hustle."""
    
    llm = ChatOpenAI(model="gpt-4o")

    # 1. The Trend Hunter
    hunter = Agent(
        role='Viral Trend Hunter',
        goal=f'Identify 3 highly profitable niches for {goal}',
        backstory='Expert in market analysis and finding gaps in the AI tools market.',
        llm=llm,
        verbose=True
    )

    # 2. The Copywriter
    writer = Agent(
        role='Viral Storyteller',
        goal='Create 5 high-converting social media hooks and a landing page pitch',
        backstory='Master of psychological marketing and writing viral content for X and LinkedIn.',
        llm=llm,
        verbose=True
    )

    # 3. The Strategist
    strategist = Agent(
        role='Launch Strategist',
        goal='Develop a 7-day launch plan for Product Hunt and Indie Hackers',
        backstory='Has launched dozens of top-ranking products on Product Hunt.',
        llm=llm,
        verbose=True
    )

    # Tasks
    t1 = Task(description=f"Analyze the current market for {goal} and find 3 winning niches.", agent=hunter, expected_output="A list of 3 specific niches with reasoning.")
    t2 = Task(description="Write 5 viral hooks and a main pitch for the top niche found.", agent=writer, expected_output="A marketing copy document.")
    t3 = Task(description="Provide a day-by-day launch plan for the first 7 days.", agent=strategist, expected_output="A tactical 7-day checklist.")

    crew = Crew(
        agents=[hunter, writer, strategist],
        tasks=[t1, t2, t3],
        process=Process.sequential
    )

    return crew.kickoff()
