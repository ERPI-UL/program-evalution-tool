# Programm Evaluation Tool

This repository contains a web app that supports the evaluation of innovation program. It provides dashboards, list of indicators and form to collect data for each evaluation in the program. 
The aim of the tool is to evaluate pragram that are based on the triple/quadruple helix innovation model.

## Installation procedure
1. Start the entire service
'''sh
docker-compose up -d 
'''

2. Set up the authentification service
go to the appwrite admin interface

3. Modifiy the environment variable of the frond end

4. Restart the service in order to allow the front to connect to the auth system 
'''sh
docker-compose restart 
'''

## Structure
Front 
* Vite + vueJS

Back
* Appwrite
* Api Python (FastAPI) + ontology