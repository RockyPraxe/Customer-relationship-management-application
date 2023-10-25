# CRM Application

![am I responsive screenshot](static/)

## Customer relationship management application
> A CRM (Customer Relationship Management) application is a software solution that enables businesses to effectively manage and optimize their interactions with customers and potential clients. The primary goal of a CRM system is to centralize and streamline customer-related information, enhance communication, and improve overall customer satisfaction.

## **[Live site](https://customer-r-m-app-8abc1380955d.herokuapp.com/)**

---

## **[Repository](https://github.com/RockyPraxe/Customer-relationship-management-application)**

---

## Table of contents
<a name="contents">Back to Top</a>
 1. [ UX ](#ux)
 2. [Agile Development](#agile)
 3. [ Features ](#features)  
 4. [ Features Left to Implement ](#left)  
 5. [ Technology used ](#tech) 
 6. [ Testing ](#testing)  
 7. [ Bugs ](#bugs)  
 8. [ Deployment](#deployment)
 9. [ Credits](#credits)
 10. [ Content](#content)  
 11. [ Acknowledgements](#acknowledgements)  

## UX

<a name="ux"></a>
#### Pre-project Planning

> Database Structure

![Lucid Diagram](static/)

- When I decided on my initial concept of CRM Application I knew I needed to understand what type of data I would need to store and the relationships between them.
- I created the above diagram on lucidchart to help guide me.


### Database Schema
#### Customer Model

| id | Field |
|--|--|
| Customer_id | PK  |
|name |CharField|
|phone|CharField|
|email|EmailField|
|date_created|DateField|

---

#### Product Model

| id | Field |
|--|--|
| Product_id | PK  |
|name |CharField|
|price|FloatField|
|category|CharField|
|description|CharField|
|date_created|DateField|

---

#### Order Model

| id | Field |
|--|--|
| Order_id | PK  |
|date_created|DateField|
|status |CharField|
|note|FloatField|
|customer_id|FK|
|product_tags_id|FK|

---

#### Product_tags Model

| id | Field |
|--|--|
| Product_tags | PK  |
|product_id|FK|
|tag_id |FK|

---

#### Tag Model

| id | Field |
|--|--|
|Tag_id |PK |
|name|CharField|

# UX design

## Overview

CRM Application is a Fictional software solution that enables businesses to effectively manage their interactions with customers.
The primary goal of a CRM system is to centralize and streamline customer-related information, enhance communication, and improve overall customer satisfaction and also the company's business goals.
It should be taken into account that this website has implemented only basic CRUD functionality. The customer can only view the order and change his personal data. Only the admin can create, change, filter or delete an order.


### Design
Once the project was chosen I decided that I wanted this website to be modern, minimalistic in it's appearance to use base colors of olive green and its shades and dark where possible.
I only deviate from this where it helps user experience in regards to buttons, links or feedback.

### Site User

- Customer: Someone who ordered products from the company and wants to have an overview of the order.
- Admin: A person who has access to all system functions, only admin can create, change, filter or delete an order.
- Marketing Professionals: Marketing professionals can benefit from the CRM's marketing automation features, enabling them to run targeted marketing campaigns, analyze customer data, and engage with leads and customers    effectively.
- Business Owners and Managers: Business owners and managers can use the CRM application to enhance customer relationships, streamline sales processes, and improve decision-making by accessing valuable customer data.

### Goals for the website
- Improve Customer Relationships: The primary goal of the CRM application is to help businesses strengthen their customer relationships. This includes providing tools and insights to personalize interactions, leading to higher customer satisfaction and loyalty.
- Streamline Sales and Lead Management: One of the key goals is to streamline the sales process, making it more efficient and effective. This includes managing leads, tracking sales opportunities, and ultimately increasing revenue.
- Enhance Marketing Effectiveness: The CRM system aims to improve marketing efforts by automating campaigns, segmenting customer lists, and providing data-driven insights. The goal is to boost the return on investment (ROI) for marketing activities.
  
## Wireframes

###  Wireframes
> Home Page

![Home page balsamic](static/)

My goal for this project was to create a simple sleek website that allowed the admin create, change, filter or delete an order and the customer can see his profile with the possibility of changing the data and also see what and when he ordered and the status of his order.

---

![Responsive1](static/)

---

![Responsive1](static/)

---

![Responsive1](static/)

---

![Responsive1](static/)

---

![Responsive1](static/)

## Agile Development

<a name="agile"></a>

### Agile Overview

This project was started alongside a GitHub Projects Page to track and manage the expected workload ahead.
The aim was to set out my expected workload, list the epics and then break them down into user stories to work towards and ultimately finish the site in good time.

To see Kanban please click [here](https://github.com/users/RockyPraxe/projects/3).

At the initial stages I decided on 2 epics and 10 user stories. When I started working on user stories and epics I moved them from **todo** to **in progress**, when I finished them I moved them from **in progress** to **done**

#### User stories

#####  Completed User Stories

To view any of the expanded details of the user stories please click on a user story below to be taken to the Kanban project.
If the specific user story does not auto pop up then please click on it from the project page and you will see the details and comments.

 1. [USER STORY: Create Superuser ](https://github.com/RockyPraxe/Customer-relationship-management-application/issues/10)
 2. [USER STORY: Admin Order Management](https://github.com/RockyPraxe/Customer-relationship-management-application/issues/5)
 3. [USER STORY: Admin Full Access](https://github.com/RockyPraxe/Customer-relationship-management-application/issues/4)
 4. [USER STORY: Admin Customer Management](https://github.com/RockyPraxe/Customer-relationship-management-application/issues/6)
 5. [USER STORY: Order Creation](https://github.com/RockyPraxe/Customer-relationship-management-application/issues/8)
 6. [USER STORY: Order Management](https://github.com/RockyPraxe/Customer-relationship-management-application/issues/9)
 7. [USER STORY:Settings](https://github.com/RockyPraxe/Customer-relationship-management-application/issues/7)
 8. [USER STORY: User Registration](https://github.com/RockyPraxe/Customer-relationship-management-application/issues/1)
 9. [USER STORY: User Login](https://github.com/RockyPraxe/Customer-relationship-management-application/issues/2)
 10. [USER STORY: User Logout](https://github.com/RockyPraxe/Customer-relationship-management-application/issues/3)

[Back to Top of page](#contents)

---

## Features

<a name="features"></a>

#### User based Features Implemented:

- **Users/Admin can** create an customer or user in admin panel (**Create**)
- **Users/Admin can** log into their account
- **Users/Admin can** log out of their account
- **Users/Admin can** create the order for the customer
- **Users/Admin can** update the order for the cutomer
- **Users/Admin can** update the customer's personal data in the admin panel
- **Users/Admin can** delete the customer's order
- **Users/Admin can** filter the customer orders
- **Users/Admin can** see the product page
- **Users/Admin can** see the page with customers and their orders
- **Users/Admin can** click on social media links in the footer
- **Users/Admin can** see the status of the order

---

- **Users/Customers can** create an account (**Create**)
- **Users/Customers can** log into their account
- **Users/Customers can** log out of their account
- **Users/Customers can** see the status of the order
- **Users/Customers can** change personal data
- **Users/Customers can** click on social media links in the footer

#### Account restrictions:

- **Users/Customers cannot** create the order
- **Users/Customers cannot** update the order
- **Users/Customers cannot** delete the order
- **Users/Customers cannot** filter the orders
- **Users/Customers cannot** see the product page
- **Users/Customers cannot** see the page with all the customers and their orders

#### Website features:

##### Dynamic creation, editing, filtering and deletion of orders
- The website dynamically displays orders that were updated on the back-end and displayed on the front-end depending on which product the user selects.
– The website dynamically displays the orders that were created on the back-end and displayed on the front-end.
– The website filters dynamically the orders that were created on the back-end and displayed on the front-end.
– We can delete the order on the website and it will be dynamically updated.

##### Registration system
- The customer can register on the website
- The customer can log in to the website
- The customer can log out of the website


### dashboard.html

#### Desktop

> Desktop Navigation

---

> Home Page

---

![Home page](static/)

---

> Customer Page

---

![Customer page](static/)

---

>  Products Page

---

![Products page](static/)

---

>  Order Page

---

![Order page](static/)

---

>  Update Order Page

---

![Update order page](static/)

---

>  Delete Order Page

---

![Delete order page](static/)

---

> User Page

---

![User page](static/)

---

> User Settings Page

---

![User settings page](static/)

---

> Login Page

---

![Login page](static/)

---
 
>  Register Page

---

![Registration page](static/)

---

>  Footer 

---

![Footer](static/)

---

[Back to Top of page](#contents)

---

<a name="left"></a>
## Features left to Implement 

- Add the possibility for the customer to reset or change the password
- Add the option for the customer to upload a profile photo
- Add an e-mail notification for any changes associated with a change in personal data or an order
- Add images and a more detailed description to the products

[Back to Top of page](#contents)

---

<a name="tech"></a>
##  Technology Used

### Html

 - Used to structure my webpages and the base templating language

### CSS

 - Custom CSS was written on large chunks of this site to make it as close to the wireframes as I felt it needed to be.

### JavaScript

 -  Used for registration page.

### Python

 -  Used for the logic in this project.

### Django

 -  Framework used to build this project. Provides a ready installed admin panel and includes many helper template tags that make writing code quick and efficient.

### Font Awesome

 -  Icon library used for the profile and admin panel section.

### Bootstrap 
 - Used as the base front end framework to work alongside Django

### Jinja Templating with Django
 - Used to render logic within html documents and make the website more dynamic.

### GitHub
 - Used to store the code for this project & for the projects Kanban board used to complete it.

### Heroku
- Used to host and deploy this project

### Heroku PostgreSQL
-Heroku PostgreSQL was used as the database for this project during development and in production.

### Cloudinary
- Used to host the static files for this project including user profile images.

### Git
- Used for version control throughout the project and to ensure a good clean record of work done was maintained.

[Back to Top of page](#contents)

---

<a name="testing"></a>
## Testing

### Admin for testing purposes

>I created a test_admin for the evaluator of this project so that he could try out all the functionalities
 User name : TestAdmin
 Password : tester100

### Testing Phase

#### Manual Testing

> Each user story was manually tested in line with intended functionality on both desktop & mobile.
> As this project was driven by my own User Stories I  felt manual testing was applicable on all logic code.


>If the intended outcome completes then this will be flagged as pass. If it does not then this is a fail.


#### Account Registration Tests
| Test |Result  |
|--|--|
| User can create account | Pass |
| User can log into account| Pass|
|User can log out of account|Pass|

---

#### Account Security Tests

| Test |Result  |
|--|--|
|Non logged in user can make nothing | Pass |
|Non logged in user cannot access profile page| Pass|
|Non superuser cannot access admin panel|Pass|

--- 

#### Profile Tests

| Test |Result  |
|--|--|
|User can edit their user name from the profile page | Pass |
|User can edit / add a phone number to their account| Pass|
|User can add / edit their email address|Pass|

---

#### Admin Tests

| Test |Result  |
|--|--|
|Admin can add products |Pass|
|Admin can create the order|Pass|
|Admin can create the order|Pass|
|Admin can update the order|Pass|
|Items they display correctly on front-end when updated / added|Pass|

---

### User Tests

> Creating user
![Creating user](static/)
---
> Wrong password message
![Wrong password message](static/)
---
> Account created
![Account created](static/)
---
> User login
![User login](static/)
---
> Updating user information
![Updating user](static/)
---
> Personal info updated in admin view
![Personal info](static/)
---
> Creating new order in admin view
![Creating user](static/)
---
> Order confirmed
![Order confirmed](static/)
---
> Update the order
![Creating user](static/)
---
> Update confirm
![Update confirm](static/)
---
> Deletion of the order
![Order delete](static/)
---


## Google Lighthouse Testing

### Desktop
> dashboard.html

![Google Lighthouse Desktop](static/)


### Mobile
> dashboard.html

![Google Lighthouse Mobile](static/)

## HTML W3 Validation

### base.html


![W3 Validation checker](static/)
#### Result: No Errors

### CSS Validation


![w3 Jigsaw CSS checker](static/)
#### Result: Pass - No Errors

[Back to Top of page](#contents)

---

<a name="deployment"></a>
## Deployment

> I have broken up the deployment into two sections as it is quite extensive and can be hard to follow.

To deploy the project through Heroku I followed these steps:

- Sign up / Log in to  [Heroku](https://www.heroku.com/)
- From the main Heroku Dashboard page select 'New' and then 'Create New App'
- Give the project a name - I decided on the devils kitchen and selected EU as that is the closes region to me.
- After this you select select create app. 
- The name for the app must be unique or you will not be able to continue.
- Heroku will create the app and bring you to the deploy tab. 
- From the submenu at the top, navigate to the resources tab.
- Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
- Click on the setting tab
- Open the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
- Inside the Django app repository create a new file called env.py
- within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. 
- The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
-   Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
-   Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
-   In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
-   insert the line if os.path.isfile("env.py"): import env
-   remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
-   replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
-   In the terminal migrate the models over to the new database connection
---
-   Navigate in a browser to cloudinary, log in, or create an account and log in.
-   From the dashboard - copy the CLOUDINARY_URL to the clipboard
-   In the env.py file - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
-   In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
-   Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
-   this key value pair must be removed prior to final deployment
-   Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.
-   in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
-   Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
-   Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
-   Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
-   In your code editor, create three new top level folders, media, static, templates
-   Create a new file on the top level directory - Procfile
-   Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
-   In the terminal, add the changed files, commit and push to GitHub
-   In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
-   Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

#### Forking the repository

By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository.
You can do this by: 
-  Logging into GitHub or create an account. 
- Locate the repository at  [here](https://github.com/RockyPraxe/Customer-relationship-management-application)  . 
-  At the top of the repository, on the right side of the page, select "Fork" from the buttons available. 
-  A copy of the repository should now be created in your own repository.

#### [](https://github.com/RockyPraxe/Customer-relationship-management-application)Create a clone of this repository

Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally: This can be done by:

-   Navigate to  [https://github.com/RockyPraxe/Customer-relationship-management-application](https://github.com/RockyPraxe/Customer-relationship-management-application)
-   click on the arrow on the green code button at the top of the list of files
-   select the clone by https option and copy the URL it provides to the clipboard
-   navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
-   type 'git clone' and paste the https link you copied from github
-   press enter and git will clone the repository to your local machine

[Back to Top of page](#contents)

---
  
<a name="credits"></a>
## Credits

##### Dennis ivy
  - I watched some of Dennis's videos on youtube around django signals and extending the user model.
  - This inspired me to take this action however I followed on from the django documentation.
  
  
##### Md bootstrap
  - I went through the bootstrap navigation information and footer information to determine how best to approach my desired design.
  - I always find Md Bootstrap helpful with examples of how best to implement boostrap components.

[Back to Top of page](#contents)

---

<a name="content"></a>
## Content & Resources

##### Django Documentation
  - Read through the django documentation multiple times when trying to implement models and other content.
  
##### W3 Schools
  - Used for reference throughout for simple css examples.
  
##### Code Institute
  - Course content for portfolio project 4 helped greatly in being able to complete this project.
  - I found the walkthroughs informative and well paced.
  - Initial structure based heavily on the CI walkthrough until I got more comfortable with the framework and started to make it my own.
  - Some legacy code regarding nav remains.

[Back to Top of page](#contents)

<a name="acknowlegements"></a>
## Acknowledgements

### The tutors at Code institute
> To all the tutors in CI, thank you for your help!!







































