from fastapi import FastAPI
from llm_magic import llm_generate_prompt
import json

from w3b_scr4ap3r import rec_find

# MODEL = "qwen2:0.5b"
MODEL = "adrienbrault/nous-hermes2pro:Q5_K_M-json"

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/weather/")
def generate_prompt(country: str):
    user_query = f"What is the weather in {country}?"
    output = llm_generate_prompt(MODEL, user_query)
    return {"Message": output["response"]}

@app.get("/prompt/")
def get_prompt(query: str):
    output = llm_generate_prompt(MODEL, query)
    try:
        data = json.loads(output["response"])
        return data
    except:
        return output["response"]
