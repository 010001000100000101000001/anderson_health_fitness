# Anderson Health & Fitness



## Introduction

This is my fifth project in Code Institute Diploma in Software Development with eCommerce. The Anderson Health & Fitness project is an e-commerce application designed to allow users to browse, search, and purchase workout gear. The application also includes user authentication, shopping cart functionality, user profile management and a section for users to leave product reviews. The application is built with Django and follows best practices for user interface design, focusing on user-friendliness and mobile responsiveness. The application is styled using Bootstrap 5 and utilizes the Stripe payment gateway for secure transactions.


## Table of Contents

- [Introduction](#introduction)
- [Epics and User Stories](#epics-and-user-stories)
- [Marketing Strategy](#marketing-strategy)
- [Facebook Page](#facebook-page)
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

## Marketing Strategy for Anderson Health & Fitness

Business Strategy for Anderson Health & Fitness

Increase brand awareness, drive sales through digital and traditional marketing, and build a loyal customer base.
Build a social media presence and focus on platforms Instagram, Facebook, TikTok, YouTube and X.
Share engaging content such as workout tips, motivational quotes, and behind-the-scenes videos. Utilize short-form videos (Reels, TikToks) for quick engagement.
Partner with fitness influencers to reach broader audiences. Use authentic endorsements to build trust.
Create workout tutorials, product reviews, and success stories. Host live Q&A sessions to engage directly with the audience.
Make use of relevant keywords and hashtags to increase visibility.
Highlight new products, upcoming launches, and exclusive promotions in the Weekly Newsletter.
Host regular competitions on social media to increase engagement and the visibility of  the Anderson Health & Fitness brand. Offer branded merchandise as prizes.
Create a Facebook group or online forum for members to share experiences and support each other.
Host virtual events or webinars focusing on holistic wellness topics like nutrition and mindfulness and fitness based advice.
Use targeted ads on social media platforms to reach specific demographics interested in fitness.
Implement retargeting strategies to convert visitors into customers.
Offer seasonal discounts or bundle deals to encourage purchases.
Highlight limited-time offers in newsletters and social media posts.
Expand product lines to include popular fitness gear and apparel.
Promote new arrivals through all marketing channels.
Track website traffic, social media engagement, and sales data to refine strategies.
Use analytics tools to understand customer behavior and preferences.
Encourage reviews and testimonials on products and services and use this customer feedback to constantly improve.

## Facebook Page

![image](https://github.com/user-attachments/assets/aa64b0e5-8741-4d7c-9b09-7aff0a9331d0)


![image](https://github.com/user-attachments/assets/173b7adb-8cd4-4649-8b0a-dc6b20cf31b8)


![image](https://github.com/user-attachments/assets/65344a30-d7ac-4c9d-ad67-4c1d12c831ac)






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


- **404 Error Page**:

  ![image](https://github.com/user-attachments/assets/20a17eec-2294-467f-8e10-40674f0392ea)


- **500 Error Page**:

  ![image](https://github.com/user-attachments/assets/6fa899db-8ea2-47f8-a7c9-0d86c69363ab)




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

### Reviews Section

| Feature Tested                 | Expected Outcome                                                   | Testing Performed        | Actual Outcome                                | Result   |
|------------------------------- |--------------------------------------------------------------------|--------------------------|-----------------------------------------------|----------|
| Add Review                     | Allows a logged-in user to submit a review                         | Submit review form       | Review added and displayed on product page    | Pass     |
| Edit Review                    | Allows a user to edit their existing review                        | Edit review and submit   | Review updated and changes reflected          | Pass     |
| Delete Review                  | Allows a user to delete their existing review                      | Delete review            | Review removed from product page              | Pass     |
| Prevent Duplicate Review       | Prevents the same user from submitting multiple reviews on a product | Attempt to submit multiple reviews | Duplicate review prevented, feedback given  | Pass     |
| Average Rating Calculation     | Displays the correct average rating for the product                | Submit multiple reviews  | Average rating is calculated and displayed correctly | Pass     |
| Review Display Formatting      | Reviews display correctly with username, rating, and comment       | View product page        | Reviews are formatted and displayed correctly | Pass     |


### Email Confirmation Testing

| Feature Tested                 | Expected Outcome                                                     | Testing Performed           | Actual Outcome                              | Result   |
|------------------------------- |---------------------------------------------------------------------|-----------------------------|---------------------------------------------|----------|
| Registration Email Sent        | Confirmation email is sent to the user’s email upon registration    | Register using the app      | Confirmation email received                 | Pass     |
| Email Confirmation Link        | Clicking the link confirms the email and activates the account      | Click the link in the email | Account successfully activated              | Pass     |
| Invalid Email Format           | Entering an invalid email prevents registration                     | Register with invalid email | Registration not completed, error shown     | Pass     |
| Test with `generator.email`    | Registration with a temporary email from `generator.email`          | Register using `generator.email` | Confirmation email successfully received | Pass     |
| Confirmation Email Resend      | Resending the confirmation email if the first one is lost/expired   | Click "Resend Email" button | New confirmation email received             | Pass     |


![image](https://github.com/user-attachments/assets/e4aede78-fcea-4c6a-8fbd-586b7bdbf37d)


![image](https://github.com/user-attachments/assets/842a5338-db0e-4bb1-8c09-40c3c29ff160)



In this project, I began building a news section aimed at keeping users up-to-date with Anderson Health & Fitness’s latest developments, fitness tips, and special promotions. The idea was to provide a space for content that goes beyond just products, adding value to the user experience by offering insightful and relevant information that complements our workout gear. This news section was envisioned as a lively, interactive feature where users could find everything from new product launches to expert advice on achieving their fitness goals.

Despite making a solid start, I couldn't fully implement or test this feature before the current project deadline. The basic structure is in place – including preliminary layouts and placeholder content – but it still requires further work to seamlessly integrate with the rest of the application. More testing is needed to make sure it is functional and visible.
Given more time I am confident I can complete this section. When revisiting the news section, I plan to focus on refining its design, incorporating dynamic content management so that updates can be made easily, and conducting extensive testing to ensure that it not only looks great but also performs smoothly. For now, it remains an exciting work-in-progress that I look forward to completing soon!

### Stripe Webhooks

![image](https://github.com/user-attachments/assets/4f4e85a6-b85f-44e2-b327-07e3ceff0e31)


![image](https://github.com/user-attachments/assets/bd6f9aaa-c5ee-4060-9f53-7ceb31dd3456)



### Lighthouse Tests

#### Home

Desktop:
![image](https://github.com/user-attachments/assets/fbdb556e-d59d-4f96-9fca-1620fb5761ed)


Mobile:
![image](https://github.com/user-attachments/assets/99255cd1-5cbb-4ef9-8b7e-18cc782e5e24)


#### All Gear Page

Desktop:
![image](https://github.com/user-attachments/assets/4416b1c5-82d0-42c6-a5bc-b239ac0a763c)

Mobile:
![image](https://github.com/user-attachments/assets/e972c588-c96c-43ec-a900-5d46e26bcad7)


#### Clothing

Desktop:
![image](https://github.com/user-attachments/assets/29c0788c-382b-4ab1-8198-676f1f56543d)


Mobile:
![image](https://github.com/user-attachments/assets/077239db-a3c8-4a9d-a26f-57dd622b1c02)


#### Accessories

Desktop:
![image](https://github.com/user-attachments/assets/f613f2c5-211a-4036-96eb-27e24651970b)


Mobile: 
![image](https://github.com/user-attachments/assets/a5cd7c65-53db-4eef-bc65-8f667c7ecdbd)



#### Equipment

Desktop:
![image](https://github.com/user-attachments/assets/bbb2a5ce-19d8-4156-b02b-bad8bd70dc3c)


Mobile:
![image](https://github.com/user-attachments/assets/58db260d-fcb9-4e45-abd9-6bb34cebf00b)


#### Cart

Desktop:
![image](https://github.com/user-attachments/assets/f358f476-fd6b-4d25-bf63-f2adb1d470cc)



Mobile:
![image](https://github.com/user-attachments/assets/a2290d3d-67cb-4a1b-94b3-da555e072f26)



#### Checkout

Desktop:
![image](https://github.com/user-attachments/assets/8c89051f-46f9-4a7c-881e-d7fb81e6b29f)


Mobile:
![image](https://github.com/user-attachments/assets/116a669f-f112-4d23-9ebc-b94b84434528)



#### Login

Desktop:
![image](https://github.com/user-attachments/assets/3f7faa83-da80-4669-801a-e2faf37aa708)


Mobile:
![image](https://github.com/user-attachments/assets/869864f8-fea6-4aa2-b8cb-d2851c703454)


#### Signup

Destop:
![image](https://github.com/user-attachments/assets/2bc21053-3af6-4782-8c83-528c42d39950)



Mobile:
![image](https://github.com/user-attachments/assets/87b4f699-9d6b-4d67-97ba-61bf9898d052)



#### Search Results

Desktop:
![image](https://github.com/user-attachments/assets/4ece3ae8-a671-48d8-a216-b3cbb5033feb)



Mobile:
![image](https://github.com/user-attachments/assets/8198440e-27d0-4589-a4a6-3a78b0b4afc9)




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

#### Links and Resources

#### Official Documentation

- [Django Documentation](https://docs.djangoproject.com/en/stable/)  
  The official Django documentation, providing a comprehensive guide to all of Django's features, including models, views, templates, and the Django admin.

- [Django REST Framework](https://www.django-rest-framework.org/)  
  A powerful toolkit for building Web APIs with Django. This is useful for implementing an API backend if the project expands to include features like mobile app integration.

- [Stripe API Documentation](https://stripe.com/docs/api)  
  Official Stripe documentation, including guides for implementing payments, subscriptions, and webhooks. Vital for ensuring a secure and seamless payment experience within the application.

- [Stripe Webhooks](https://stripe.com/docs/webhooks)  
  Comprehensive information on setting up and handling webhooks with Stripe. This is essential for tasks like payment confirmation, refund processing, and order fulfillment.

- [Stripe Integration with Django](https://stripe.com/docs/payments/integration-builder)  
  Step-by-step guides for integrating Stripe payments within a Django application. This includes handling events like `payment_intent.succeeded` and setting up secure payments.

#### Tutorials & Learning Resources

- [Django Allauth Documentation](https://django-allauth.readthedocs.io/en/latest/)  
  Documentation for `django-allauth`, which manages user registration, login, and account management. It provides helpful insights into social authentication and more complex user flows.

- [Django Crispy Forms Documentation](https://django-crispy-forms.readthedocs.io/en/latest/)  
  A guide to styling Django forms with Crispy Forms, which is integrated into the Anderson Health & Fitness project for a polished, user-friendly interface.

- [Django Deployment with Heroku](https://devcenter.heroku.com/articles/deploying-python)  
  A detailed guide to deploying Django applications on Heroku. It covers setting up PostgreSQL, environment variables, and handling static files, which is crucial for project deployment.

- [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)  
  Official Bootstrap 5 documentation, which includes information on using the grid system, components, utilities, and customization for building responsive designs.

#### Stripe Payment Integration

- [Test Card Numbers for Stripe](https://stripe.com/docs/testing)  
  A useful guide to Stripe's test card numbers and how to simulate different payment scenarios, which is important for testing various payment outcomes without processing real transactions.

- [Testing Stripe Webhooks Locally](https://stripe.com/docs/webhooks/test)  
  Instructions for testing webhooks locally with the Stripe CLI. This guide explains how to receive webhook events on your local server during development.

#### Community & Blogs

- [Real Python](https://realpython.com/)  
  A comprehensive platform offering Python tutorials and articles. Contains many guides related to Django, Stripe integration, and improving the overall application performance.

- [Simple is Better Than Complex](https://simpleisbetterthancomplex.com/)  
  A blog with in-depth Django tutorials and guides, covering everything from basic model setup to complex form handling and deployment.

- [Django Packages](https://djangopackages.org/)  
  A directory of reusable Django packages. Useful for finding third-party packages that can add additional functionality to the project, like image galleries, email handling, and more.

#### Tools & Utilities

- [PythonAnywhere](https://www.pythonanywhere.com/)  
  A beginner-friendly platform for deploying small-scale Django projects. While Heroku is used for Anderson Health & Fitness, PythonAnywhere is a good alternative for practice and learning.

- [Postman](https://www.postman.com/)  
  An API testing tool to validate Stripe's API responses and ensure that the webhook handlers are functioning correctly.

#### Additional Reading

- [Improving Django Performance](https://docs.djangoproject.com/en/stable/topics/performance/)  
  Best practices and tips for improving the performance of Django applications, such as using caching, database optimization, and query efficiency.

- [Security Best Practices in Django](https://docs.djangoproject.com/en/stable/topics/security/)  
  A must-read guide on securing a Django application, including the use of CSRF tokens, secure password storage, and best practices for handling sensitive data.
  
- [W3Schools: HTML, CSS, JavaScript](https://www.w3schools.com/)  
  A helpful resource for learning or refreshing your knowledge on HTML, CSS, and JavaScript, which are fundamental to customizing the frontend components of the project.


### Media

- The media content for products was created specifically for this project using AI tools such as DALL·E 2 on sites such as [Link](https://picsart.com/) and [Link](https://chatgpt.com/) and are to serve as an example of real world products only. The Hero image was taken from Pixabay on free usage licence.



### Favicons

Font awesome icons are used througout the site. [Link](https://fontawesome.com/).



## Acknowledgements

Thanks to the Code Institute tutors staff and my mentor Matt Bodden for their support.

