# Little Pont - Testing

![Responsive Mockup]()


## Contents
* [Manual Testing](#testing)
  * [Testing User Stories](#testing-user-stories)
  * [Testing Site Functionality](#testing-site-functionality)
  * [Further Testing](#further-testing)
* [Automated testing](#automated-testing)
  * [HTML validation](#html-validation)
  * [CSS validation](#css-validation)
  * [Javascript validation](#javascript-validation)
  * [Python validation](#python-validation)
  * [WAVE Testing](#wave-testing)
  * [Lighthouse](#lighthouse)
* [Bugs](#bugs)
  * [Fixed Bugs](#fixed-bugs)

- - - 

## Manual Testing 

-   ### Testing User Stories

    -   #### Viewing and Navigation

        1. As a site user, i want to be able to view the website on a range of device size and it needs to be aestheitc and functional
        2. As a parent/guardian, i want to easily understand the purpose of the webite
        3. As a parent/guardian, i want to be able to view course details to understand which course is suitable for my child.
        4. As a parent/guardian, i want to be able to see the available courses, the course dates and times so that i can decide if it is suitable to book.
        4. As a registered site user, i want to view the contents of my shopping basket and be able to add, edit or delete any items in it. 
        5. As a registered site user, i want to have a personlalised profile where i am able to view my order history and update my profile details
        6. As a parent/guardian, i want to be abe to meet the team who run the courses and understand more about them and their qualifications so that i know the sessions are being run by competent pracitioners
        7. As a parent/guardian, i want to be able to see where the courses are being held so that i know where i am going to be travelling to and can plan my journey
        8. As a site user, i want to be able to contact the site owners if i have any queries and recieve email confirmation that my message has been successfully sent
        9. As a parent/guardian, i want to be able to make a party booking enquiry
        
    
    -   #### Registration and User Account

        1. As site user, i want to be able to easily register and account
        2. As a registered user, i want to easily be able to login and logout of my account
        3. As a registered user, i want to be able to recover my password if i have forgotten it
        4. As a registered user, i want to recieve an email to confirm that i have successfully regitered an account
        5. As site admin, i want to ensure all form fields are completed correctly
        6. As a site user i want to be able to edit or update my profile details

    -   #### Purchasing and Checkout
        1. As a parent/guardian, i want to select and purchase a course for my child
        2. As a site user, i want an easy and streamlined payment process
        3. As a site administrator, i want to be able to track all course bookings to ensure that they are processed correctly and payment is recieved

    -   #### Site Administrator

        1. As a site admin, i want to be able to easily add, edit and delete courses so that i have full control over what courses i make available to the user
        2. As a site admin, i want to easily be able to add, edit or delete a users order in case they have made a booking error and it needs to be ammended, in order to provide a good user experience for them.
        3. As an admin, i want to have a clear view of courses, bookings and payment status to ensure good business management
        

- - -

-   ### Testing site functionality

| Feature/Site Page                                            | Expected Outcome                                                                                                                     | Testing Performed                                                                      | Result                                                                                                                                                                          | Pass/Fail |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| NAVBAR/HEADER                                                |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
| 'My Account' dropdown as logged out user                     | When clicked a dropdown appears showing Register and Login to logged out user                                                        | As a logged out user, clicked My Account                                               | Dropdown appears with Register and Login options                                                                                                                                | PASS      |
| Login in 'My Account' dropdown                               | When clicked, navigates to Login page                                                                                                | Clicked Login in 'My Account' dropdown                                                 | Taken to Login page                                                                                                                                                             | PASS      |
| Register in 'My Account' dropdown                            | When clicked, navigates to Register page                                                                                             | Clicked Register in 'My Account' dropdown                                              | Taken to Register page                                                                                                                                                          | PASS      |
| Register button on Login page                                | When clicked, navigates to Register page                                                                                             | Clicked Register button on Login page                                                  | Taken to Register page                                                                                                                                                          | PASS      |
| Login button on Register page                                | When clicked, navigates to Login page                                                                                                | Clicked Login button on Register page                                                  | Taken to Login page                                                                                                                                                             | PASS      |
| Register user on Register page                               | Completed regitration form on Register page                                                                                          | Correctly completed input fields, clicked Register button                              | Taken to Verify Email page with Alert Message informing user that a verification email has been sent to their email                                                             | PASS      |
| Verification Email                                           | Complete new user registration and direct user to login page with prefilled login input fields                                       | Clicked link in verification email and taken to Login page with success message        | Successfully registered new user                                                                                                                                                | PASS      |
| 'Back to Login' button on Register page                      | Takes user to Login page                                                                                                             | Clicked Back to Login button                                                           | Taken to Login page                                                                                                                                                             | PASS      |
| Home button on Login page                                    | Takes user to Home page                                                                                                              | Clicked Home button                                                                    | Taken to Home page                                                                                                                                                              | PASS      |
| Password Reset button on Login page                          | Takes user to Password Reset page                                                                                                    | Clicked Forgotten Password button                                                      | Taken to Password Reset page                                                                                                                                                    | PASS      |
| Back to Login button on Password Reset page                  | Takes user to login page                                                                                                             | Clicked Back to Login button                                                           | Taken to Login page                                                                                                                                                             | PASS      |
| Login user on Login page                                     | Successfully logs in user to site with success message                                                                               | Correctly input fields with registered username and password, clicked Register         | Taken to Home page with success message 'Successfully signed in as 'cle1234'                                                                                                    | PASS      |
| 'My Account' dropdown as logged in superuser                 | When clicked, dropdown shows Course management and Team management tabs as well as My profile and logout                             | Clicked My Accounts when logged in as a superuser                                      | Dropdown menu shows Course management, Team management, My Profile and Login                                                                                                    | PASS      |
| Course management option in 'My Account'                     | When clicked, takes superuser to Course Management -Add a Course page                                                                | Clicked Course Management                                                              | Taken to Course Management page                                                                                                                                                 | PASS      |
| Team management option in 'My Account'                       | When clicked, takes superuser to Team Management - Add an Instructor page                                                            | Clicked Team Management                                                                | Taken to Team Management page                                                                                                                                                   | PASS      |
| Shopping bag icon                                            | Takes user to their shopping bag page                                                                                                | Clicked Shopping bag icon                                                              | Taken to shopping bag                                                                                                                                                           | PASS      |
| Home button on navbar                                        | Takes user to Home page when clicked                                                                                                 | Clicked Home                                                                           | Taken to Home page                                                                                                                                                              | PASS      |
| About button on navbar                                       | When clicked, shows dropdown menu with About us, What we Offer, Meet the Team and Cafe links                                         | Clicked About                                                                          | Dropdown menu shows with menu as expected                                                                                                                                       | PASS      |
| Courses button on navbar                                     | When clicked, shows dropdown menu with View all courses, Babies, Toddlers, Preschool and Early Years course links                    | Clicked Courses                                                                        | Dropdown menu shows with menu as expected                                                                                                                                       | PASS      |
| Contact button on navbar                                     |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
| About Us link in About dropdown                              | Takes user to About Us section on Home page                                                                                          | Clicked About Us                                                                       | Taken to About Us section on Home page                                                                                                                                          | PASS      |
| What We Offer link in About dropdown                         | Takes user to What We Offer section on Home page                                                                                     | Clicked What We Offer                                                                  | Taken to What We Offer section on Home page                                                                                                                                     | PASS      |
| Meet The Team link in About dropdown                         | Takes user to Meet The Team page                                                                                                     | Clicked Meet The Team                                                                  | Taken to to Meet The Team page                                                                                                                                                  | PASS      |
| Cafe link in About dropdown                                  |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
| Cafe link in What We Offer Section                           |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
| Party Booking link in What We Offer Section                  |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
| Book A Course button links  within the What We Offer Section | Each of the four buttons takes the user to the corresponding Course page                                                             | Clicked Babies, Toddlers, Preschool, Early Years buttons                               | Babies button- taken to Babies group page; Toddlers button- taken to Toddler group page; Preschool- taken to Preschool group page, Early Years- taken to Early Years group page | PASS      |
| Meet Our Team link in What We Offer Section                  | When clicked, takes user to Meet Our Team page                                                                                       | Clicked Meet Our Team link                                                             | Taken to Meet Our Team page                                                                                                                                                     | PASS      |
| Book Now button within Home page hero image                  | User taken to the Courses page                                                                                                       | Clicked Book Now button                                                                | Taken to Courses page                                                                                                                                                           | PASS      |
| Quick Picks in Footer                                        | Home, Courses and Meet the Team links take user to the page as named                                                                 | Clicked Home, Courses and Meet the Team links individually                             | Home- taken to home page; Courses- taken to Courses page, Meet The Team- taken to Meet The Team page                                                                            | PASS      |
| Join Us! links in Footer                                     |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
| Socials links in Footer                                      | LinkedIn, Facebook and Instagram links each opens new window with correct website loaded                                             | Clicked LinkedIn, Facebook and Instagram icon links individually                       | LinkedIn- opens new window with LinkedIn login page; Facebook- opens new window with facebook login page; Instagram- opens new window with instagram login page                 | PASS      |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
| Babies button on Shopping bag page                           | When clicked, takes user to Babies group page                                                                                        | Clicked Babies button                                                                  | Taken to Babies group page                                                                                                                                                      | PASS      |
| Toddlers button on Shopping bag page                         | When clicked, takes user to Toddlers group page                                                                                      | Clicked Toddlers button                                                                | Taken to Toddlers group page                                                                                                                                                    | PASS      |
| Preschool button on Shopping bag page                        | When clicked, takes user to Preschool group page                                                                                     | Clicked Preschool button                                                               | Taken to Preschool group page                                                                                                                                                   | PASS      |
| Early Years button on Shopping bag page                      | When clicked, takes user to Early years group page                                                                                   | Clicked Early Years button                                                             | Taken to Early Years group page                                                                                                                                                 | PASS      |
| Add Instructor button on Team Management page                | When all 'Add an Instructor' form fields correctly completed, click Add Instructor, taken to Meet The Team page with success message | Input form fields correctly, clicked Add Instructor button                             | Taken to Meet Our Team page with success message 'Instructor added successfully!' and new Instructor added to page                                                              | PASS      |
| Cancel button on course management page                      | Takes user back to Courses page when clicked                                                                                         | Clicked Cancel button                                                                  | Taken to Courses page                                                                                                                                                           | PASS      |
| Select Image button in Add an Instructor form                | When clicked, opens downloads window so that user can choose an image from their own files                                           | Clicked Select Image button                                                            | Downloads window opens                                                                                                                                                          | PASS      |
| Add Course button on Course Management page                  | When all 'Add Course' form fields correctly completed, click Add Course, taken to All Courses page with success message              | Input form fields correctly, clicked Add Course button                                 | Taken to Courses page with success message 'Course added successfully!' and new course added to page in alphabetical order                                                      | PASS      |
| Cancel button on course management page                      | Takes user back to Courses page when clicked                                                                                         | Clicked Cancel button                                                                  | Taken to Courses page                                                                                                                                                           | PASS      |
| My Profile in 'My Account' dropdown                          | Takes user to My Profile page                                                                                                        | Clicked My Profile                                                                     | Taken to My Profile page                                                                                                                                                        | PASS      |
| Update Information button on My Profile page                 | Updates Default Billing information and saves in form fields, success message to keep user informed                                  | Input new default billing information in form field, clicked Update Information button | Stay on page, Success message 'Profile updated!', Can see information inout has been saved in form so it is visible                                                             | PASS      |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                      |                                                                                        |                                                                                                                                                                                 |           |
| Cancel button on Log Out page                                | Takes user back to home page                                                                                                         | Clicked Cancel button                                                                  | Taken back to Home page                                                                                                                                                         | PASS      |
| Logout button on Log Off page                                | Logs user out with success message                                                                                                   | Clicked Logout button in 'My Accounts' dropdown                                        | Logged out of site, Success message 'You have signed out' and taken to Home page                                                                                                | PASS      |
                                                                                                 


Each action was tested and found to work as expected. 

- - - 

-   ###  Further Testing

Testing was an ongoing process throughout this project. Google Chrome Developer tools were used to ensure the app was running correctly at each stage and it supported troubleshooting of issues when the project wasnt running as expected or the design required further work. It was particularly useful when adjusting the site styling to improve responsiveness.

The Website was tested on Google Chrome, Microsoft Edge, Firefox and Safari browsers. The site was viewed on a variety of devices such as Desktop, Laptop, Tablets and Phones using dev tools and real devices.
The deployed site sent to friends and young family members to review the site and test it from a user perspective.

- - - 

## Automated Testing 
         
-   ### HTML Validation 
    [W3C](https://validator.w3.org/) Markup Validator was used to validate this project to ensure that there were no syntax errors in the project. 
    * [Home page]()
    * [Login page]()
    * [Register page]()
    * [ page]()
    * [ page]()
    * [ page]()
    * [page]()
    * [ page]()
    * [ page]()- no errors or warnings
    

- - - 

-   ### CSS Validation 
    All pages were tested using [W3C jigsaw css validator](https://jigsaw.w3.org/css-validator/) 
    * [style.css]()- no errors or warnings

- - - 
    
-   ### Javascript Validation
    [Jshint](https://jshint.com/) was utilised as the javascript validation tool
    * []()

- - - 

-   ### Python Validation
    PEP8 compliant.[CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code.
    * []() 
    * [models.py]()
    * [manage.py]()
    * [__init__.py!]()

- - -

-   ### WAVE Testing

    See the WAVE reports for:

    * [Home page]()
    * [Login page]()
    * [Register page]()
    * [ page]()
    * [ page]()
    * [ page]()
    * [page]()
    * [ page]()
    * [ page]()

- - -

-   ### Lighthouse 

    Lighthouse within the Chrome Developer Tools was used to test performance, accessibility, best practices and SEO of this website. See the lighthouse reports for each page within the site:
  
    * [Home page]()
    * [Login page]()
    * [Register page]()
    * [ page]()
    * [ page]()
    * [ page]()
    * [page]()
    * [ page]()
    * [ page]()

  - - -

## Bugs

-   ### Fixed Bugs

    * Dropdown-toggle not working correctly in the topnav or main-nav. Ensured the selector was correctly identified within the html using the id and #prefix in the data-toggle attribute but this did not fix the problem. Tried moving the js files to the postload block at the bottom of the base.html body to ensure all content loading first but this also did not fix the problem. Found that i had accidentally used data-bs-toggle on the account dropdown which is only compatible with Bootstrap 5. I used Bootstrap 4 which uses the dtat-toggle attribute. Once this was corrected the dropdown functionality worked. Although i noted that if i went to click to close the dropdown on the About and Courses dropdowns, neither closed, however the account dropdown closed when clicked again. 

    * When booking a course, the courses are looped through to display the course associated with the age group of the page the user is on. This caused some issues when trying to use django template. The form action could not be submitted using the course.id as it was selecting the first course_id in the list of course dates/times rather than the one selected using the radio button. To get around this i tried using javascript to add the course id depending on which radio button was selected but this caused an error of an empty string. Therefore i used javascript to manually construct the file path. The correct course id is injected into the path to ensure the item_id is valid. Denis Belangers post on [Medium](https://medium.com/@tempmailwithpassword/determining-the-selected-radio-button-using-jquery-fb26274859f0#:~:text=Use%20the%20jQuery%20validation%20plugin,options'%5D%3Achecked%E2%80%9D) alongside [Jquery APIdocs](https://api.jquery.com/attr/) helped to find the solution to this bug.

    * I came across a bug which took some head scratching. The 'remove' button was not removing the item from the bag and the console gave an error 400. I'd initally thought the issue was with the view and found [Codemys](https://www.youtube.com/watch?v=unoBXAfC5aM) video helpful but on further inspection of the console, when trying to remove an item from the bag, the server gave a 403 error. Searching stack overflow and google i found (Bright)[https://brightsec.com/blog/what-is-csrf-token-mismatch-and-6-ways-to-fix-it/]blog about CSRF token mismatch which led me to look further into the ajax request within the javascript i'd written to handle the update and remove quantity within the bag. A variable to get the csrf token is there. However after further reading a (Stack Overflow)[https://stackoverflow.com/questions/22063612/adding-csrftoken-to-ajax-request] post showed me how to pass the CSRF token as a parameter to make it available in the POST request. This fixed the bug.
    
    * Issue with images rendering in the templates. Added image field to instructor model so that i could include image within loop to iterate through instructors and reduce unneccessary html. Images not rendering. Deleted and re-added images directly to django admin. Checked using correct template usage and id accidentally used {%instructor.instructor.image %} rather than accessing it directly using {% instructor.image %}. Images rendered correctly within the loop. 

    * I had an issue with the instructor and course model relationships. I was trying to display the courses linked to each instructor but what i actually nneded to do was to display the age-group associated with each instructor. I had created a fk on both the course and instructor models which was unnecessary. I also didnt require the speciality_age_group on the instructor model as i could access the age_group using the fk on the course model to access age_group. I made these changes then adjusted the view to filter the course objects by age_group. Then i was able to access the age-group associated with the intructor in the template.

    * When sending real emails with Django i came across a bug in my deployed site. There were no errors in the console and no error codes but i noticed when registering a new user, they were automatically signed into the site rather than having to verify their email. Django admin showed the user and their email has been created but not verified. I checked settings.py and the config variables in Heroku. I found that i still had email_verification set to 'none'. I changed it to 'mandatory'. Progress made as I was now getting a 500 server error when trying to register a new user. 
    I changed debug to `DEBUG = True` in settings.py to see if I could gain any further info about the error. The new error message showed `SMTP.strattls() got an unexpected keyword 'keyfile'`. A search of slack led me to a super helpful post which helped to solve the issue. I upgraded django all-auth with `pip install --upgrade django-allauth==0.54` then `touch runtime.txt && echo "python-3.11.9" > runtime.txt`. This fixed the bug and django all auth now working as expected.

    * When submitting the Booking Enquiry form, the user correctly recieves an email fromthe site confirming that the enquiry has been recieved. The database is also correctly populated with the Booking enquiry info and this can be view within DJango admin. However the user recieves both the error and success messages. When trying to figure out why this could be i checked the Booking Enquiry view again. I wasn't sure what the issue could be. I searched and found a helpful [StackOverflow](https://stackoverflow.com/questions/1508467/log-exception-with-traceback-in-python) thread which helped me to troubleshoot the bug. I added `except Exeption as e` in replacement of the else block to try to catch the error and log it in the string of the error message. Once this change was made the bug was fixed.

    * Instructor images were not rendering after depployment and hosting them within AWS. I added each instructor image via Django admin using the AWS S3 bucket url. They didnt render. I tried a number of things to try to get them to render correctly- cleared the cache, checked the permissions within AWS, checked the image URL was correct by loading the image in a new tab which it did, tried rendering the image in a paragraph outside of the instructor loop which didnt render the image. Checked the DB model to see if I had a mistake in the way the image was being stored. After a quick search of google i found a [Stack Overflow](https://stackoverflow.com/questions/8850535/how-to-get-an-imagefield-url-within-a-template) post which helped me to realise that i was trying to access the empty 'image' field rather than 'image_url', the field i was using to store the image in the database. Once accessing the image_url using `instructors.image_url` the images rendered correctly.

- - - 



