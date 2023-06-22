# Food Delivery API (Python, Django & Django REST)

## Important Notes

```
1. Logically, since this is an online food delivery system it should be possible for a customer to order food from multiple restaurants at once, i saw it fit at this moment to only allow customer to order food from a single restaurant, meaning if a customer wanted to order from two different restaurants, they will have to place two separate orders.
```

## How To Run 

### To make it possible for the person testing the work to be able to test the work without limitations, have provided multiple ways to run the application.

### 1. Using Python Virtual Environment

If you decide to test the application on your machine/laptop/computer directly, 
it is advisable that you create a python virtual environment where you can install 
all the required dependents and then run the app with easy. The steps are as follows;-
(execute this commands, in this order, assuming you are using a mac or linux os, 
if you are using windows please refer to 
https://medium.com/co-learning-lounge/create-virtual-environment-python-windows-2021-d947c3a3ca78)
```
mkdir FoodDeliveryAPI
cd FoodDeliveryAPI
python3 -m venv restaurantenv
git clone https://github.com/Paulndambo/Food-Delivery-API.git
pip install -r requirements.txt
source restaurantenv/bin/active
python manage.py runserver 8000
```
### 2. Using Docker
#### 2.1 Building the Docker Image Locally
If you prefer to test the application using docker, follow the following steps;-
```
mkdir FoodDeliveryAPI
cd FoodDeliveryAPI
git clone https://github.com/Paulndambo/Food-Delivery-API.git
docker build -it food-delivery-backend:lastest .
docker run -p 8000:8000 food-delivery-backend
```
#### 2.2 Using The Docker Image Published On Docker Hub Already
```
docker run -p 8000:8000 40781998/food-delivery-backend:latest
```
### 3. Using Kubernetes
#### 3.1 Using Kubernetes (Builing the Images Locally)

If you prefer to test the application on kubernetes, follow the following steps;-
(This section assumes that you have all the requirements for running containerized applications on kubernetes)
(go into k8s/deployment.yaml, update line 16, add your docker username, 
for clarity you refer to k8s/paul-deployment.yaml file)
```
mkdir FoodDeliveryAPI
cd FoodDeliveryAPI
git clone https://github.com/Paulndambo/Food-Delivery-API.git
docker build -it <your docker username>/food-delivery-backend:lastest .
docker push <your docker username>/food-delivery-backend:lastest 
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```
#### 3.2 Using Kubernetes (Deploying Existing Images)
```
mkdir FoodDeliveryAPI
cd FoodDeliveryAPI
kubectl apply -f k8s/paul-deployment.yaml
kubectl apply -f k8s/service.yaml
```