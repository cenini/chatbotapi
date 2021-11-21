# Chatbot api

## Overview
Runs a FastAPI-based api for storing chat sessions for customers. Offers an endpoint for deleting customer data, and an endpoint where data can be harvested. Data is stored in an accompanying MongoDb container (note: no volume -- no persistence!).

## Get started
0. Install Docker for your system
1. In `root`, build the docker image like `docker build -t chatbotapi:latest -f docker/dockerfile .`
2. Run the stack with docker-compose like `docker-compose -f docker/docker-compose.yaml up -d`
3. Browse to `localhost:8000/docs` (or change the port if you have chosen a different port for the API) for the Swagger docs.

## Run tests
0. Set up your environment by installing the `requirements.txt`.
1. Run `docker-compose -f docker/docker-compose-tests.yaml up -d`
2. Run the desired tests in your unittest runner.