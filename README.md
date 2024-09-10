# Anderson Health & Fitness



## Introduction

This is my fifth project in Code Institute Diploma in Software Development with eCommerce. The Anderson Health & Fitness project is an e-commerce application designed to allow users to browse, search, and purchase workout gear. The application also includes user authentication, shopping cart functionality, user profile management and a section for users to leave product reviews.

## Table of Contents

- [Introduction](#introduction)
- [Epics and User Stories](#epics-and-user-stories)
- [Database Schema](#database-schema)
- [Features](#features)
  - [Existing Features](#existing-features)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
  - [Set Up the Application Locally](#set-up-the-application-locally)
  - [Deploy to Heroku](#deploy-to-heroku)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Favicons](#favicons)
- [Acknowledgements](#acknowledgements)


## Epics and User Stories

### Epic 1: User Registration and Authentication

As a **New Site User**, I can **register for an account** so that **I can access personalised features and make purchases**.

- **Acceptance criteria 1**: The registration form requires username, email, and password input fields.
- **Acceptance criteria 2**: The system confirms the email by requiring it to be entered twice to avoid user mistakes.
- **Acceptance criteria 3**: After successful registration, I receive an email verification link.

As a **Site User**, I can **log in to my account** so that **I can access my profile, view past orders, and make new purchases**.

- **Acceptance criteria 1**: The login form requires either a username or email, along with a password to be input.
- **Acceptance criteria 2**: If login credentials are incorrect, I receive appropriate feedback.

As a **Site User**, I can **log in using my social media accounts** so that **I can access my account without needing to remember a separate password**.

- **Acceptance criteria 1**: I can log in using Google, Facebook, or other supported social media accounts.
- **Acceptance criteria 2**: The system seamlessly handles social logins and links them to my profile.

As a **Site User**, I can **reset my password if I forget it** so that **I can regain access to my account**.

- **Acceptance criteria 1**: I can request a password reset link via my registered email.
- **Acceptance criteria 2**: The system sends a secure link to reset the password, and I can update it as a site user.

### Epic 2: Product Browsing and Search

As a **Site User**, I can **browse workout gear by category** so that **I can easily find the type of product I’m looking for**.

- **Acceptance criteria 1**: Categories are displayed on the navigation bar with a dropdown menu.
- **Acceptance criteria 2**: I can click on a category to view all items within that category.

As a **Site User**, I can **search for workout gear** so that **I can quickly find specific items without browsing through categories**.

- **Acceptance criteria 1**: The search bar is available on all pages and on various mobile, tablet and desktop screens.
- **Acceptance criteria 2**: The search returns relevant results based on workout gear item names and detailed descriptions.
- **Acceptance criteria 3**: There is a button to reveal and hide the search bar when not in use, on mobile and tablet screen sizes to save screen space on smaller devices.

As a **Site User**, I can **view detailed information about a specific product** so that **I can make an informed decision before purchasing**.

- **Acceptance criteria 1**: I can click on a product to view its details, including name, price, description, image, stock availability, and other specifications like material and weight.

### Epic 3: Shopping Cart and Checkout

As a **Site User**, I can **add items to my shopping cart** so that **I can purchase multiple items in one transaction**.

- **Acceptance criteria 1**: Each product detail page includes an "Add to Cart" button.
- **Acceptance criteria 2**: The shopping cart dynamically updates to reflect the added items.

As a **Site User**, I can **view the contents of my shopping cart** so that **I can review the items before proceeding to checkout**.

- **Acceptance criteria 1**: I can access my shopping cart from any page via a shopping cart icon.
- **Acceptance criteria 2**: The cart displays items, quantities, and the total price.

As a **Site User**, I can **securely checkout and pay for my items** so that **I can complete my purchase and have the items delivered to me**.

- **Acceptance criteria 1**: The checkout process includes forms for entering shipping and payment information.
- **Acceptance criteria 2**: Payment processing is handled securely, using Stripe.
- **Acceptance criteria 3**: Upon successful payment, I receive a confirmation email with order details.

### Epic 4: User Profile and Order Management

As a **Site User**, I can **view my past orders** so that **I can track my purchase history and reorder items if needed**.

- **Acceptance criteria 1**: The user profile includes a section to view past orders, with details such as order date, items purchased, and total cost.

As a **Site User**, I can **update my personal information** so that **my account details are always accurate and up-to-date**.

- **Acceptance criteria 1**: I can update my name, email, password, and other personal details from my profile page.

### Epic 5: Marketing and Promotions

As a **Site User**, I can **see a promotional banner on the site** so that **I can take advantage of free delivery**.

- **Acceptance criteria 1**: The promotional banner is visible on the homepage and other relevant pages.
- **Acceptance criteria 2**: The banner highlights free delivery on orders over €100!

### Epic 6: Site Administration

As a **Site Admin**, I can **add, edit, and delete products** so that **the store’s inventory is always up-to-date**.

- **Acceptance criteria 1**: Admins have access to an interface to manage products, including adding new items, editing existing ones, and removing products that are no longer available.
- **Acceptance criteria 2**: Changes are immediately reflected on the site.

### Epic 7: Product Reviews

As a **Site User**, I can **leave reviews for products** so that **I can share my feedback and experiences with other users**.

- **Acceptance criteria 1**: I can submit a review on a product page, providing a rating and a comment.
- **Acceptance criteria 2**: Reviews are visible on the product detail page and display the username, rating, and comment.
- **Acceptance criteria 3**: I can edit or delete my reviews if I change my mind.
- **Acceptance criteria 4**: The system prevents me from submitting multiple reviews on the same item.
- **Acceptance criteria 5**: Admins can moderate and remove inappropriate reviews.


## Database Schema

### GearCategory

| Attribute         | Data Type   | Description                                                                                  |
|-------------------|-------------|----------------------------------------------------------------------------------------------|
| **id**            | AutoField   | Each category's unique primary key is automatically generated.                                         |
| **name**          | CharField   | A condensed name for the group. 100 characters is the maximum length allowed. Needs to be distinct (no duplicates). |
| **friendly_name** | CharField   | A more easily understood name for the group. There is a 254 character maximum. This is an optional field that can be left empty. |
| **overview**      | TextField   | A synopsis or synopsis of the category. This is an optional field that can be left empty. |

#### Relationships:
- One-to-Many with 'GearItem' (A category can have multiple gear items)

---


### GearItem

| Attribute          | Data Type           | Description                                                                                 |
|--------------------|---------------------|---------------------------------------------------------------------------------------------|
| **id**             | AutoField           | A primary key generated automatically by AutoField for every gear item.                                       |
| **category**       | ForeignKey          | Connects a "GearCategory" to the gear item. All associated products will be deleted along with the category (CASCADE). |
| **name**           | CharField           | The gear item's name. up to 255 characters in length.                                 |
| **details**        | TextField           | A detailed description of the product along with benefits in some cases and sizing charts in others.                                                   |
| **cost**           | DecimalField        | The price of the item. It can store up to 8 digits, with 2 digits after the decimal point.|
| **stock_quantity** | PositiveIntegerField | The number of how many products that are kept in stock. The default value is 0, and it must be a positive integer.              |
| **weight**         | CharField           | The item's weight (for example, "2kg"). 20 characters at most in length. This is an optional field that can be left empty. |
| **material_type**  | CharField           | The item's composition (for example, "Cotton"). 100 characters is the maximum length allowed. This is an optional field that can be left empty. |
| **image_url**      | URLField            | The web address at which the products image is hosted. Ten twenty-four characters maximum. This is an optional field that can be left empty. |
| **image_file**     | ImageField          | Uploading an image file for the product is possible with ImageField. The folder titled "gear_images/" contains the images. This is an optional field that can be left empty. |
| **highlight**      | BooleanField        | A true/false value to indicate whether the item should be highlighted. A number that indicates whether or not the item should be highlighted (for example, on a page featuring featured products). False is the default. |
| **created_on**     | DateTimeField       | The time and date of the products initial creation. At the time the item is created, this is automatically set. |
| **modified_on**    | DateTimeField       | The date and time when the product was last updated. This is automatically updated whenever changes are made to the item. |
| **rating**         | DecimalField        | The products average customer rating. able to hold two digits, one of which comes after the decimal point (e.g., 4.5). This is an optional field that can be left empty.

#### Relationships:
- One-to-Many with 'ProductReview' (A gear item can have multiple reviews)

---


### ProductReview

| Attribute          | Data Type           | Description                                                                                 |
|--------------------|---------------------|---------------------------------------------------------------------------------------------|
| **id**             | AutoField           | Auto-generated unique primary key for each review.                                           |
| **gear_item**      | ForeignKey          | Links the review to a 'GearItem'. If the gear item is deleted, all related reviews will be deleted too (CASCADE). |
| **user**           | ForeignKey          | Links the review to a 'User'. If the user is deleted, all related reviews will be deleted too (CASCADE). |
| **rating**         | PositiveIntegerField | The rating given by the user to the gear item. Must be a number between 1 and 5.             |
| **comment**        | TextField           | The written review or comment about the gear item.                                           |
| **created_at**     | DateTimeField       | The date and time when the review was first created. This is automatically set when the review is submitted. |
| **updated_at**     | DateTimeField       | The date and time when the review was last updated. This is automatically updated whenever changes are made to the review. |


#### Relationships:
- Many-to-One with 'GearItem' (A gear item can have many reviews, but a review belongs to one gear item)
- Many-to-One with 'User' (A user can write many reviews, but a review belongs to one user)



## Features

### Existing Features

- **Navigation Bar**: Allows users to navigate through different sections of the site, including Workout Gear, Search, Profile  and Cart.
- **Responsive Design**: The site is fully responsive, ensuring it looks and functions well on mobiles, tablets and desktops.
- **User Authentication**: Users can register, log in, and manage their profiles. Social authentication is also supported.
- **Product Browsing**: Users can browse workout gear by category, view product details, and add items to their cart.
- **Shopping Cart**: Users can add items to their cart, view the cart, and proceed to checkout.
- **Search Functionality**: Users can search for products based on names and details.
- **Promotional Banners**: The site features a promotional banner to highlight free delivery of orders over €100.


 ## Technologies Used

- **Django**: The web framework used to build the application.
- **Bootstrap**: Used for responsive design and styling.
- **Font Awesome**: Provides icons throughout the site.
- **SQLite**: The database used for development.
- **Pillow**: Used for image processing in the application.
- **Django Allauth**: Handles user authentication, including social logins.




## Deployment


### Set Up the Application Locally


### Deploy to Heroku





## Credits 

### Content


#### Links and sources




### Media

- The media content for products was created specifically for this project using AI tools such as DALL·E 2 on sites such as [Link](https://picsart.com/) and [Link](https://chatgpt.com/) and are to serve as an example of real world products only.



### Favicons

Font awesome icons are used througout the site. [Link](https://fontawesome.com/).



## Acknowledgements

