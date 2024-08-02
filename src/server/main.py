from typing import Union
from fastapi import FastAPI
import ollama
from ollama import Client

MODEL = "qwen2:0.5b"
app = FastAPI()
# Why use the client, since we have this crazy networking going on
client = Client(host="http://ollama:11434")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/weather/")
def generate_prompt(country: str):
    user_query = f"What is the weather in {country}?"
    output = llm_generate_prompt(MODEL, user_query)
    return {"Message": output["response"]}


def llm_generate_prompt(model, query):
    print("Start generate response from LLM", flush=True)
    response = client.generate(model=model, prompt=query)
    response.pop("context")
    print(response, flush=True)
    return response
