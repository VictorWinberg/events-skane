#!/bin/bash

echo "Starting Ollama server..."
ollama serve &
SERVER_PID=$!

echo "Waiting for Ollama server to start..."
while ! cat < /dev/null > /dev/tcp/localhost/11434; do
  sleep 1
done

ollama pull qwen2:0.5b

echo "Waiting for the model to be downloaded..."
while ! ollama list | grep -q 'qwen2:0.5b'; do
  sleep 1
done

echo "Ollama server is ready!"
touch /tmp/ollama_ready

echo "Keeping the Ollama server running..."
while kill -0 "$SERVER_PID" 2>/dev/null; do
    sleep 10
done