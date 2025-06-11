# BoxAiAgentToolkit Crew

Welcome to the BoxAiAgentToolkit Crew project, powered by [crewAI](https://crewai.com). This project is an example of setting up a Box Agent in CrewAI to enrich your insights by finding relevant items in a Box Account and utilizing Box AI to extract insights in those documents.

## Installation

Ensure you have Python >=3.11 <3.13 installed on your system. 

If you do not have CrewAI installed, we should do that first:

```bash
pip install crewai
```

Next, navigate to your project directory and lock and install the dependencies:

```bash
crewai install
```
### Environment Setup

This project uses OpenAI, so you will need to generate an API key through their developer site.

- Add your `OPENAI_API_KEY` into the `.env` file
- Specify the OpenAI `MODEL` in the `.env` file (ex: gpt-4o)

Additionally, to connect to Box, we are going to be using a Client Credential Grant application. You can read through the [steps to set up a Client Credential App](https://developer.box.com/guides/authentication/client-credentials/client-credentials-setup/) in our documentation.

Once you have the app set up, modify the `.env` file

- `BOX_CLIENT_ID` is the client id for your application 
- `BOX_CLIENT_SECRET` is the client secret that you obtain from your application 
- `BOX_SUBJECT_TYPE` we'll use `user`. Make sure that the user id you are passing in has access to relevant content 
- `BOX_SUBJECT_ID` is the numeric id of the Box user you want to make API calls for.

You can then customize the behavior of the Box agent or add additional agents to your crew:

- Modify `src/box_ai_agent_toolkit/config/agents.yaml` to define your agents
- Modify `src/box_ai_agent_toolkit/config/tasks.yaml` to define your tasks
- Modify `src/box_ai_agent_toolkit/crew.py` to add your own logic, tools and specific args
- Modify `src/box_ai_agent_toolkit/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the box_ai_agent_toolkit Crew, assembling the agents and assigning them tasks as defined in your configuration.

It will ask you for an input on what topic you are looking the Box agent to research, and will output a relevant summary.

Currently, the agent is set to `verbose=True` in this example, so you can see the steps that the agent is going through in the output. If you only want the final output, modify the `@crew verbose` parameter in `src/box_ai_agent_toolkit/crew.py`

## Understanding Your Crew

The box_ai_agent_toolkit Crew is an example of utilizing a Box agent as a quickstart. You can add additional agents to the Crew to take the information that Box agent extracts to do further analysis. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

