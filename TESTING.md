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

    * 
    * 

    * 
- - - 



