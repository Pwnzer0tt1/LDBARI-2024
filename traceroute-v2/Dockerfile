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

# Switch to the non-privileged user
USER player

# Expose the port that FastAPI will run on
EXPOSE 8005

COPY ./app.py index.html flag.txt .

# Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8005"]
