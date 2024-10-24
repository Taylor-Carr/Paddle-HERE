# PaddleHere - Taylor Carr

![Responsive](/static/images/readme/responsive.png)


---


## Contents

  
-  [Project Overview](#project-overview)

-  [Site Users' Goals](#site-users-goals)

- [Site Owner's Goals](#site-owners-goals)

- [Current Features](#current-features)

- [Future Features](#future-features) 

- [Project ERD and Database Design](#project-erd-and-database-design)

- [Development Strategy](#development-strategy)

- [Wireframes](#wireframes)

- [Flow Chart](#flow-chart)

- [Frontend Design](#frontend-design)

- [Manual Testing](#maunal-testing)

- [Deployment Process](#deployment-process)

- [Tech Stack and Tools used](#tech-stack-and-tools-used)

- [Credits](#credits)

  
---


## Project Overview

 
**PaddleHere** - is a blogging platform designed to enable users to discover, share and find paddle boarding, surfing and kayaking locations in and around the UK. Our mission is to create a community where enthusiasts can connect and share there experiences.


---


### Site Users' Goals:


- **Discover Locations and Compare Experiences**: Users can search for and find paddle boarding, surfing and kayaking locations (spots) within the UK They can also read others' experiences and reviews of these locations.

- **Share Locations and Experiences**: Users can create and share their own posts that include locations specific title, country, caption, images, tags, proficiency level. This allows them to document their adventures in detail and contribute to the wider community.

- **Engage with Community**: Users can interact with others by commenting on posts, liking posts and comments and viewing other users profiles and previous posts.
 

### Site Owner's Goals:

- **Facilitate Discovery**: Enable users to easily locate new paddle boarding, surfing and kayaking locations.

- **Encourage Interaction**: Allow Users to engage with content through comments and likes.
 

### Current Features
  
- **User Authentication**: Users can register and log in to their accounts, creating profiles that showcase their experiences and preferences.

- **Profile Managaement**: Users can manage their profile including adding a profile picture, banner image, bio and proficiency level, helping to personalise there experience on the platform 

- **Blog Post Creation**: Users can create and update their blog posts related to their chosen sport within the categories. Each post can include A location specific title, location and country (pre defined), a caption, image, a pre defined tag and their opinion on the profficency level related to the location.

- **Commenting System**: Users can respond to posts via comments, facilitating disussions and promoting enagagement within the community.

- **Like Funcionality**: Users can like posts and comments, helping users to identitfy popular location or opinions of locations/posts.

- **Categories**: Users can filter blog posts by category, these categorys are pre defined by sport. 

- **Search Functionality**: Users can search blog posts more specifically through exact location, country or sport.



### Future Features 

- **Saving Posts**: Users will be able to save their favourite blog posts to re visit at a later date.

- **Current Weather API**: Users will be provided with current weather condition at the location of the blog post.

- **Google Maps API**: Users will be able to quickly find the exact location of a post through an interactive map, othering directions and a visual representation of the location.

---

## Wireframes

  
![PaddleHere - Landing Page](/static/images/readme/wf1.png)

  

![PaddleHere - Blog Posts Page](/static/images/readme/wf2.png)

  

![PaddleHere - Blog Details Page](/static/images/readme/wf3.png)
  

### Project ERD and Database Design

  

![Project ERD](/static/images/readme/phdatachsheme.png)

  

## Flow Chart

  

![FlowChart](/static/images/readme/phflowchart.png)

  

## Developement Strategy 

  
To implement an agile development methodology, I utilized GitHub Projects as my primary tool. I documented prioritized user stories and additional features, ensuring that a Minimum Viable Product (MVP) could be effectively achieved.

![GitHub Projects](/static/images/readme/kanbanph.png)

  
---

## Frontend Design

**PaddleHere** is a fully responsive, mobile-first website desinged with the on-the-go users in mind. Mobile usability was a key consideration throughtout the design proccess, resulting in features such as:

- **Card Layouts** familiar to IOS users.

- **Back Buttons** for intuitive navigation.

- **Bottom-Placed Buttons** for easy access on mobile and tablet devices.

### Colour Scheme

The design features a muted colour palette with:

- **Light Blue Accents** to tie in with the overall watersports theme.

- A prodimently **Off white background** to highlight blog posts and other ui elements.

- **Bottom-Placed Buttons** for easy access on mobile and tablet devices.

### Typography

The typography was chosen to reflect the brands identity and over all theme of the website aswell as maintaining readability:

- **Genty** is used for the brand logo, offering a surfer-inspired look. 

- **Montserrat** is used across the site for its headings, body text and key details (such as author headings, post timestamps etc) due to it's readability and versatility.

---

## Manual Testing
 
Each section of the site was manually tested to ensure it functions as expected, including buttons, links, input fields, and navigation. Tests covered both "happy flows" (where everything works as intended) and exception/bad flows (handling incorrect input or edge cases).

## 1. Buttons & Links

**Expected:**  
- Buttons should trigger the appropriate action (e.g. submission, navigation) when clicked and return a success or error message if related to a form submission. 
- Links should navigate to the correct page or section.

![Profile before](/static/images/readme/userstoryfirst.png)
![Profile after](/static/images/readme/userstorysecond.png)

**Testing:**  
- Clicked on all buttons, including "Submit," "Edit," and "Delete" on posts and comments.
- Tested all navigation links from the navbar, navbar dropdown, footer, and internal links.

**Result:**  
- All buttons and links responded as expected.
- All functions with related success and error messages work as intended.

**Fix:**  
- No fixes were necessary.

## 2. Responsive Design Testing

To ensure a seamless user experience across devices, I used a responsive design checker.

![Responsive](/static/images/readme/responsive.png)

## 3. Code Validation

Validation tools were used to check the quality of the HTML and CSS for compliance with web standards.


### HTML & CSS Validation

![CSS validation](/static/images/readme/cssvalidation.png)

**Tools Used:**  
- W3C Validator for HTML  
- CSS Validator for CSS

**Result:**  

#Validation errors for html: 

- Figcaption elements were not nested in figure elements.
- Div nested in header title H1 element.
- Form select inputs had a max input of characters. 

**Fix:**  
- Figcaptions were nested in figure elements.
- Nested div in header title H1 was changed to a span element.
- Max characters in form select inputs were removed.


## 4. Testing User Stories and Features

Every user story and corresponding feature was tested to ensure it meets the outlined functionality.

### User Sign Up & Sign In

**Expected:**  
- Users should be able to sign up, sign in, and access personalised content such as blog post details, user profiles (theirs and other users'), commenting, liking and searching by location and or filtering by sport.
- Unauthorized users should be prevented from accessing any part of the site beyond the public homepage.

**Testing:**  
- Attempted to register accounts using both valid (e.g., correct email and password) and invalid inputs (e.g., missing fields, weak passwords).
- Successfully logged in with registered accounts and verified redirection to user profile page creation.
- Attempted to access restricted pages without logging in to confirm proper redirection to the homepage.

**Result:**  
- User registration was successful, with appropriate success messages for valid inputs and error messages for invalid inputs displayed clearly.
- Account creation successful message displays, prompting user to edit profile.
- The login/logout process worked seamlessly, correctly redirecting users to the auth or un-auth home page after logging in and after logging out.
- Unauthorized users were correctly blocked from accessing restricted content, maintaining site security.

---

### Search Functionality

**Expected:**  
- Users should be able to input a specific location, country or sport into the search bar and receive relevant blog posts in response.
- Users searching with invalid search terms or for empty categories / locations should recieve a message notifying them that there are no results for their query.

**Testing:**  
- Conducted searches using various keywords, including partial words and phrases, to assess search accuracy and relevance.

**Result:**  
- Search functionality operated as expected, returning accurate blog post results that matched the entered search term.
- Incorrect search terms would return a message notifying them that there are no results for their query.

---

### Category Filtering

**Expected:**  
- Users should be able to filter blog posts based on pre defined categories (paddle boarding, surfing, kayaking) to find content relevant to their chosen sport.

**Testing:**  
- Tested the filtering system by creating posts in different categories and selecting different category links on the home page and observing the resulting post lists for accuracy.

**Result:**  
- The filtering feature functioned correctly, displaying only the posts associated with the selected category.

---

### Commenting

**Expected:**  
- Users should have the ability to comment on blog posts facilitating user interaction, users should also be able to edit and delete their own comments.

**Testing:**  
- Posted multiple comments on various blog entries from various accounts.

**Result:**  
- Commenting feature worked as expected, with real-time updates displayed on the post. Users weren't able to delete or alter other users comments.

---

### Liking Comments and Posts

**Expected:**  
- Users should be able to like comments and posts made by other users, indicating approval and fostering interaction.
- Only one like should be given for that given user on the given post or comment. 
- If un-liked, the like should be removed, effecting the overall number of likes.

**Testing:**  
- Liked various comments and blog posts on various different accounts to verify that the like feature was functional.

**Result:**  
- The liking and un-liking functionality performed as expected, with a clear increase and decrease in like counts displayed immediately. Users could not like the same post or comment more than once.

---

### Profile Management

**Expected:**  
- Users should be able to update their profile information (such as bio, banner image, profiency level and profile picture) and delete their accounts if desired.
- When a user profile is edited they recieve a success message.
- User should only be able to alter their own profile. 
- Profile pages should also display a users previous blog posts giving them the option to quickly find, edit or delete their posts. Or promt them to share a post if they have no previous posts.

**Testing:**  
- Updated all profile fields, including changing and deleting the profile picture and banner image, re-writing bio, changing profiency level. 
- Uploading blog posts before and after updating profile.
- Visted various other user profiles. 

**Result:**  
- Profile updates were processed successfully, with users receiving confirmation messages for change was made. Account deletion was effective, removing the user data as expected while notifying users of the outcome.
- Users could not alter other users profiles, only profile owners were presented with the option to delete or update their profile.
- After creating posts for specific users and performing updates to their profiles, the recent blog post were un-affected and rendered correctly for the author of the post on their profile.

---

### Adding Posts

**Expected:**  
- Users should be able to create, edit and delete there blog posts with a specific location of there choosing, a country (pre defined), in a category (pre defined), with a description, an image, a pre defined tag, profficiency level related to the location.

**Testing:**  
- Created multiple posts using valid inputs and or empty fields including text and image uploads, and verified their visibility on the blog and within their chosen category and search term.
- Deleted blog posts specific to the sign in author.
- Attemped to edit and delete other users blog posts.

**Result:**  
- The post-creation functionality worked as intended, with new posts appearing immediately on the site home page and on the relative profile pages of the author, and confirmation messages were displayed successfully.
- Users could not delete or alter a post they were the author of.

---

### Editing Posts

**Expected:**  
- Users should be able to edit or delete their existing blog posts to update content or correct mistakes.

**Testing:**  
- Deleted and edited several posts, changing specific locations, caption(body text), tags, proffiency levels, images, category and country. Then saved the changes to verify updates.

**Result:**  
- Post editing operated smoothly, reflecting changes immediately on the site, with users receiving confirmation of successful edits.


## 5. Bug Documentation

Any bugs encountered during development were documented, including steps to reproduce, analysis, and resolution.

### Bug: Inconsistent Category Links

![Category bug](/static/images/readme/categorybug.png)

**Description:**  

- Category links on posts were dynamically generated based on user-created categories, leading to inconsistencies in the displayed categories as new posts were added.

**Testing:**  
- Tested the behavior by creating multiple posts with different categories and observed that the links were not aligned with predefined category options.


**Result:**  
- Categories appeared incorrectly, causing confusion and navigation issues for users.

**Fix:**  
- Decoupled category display from user input by implementing a predefined set of categories. I ensured that only these categories were rendered as clickable links, resulting in consistent behavior across the site.


---

# Deployment Process

This outlines the steps I followed to deploy my Django application to Heroku.

## Prerequisites

Before starting, I ensured the following:

- A **Heroku** account was created.
- My project was fully tested locally and ready for deployment.
- Set DEBUG to False.


## Steps I Followed

### 1. Create a Procfile

I created a `Procfile` in the root directory of my project to instruct Heroku on how to run the application.

### 2. Log in to Heroku

- I logged in to the [Heroku dashboard](https://dashboard.heroku.com/).

### 3. Created a New App on the Heroku Dashboard

- I clicked on **New** > **Create New App**.
- I chose a unique app name and selected my region.
- I clicked **Create App**.

### 4. Configure Environment Variables

- I navigated to the **Settings** tab in Heroku.
- In the **Config Vars** section, I clicked **Reveal Config Vars** and added the my environment variables.

![Config](/static/images/readme/config.png)


### 5. Set Buildpacks

- In the **Settings** tab, I located the **Buildpacks** section.
- I clicked on **Add Buildpacks** and selected **Python** as the buildpack.

![Packs](/static/images/readme/packs.png)

### 6. Connect GitHub to Heroku

- From the **Deploy** tab on the Heroku dashboard, I selected **GitHub** as the deployment method.
- I searched for my repository name and clicked **Connect** to link the repository to my Heroku app.

![Connect](/static/images/readme/connect.png)

### 7. Enable Automatic Deploys

- Under **Automatic Deploys**, I enabled automatic deployment from the main branch on GitHub.
- I triggered a manual deploy for the first deployment using the **Deploy Branch** button.

![Deploy](/static/images/readme/deploy.png)

### Live Application

You can view the live application by clicking the link below:

[Visit the Heroku Site](https://paddlehere-0bbeb424045b.herokuapp.com/)

---

## Tech Stack & Tools Used

- **Lucid**: For wireframing and diagraming

- **GitHub Projects**: For project management and mapping of user stories.

- **GitHub**: Used for version control.

- **HTML5**: Markup language for structuring the content.

- **CSS3**: For styling and responsive design.

- **Bootstrap**: For responsive front-end design.

- **JavaScript**: For client-side functionality and interactive elements.

- **Python**: Used for back-end programming and logic.

- **django**: Used as the back-end framework.

- **Cloudinary**: For image storage.

- **Heroku**: For deploying the back-end application.

  

## Credits

Special thanks to the following people and resources for their guidance and support:


- **David Calikes**, **Kevin** and **Martin** at Code Institute for their exceptional guidance and support.

- **Alls Well** - Hackathon project for inspiration.

- **Codemy**

- **Hero Image** - **Matt-Zhou** - Unsplash




