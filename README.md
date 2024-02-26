# E-commerce Web App
## Overview
This is my submission of interview case. This repository contains the source code for an E-commerce web application built with Next.js, Flask and MySQL. The application is designed to provide a seamless shopping experience for users, integrating both front-end and back-end technologies.

## Features
* Auth (Login & Registration)
* Dashboard (For Admin/Operators & Users)
* Shopping Cart: Add and remove items from the shopping cart.
* Order Management: Track and manage your orders.
* Responsive Design: A mobile-friendly user interface for a consistent experience across devices.

## Tech Stack
* NextJS for frontend
* Flask Python for backend
* MySQL for database

# Get Started
## Prerequisites
* Node.js and npm installed.
* Python and pip installed.

## Installation
1. Clone this repository
2. Install dependencies:
   ### For frontend folder:
     - cd frontend
     - npm i
   ### For backend folder:
   1. Start with create env folder:
        - python -m virtualenv env
        (Must install this library. If you don't have it just install with "pip install virtualenv")
   2. Activate the environment mode:
        - cd /env/Scripts then ./activate, then go back to root "backend" folder.
        - If Linux/Mac:
            ```$ source env/bin/activate```
   3. Then install the dependencies from requirements.txt:
        - pip install -r requirements.txt
   4. Create the Database `interview_commerce` from your local database (MySQL Workbench or PHPMyAdmin).
   5. Do ```flask db init``` for initialize the database.
   6. ```flask db migrate``` for fill the tables from the models folder.
   7. And finally ```flask db upgrade``` for ready to use.
3. For Flask backend folder:
   ```python server.py```
4. For Nextjs frontend folder:
   ```npm run dev```
   
