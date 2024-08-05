# VadHänder?

## Set up project
**Start project:**
```sh
docker-compose up
```
**Stop project:** 
```sh
docker-compose down
```
### Running Ollama 🦙
When using docker it can be a bit tricky the first time since it need to pull the model for the first time. The process might get stuck in a loop giving you error message: `ollama exit code 0`.

The solution to the issue was to simply restart and remove the container & volume. Otherwise it pretty awesome! (If you are a MAC fag stop complaining, I am using Windows aka hard-mode and I get it to run)

## Test connection
Run in terminal: 

Fast API server:
```sh
curl --location "http://localhost:80/weather/?country=Sweden"
```
Ollama server:
```sh
curl --location "http://127.0.0.1:11434/api/generate" --header "Content-Type: application/json" --data-raw "{\"model\": \"qwen2:0.5b\", \"prompt\": \"Why is the sky blue?\", \"stream\": true}"
```
