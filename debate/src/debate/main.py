#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from debate.crew import Debate

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
   
    inputs = {
        'topic': '10 hottest Stocks to lookout for today',
        'current_day': str(datetime.now().date())
    }

    try:
        Debate().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


