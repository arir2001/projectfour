# Project Four: Full-Stack Web Application: Anna Rooney Coaching

## Overview

This project is a Full-Stack web application developed using the MVC framework. The application includes a blog, testimonials, comment sections, inquiry form and front-end admin features. The development process followed Agile methodologies, ensuring iterative progress and continuous improvement through regular feedback.

## Design
A pinterest was set up to inspire the design of the website, which you can view [here](https://ie.pinterest.com/23annarooney/anna-website/). The mood of the website was strong female entreperneur.

Then Figma was used to design the layout and stylings. You can view the design [here]([https://github.com/NielMc/django_blog](https://www.figma.com/design/oDYCdAq0j987KhdHqZX7iE/anna-coaching?node-id=0-1&t=xUBvgB8R1oULULuY-1)). The idea was to have a home page, about me page, about you page (services) and a content page with links to youtube, blog and other content. The final design ended up being simpler, with just a home page, inquire page, blog page, login/out/register page, and for the super users, an admin page. 

The colors of the site: 

![colors](https://github.com/user-attachments/assets/fc8f2fa6-a305-4ad4-97d7-561c5457b864)

## Responsiveness: 


<img width="578" alt="Screenshot 2024-09-02 at 09 34 49" src="https://github.com/user-attachments/assets/5230c30a-70fd-4bd1-9424-c8fd381728c3">

<img width="632" alt="Screenshot 2024-09-02 at 09 35 26" src="https://github.com/user-attachments/assets/376c56d7-58d4-4186-a36d-7284f3d99654">

<img width="969" alt="Screenshot 2024-09-02 at 09 35 58" src="https://github.com/user-attachments/assets/17b6592d-c7cd-4dc7-83d2-b7950b623996">




## Agile Development Process

### User Stories
User stories were created to capture the requirements and expectations of the end-users. These stories were used to guide the development process, with each story tied to a specific sprint.

### Sprints
The project was divided into multiple sprints. Each sprint focused on delivering a specific set of features, with tasks tracked and managed using [Agile Tool/Platform used].

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
- Users can submit testimonials.
- Admins can approve or reject testimonials.

### Comments
- Users can comment on blog posts.
- Comments are moderated by admins.
- **Reply to Comments**: Users can reply to specific comments, enabling threaded discussions.

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

### Reply Model (New)
- **Fields**: `comment`, `author`, `content`, `created_at`
- **Description**: Stores replies to specific comments, allowing users to engage in threaded discussions.

## Technologies Used

- **Backend**: Django (MVC Framework)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Version Control**: Git & GitHub
- **Deployment**: [Cloud Platform]

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
My project extends the functionality of the reference project by adding a `Testimonial` model, role-based access control, and enhanced admin features. The reference project is simpler, focusing primarily on the blog and comment system without these additional features. 

My project has a more comprehensive structure and user interaction model, but it doesn’t include a `Reply` model as I previously mentioned. My apologies for that error. Instead, my key differentiator is the inclusion of testimonials and more robust user roles.



## Installation & Setup
The site was deployed to Heruko App. The steps to do so are as follows:
- Launch Heroku app
- Select new app set up, name the game, select appropriate region
- Link github repository
- In settings of the app page, add Python and Nodes.js buildpacks
- Config Vars was set to the appropriate Cloudinary Platform, the approrpiate data base set up by code institute, and the secret keys. 
- Deploy the branch, let the game build itself, and the launch.


## Testing


## Deployment

The application is deployed on [Cloud Platform]. Follow the deployment guide in the `README` for detailed instructions.

## Contributing

Please follow the contribution guidelines in the `CONTRIBUTING.md` file.

