# Food Delivery API (Python, Django & Django REST)

## Important Notes

```
1. Logically, since this is an online food delivery system it should be possible for a customer to order food from multiple restaurants at once, i saw it fit at this moment to only allow customer to order food from a single restaurant, meaning if a customer wanted to order from two different restaurants, they will have to place two separate orders.
```

## How To Run 

### To make it possible for the person testing the work to be able to test the work without limitations, have provided multiple ways to run the application.

```
1. Using Python Virtual Environment.
If you decide to test the application on your machine/laptop/computer directly, it is advisable that you create a python virtual environment where you can install all the required dependents and then run the app with easy. The steps are as follows;-
(execute this commands, in this order, assuming you are using a mac or linux os, if you are using windows please )

i. mkdir FoodDeliveryAPI
ii. cd FoodDeliveryAPI
iii. python3 -m venv restaurantenv
iv. source restaurantenv/bin/active
v. python manage.py runserver 8000
```