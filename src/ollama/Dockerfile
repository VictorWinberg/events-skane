FROM ollama/ollama:latest

# Copy the run_ollama.sh script into the /tmp directory
COPY ./run_ollama.sh /tmp/run_ollama.sh

# Set the working directory
WORKDIR /tmp

# Make the script executable
RUN chmod +x run_ollama.sh

# Expose the port
EXPOSE 11434

# Use the script as the entrypoint
ENTRYPOINT ["/tmp/run_ollama.sh"]
