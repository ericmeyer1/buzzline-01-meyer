# buzzline-01-meyer

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)

This project introduces streaming data.  
The Python language includes generators - we'll use this feature to generate some streaming **manufacturing log messages**.  
As the code runs, it will continuously update the log file.  
We'll use a consumer to monitor the log file and **alert us when errors or warnings are detected**.  

---

## Task 1. Set Up Your Machine & Sign up for GitHub

We practice professional Python. In each course that uses Python, we use a standard set of popular professional tools. 
This course uses advanced tools such as Apache Kafka that requires **Python 3.11**. 
You are encouraged to install and practice with multiple versions. 
If space is an issue, we only need Python 3.11 for this course. 

Follow instructions at [pro-analytics-01](https://github.com/denisecase/pro-analytics-01), **Part 1: Set Up Machine & Sign up for GitHub**.

**Setup is critical.** Follow all steps exactly and verify success before proceeding.  
Missing or incomplete setup steps can make the course impossible to complete.

## Task 2. Initialize a Project

Once your machine is ready, you'll copy this template repository into your own GitHub account  
and create your personal version of the project to run and explore. 
Name it **buzzline-01-yourname** (replace `yourname` with something unique to you).  

Follow instructions at [pro-analytics-01](https://github.com/denisecase/pro-analytics-01), **Part 2: Initialize a Project**.
This will get your project stored safely in the cloud - and ready for work on your machine. 

## Personalization of the Producer. Generate Streaming Data with Custom Producer (Terminal 1)

We created a custom producer that mimics **manufacturing logs**.  
It randomly simulates machine starts, stops, completions, and status alerts (OK, Warning, or Error).  

In VS Code, open a terminal.  
Use the commands below to activate `.venv`, and run the generator as a module.  

Windows PowerShell:

```shell```
.venv\Scripts\activate
py -m producers.basic_producer_meyer

## Personalization of the Consumer – Monitor Streaming Manufacturing Logs (Terminal 2)

We created a custom consumer that reads **manufacturing log messages** in real time.  
It monitors machine events and raises alerts for important statuses:  

- ✅ Completed job  
- ⚠️ Warning  
- 🚨 Error  

The consumer prints structured log entries to the terminal and can be used to simulate a **real-time factory dashboard**.

### Running the Consumer

**Windows PowerShell:**
```shell
.venv\Scripts\activate
py -m consumers.basic_consumer_meyer