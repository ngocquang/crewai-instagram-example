# Instagram Crew

Welcome to the Instagram Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:

```bash
poetry lock
```

```bash
poetry install
```

```bash
python3 -m venv myenv
source myenv/bin/activate # MacOS
pip3 install -r requirements.txt

streamlit run src/post_social/streamlit_app.py

python3 src/financial_analyst/main.py

python3 src/facebook/main.py
streamlit run src/facebook/streamlit_app.py


python3 src/content_planning/main.py
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/instagram/config/agents.yaml` to define your agents
- Modify `src/instagram/config/tasks.yaml` to define your tasks
- Modify `src/instagram/crew.py` to add your own logic, tools and specific args
- Modify `src/instagram/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
poetry run instagram
```

This command initializes the instagram Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folser

## Understanding Your Crew

The instagram Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Instagram Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Joing our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat wtih our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

## Example

Pusoy ZingPlay Philippines is a popular online card game that brings the traditional Filipino game of Pusoy to the digital world. This game, also known as Chinese Poker, allows players to experience the excitement and strategy of Pusoy on their mobile devices. The game is designed with vibrant graphics and an intuitive user interface, making it accessible and enjoyable for both seasoned players and beginners.

In Pusoy ZingPlay, players compete against each other to form the best possible three poker hands out of the 13 cards dealt to them. The objective is to beat the other players' hands and accumulate points to climb the leaderboards. The game offers various modes, including practice sessions for newcomers, competitive matches for seasoned players, and tournaments with exciting rewards.

Pusoy ZingPlay also features social elements, allowing players to connect with friends, join clubs, and participate in club events. The game's chat and emoji functions enhance the social experience, making each match more interactive and fun. Regular updates and special events keep the gameplay fresh and engaging, offering new challenges and rewards.

Whether you're looking to sharpen your Pusoy skills or simply enjoy a fun and strategic card game, Pusoy ZingPlay Philippines provides a comprehensive and entertaining platform to do so.
