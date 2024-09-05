# Project Four: Full-Stack Web Application: Anna Rooney Coaching

## Overview

This project is a Full-Stack web application developed using the model-view-container framework. The website includes a blog, testimonials, comment sections, inquiry form and front-end admin features. The development process followed Agile methodologies, ensuring iterative progress and continuous improvement through regular feedback.


## Design
A pinterest was set up to inspire the design of the website, which you can view [here](https://ie.pinterest.com/23annarooney/anna-website/). The mood of the website was strong female entreperneur.

Then Figma was used to design the layout and stylings. You can view the design [here]([https://github.com/NielMc/django_blog](https://www.figma.com/design/oDYCdAq0j987KhdHqZX7iE/anna-coaching?node-id=0-1&t=xUBvgB8R1oULULuY-1)). The idea was to have a home page, about me page, about you page (services) and a content page with links to youtube, blog and other content. The final design ended up being simpler, with just a home page, inquire page, blog page, login/out/register page, and for the super users, an admin page. 

The colors and fonts of the site: 
<div align="center"> 
    <img width = "33%" alt="Color theme" src="https://github.com/user-attachments/assets/fc8f2fa6-a305-4ad4-97d7-561c5457b864">
    <img width="50%" alt="fonts" src="https://github.com/user-attachments/assets/77bc35b3-44e3-4e6d-a461-1020bbdfe1b8">
</div>

## Visitor experiences

# As a first time visitor, I want to:

- See testimonials
- View the blog to get a sense of the life coach

# As a returning visitor, I want to:

- Sign up as a user
- Read the blog
- Comment on the blog
- Edit my comments if necessary

# As a frequent visitor, I want to:

- Share blog posts
- Inquire about possibly working together
- View updates on how the beverages are brewed through their social media sites.

## Responsiveness: 

Bootstrap classes were used so each item was responsive for all screen sizes.

<div style="display: flex; justify-content: center;">
  <img width = "31%" alt="Iphone response" src="https://github.com/user-attachments/assets/5230c30a-70fd-4bd1-9424-c8fd381728c3">
  
  <img width = "31%" alt="Ipad response" src="https://github.com/user-attachments/assets/376c56d7-58d4-4186-a36d-7284f3d99654">
  
  <img width = "31%" alt="Nest hub max response" src="https://github.com/user-attachments/assets/17b6592d-c7cd-4dc7-83d2-b7950b623996">
</div>

## User differences
The navbar changes according to user profile: 
<div align="center">
  Superuser navbar: 
  <img width="80%" alt="navbar superuser" src="https://github.com/user-attachments/assets/59afba7f-5c82-450e-8ee8-cfad78f6a2bf">

  Non user navbar: 
  <img width="80%" alt="navbar non user" src="https://github.com/user-attachments/assets/a1a6ea37-b6d4-4683-977d-4e1e63d9a16c">

  Normal user navbar: 
  <img width="80%" alt="navbar norrmal user" src="https://github.com/user-attachments/assets/8c5a1ce5-fb6a-4266-a0c9-2e2c9bbb250f">
</div> 


Non-users:
- can view blog posts, comments, and all public pages.

Normal users:
- can view all public pages
- post and edit their comments

Super users:
- can view all pages
- in admin, approve and delete coments
- in admin, approve, delete, edit blog posts
- press reply to inquiries, which redirects you to email
- archive/ unarchive inquiries.

If a normal user or non user attempts to access Super User pages, for example like the blog admin page, they are redirected to the log in page. 
## Agile Development Process

### User Stories
User stories were created to capture the requirements and expectations of the end-users. These stories were used to guide the development process, with each story tied to a specific sprint.

### Sprints
The project was divided into multiple sprints. Each sprint focused on delivering a specific set of features, with tasks tracked and managed using github projects and issues: [Github projects](https://github.com/users/arir2001/projects/2): 

- **Sprint 1: Initial Setup & Core Features**
  - Setup MVC Framework: Established the project structure using Django. Basic template from [Code Institute's Blog app](https://github.com/NielMc/django_blog): 
  - User Authentication: Implemented user login, registration, and role-based access control.

- **Sprint 2: Blog & Testimonials**
  - Blog Functionality: Developed blog post creation, editing, and deletion.
  - Testimonials: Added testimonial submission and admin approval features.

- **Sprint 3: Comments & UI Enhancements**
  - Comment System: Enabled commenting on blog posts with moderation.
  - UI Enhancements: Improved UI elements and responsiveness.

- **Sprint 4: Admin Features & Deployment**
  - Admin Dashboard: Completed admin functionalities for content management.
  - Final Testing & Deployment: Conducted testing, fixed bugs, and deployed the application.

## Features

### Blog
- Users can create, edit, and delete posts.
- Posts can include images, categories, and tags.

### Testimonials
- Testimonials can be updated through back end admin
- In the future, an ability for registered users to submit testimonials which would then be approved by admins. 

### Comments
- Users can comment on blog posts.
- Comments are moderated by admins, and to be viewed by public must be approved. 

### Admin Features
- **Dashboard**: Admins have access to a dedicated dashboard for managing site content.
- **User Management**: Admins can assign roles and manage user access.
- **Content Moderation**: Admins can approve or delete comments and testimonials.

## Models

### User Model
- **Fields**: `username`, `email`, `password`, `role`
- **Description**: Manages user authentication and authorization. Includes role-based access control.

### Post Model
- **Fields**: `title`, `content`, `author`, `created_at`, `updated_at`
- **Description**: Stores blog posts, including metadata about the author and timestamps for creation and updates.

### Comment Model
- **Fields**: `post`, `author`, `content`, `created_at`
- **Description**: Stores comments associated with blog posts, allowing users to interact with content.

### Testimonial Model
- **Fields**: `user`, `content`, `approved`, `created_at`
- **Description**: Stores testimonials submitted by users, which admins can approve or reject.

## Technologies Used

- **Backend**: Django (MVC Framework)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Version Control**: Git & GitHub
- **Deployment**: Cloudinary

### Difference between my project and Code Institute's

As there are quite a few similarities between this project and Code Institute's upon which this is based, here is a detailed break down of what I added: 
#### **1. Project Structure**
- **This Project's (`projectfour`)**:
  - **File**: `models.py` (in `blog, home` apps)
    - Models: `Post`, `Comment`, `Testimonial`
    - difference:  `Testimonial` model and more detailed user authentication with role-based access control.
  - **File**: `views.py` (in `blog` app)
    - Handles CRUD operations for posts, comments, and testimonials.

- **Reference Project (`django_blog`)**:
  - **File**: `models.py` (in `blog` app)
    - Models: `Post`, `Comment`
    - Simpler structure focusing mainly on posts and comments.
  - **File**: `views.py` (in `blog` app)
    - Basic blog functionality without additional models like `Testimonial`.

#### **2. Models Comparison**
- **Post Model**:
  - Both projects use a `Post` model with similar fields (`title`, `content`, `author`, `created_at`, `updated_at`).

- **Comment Model**:
  - Both projects include a `Comment` model associated with `Post` and CRUD abilities. 

- **Testimonial Model**:
  - **My Project**:
    - `Testimonial` model (not present in `django_blog`):
      - Fields: `user`, `content`, `approved`, `created_at`.
      - **File**: `models.py` (in `home` app).
      - Adds a layer for user-submitted testimonials, managed by admins.
  - **Reference Project**:
    - Does not include this model.

#### **3. Views Comparison**
- **My Project**:
  - Manages posts, comments, and testimonials with separate views. Admin functionality is more developed with additional views for managing testimonials.
  - **Files**: `views.py` (in `blog` app).
- **Reference Project**:
  - Focuses on simpler blog post and comment views without additional admin features or testimonial management.
  - **Files**: `views.py` (in `blog` app).

#### **4. Features**
- **My Project**:
  - **Added Features**: Testimonial submissions, role-based access control, admin dashboard.
  - More complex interactions, allowing admins to moderate comments and testimonials.
- **Reference Project**:
  - Basic blog and comment features without the additional layers of user roles or testimonials.

### Summary of Differences
My project extends the functionality of the reference project by adding a `Testimonial` model, role-based access control, and enhanced font-end admin features. The reference project is simpler, focusing primarily on the blog and comment system without these additional features. My project has a more comprehensive structure and user interaction model. 



## Installation & Setup
The site was deployed to Heruko App. The steps to do so are as follows:
- Launch Heroku app
- Select new app set up, name the game, select appropriate region
- Link github repository
- In settings of the app page, add Python and Nodes.js buildpacks
- Config Vars was set to the appropriate Cloudinary Platform, the approrpiate data base set up by code institute, and the secret keys. 
- Deploy the branch, and launch.


## Testing


## Deployment

The application is deployed on Heroku.


