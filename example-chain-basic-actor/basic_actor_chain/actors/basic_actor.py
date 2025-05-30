"""
© 2025 Stratio Big Data Inc., Sucursal en España. All rights reserved.

This software – including all its source code – contains proprietary
information of Stratio Big Data Inc., Sucursal en España and
may not be revealed, sold, transferred, modified, distributed or
otherwise made available, licensed or sublicensed to third parties;
nor reverse engineered, disassembled or decompiled, without express
written authorization from Stratio Big Data Inc., Sucursal en España.
"""

from typing import List, Type, Union

from genai_core.actors.base import ActorInput
from genai_core.actors.gateway_actor import GatewayActor
from genai_core.constants.constants import CHAIN_KEY_USER_REQUEST
from langchain_core.messages import BaseMessage
from langchain_core.prompts.chat import BaseMessagePromptTemplate
from pydantic import BaseModel

from ..constants.constants import (
    CHAIN_KEY_USER_NAME,
    SCENARIO_INPUT_MSG,
    USER_REQUEST_EXPLANATION,
)

# This block represents the instructions for the given actor.
# The context: the actor is a character from Alice in Wonderland, the Mad Hatter.
# The objective: the actor's objective is to answer the user's request by rephrasing it into a riddle.
# The riddle should be fun to read and rhyme.
# The task: the actor should analyze the user's request and reply with a riddle as the Mad Hatter character.
# We should define the expected input as a template and the expected output.

INSTRUCTIONS = f"""# CONTEXT #
You are the Mad Hatter character in Alice in Wonderland novel.

# OBJECTIVE #
Your objective is to answer the user's request as you where the Mad Hatter character in Alice in Wonderland novel.
Yous should rephrase the user's request into a riddle that answers the user's request.
The riddle should re on rhymes and be fun to read.
If the user is asking a question, the riddle should be another question that answers the user's question.

# SCENARIO #
{SCENARIO_INPUT_MSG}
{USER_REQUEST_EXPLANATION}

# TASK #
Task Objective: Analyze the USER REQUEST and reply with a riddle as the Mad Hatter character in Alice in Wonderland novel.

Follow the steps below to complete the task:    
1. **Analyze the USER REQUEST**:
	- Understand and break down the USER REQUEST: 
		* Request and sub-request broken down to simpler parts.
	- Summarize your analysis of the USER REQUEST into the 'user_request_explanation' field.

2. **Create a riddle that answers the USER REQUEST**:
	- Generate a valid riddle that accurately answers the USER REQUEST.
	- Write the generated riddle in the 'mad_hutter_riddle' field.
	- Write a short explanation of the riddle in the 'message' field. 
    - Your response should be in user's language and if the USER NAME is Alice the mad_hutter_riddle should be returned backword in user's language.

# EXPECTED OUTCOME #
The output must contain the following fields:
	* user_request_explanation: (up to 50 words).
	* mad_hutter_riddle: (up to 100 words).
	* message: (up to 100 words).
"""

INPUT_TEMPLATE = f"""# USER REQUEST START #
{{{CHAIN_KEY_USER_REQUEST}}}
# USER REQUEST END #

# USER NAME START #
{{{CHAIN_KEY_USER_NAME}}} 
# USER NAME END #

"""


class BasicExampleActorOutput(BaseModel):
    """
    This object represents the output of the actor.
    The actor should return a riddle that answers the user's request
    and an explanation of the user's request and a message explaining the riddle.

    Attributes:
        user_request_explanation (str): Explanation of the user's request.
        mad_hutter_riddle (str): The riddle generated by the Mad Hatter character.
        message (str): A short explanation of the riddle.
    """

    user_request_explanation: str
    mad_hutter_riddle: str
    message: str

    def __str__(self):
        """
        Returns the riddle as a string representation of the object.

        :return: The riddle generated by the Mad Hatter character.
        """
        return f"{self.mad_hutter_riddle}"


class BasicExampleActorInput(ActorInput):
    """
    This object represents the input of the actor.
    The actor should receive the user's request, and the user's name.

    Attributes:
        template (str): The input template for the actor.
        input_variables (list): List of input variables required by the actor.
    """

    template = INPUT_TEMPLATE
    input_variables = [CHAIN_KEY_USER_REQUEST, CHAIN_KEY_USER_NAME]


class BasicExampleActor(GatewayActor):
    """
    This object represents the actor.
    This object extends the GatewayActor class which requires to
    define the unique actor's key identifier, the input type, the output model,
    the instructions, the examples, and some post prompts processing.

    Attributes:
        actor_key (str): The key identifying the actor.
        temperature (int): The temperature setting for the actor.
    """

    actor_key = "basic_actor"
    temperature = 0

    def input_type(self) -> Type[ActorInput]:
        """
        Returns the input type for the actor.

        :return: The input type for the actor.
        """
        return BasicExampleActorInput

    def output_model(self) -> Union[Type[BaseModel], None]:
        """
        Returns the output model for the actor.

        :return: The output model for the actor.
        """
        return BasicExampleActorOutput

    def instructions(self) -> str:
        """
        Returns the instructions for the actor.

        :return: The instructions for the actor.
        """
        return INSTRUCTIONS

    def examples(self) -> List[BaseMessage]:
        """
        Returns a list of example messages for the actor.

        :return: A list of example messages.
        """
        return []

    def post_prompt(self) -> List[BaseMessagePromptTemplate]:
        """
        Returns a list of post-prompt templates for the actor.

        :return: A list of post-prompt templates.
        """
        return []
