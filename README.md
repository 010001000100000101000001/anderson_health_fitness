# Anderson Health & Fitness



## Introduction

This is my fifth project in Code Institute Diploma in Software Development with eCommerce. The Anderson Health & Fitness project is an e-commerce application designed to allow users to browse, search, and purchase workout gear. The application also includes user authentication, shopping cart functionality, user profile management and a section for users to leave product reviews. The application is built with Django and follows best practices for user interface design, focusing on user-friendliness and mobile responsiveness. The application is styled using Bootstrap 5 and utilizes the Stripe payment gateway for secure transactions.


## Table of Contents

- [Introduction](#introduction)
- [Epics and User Stories](#epics-and-user-stories)
- [Wire Fames](#wire-frames)
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

---

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

---

### Epic 3: Sorting and Filtering

As a **Site User**, I can **easily locate the highest rated, cheapest or alphabetical (A-Z or Z-A)** so that **I can quickly find the best-rated, lowest-priced, or find products alphabetically**.

- **Acceptance criteria 1**: Items can be sorted alphabetically (A-Z or Z-A), by price (ascending or descending), or by rating.
- **Acceptance criteria 2**: The workout out gear category page makes sorting choices easily accessible and visible..

As a **Site User**, I can **select things that meet my personal interests by filtering fitness gear items by category, price range, or rating.** so that **I can find products that fit my specific preferences**.

- **Acceptance criteria 1**: Users can filter by category (Clothing, Accessories, Equipment).
- **Acceptance criteria 2**: Filter options are presented clearly and the user has a clearly visible backpage arrow to return to the previous page.

---

### Epic 4: Shopping Cart and Checkout

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

---

### Epic 5: User Profile and Order Management

As a **Site User**, I can **view my past orders** so that **I can track my purchase history and reorder items if needed**.

- **Acceptance criteria 1**: The user profile includes a section to view past orders, with details such as order date, items purchased, and total cost.

As a **Site User**, I can **update my personal information** so that **my account details are always accurate and up-to-date**.

- **Acceptance criteria 1**: I can update my name, email, password, and other personal details from my profile page.

---

### Epic 6: Site Administration

As a **Site Admin**, I can **add, edit, and delete products** so that **the store’s inventory is always up-to-date**.

- **Acceptance criteria 1**: Admins have access to an interface to manage products, including adding new items, editing existing ones, and removing products that are no longer available.
- **Acceptance criteria 2**: Changes are immediately reflected on the site.

---

### Epic 7: Product Reviews

As a **Site User**, I can **leave reviews for products** so that **I can share my feedback and experiences with other users**.

- **Acceptance criteria 1**: I can submit a review on a product page, providing a rating and a comment.
- **Acceptance criteria 2**: Reviews are visible on the product detail page and display the username, rating, and comment.
- **Acceptance criteria 3**: I can edit or delete my reviews if I change my mind.
- **Acceptance criteria 4**: The system prevents me from submitting multiple reviews on the same item.
- **Acceptance criteria 5**: Admins can moderate and remove inappropriate reviews.

### Epic 8: Marketing and Promotions

As a **Site User**, I can **see a promotional banner on the site** so that **I can take advantage of free delivery**.

- **Acceptance criteria 1**: The promotional banner is visible on the homepage and other relevant pages.
- **Acceptance criteria 2**: The banner highlights free delivery on orders over €100!

---

### Epic 9: Search Enhancement

As a **Site User**, I can **view a list of the items that were found overall in the search results summary.** so that **I can quickly decide if I need to refine my search or browse the results**.

- **Acceptance criteria 1**: The total number of matching products is displayed on the search results page.
- **Acceptance criteria 2**: It is simple to perform a new search and refine the results.

---

### Epic 10: Order Management

As a **Site User**, I can **view a history of my past purchases** so that **track how much I've spent and review past orders**.

- **Acceptance criteria 1**: An overview of previous orders, including the total amount paid, is included in the user profile.
- **Acceptance criteria 2**: Users are able to read information about specific products as well as the order date and total amount.

---


### Epic 11: Mobile Experience

As a **Mobile Site User**, I can **view my profile on the go by simply accessing the website from my mobile device** so that **I can quickly explore, shop, browse, make purchases and view my profile on the go**.

- **Acceptance criteria 1**: The website's mobile version functions flawlessly across all screen sizes and is fully responsive.
- **Acceptance criteria 2**: Important features such as the navigation menu, search bar, and shopping cart are easily navigable and useable on mobile devices.
- **Acceptance criteria 3**: Product photos and descriptions are displayed as best they can on smaller screens thanks to the mobile layout.
---

## Wire Frames

Laptop & Desktop:

![image](https://github.com/user-attachments/assets/032ec8cc-d179-4cde-b208-dccace734417)

![image](https://github.com/user-attachments/assets/a4587cba-e2ca-4b94-a233-f96d11188f2e)

Tablet:

![image](https://github.com/user-attachments/assets/6c996062-ede7-41e9-b31f-c2e4e7d95593)


Mobile: iphone & android:

![image](https://github.com/user-attachments/assets/8419fa17-a877-4de5-bd5d-d074081fe80d)



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

![image](https://github.com/user-attachments/assets/8b3e0324-f481-4f43-90c9-33678b52b030)



- **Responsive Design**: The site is fully responsive, ensuring it looks and functions well on mobiles, tablets and desktops.

![image](https://github.com/user-attachments/assets/5c919f4f-a5b6-4c32-91ea-25134add3e4c)    ![image](https://github.com/user-attachments/assets/a9e7bb1e-4bce-4b94-9626-fbd2af46bf40)


- **User Authentication**: Users can register, log in, and manage their profiles.

![image](https://github.com/user-attachments/assets/56ac5ce1-96ac-4872-9ce7-4dae73563edb)



- **Product Browsing**: Users can browse workout gear by category, view product details, and add items to their cart.

![image](https://github.com/user-attachments/assets/8be3f132-cea4-4381-80c4-ad3157b81e92)



- **Shopping Cart**: Users can add items to their cart, view the cart, and proceed to checkout.

![image](https://github.com/user-attachments/assets/15dea3f8-01fe-4efb-9d9f-77b9c107b61a)

- **Search Functionality**: Users can search for products based on names and details.

![image](https://github.com/user-attachments/assets/d80a9b98-62e9-412e-8106-f4931bc44c9d)

 **Message to show no results**

  ![image](https://github.com/user-attachments/assets/f2b724dd-3677-4bba-b503-7b475fed12a9)



- **Promotional Banners**: The site features a promotional banner to highlight free delivery of orders over €100.


![image](https://github.com/user-attachments/assets/99cc4758-48b1-440a-9bd9-2251fcde49af)


- **Order Management**: Users can view past orders in their profile and track their purchase history. The application integrates with Stripe to handle payment processing, ensuring secure transactions.

  ![image](https://github.com/user-attachments/assets/b55ca428-ad83-4032-a88c-d433101d49ef)


- **Toast Notifications**: The site provides real-time toast notifications for actions like adding items to the cart, submitting a review, and order completion. These notifications enhance the user experience by providing instant feedback.

 
![image](https://github.com/user-attachments/assets/c5c28283-aa05-4c5e-b158-56376c5172ca)    ![image](https://github.com/user-attachments/assets/a8d5f06a-50d0-4030-a05e-9631477574a9)  ![image](https://github.com/user-attachments/assets/e4411eae-168a-474c-8f16-05d49815245c)


- **Review Order at Checkout**: Review your order details at the checkout.

  ![image](https://github.com/user-attachments/assets/8abb2dc7-c401-4579-b3a2-6734d1b864ca)



### Manual Tests

### Navigation Bar

| Feature Tested                 | Expected Outcome                                                   | Testing Performed        | Actual Outcome                                | Result   |
|------------------------------- |--------------------------------------------------------------------|--------------------------|-----------------------------------------------|----------|
| Anderson Health & Fitness logo | Directs user to the home page                                      | Click "Anderson Health & Fitness" logo | Directed to home page                         | Pass     |
| Home link                      | Directs user to the home page                                      | Click "Home"             | Directed to home page                         | Pass     |
| Shop link                      | Directs user to the shop page                                      | Click "Shop"             | Directed to shop page                         | Pass     |
| Cart icon                      | Directs user to the cart page                                      | Click "Cart" icon        | Directed to cart page                         | Pass     |
| Search icon                    | Opens the search bar                                               | Click "Search" icon      | Search bar is revealed                        | Pass     |
| Profile link (logged out)      | Directs user to the login page                                     | Click "Profile"          | Directed to login page                        | Pass     |
| Profile link (logged in)       | Directs user to the profile page                                   | Click "Profile"          | Directed to profile page                      | Pass     |
| Register link                  | Directs user to the sign-up page                                   | Click "Register"         | Directed to sign-up page                      | Pass     |
| Login link                     | Directs user to the login page                                     | Click "Login"            | Directed to login page                        | Pass     |
| Logout link (signed in)        | Directs user to the home page / Displays feedback message          | Click "Logout"           | Directed to home page, displays feedback message | Pass     |
| Responsive Navbar              | Navbar collapses into a menu on smaller screens                    | Change screen size (DevTools) | Navbar collapses correctly                    | Pass     |

### Home Page

| Feature Tested                 | Expected Outcome                                                   | Testing Performed        | Actual Outcome                                | Result   |
|------------------------------- |--------------------------------------------------------------------|--------------------------|-----------------------------------------------|----------|
| Responsive Design              | The page adjusts content to fit all screen sizes                   | Change sizes (DevTools)  | The page is responsive, content fits          | Pass     |
| Text Readability               | Text is readable at all screen sizes                               | Read all text blocks     | The text is readable at all breakpoints       | Pass     |
| Featured Products Click        | Clicking a featured product redirects to product detail page       | Click product image      | Redirected to the product detail page         | Pass     |
| Shop Now Button                | Redirects user to the All Gear page                                    | Click "Shop Now" button  | Redirected to shop page                       | Pass     |

### Shop Page

| Feature Tested                 | Expected Outcome                                                   | Testing Performed        | Actual Outcome                                | Result   |
|------------------------------- |--------------------------------------------------------------------|--------------------------|-----------------------------------------------|----------|
| Product Categories             | Allows filtering by categories                                     | Click on a category      | Products filtered by selected category        | Pass     |
| Sort Products                  | Sorts products based on selected criteria (price, rating, etc.)    | Use sort dropdown        | Products sorted correctly                    | Pass     |
| Search Products                | Displays relevant products based on search query                   | Enter search term        | Correct products are displayed                | Pass     |
| Add to Cart                    | Adds product to the cart                                           | Click "Add to Cart" button | Product added to cart successfully           | Pass     |
| Product Image Click            | Clicking product image redirects to product detail page            | Click product image      | Redirected to product detail page             | Pass     |

### Cart Page

| Feature Tested                 | Expected Outcome                                                   | Testing Performed        | Actual Outcome                                | Result   |
|------------------------------- |--------------------------------------------------------------------|--------------------------|-----------------------------------------------|----------|
| View Cart Items                | Displays all added items in the cart                               | Open cart page           | Cart displays all added items                 | Pass     |
| Update Item Quantity           | Updates the item quantity in the cart                              | Change item quantity     | Quantity updated and total recalculated       | Pass     |
| Remove Item                    | Removes an item from the cart                                      | Click "Remove" button    | Item is removed from the cart                 | Pass     |
| Proceed to Checkout Button     | Redirects user to the checkout page                                | Click "Checkout" button  | Redirected to checkout page                   | Pass     |

### Checkout Page

| Feature Tested                 | Expected Outcome                                                   | Testing Performed        | Actual Outcome                                | Result   |
|------------------------------- |--------------------------------------------------------------------|--------------------------|-----------------------------------------------|----------|
| Form Validation                | Shows validation errors for incorrect form inputs                  | Submit with invalid input | Validation errors displayed                   | Pass     |
| Payment Processing             | Processes payment securely using Stripe                            | Enter valid card details | Payment processed successfully                | Pass     |
| Save Information Checkbox      | Saves user shipping information to their profile                   | Check "Save Info" box    | Information saved to user profile             | Pass     |
| Order Confirmation             | Displays order confirmation message                                | Complete checkout        | Order confirmation displayed                  | Pass     |

### Profile Page

| Feature Tested                 | Expected Outcome                                                   | Testing Performed        | Actual Outcome                                | Result   |
|------------------------------- |--------------------------------------------------------------------|--------------------------|-----------------------------------------------|----------|
| View Order History             | Displays a list of past orders                                     | Open profile page        | Order history is displayed                   | Pass     |
| Update Profile Information     | Updates user profile details                                       | Submit updated info      | Profile information updated successfully     | Pass     |
| Saved Shipping Info            | Displays saved shipping information                                | Open profile page        | Shipping info is displayed                   | Pass     |

### Product Detail Page

| Feature Tested                 | Expected Outcome                                                   | Testing Performed        | Actual Outcome                                | Result   |
|------------------------------- |--------------------------------------------------------------------|--------------------------|-----------------------------------------------|----------|
| Add Review                     | Allows logged-in user to add a review                              | Submit review form       | Review added successfully                    | Pass     |
| Edit Review                    | Allows user to edit their existing review                          | Edit review              | Review updated successfully                  | Pass     |
| Delete Review                  | Allows user to delete their existing review                        | Delete review            | Review deleted successfully                  | Pass     |
| Rating System                  | Displays average rating for the product                            | View product detail      | Average rating is displayed                  | Pass     |

### Search Functionality

| Feature Tested                 | Expected Outcome                                                   | Testing Performed        | Actual Outcome                                | Result   |
|------------------------------- |--------------------------------------------------------------------|--------------------------|-----------------------------------------------|----------|
| Search Bar Visibility          | Search bar is visible and functional                               | Open search bar          | Search bar is visible                         | Pass     |
| Search Results                 | Displays products matching search criteria                         | Enter search term        | Relevant products displayed                   | Pass     |
| No Results Message             | Shows message when no products match the search                    | Enter non-existent product | "No results" message displayed               | Pass     |


### Stripe Webhooks

![image](https://github.com/user-attachments/assets/4f4e85a6-b85f-44e2-b327-07e3ceff0e31)


![image](https://github.com/user-attachments/assets/bd6f9aaa-c5ee-4060-9f53-7ceb31dd3456)



 ## Technologies Used

- **Django**: The web framework used to build the application.
- **Bootstrap**: Used for responsive design and styling.
- **Font Awesome**: Provides icons throughout the site.
- **SQLite**: The database used for development.
- **Pillow**: Used for image processing in the application.
- **Django Allauth**: Handles user authentication, including social logins.
- **Crispy Forms**: For better form rendering and styling using Bootstrap 5.
- **django-countries**: Provides a country field in forms, enhancing user experience during checkout.
- **Stripe**: Used for processing payments securely and handling webhooks for order verification.
- **Custom CSS & JavaScript**: Additional styling and interactivity tailored to the fitness e-commerce theme.





## Deployment

### Fork the Repository

1. Click the "Fork" button at the top right corner of the GitHub repository page.
2. This action creates a copy of the repository under your GitHub account.

### Clone the Repository Locally

1. Go to your GitHub account and open the forked repository.
2. Click the "Code" button and copy the provided URL.
3. Open your command line interface (CLI) and navigate to the directory where you want to clone the repository.
4. Run the command: git clone *copied-URL*

Move into the cloned directory: cd anderson-health-fitness

Set Up the Application Locally
Install Dependencies:

Ensure you have Python and pip installed.
Run the following command to install the required packages: pip install -r requirements.txt

Set Up Environment Variables:

Create a .env file in the project root.
Add the following environment variables:

STRIPE_PUBLIC_KEY=*your-stripe-public-key*
STRIPE_SECRET_KEY=*your-stripe-secret-key*
EMAIL_HOST_USER=*your-email*
SECRET_KEY=*your-secret-key*
DATABASE_URL=*your-database-url*
CLOUDINARY_URL=*your-cloudinary-url*

Run Migrations:

Apply database migrations to set up the local database: python manage.py migrate

Run the Application:

Start the development server: python manage.py runserver



### Deploy to Heroku

Open Heroku:

Go to Heroku and log in to your account.
Create a New Application:

Click on "New" in the top right corner and select "Create new app".
Choose a unique app name and select your region.
Press "Create app".
Configure the Application:

Config Vars:
Navigate to the "Settings" tab.
Under "Config Vars", click "Reveal Config Vars".
Add the required environment variables such as DATABASE_URL, CLOUDINARY_URL, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, EMAIL_HOST_USER, and SECRET_KEY.
Buildpacks:
Scroll to the "Buildpacks" section and click "Add buildpack".
Select "Python" and press "Save changes".
Deploy the Application:

Connect to GitHub:
Go to the "Deploy" tab.
In the "Deployment method" section, select "GitHub".
Search for your forked repository and press "Connect".
Manual Deploy:
Scroll down to the "Manual deploy" section.
Select the branch you want to deploy and click "Deploy Branch".
Heroku will now build and deploy the application.
Apply Database Migrations.





## Credits 

### Content


#### Links and sources




### Media

- The media content for products was created specifically for this project using AI tools such as DALL·E 2 on sites such as [Link](https://picsart.com/) and [Link](https://chatgpt.com/) and are to serve as an example of real world products only. The Hero image was taken from Pixabay on free usage licence.



### Favicons

Font awesome icons are used througout the site. [Link](https://fontawesome.com/).



## Acknowledgements

Thanks to the Code Institute tutors staff and my mentor Matt Bodden for their support.

