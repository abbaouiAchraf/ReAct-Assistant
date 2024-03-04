import os
import pandas as pd
from utils.prompts import new_prompt, instruction_str
from llama_index.core.query_engine import PandasQueryEngine
"""
PandasQueryEngine: convert natural language to Pandas python code using LLMs.
"""


def population_query_engine() -> PandasQueryEngine:
    try:
        csv_path = os.path.join("data", "Population2023.csv")
        population_df = pd.read_csv(csv_path)
        population_qe = PandasQueryEngine(population_df, verbose=False, instruction_str=instruction_str)
        population_qe.update_prompts({"pandas_prompt": new_prompt})
        return population_qe
    except Exception as e:
        print(f"Issue related to pandas query engine, error: \n{e}")



