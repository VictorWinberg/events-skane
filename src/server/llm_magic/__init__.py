from ollama import Client

# Why use the client, since we have this crazy networking going on
client = Client(host="http://ollama:11434")

def llm_generate_prompt(model, query):
    print("Start generate response from LLM", flush=True)
    response = client.generate(model=model, prompt=query)
    response.pop("context")
    print(response, flush=True)
    return response
