FROM python:3.9

# Set the working directory to /code
WORKDIR /code

# Copy requirements.txt into the container at /code
COPY ./requirements.txt /code/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of the code into the container at /code
COPY ./ /code

# Expose the port the app runs on
EXPOSE 80

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--reload-dir", "/code"]
