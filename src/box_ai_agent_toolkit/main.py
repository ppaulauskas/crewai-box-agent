#!/usr/bin/env python
import sys
import warnings
import logging

from datetime import datetime
from box_ai_agent_toolkit.crew import BoxAiAgentToolkit
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.CRITICAL)

    topic = input("What topic would you like to explore?\n")

    inputs = {
        'topic': topic
    }
    
    try:
        result=BoxAiAgentToolkit().crew().kickoff(inputs=inputs)
        print("Here's what I found on your topic and the files I referenced in Box:\n\n")
        print(result)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")