19th August 2024: 

Current Apps and models: 

Coaching project

Blog  -- app adapted from Code Institute Djaango Blog. 
- Post model
  -in django Admin, publish, archive, delete posts
- Comment model
  -in django Admin, publish, archive, delete comments
  - views.py linked so users can comment 

  Template Tags: 
  - blog_extras.py 
    - gets recent blog post, so index.html can link recent post in teaser div. 

Home
- Testimonial model
  -in django Admin, publish, archive, delete posts
  -views.py linked so div on index.html can display in slideshow


to do: 
css, html
-index.html page is a mess- use bootstrap to make sure everything is responsive!! Implement the correct photos on the landing page. 
- post_list.html : include a search bar for tags+title, change so instead of pagination is is an infitie scroll, allow for photos to be viewed on the card
- blogpost.html: allow for image to be included on head. 


models: 
- blog Post model: 
    allow for tags to be included so they can be found in search bar
    log in/log out page to allow the owner to post in a html page so no longer in django admin
    asllow commenters to be users, log in/log out

- comment model: allow people to comment in using their social medias

apps:
Client
- user portal model: allow clients view a portal with their homework, links to video calls, etc.
- goal model: allows user to track goals along a timeline, progress etc
- session model: tracks sessions and logs what happened.