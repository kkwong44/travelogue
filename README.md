# WorldTravelogue
WorldTravelogue is a free online travel diary for travellers across the world. It works from internet cafes and computers world wide, to allow you to update an online travel diary and share your experiences, it is free to join and takes just minutes to signup.
On this site the blogs are based on the theme in Travel and is a collection of tools so that travellers can write down a journal and share it to family, friends and other travellers. Photo and link to useful sites about the areas can be added to your blog. Also, comments can be added to the blog by other users so it can help out future travellers to the area.

Click [here](https://travelogue22kw.herokuapp.com/) to access live site.

*Screenshot - Mockup on WorldTravelogue App, generated from [Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/index.php)*

![Screenshot on Mockup](readme/images/mockup.png)

---

## Objectives
The main objective of this site is to provide a platform for travelers to keep a journal online and share it with families and friends as well as other travelers.

The target audients will be travelers who wants to post their journal and people who want to contribute and find out more about the travel destinations.

### Application Goals
* Create a community to share travel experiences on destinations across the world.
* A platform that allows the users to create and update their travel journal instantly and share it with families and friends.
* A platform that allows users to get information about the travel destinations by reading other people's posts.
* Administrators to control and maintain users and posts.

### User Goals
* Any users can view posts on the site.
* Signup to create posts with photos and descriptions.
* Registered users can maintain their personal posts.
* Registered users can leave comments and like posts by other users.
* Registered users can update and maintain their own account profile.

---
## Application Design

This application will be built using Bootstrap, Django and Cloudinary to store images. The final application will be deployed and running on Heroku.

### Initial Design

The following are initial wireframe designs to meet the main objective.

*Wireframe - Home Page*

![Wireframe on Home Page](readme/images/wireframe-home-page.jpg)

*Wireframe - Example of a Home Page after signin*

![Wireframe on User Home Page](readme/images/wireframe-signed-in-home-page.jpg)

*Wireframe - Post Detail Page*

![Wireframe on Post Detail Page](readme/images/wireframe-post-detail-page.jpg)

### Design Approach

The development approach on this project is based on the Principles of Agile and use the common agile practices.

The design has broken down into User Stories and grouped into Epics. Each User Story has been allocated its priority, story point and set acceptance criteria and tasks. Timeboxing approach will be used to process the product backlog.

**User Stories**

There are 37 user stories identified at the beginning of the project and they were grouped into 7 Epics as listed in the table below.

**[User Stories Full Detailed Report (Click to view)](readme/user-stories/user-stories.md#user-stories)**

*Summary of Epics and User Stories*

![Summary of User Stories](readme/user-stories/user-stories-summary.jpg)


### Process Map

The following is the process map for the site. The site can be accessed by non-registered users, registered users and administrators.

* Non-registered users have restricted access and only can view posts on the site.
* Registered users can create, read, update and delete posts. These users also have restricted access and only can manage their own posts.
* Administrators are users that have both access to the site and the control panel where they have full control to user profiles, posts and approve comments.

*Site Process Map*

![Process Map](readme/images/process-map.jpg)
___

## Project Requirements

This project has been developed using Python Django, Bootstrap and Deployed in Heroku. The following are the project requirements in order to run the application.

* Django
* Gunicorn
* dj_databases_url
* Psycopg2
* Cloudinary
* dj3_cloudinary_storage
* PostgreSQL
* Django summernote
* Django countries
* Django crispy Forms
* Django allauth
* Heroku
* Bootstrap v5.0.2
___

## Features

The aim of this site is to create a community to share travel experiences and let other potential visitors to find more information about the destinations.

In order to meet the aim and allow the community to grow. There are no restriction to visit the site but different access rights will be set to different user groups. The user groups have been defined into 3 different types for this site.

1. **Non-registered users**
    * Only allow to view posts and comments
    * Allow to register

2. **Registered users**
    * Allow to login
    * View posts, like or unlike and leave comment to other users’ posts
    * Create, Read, Update and Delete personal posts
    * View, update and delete personal account

3. **Administrators**
    * Allow to login
    * View posts, like or unlike and leave comment to other users’ posts
    * Create, Read, Update and Delete personal posts
    * View and update personal account
    * Access to control panel to perform site maintenance

This application has 2 separate sites:
* [Users site for general access - Frontend access](#frontend---header-and-footer)
* [Administrators site for maintenance - Backend access](#backend---administrator-control-panel)

### Frontend - Header and Footer

Users should be able to navigate and find information easily.

To help users to navigate and find information easily, all pages have a header with a navigation bar and a footer. The navigation bar items are depending on user access rights. Footer is where users can find the link to "Contact us" page and links to social media platform. Each social media link will be opened in a separate window.

#### Header for Non-Registered users

* Menu Items:

    * Home___About___Register___Login

![header-non-registered](/readme/images/header-footer-non-registered.png)

#### Header for Registered Users

* Menu Items:
    * Home___New Post___User Profile___About___Logout

![header-registered](/readme/images/header-footer-registered.png)

#### Header for Administrators

* Menu Items:
    * Home___New Post___User Profile___About___Control Panel___Logout

![header-administrators](/readme/images/header-footer-adminstrators.png)

#### Header and Footer with Collapsed Menu Bar For Mobile Devices

![header-collapsed](/readme/images/header-footer-collapsed.png)

### Frontend - Home Page

Users should able to view posts when they visiting this site.

When users visiting this site, they should be landed onto the home page. The home page is where all the published posts are listed and the site has set a maximum of 4 posts per page. Navigation buttons are available to select next and previous page when there are more than 4 posts.

#### Posts list in Home Page

Each Post has the following layout:

* Feature image - either a default or uploaded by the user
* Author's username
* Country that the post is related
* Post Title
* A summary description about the post
* A "Read more" button
* Date and time stamp when the post was created
* Number of likes for the post

![post-layout](/readme/images/post-listing.png)

#### Users Access Rights to Posts

Different user groups have different access rights to the posts.

#### *Access rights for Non-Registered users*

* Allow to register as a site member by clicking the "Register" from the menu bar
* Read about the site by clicking the "About" from the menu bar
* View individual post by clicking the "Read More" button from a post
* Select posts to view from popular country by clicking the country from the side widget named "Popular Countries"
* Select posts to view from a country by clicking the Country from a post
* Select posts to view from an author by clicking the Author from a post

![home-page-non-registered](/readme/images/home-page-non-registered.png)

#### *Access rights for Registered users*

* Allow to login to the site by clicking the "Login" from the menu bar
* Allow to create a new post by clicking the "New Post" from the menu bar
* Allow to view and update user profile by clicking the "User Profile" from the menu bar
* View individual post by clicking the "Read More" button from a post
* Select personal posts to view by clicking the username from the side widget named "My Posts"
* Select posts to view from popular country by clicking the country from the side widget named "Popular Countries"
* Select posts to view from a country by clicking the Country from a post
* Select posts to view from an author by clicking the Author from a post

![home-page-registered](/readme/images/home-page-registered.png)

#### *Access rights for Administrators*

* Allow to login to the site by clicking the "Login" from the menu bar
* Allow to create a new post by clicking the "New Post" from the menu bar
* Allow to view and update user profile by clicking the "User Profile" from the menu bar
* Allow to access to the control panel by clicking the "Control Panel" from the menu bar
* View individual post by clicking the "Read More" button from a post
* Select personal posts to view by clicking the username from the side widget named "My Posts"
* Select posts to view from popular country by clicking the country from the side widget named "Popular Countries"
* Select posts to view from a country by clicking the Country from a post
* Select posts to view from an author by clicking the Author from a post

![home-page-administrators](/readme/images/home-page-administrator.png)

#### Responsive on Mobile Devices

For mobile devices, 1 post per row and side widgets are re-arranged below the posts.

![home-page-collapsed](/readme/images/home-page-mobile.png)

#### Filter Posts

Users should be able to view posts that is more relevant to them.

This site can narrow down the posts by offering filters to the users by Country or Author.

#### Filter By Country

Select a country from the side widget for "Popular Countries" or the country from a post. All the posts related to the selected country will return as a new list. A message will say "No Posts Found!" when there are no posts for the selected country and the side widget shows the current filter is set to the selected country. Select "All" to clear the current filter.

![posts-filtered-by-country](/readme/images/posts-by-country.png)

#### Filter By Author

Select your own posts from the side widget for "My Posts" or an author from a post. All the posts related to the selected author will return as a new list. A message will say "No Posts Found!" when there are no posts for the selected author and the side widget shows the current filter is set to the selected author. Select "All" to clear the current filter.

![posts-filtered-by-country](/readme/images/posts-by-author.png)

### Frontend - Create New Posts

Registered users should allow to create new personal posts.

When a user signed in to the site then a new post can be created by clicking "New Post" from the menu bar.

Create a New Post form is presented to the user and all the mandatory fields need to be filled in before it can be submitted.

**Create a New Post Form**

![post-create](/readme/images/post-create.png)

### Frontend - Post Detail

Users should able to access the detail of each post.

All users can view post in details and read comments that associated with the post. Registered users can leave comments and like/unlike posts.

Each Detail Post has the following layout:

* Inside the Banner
    * Post Title
    * Author's username | Date and time stamp when the post was created
    * Country that the post is related
* Detail Section
    * Feature image - either a default or uploaded by the user
    * Edit and Delete buttons (Post's Owner Only)
    * A summary description about the post
    * A detail description about the post
    * Number of likes for the post
    * Number of comments for the post
* Comments Section
    * A list of comments from most recent first with Author and Date stamp
    * Leave a comment form with a Submit button (Registered Users Only)

#### Users Access Rights to Post Detail

Different user groups have different access rights to the post detail.

#### *Access Rights for Non-Registered Users*

* View post details only
* View comments only

![post-detail-non-registered](/readme/images/post-detail-non-registered.png)

#### *Access Rights for Registered Users*

* View post details
* Leave comment to any post
* Like/Unlike any post

![post-detail-registered](/readme/images/post-detail-registered.png)

#### *Access Rights for Owner's Post*

* View post details
* Leave comment to any post
* Like/Unlike any post
* Edit and update personal posts
* Delete personal posts

![post-detail-non-registered](/readme/images/post-detail-owner.png)

### Frontend - Leave Comment to a Post

Registered users should able to comment any posts

A form is available in the detail post where registered users can fill in and submit the form. The comment counter goes up by 1 when a comment has submitted successfully.

**Example of leaving a comment**

In this example, the author submitted a comment "Very tasty" and it appears on the left and the system ask whether the user wish to leave another comment. Select the "Add Another Comment" takes the user back the comment form and select "Go Back" takes the user back to the home page.

![leave-comment](/readme/images/comment-add.png)

### Frontend - Like/Unlike Post

Registered users should able to like/unlike any posts

The option to like or unlike a post is available in the detail post and it is in a form of a "Heart" shape.

* It should be grey out for non-registered users
* Click to toggle between like or unlike post
    * Red outline heart shape means the current user has not liked the post yet
    * Solid heart shape means current user liked the post
    * Likes counter goes up or down by 1 when toggle between like and unlike post

### Frontend - Edit Personal Post

Registered users should able to edit and update personal posts

When the registered user signed in to the site and select a personal post then the post can be updated by submitting the form.

**A Form to Edit and Update Post**

![edit-post](/readme/images/post-edit.png)

### Frontend - Delete Personal Post

Registered users should able to delete personal posts

When the registered user signed in to the site and select a personal post then the post can be deleted.

**Confirmation Message to Delete a Post**

![edit-post](/readme/images/post-delete.png)

### Frontend - User Accounts

Users should be able to create, read, update and delete their own account profile.

The site allows viewers to create an account. After signed in to the account, the owner can view, update and delete their account profile.

#### Create an Account

Select Register from the menu bar, fill and submit the form.

![account-create](/readme/images/account-register.png)

#### Sign in to an Account

Select Login from the menu bar,  fill and submit user details

![account-login](/readme/images/account-login.png)

#### Sign out from Account

Select Logout from the menu bar and confirm sign out.

![account-logout](/readme/images/account-logout.png)

#### View an Account Profile

Login and select User Profile from the menu bar

![user-profile-read](/readme/images/user-profile.png)

#### Update an Account Profile

Login and select User Profile from the menu bar

Edit and select Update to update profile

![user-profile-update](/readme/images/user-profile.png)

#### Change an Account Password

Login and select User Profile from the menu bar

Select Change Password

Fill details and submit changes

![user-profile-change-password](/readme/images/user-propfile-change-password.png)

#### Delete an Account

Login and select User Profile from the menu bar

Select Delete and confirm delete account

![user-profile-delete](/readme/images/user-profile-delete.png)

### Frontend - About Page

Users should able to find more information about the site.

The About page offer information about the site and the user can access it by selecting "About" from the menu bar.

![about-page](/readme/images/about-page.png)

### Frontend - Contact us Page

Users should able to contact the site support team.

The Contact us page contains information for user to contact the support team and can be access by selecting "Contact us" in the footer.

![contact-us-page](/readme/images/contact-us-page.png)

### Frontend - Message Bar

Users should be able to confirm actions have been performed.

On this site, a message bar has been created to confirm action has been performed. Message only appears for 3 seconds when the action has been performed. Examples are Login and Logout successfully, Post and Comment added successfully.

**Message shows signed in as admin**

![message](/readme/images/message.png)

### Backend - Administrator Control Panel

Site administrators need a facility to maintain users, posts and comments.

Django administration allows to extend the basic features in the control panel. This has been modified to offer extra functionalities to maintain the blog posts and comment.

Site superuser account need to be created in order to access to the control panel via the site or URL link by adding "/admin" to the home page url.

**Control Panel - Login Page**

![Control-Panel-login](/readme/images/control-panel-login.png)

**Control Panel - Home Page**

![Control-Panel-Home-Page](/readme/images/control-panel.png)

#### Blog Posts

This is the section to maintain the posts in the blog application. The standard features in this section allows to Create, Read, Update and Delete posts.

Following are customised features:
* List Display
    * Display Fields: Title, Country, Status and Created On
* Search Bar
    * Search fields: Title, Country and Content
* Filters
    * By Status
    * By Created On
* Action in Bulk
    * Delete selected posts
    * Publish posts
    * Disapprove posts

![control-panel-posts](/readme/images/control-panel-posts.png)

#### Blog Post Comments

This is the section to maintain the comments in the blog application. The standard features in this section allows to Create, Read, Update and Delete comments.

Following are customised features:
* List Display
    * Display Fields: Name, Body, Post, Created On and Approved
* Search Bar
    * Search fields: Name, email and body
* Filters
    * By Approved
    * By Created On
* Action in Bulk
    * Delete selected comments
    * Approve Comments
    * Disapprove Comments

![control-panel-comments](/readme/images/control-panel-comments.png)

#### User Profiles

This is the section to maintain the user profiles in the travelogue project. For this initial phase the profiles are only extension of the users from the Authentication and Authorization section. Additional features can be added to the profiles in future development.

___
## Future Features

Five user stories were decided not to be included at the initial phase of the project. These can be implemented in the next milestone.

The user stories are:

* Reset Password
    * User able to reset forgotten password
* Filter by Country
    * User able to filter posts from list of all countries
* Sort Posts
    * User able to sort posts by fields such as date and country
* Contact Form
    * Provide users a contact form
* Response to Request
    * Initial response to contact form automatically by email

As mentioned in the features section that current User Profiles is only an extension of users from Django table. The intention of the user profiles is to provide additional future features such as user’s photo or avatar, social media accounts and date joined as a member.

The site can greatly improve by allowing multiple images to upload and display in a post.

Another feature is to create an image gallery so viewer can view all images by an author or a country.

___
## Validator Testing
___
## Testing

For this project, tests have been carried out using both Django Unit Tests and Manual Tests.

**Django Unit Tests**

These are automated tests by executing test scripts from the terminal. In this project, only URLs have been tested in this method.

There are 10 URLs tests and they all passed the test.

* Test 'home' url
* Test 'popular country' url
* Test 'posts by author' url
* Test 'detail post' url
* Test 'like/unlike' url
* Test 'create new post' url
* Test 'edit/update post' url
* Test 'delete post' url
* Test 'about' page url
* Test 'contact us' page url

*Test Results*

![unit-tests-results](/readme/testing/unit-tests.png)

**Manual Testing**

Functional testing on this project has been carried out by executing the test scripts as defined below in the test report.

**[Manual Tests Report (Click to view)](readme/testing/testing.md#manual-testing-for-travelogue22kw-project)**

___
## Bugs

During testing, it was noticed that there is an 'Uncaught TypeError' showing in the console log. The error shown below indicates there is a problem with bootstrap. This error seems to be resolved by correcting the version of bootstrap. Futher monitoring is recommended to confirm this bug has fixed throughout the site.

![bug-error-log-1](/readme/testing/bug-console-log1.jpg)

![bug-error-log-2](/readme/testing/bug-console-log2.jpg)

___
## Deployment

This is a Django project and deployed in Heroku.

At the beginning of the project, a simple skeleton Django project was deployed to Heroku to ensure the project is connected and running sucessfully in Heroku.

The final version of code at each phase of the project is then needs to deploy to Heroku so the site is running the latest version of the project.

The deployed app can be found [here](https://travelogue22kw.herokuapp.com/).

### Development tools
* GitHub is a code hosting platform for version control and collaboration
* Gitpod is a ready-to-code developer environment
* Heroku for building, deploying, and managing apps

### Development processes

* All the development works are carried out in Gitpod
* Create a repository in Github through Gitpod
* Start the project from a template written by Code Institute. The full template can be copied from [here](https://github.com/Code-Institute-Org/gitpod-full-template)

    **Repeat the following until project completion**

* Developing your site, save your project in your Gitpod workspaces
* Use git add command to add files to local repository
* Use git commit command to commit the changes to local repository

### Deployment to Github Pages

* Use git push to upload local repository content (Gitpod) to a remote repository (Github)
* The latest code pushed to Github then can be deployed to Heroku

***You can use GitHub Desktop to clone and fork repositories that exist on GitHub.***

Click [here](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop) for more information on Cloning and forking repositories from GitHub Desktop.

### Steps for Setting up basic Django Project and Deploying to Heroku

The following are the steps to setting up Django project and deploying to Heroku.

![Deployment-1](/readme/images/deployment-1.png)
![Deployment-2](/readme/images/deployment-2.png)
![Deployment-3](/readme/images/deployment-3.png)
![Deployment-4](/readme/images/deployment-4.png)
![Deployment-5](/readme/images/deployment-5.png)
![Deployment-6](/readme/images/deployment-6.png)
![Deployment-7](/readme/images/deployment-7.png)

___
## Tools
The tools used to carry out the development and deployment on this project are:
* Gitpod and Github
* Python modules
* Django and libraries
* Cloudinary
* Chrome Dev Tools
* Webpage Screenshots - Chrome app extension (FireShot)
* [Lucid Chart](https://www.lucidchart.com/) for creating flow chart
* [PEP8 online checker](http://pep8online.com/) for code validation
* [Heroku](https://id.heroku.com/login) for building, deploying, and managing apps
* [Pixerbay](https://pixabay.com/) for images

___
## Credits

* [Template](https://github.com/Code-Institute-Org/gitpod-full-template) created by [Code Institute](https://codeinstitute.net/)
* [W3Schools](https://www.w3schools.com/python/default.asp) for research, examples and techniques in Python programming
* [Bootstrap](https://getbootstrap.com)
* [Bootstrap Templates](https://startbootstrap.com)
* [Django Testing Tutorial - Youtube By The Dumbfounds](https://www.youtube.com/watch?v=qwypH3YvMKc&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=1)
* [Django Filter And Pagination - Youtube by TauhidCodes](https://www.youtube.com/watch?v=dkJ3uqkdCcY&t=1138s)
* Code Institute Full Stack Framework tutorials

___
## Acknowledgment

I would like to thank the following to support the development of this site.

* Learning Support - Code Institute
* Mentoring Support - Daisy McGirr