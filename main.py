from dotenv import load_dotenv
from llama_index.core.tools import QueryEngineTool, ToolMetadata

from utils.engine_functions.log_engine import log_engine
from utils.engine_functions.pd_query_engine import population_query_engine
from utils.engine_functions.cmd_engine import cmd_engine
from utils.prompts import context

from llama_index.legacy.llms import OpenAI
from llama_index.legacy.agent import ReActAgent
"""
Top-level agent orchestrator that can create tasks, run each step in a task,
or run a task e2e. Stores state and keeps track of tasks
"""
import warnings
warnings.filterwarnings("ignore")


load_dotenv()
query_engine = population_query_engine()


tools = [
    log_engine,
    cmd_engine,
    QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name="population_data",
            description="This tool allow to have information's about the population in 2023 and it demographics",
        ),
    )
]

try:
    llm = OpenAI("gpt-3.5-turbo-0613")
    agent = ReActAgent.from_tools(tools=tools, llm=llm, verbose=True, context=context)

    while (prompt := input("> Insert you question (`q` to quit): ")) != "q":
        response = agent.query(prompt)
        print(response)
except Exception as e:
    print(f"Error in agent, error: \n{e}")