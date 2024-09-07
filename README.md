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
## INDEX PAGE
<img width="80%" alt="LANDING SECTION" src="https://github.com/user-attachments/assets/a43573fb-c821-4736-bf38-491250e8b78e">
<img width="80%" alt="ABOUT SECTION" src="https://github.com/user-attachments/assets/2ffcd78f-2ea0-4e70-b0db-ec3321c4eaa8">
<img width="80%" alt="INQUIRE SECTION" 2024-09-07 at 20 24 10" src="https://github.com/user-attachments/assets/6601ccdb-0530-4ee5-8b29-f0f38eb305a5">
<img width="80%" alt="TESTIMONIAL SECTION" src="https://github.com/user-attachments/assets/64c62832-ce6c-413d-909c-47ebc0300221">
<img width="80%" alt="FOOTER, CONTENT SECTION"   src="https://github.com/user-attachments/assets/c558666e-1f3e-401c-a48d-4c90e34d68b3">

## INQUIRE PAGE
<img width="80%" alt="INQUIRE" src="https://github.com/user-attachments/assets/1f5757fb-6ef3-44a7-9faa-22e4031b775e">

## BLOG PAGE
<img width="80%" alt="POSTS"  src="https://github.com/user-attachments/assets/1b281ece-f4db-4ce1-aaf4-956aec68affc">
<img width="80%" alt="BLOG PAGE" src="https://github.com/user-attachments/assets/da5b8afa-e119-4ec6-bcc9-5c828892dc37">
<img width="80%" alt="COMMENTS ON BLOG PAGE" src="https://github.com/user-attachments/assets/42375f57-6f2a-4b24-a9d2-06420f776755">
<img width="80%" alt="COMMENT AWAITING APPROVAL" src="https://github.com/user-attachments/assets/02ba6aad-b819-43f2-acf1-66d25ca8cddf">

## ADMIN PAGE
<img width="80%" alt="ADMIN PAGE" src="https://github.com/user-attachments/assets/d81d55f9-4a86-4562-a7c0-cf2f5eb5d416">
<img width="80%" alt="POST ADMIN PAGE" src="https://github.com/user-attachments/assets/ee6cef8a-1e2d-4205-840b-1792ad272666">
<img width="80%" alt="CREATE POST ADMIN PAGE" src="https://github.com/user-attachments/assets/ec9efe9e-ecdb-4964-9604-aecca430ef03">
<img width="80%" alt="COMMENTS ADMIN PAGE"  src="https://github.com/user-attachments/assets/7652913e-1d8c-44f1-bba9-f234c47516a4">
<img width="80%" alt="INQUIRIES PAGE" src="https://github.com/user-attachments/assets/5e43656c-c648-485e-ab6a-497cc5228a14">
<img width="80%" alt="TESTIMONIALS ADMIN PAGE"  src="https://github.com/user-attachments/assets/6e252ea8-cdb2-4b17-a061-804c7e402ac3">

## SUBMISSION PAGE
<img width="80%" alt="TESTIMONIALS SUBMIT PAGE" src="https://github.com/user-attachments/assets/208e816d-ab27-4725-be38-7b4ee4bf00b5">

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
- These are then viewed on the index page in a slide show. 

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

# Manual Testing
Views: Each view was manually tested to ensure correct functionality, such as page loading, navigation, and user interactions (e.g., posting and commenting).
Responsiveness: The website was tested across various devices (mobile, tablet, desktop) to ensure a consistent user experience.

# Django Testing
# Automated Testing
The test_views.py files in the blog and home apps include tests for:

- View Accessibility: Ensuring views return the correct HTTP status codes (e.g., 200 OK for accessible pages).
- Template Usage: Verifying that the correct templates are rendered for specific views.
- Redirection: Testing that unauthenticated users are correctly redirected (e.g., to the login page).
- CRUD Operations: Tests for creating, editing, and deleting posts and comments.

There are also test_forms.py for both apps, which check if the forms are valid. 

Running THE Tests:
To run the tests locally, the following command was put into the terminal: python manage.py test.

## HTML, CSS, JS TESTING 

### HTML
https://validator.w3.org/nu/
In the html checker, there were a few issues with unclosed divs. These errors were due to the nature of django templates, and though effort was taken to ensure proper indentation, this cannot be avoided in django. 
<div>
    <img width="45%" alt="html index page checked" src="https://github.com/user-attachments/assets/830769c5-e076-4fa1-8825-9124ae087578">
    <img width="45%" alt="html testimonial page checked"  src="https://github.com/user-attachments/assets/4e0425ca-4ee4-4f21-9d63-91149a7e46c7">
</div>
<div>
    <img width="45%" alt="html collaborate page checked" src="https://github.com/user-attachments/assets/eb6bbd83-801c-48b2-859f-9792cb24f612">
    <img width="45%" alt="html blog post page checked"  src="https://github.com/user-attachments/assets/f10aa539-092b-41f8-a0d3-eee8c4f626af">
</div>
<div>
    <img width="45%" alt="html individual post page checked"  src="https://github.com/user-attachments/assets/2456681b-afed-414c-a84d-8ba8beeb143d">
    <img width="45%" alt="html blog post page checked"  src="https://github.com/user-attachments/assets/f10aa539-092b-41f8-a0d3-eee8c4f626af">
</div>
<div>
    <img width="45%" alt="html individual post page checked"  src="https://github.com/user-attachments/assets/2456681b-afed-414c-a84d-8ba8beeb143d">
    <img width="45%" alt="html blog post page checked"  src="https://github.com/user-attachments/assets/f10aa539-092b-41f8-a0d3-eee8c4f626af">
</div>

- each an every page was checked, with any errors only being the django template issues, and so for levity, only a few screenshots are uploaded. 
- The only exception were the pages in which the summer note form is inserted in the page, like the post creation page. These errors cannot be helped as thee html checker does not understand the nature of the summernote widget being inserted.
<img width="75%"  alt="summer note errors" src="https://github.com/user-attachments/assets/5cf5e88b-a2ad-4c5f-b0f3-22d6c1cbbd46">
These errors did not affect the user experience.

### CSS
https://jigsaw.w3.org/css-validator/
There were no CSS errors.
<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

### JS : 
https://jshint.com/
In JS hint, all JS files were compiled. This was the analysis: 
There are 13 functions in this file.

Function with the largest signature take 1 arguments, while the median is 1.

Largest function has 17 statements in it, while the median is 4.

The most complex function has a cyclomatic complexity value of 5 while the median is 1.

There were no errors. 

### PYTHON: 
https://pep8ci.herokuapp.com/
The CI python linter checked the python code according to pep 8 guidelines: 
<img width="80%" alt="" src="https://github.com/user-attachments/assets/65a36454-96d6-4519-ba93-c1f0e989d6ca">


