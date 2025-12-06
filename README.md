# Data-Driven-Air-Pressure System (APS)-sensor-fault-detection
The Air Pressure System (APS) is a critical subsystem in heavy-duty commercial vehicles, responsible for generating pressurized air used for braking, gear shifting, and other pneumatic operations. Reliable APS performance is essential for vehicle safety, and failures can lead to costly repairs or operational downtime.

This project focuses on developing a binary classification model that determines whether a vehicle failure is caused by a specific component within the APS. The positive class represents failures directly linked to this APS component, while the negative class represents failures originating from other unrelated vehicle components.
The overarching goal is to support maintenance decision-making and reduce unnecessary repair expenses by accurately identifying APS-related faults.
### Solution Proposed
This project applies data-driven techniques to diagnose faults within the Air Pressure System (APS) of heavy-duty trucks. Since the APS provides compressed air for key functions such as braking and gear shifting, early detection of component-specific failures can significantly reduce maintenance costs and downtime.

A machine-learning classification model is developed to distinguish between:

Positive class: Failures caused by the targeted APS component

Negative class: Failures caused by components outside the APS

To minimize unnecessary repairs, the solution prioritizes reducing false APS predictions (false positives/false negatives), ensuring high reliability in identifying true APS-related issues. The final model aims to support predictive maintenance strategies and improve overall vehicle diagnostic accuracy.
## Tech Stack Used
1. Python 
2. FastAPI 
3. Machine learning algorithms
4. Docker
5. MongoDB

## Infrastructure Required.

1. AWS S3
2. AWS EC2
3. AWS ECR
4. Git Actions
5. Terraform

## How to run?
Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need AWS account to access the service like S3, ECR and EC2 instances.

## Data Collections
![image](https://user-images.githubusercontent.com/57321948/193536736-5ccff349-d1fb-486e-b920-02ad7974d089.png)


## Project Archietecture
![image](https://user-images.githubusercontent.com/57321948/193536768-ae704adc-32d9-4c6c-b234-79c152f756c5.png)


## Deployment Archietecture
![image](https://user-images.githubusercontent.com/57321948/193536973-4530fe7d-5509-4609-bfd2-cd702fc82423.png)


### Step 1: Clone the repository
```bash
git clone https://github.com/sethusaim/Sensor-Fault-Detection.git
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -n sensor-venv python=3.10 -y
```

```bash
conda activate sensor
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Export the environment variable
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

export MONGODB_URL="mongodb+srv://<username>:<password>@ineuron-ai-projects.7eh1w4s.mongodb.net/?retryWrites=true&w=majority"

```

### Step 5 - Run the application server
```bash
python app.py
```

### Step 6. Train application
```bash
http://localhost:8080/train

```

### Step 7. Prediction application
```bash
http://localhost:8080/predict

```

## Run locally

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image
```
docker build --build-arg AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> --build-arg AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> --build-arg AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION> --build-arg MONGODB_URL=<MONGODB_URL> . 

```

3. Run the Docker image
```
docker run -d -p 8080:8080 <IMAGE_NAME>
```

To run the project  first execute the below commmand.
MONGO DB URL: 
```
mongodb+srv://avnish:XglZZ9OkjjUw74pZ@ineuron-ai-projects.7eh1w4s.mongodb.net/admin?authSource=admin&replicaSet=atlas-okvkrd-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true
```
windows user

```
MONGO_DB_URL=mongodb+srv://avnish:XglZZ9OkjjUw74pZ@ineuron-ai-projects.7eh1w4s.mongodb.net/admin?authSource=admin&replicaSet=atlas-okvkrd-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true
```

Linux user

```
export MONGO_DB_URL=mongodb+srv://avnish:XglZZ9OkjjUw74pZ@ineuron-ai-projects.7eh1w4s.mongodb.net/admin?authSource=admin&replicaSet=atlas-okvkrd-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true
```

then run 
```
python main.py
```