# Project Four: Full-Stack Web Application: Anna Rooney Coaching

## Overview

This project is a Full-Stack web application developed using the moodel-views-controler framework. The application includes a blog, testimonials, comment sections, inquiry form and front-end admin features. The development process followed Agile methodologies, ensuring iterative progress and continuous improvement through regular feedback.

## Design
A pinterest was set up to inspire the design of the website, which you can view [here](https://ie.pinterest.com/23annarooney/anna-website/). The mood of the website was strong female entreperneur.

Then Figma was used to design the layout and stylings. You can view the design [here]([https://github.com/NielMc/django_blog](https://www.figma.com/design/oDYCdAq0j987KhdHqZX7iE/anna-coaching?node-id=0-1&t=xUBvgB8R1oULULuY-1)). The idea was to have a home page, about me page, about you page (services) and a content page with links to youtube, blog and other content. The final design ended up being simpler, with just a home page, inquire page, blog page, login/out/register page, and for the super users, an admin page. 

The colors and fonts of the site: 
<div align="center"> 
    <img width = "33%" alt="Color theme" src="https://github.com/user-attachments/assets/fc8f2fa6-a305-4ad4-97d7-561c5457b864">
    <img width="50%" alt="fonts" src="https://github.com/user-attachments/assets/77bc35b3-44e3-4e6d-a461-1020bbdfe1b8">
</div>

## Visitor experiences

### As a first time visitor, I want to:

- See testimonials
- View the blog to get a sense of the life coach

### As a returning visitor, I want to:

- Sign up as a user
- Read the blog
- Comment on the blog
- Edit my comments if necessary

### As a frequent visitor, I want to:

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
- post and edit their posts
- press reply to inquiries, which redirects you to email
- archive/ unarchive inquiries.

Super users:
- can view all pages
- in admin, approve and delete coments
- in admin, approve, delete, edit blog posts
- press reply to inquiries, which redirects you to email
- archive/ unarchive inquiries.

### The layout: 

<img width="80%" alt="LANDING SECTION" src="https://github.com/user-attachments/assets/a43573fb-c821-4736-bf38-491250e8b78e">
<img width="80%" alt="ABOUT SECTION" src="https://github.com/user-attachments/assets/2ffcd78f-2ea0-4e70-b0db-ec3321c4eaa8">
<img width="80%" alt="INQUIRE SECTION" src="https://github.com/user-attachments/assets/b511281c-8810-4893-9107-1edb195f541b">
<img  width="80%" alt="CONTENT SECTION" src="https://github.com/user-attachments/assets/294e0110-1141-4fb9-b323-5acbfec78880">
<img width="80%" alt="FOOTER"  src="https://github.com/user-attachments/assets/498007a3-f06d-47c5-8f83-bb78da6058a8">

## Agile Development Process

### User Stories
User stories were created to capture the requirements and expectations of the end-users. These stories were used to guide the development process, with each story tied to a specific sprint.

### Sprints
The project was divided into multiple sprints. Each sprint focused on delivering a specific set of features, with tasks tracked and managed using github projects and issues: [Github projects](https://github.com/users/arir2001/projects/2): 

- **Sprint 1: Initial Setup & Core Features**
  - Setup model-views-controller framework: Established the project structure using Django. Basic template from [Code Institute's Blog app](https://github.com/NielMc/django_blog): 
  - User Authentication: Implemented user login, registration, and role-based access control.

- **Sprint 2: Blog & Testimonials**
  - Blog Functionality: Developed blog post creation, editing, and deletion.
  - Testimonials MODEL added.

- **Sprint 3: Comments & UI Enhancements**
  - Comment System: Enabled commenting on blog posts with moderation.
  - UI Enhancements: Improved UI elements and responsiveness.

- **Sprint 4: Admin Features & Deployment**
  - Admin Dashboard: Completed admin functionalities for content management.
  - Testimonial submissions, administration.
  - Final Testing & Deployment: Conducted testing, fixed bugs, and deployed the application.

## Features

### Blog
- Superusers can create, edit, and delete posts.
- Posts can include images, categories, and tags.

### Testimonials
- Registered users can submit testimonials which would then be approved by admins.
- These are then viewed on the index page in aa slide show. 

### Comments
- Users can comment on blog posts.
- Comments are moderated by admins, and to be viewed by public must be approved. 

### Admin Features
- **Dashboard**: Admins have access to a front end dashboard for managing site content.
- **Content Moderation**: Admins can approve or delete comments, testimoniaals
- **Blog**: Admins can write, edit, post, unpublish blogs. 

## Technologies Used

- **Backend**: Django (MVC Framework)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite, Cloudinary
- **Version Control**: Git & GitHub
- **Deployment**: Heroku

# Deployment
## Installation & Setup
The site was deployed to Heruko App. The steps to do so are as follows:
- Launch Heroku app
- Select new app set up, name the game, select appropriate region
- Link github repository
- In settings of the app page, add Python and Nodes.js buildpacks
- Config Vars was set to the appropriate Cloudinary Platform, the approrpiate data base set up by code institute, and the secret keys. 
- Deploy the branch, and launch.


## Testing
The website has been tested to ensure functionality, responsiveness, and data integrity across all views and features.

# In Lighthouse: 
- The original score was 62%. This was changed to 97 by uploading the images as webp instead of pngs. 
<div>
    <img width="80%" alt="Lighthouse Report" src="https://github.com/user-attachments/assets/38075c21-0250-4325-9820-9f639fbd9dd1">
</div>

# Django Testing

# Manual Testing
Views: Each view was manually tested to ensure correct functionality, such as page loading, navigation, and user interactions (e.g., posting and commenting).
Responsiveness: The website was tested across various devices (mobile, tablet, desktop) to ensure a consistent user experience.
# Automated Testing
The test_views.py files in the blog and home apps include tests for:

- View Accessibility: Ensuring views return the correct HTTP status codes (e.g., 200 OK for accessible pages).
- Template Usage: Verifying that the correct templates are rendered for specific views.
- Redirection: Testing that unauthenticated users are correctly redirected (e.g., to the login page).
- CRUD Operations: Tests for creating, editing, and deleting posts and comments.

There are also test_forms.py for both apps, which check if the forms are valid. 

# Running Tests
To run the tests locally, the following command was put into the terminal: python manage.py test.


