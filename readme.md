# Chatbot api

## Overview
Runs a FastAPI-based api for storing chat sessions for customers. Offers an endpoint for deleting customer data, and an endpoint where data can be harvested. Data is stored in an accompanying MongoDb container (note: no volume -- no persistence!).

## Get started
0. Install Docker for your system
1. In `root`, build the docker image like `docker build -t chatbotapi:latest -f docker/dockerfile .`
2. Run the stack with docker-compose like `docker-compose -f docker/docker-compose.yaml up -d`
