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
