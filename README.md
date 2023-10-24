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
  
