# Use a lightweight Python image
FROM python:3.11-slim

# Install traceroute
RUN apt-get update && apt-get install -y traceroute

# Set the working directory in the container
WORKDIR /usr/src/app


# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Create a non-privileged user
RUN useradd -m player

# Expose the port that FastAPI will run on
EXPOSE 8000

COPY ./app.py index.html flag.txt database.db .

RUN chmod 444 database.db

USER player
# Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]
