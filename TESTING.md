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
        - Site is responsive on devices from 280px
        - Navbar available on each page for ease of navigation
        - 404 and 500 error pages and toast messages show to keep user upto date

        2. As a parent/guardian, i want to easily understand the purpose of the webite
        - The navbar and hero image on the index page instantly informs the user of the site name in the logo and what the business doess in the text on the hero image.
        - The colourful design and choice of images supports the message of what the business does.

        3. As a parent/guardian, i want to be able to view course details to understand which course is suitable for my child.
        - The navbar has a dropdown menu names 'Courses' easily visible on each page.
        - Clicking the courses dropdown shows the user lots of options for information on our different courses and also able to view all courses available
        - There are pages specific to each of the four age categories which gives more in depth information to the user alongside the age-specific course availability so that users can add the course straight to their bag.

        4. As a parent/guardian, i want to be able to see the available courses, the course dates and times so that i can decide if it is suitable to book.
        - Each age-scpecific group has its own webpage with specific information related to the course, this includes all course-specific availability so the user can easily book once they have found which course is bes tfor their child.
        - From the all courses page the user is able to see all courses, dates and times available and can click on any date which will take them to the course detals page for more information and booking options.

        5. As a registered site user, i want to view the contents of my shopping basket and be able to add, edit or delete any items in it. 
        - The shopping bag is shown as a Bag icon and price located in the top left corner of each webpage. It is in the same location regardles of where the user is within the site or what device they are viewing the site on. 
        - The price is displayed below the Bag icon and is updated with any changes to the shopping bag contents so the user can quickly and easily see their bag total.
        - Clicking on the shopping bag  takes the user to the Shopping Bag page where they are shown the contents of their bag with the relevent course details so they can clearly see what they are wanting to order.
        - The bag contents can easily be updated or removed using the +/- and update/remove buttons on each order item.
        - If the shopping bag is empty, the user is shown a message to inform them of this and directed to the course details buttons for each age group.

        6. As a registered site user, i want to have a personlalised profile where i am able to view my order history and update my profile details
        - Each registered user has a profile which can be found in the Accounts dropdown in the top left corner of the webpage
        - On clicking 'My Profile' within the Account dropdown, the user is taken to their profile page. 
        - The profile page is split into two areas. The first area shown the user their saved Billing Info(if they have chosen to save it at a previous checkout) and they can update their information directly from this page. The next section is an order summary, showing a list of all previous orders.

        7. As a parent/guardian, i want to be abe to meet the team who run the courses and understand more about them and their qualifications so that i know the sessions are being run by competent pracitioners
        - Within the navbar 'About' dropdown, a 'Meet the team' link takes the user to the associated are on the home page. Here, the user can find some information abotut he team with links to view more details about each team member. 
        - On clicking the links, the user is taken to the Meet The Team page. An image of each team member is displayed and hen the user hovers over the picture, the team members name and course speciality is shown alongside a button linking to their own page.
        - If the user then clicks the button on the instructor image, they are taken to that instructors' details page which shows some information named 'a bit about me'. This gives the user a friendly summary of the instructors' relevent qualifications and past work history.

        8. As a parent/guardian, i want to be able to see where the courses are being held so that i know where i am going to be travelling to and can plan my journey

        9. As a site user, i want to be able to contact the site owners if i have any queries and recieve email confirmation that my message has been successfully sent
        - From the navbar the user can view the 'Contact' link. When clicked, this takes the user to the Booking Enquiry page where they can fill in a short form and submit. 
        - They will get an email to say that Little Pont have recieved their enquiry and will get back to them shortly.

        10. As a parent/guardian, i want to be able to make a party booking enquiry
        - From the navbar the user can view the 'Contact' link. When clicked, this takes the user to the Booking Enquiry page where they can fill in a short form and submit. 
        - They will get an email to say that Little Pont have recieved their enquiry and will get back to them shortly.
        
    
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

| Feature/Site Page                                            | Expected Outcome                                                                                                                                         | Testing Performed                                                                      | Result                                                                                                                                                                          | Pass/Fail |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| NAVBAR/HEADER                                                |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| 'My Account' dropdown as logged out user                     | When clicked a dropdown appears showing Register and Login to logged out user                                                                            | As a logged out user, clicked My Account                                               | Dropdown appears with Register and Login options                                                                                                                                | PASS      |
| Login in 'My Account' dropdown                               | When clicked, navigates to Login page                                                                                                                    | Clicked Login in 'My Account' dropdown                                                 | Taken to Login page                                                                                                                                                             | PASS      |
| Register in 'My Account' dropdown                            | When clicked, navigates to Register page                                                                                                                 | Clicked Register in 'My Account' dropdown                                              | Taken to Register page                                                                                                                                                          | PASS      |
| Register button on Login page                                | When clicked, navigates to Register page                                                                                                                 | Clicked Register button on Login page                                                  | Taken to Register page                                                                                                                                                          | PASS      |
| Login button on Register page                                | When clicked, navigates to Login page                                                                                                                    | Clicked Login button on Register page                                                  | Taken to Login page                                                                                                                                                             | PASS      |
| Register user on Register page                               | Completed regitration form on Register page                                                                                                              | Correctly completed input fields, clicked Register button                              | Taken to Verify Email page with Alert Message informing user that a verification email has been sent to their email                                                             | PASS      |
| Verification Email                                           | Complete new user registration and direct user to login page with prefilled login input fields                                                           | Clicked link in verification email and taken to Login page with success message        | Successfully registered new user                                                                                                                                                | PASS      |
| 'Back to Login' button on Register page                      | Takes user to Login page                                                                                                                                 | Clicked Back to Login button                                                           | Taken to Login page                                                                                                                                                             | PASS      |
| Home button on Login page                                    | Takes user to Home page                                                                                                                                  | Clicked Home button                                                                    | Taken to Home page                                                                                                                                                              | PASS      |
| Password Reset button on Login page                          | Takes user to Password Reset page                                                                                                                        | Clicked Forgotten Password button                                                      | Taken to Password Reset page                                                                                                                                                    | PASS      |
| Back to Login button on Password Reset page                  | Takes user to login page                                                                                                                                 | Clicked Back to Login button                                                           | Taken to Login page                                                                                                                                                             | PASS      |
| Login user on Login page                                     | Successfully logs in user to site with success message                                                                                                   | Correctly input fields with registered username and password, clicked Register         | Taken to Home page with success message 'Successfully signed in as 'cle1234'                                                                                                    | PASS      |
| 'My Account' dropdown as logged in superuser                 | When clicked, dropdown shows Course management and Team management tabs as well as My profile and logout                                                 | Clicked My Accounts when logged in as a superuser                                      | Dropdown menu shows Course management, Team management, My Profile and Login                                                                                                    | PASS      |
| Course management option in 'My Account'                     | When clicked, takes superuser to Course Management -Add a Course page                                                                                    | Clicked Course Management                                                              | Taken to Course Management page                                                                                                                                                 | PASS      |
| Team management option in 'My Account'                       | When clicked, takes superuser to Team Management - Add an Instructor page                                                                                | Clicked Team Management                                                                | Taken to Team Management page                                                                                                                                                   | PASS      |
| Shopping bag icon                                            | Takes user to their shopping bag page                                                                                                                    | Clicked Shopping bag icon                                                              | Taken to shopping bag                                                                                                                                                           | PASS      |
| Home button on navbar                                        | Takes user to Home page when clicked                                                                                                                     | Clicked Home                                                                           | Taken to Home page                                                                                                                                                              | PASS      |
| About button on navbar                                       | When clicked, shows dropdown menu with About us, What we Offer, Meet the Team and Cafe links                                                             | Clicked About                                                                          | Dropdown menu shows with menu as expected                                                                                                                                       | PASS      |
| Courses button on navbar                                     | When clicked, shows dropdown menu with View all courses, Babies, Toddlers, Preschool and Early Years course links                                        | Clicked Courses                                                                        | Dropdown menu shows with menu as expected                                                                                                                                       | PASS      |
| Contact button on navbar                                     | Whn clicked takes user to Booking Enquiry Form                                                                                                           | Clicked Contact link                                                                   | Taken to Booking Enquiry Form                                                                                                                                                   | PASS      |
| About Us link in About dropdown                              | Takes user to About Us section on Home page                                                                                                              | Clicked About Us                                                                       | Taken to About Us section on Home page                                                                                                                                          | PASS      |
| What We Offer link in About dropdown                         | Takes user to What We Offer section on Home page                                                                                                         | Clicked What We Offer                                                                  | Taken to What We Offer section on Home page                                                                                                                                     | PASS      |
| Meet The Team link in About dropdown                         | Takes user to Meet The Team page                                                                                                                         | Clicked Meet The Team                                                                  | Taken to to Meet The Team page                                                                                                                                                  | PASS      |
| Cafe link in About dropdown                                  |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 | PASS      |
| HOME                                                         |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| Party Booking link in What We Offer Section                  | Takes user to the Booking Enquiry page                                                                                                                   | Clicked Party Booking link                                                             | Taken to Booking Enquiry page                                                                                                                                                   | PASS      |
| Book A Course button links  within the What We Offer Section | Each of the four buttons takes the user to the corresponding Course page                                                                                 | Clicked Babies, Toddlers, Preschool, Early Years buttons                               | Babies button- taken to Babies group page; Toddlers button- taken to Toddler group page; Preschool- taken to Preschool group page, Early Years- taken to Early Years group page | PASS      |
| Meet Our Team link in What We Offer Section                  | When clicked, takes user to Meet Our Team page                                                                                                           | Clicked Meet Our Team link                                                             | Taken to Meet Our Team page                                                                                                                                                     | PASS      |
| Book Now button within Home page hero image                  | User taken to the Courses page                                                                                                                           | Clicked Book Now button                                                                | Taken to Courses page                                                                                                                                                           | PASS      |
| Cafe link in What We Offer Section                           | Takes user to the Cafe page to view the cafe menu                                                                                                        | Clicked Cafe link                                                                      | aken to cafe page                                                                                                                                                               | PASS      |
| FOOTER                                                       |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| Join Us! Login link in Footer                                | Takes a user who is not logged in to the Login page                                                                                                      | Clicked Login link (as a logged out user)                                              | Taken to Login page                                                                                                                                                             | PASS      |
| Join Us! Register link in Footer                             | Takes an unregistered/logged out user to the Register page                                                                                               | Clicked Register link (as a logged out user)                                           | Taken to Register page                                                                                                                                                          | PASS      |
| Socials links in Footer                                      | Home, Courses and Meet the Team links take user to the page as named                                                                                     | Clicked Home, Courses and Meet the Team links individually                             | Home- taken to home page; Courses- taken to Courses page, Meet The Team- taken to Meet The Team page                                                                            | PASS      |
| Quick Picks in Footer                                        | LinkedIn, Facebook and Instagram links each opens new window with correct website loaded                                                                 | Clicked LinkedIn, Facebook and Instagram icon links individually                       | LinkedIn- opens new window with LinkedIn login page; Facebook- opens new window with facebook login page; Instagram- opens new window with instagram login page                 | PASS      |
| PROFILE                                                      |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| My Profile in 'My Account' dropdown                          | Takes user to My Profile page                                                                                                                            | Clicked My Profile                                                                     | Taken to My Profile page                                                                                                                                                        | PASS      |
| Update Information button on My Profile page                 | Updates Default Billing information and saves in form fields, success message to keep user informed                                                      | Input new default billing information in form field, clicked Update Information button | Stay on page, Success message 'Profile updated!', Can see information inout has been saved in form so it is visible                                                             | PASS      |
| SHOPPING BAG                                                 |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| Toddlers button on Shopping bag page                         | When clicked, takes user to Toddlers group page                                                                                                          | Clicked Toddlers button                                                                | Taken to Toddlers group page                                                                                                                                                    | PASS      |
| Preschool button on Shopping bag page                        | When clicked, takes user to Preschool group page                                                                                                         | Clicked Preschool button                                                               | Taken to Preschool group page                                                                                                                                                   | PASS      |
| Early Years button on Shopping bag page                      | When clicked, takes user to Early years group page                                                                                                       | Clicked Early Years button                                                             | Taken to Early Years group page                                                                                                                                                 | PASS      |
| Babies button on Shopping bag page                           | When clicked, takes user to Babies group page                                                                                                            | Clicked Babies button                                                                  | Taken to Babies group page                                                                                                                                                      | PASS      |
| (when shopping bag has item/s in it)                         |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| Minus button then Update button                              | With each click, will reduce the item quantity by 1 to a minimum of 1. Then click Update button to save this number and update the                       | When 2x item in bag, clicked minus button  then clicked Update button                  | Minus button reduced item quantity number from 1 to 2, then the Update button updated the Subtotal and Total to £45. Success message appears with correct info                  | PASS      |
| Plus button then Update button                               | With each click, will increase the item quantity by 1. Then click Update button to save this number and update the Subtotal and Total                    | When 1 item in bag, pressed Add button 4 times. Pressed Update button                  | Quantity number increased from 1 to 5, on Update click the Subtotal and Total updated correctly to £225. Success message shown with correct details shown                       | PASS      |
| Remove button                                                | Removes all bag items for that item                                                                                                                      | Pressed remove button                                                                  | Items relating to Remove button removed and Bag now empty so redirected to Shopping bag is empty. Success message shown and correct                                             | PASS      |
| COURSE MANAGEMENT(admin only)                                |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 | PASS      |
| Add Course button on Course Management page                  | When all 'Add Course' form fields correctly completed, click Add Course, taken to All Courses page with success message                                  | Input form fields correctly, clicked Add Course button                                 | Taken to Courses page with success message 'Course added successfully!' and new course added to page in alphabetical order                                                      | PASS      |
| Cancel button on course management page                      | Takes user back to Courses page when clicked                                                                                                             | Clicked Cancel button                                                                  | Taken to Courses page                                                                                                                                                           | PASS      |
| Delete button on Courses page                                | Deletes the Course, Success message to inform superuser                                                                                                  | Clicked Delete button on course                                                        | Course deleted, Success message shown to inform which course was successfully deleted. User stays on Courses page                                                               | PASS      |
| Edit button on Courses page                                  | When clicked, takes superuser to the Edit course page, form is prefilled with the current info. Alert message shown with the current course being edited | Clicked Edit button on one of the courses                                              | Superuser taken to the Edit Instructor page, form prefilled with correct current course info, Alert message shown with correct info                                             | PASS      |
| Update button on Edit Instructor page                        | Updates the course information and takes user to Courses page where new information can be viewed, Success message shown.                                | Edited name input and description fields on form and pressed Update button             | Taken to courses page with correct Success message and course had successfully updated                                                                                          | PASS      |
| ALL COURSES                                                  |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| Filtering dropdown and Filter button                         | Filters courses and displays courses as per input boxes                                                                                                  | Selected Start Time Descending and clicked Filter                                      | Displays Courses by Start Date with course with latest start date displayed first and organised in alphabetical order                                                           | PASS      |
| Course Titles on Courses page                                | Link to age-specific course pages                                                                                                                        | Clicked on Monday Toddlers                                                             | User taken to Toddler Course page                                                                                                                                               | PASS      |
| TEAM MANAGEMENT                                              |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| Select Image button in Add an Instructor form                | When clicked, opens downloads window so that user can choose an image from their own files                                                               | Clicked Select Image button                                                            | Downloads window opens                                                                                                                                                          | PASS      |
| Cancel button on course management page                      | Takes user back to Courses page when clicked                                                                                                             | Clicked Cancel button                                                                  | Taken to Courses page                                                                                                                                                           | PASS      |
| Add Instructor button on Team Management page                | When all 'Add an Instructor' form fields correctly completed, click Add Instructor, taken to Meet The Team page with success message                     | Input form fields correctly, clicked Add Instructor button                             | Taken to Meet Our Team page with success message 'Instructor added successfully!' and new Instructor added to page                                                              | PASS      |
| LOGOUT                                                       |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| Cancel button on Log Out page                                | Takes user back to home page                                                                                                                             | Clicked Cancel button                                                                  | Taken back to Home page                                                                                                                                                         | PASS      |
| Logout button on Log Off page                                | Logs user out with success message                                                                                                                       | Clicked Logout button in 'My Accounts' dropdown                                        | Logged out of site, Success message 'You have signed out' and taken to Home page                                                                                                | PASS      |
| AGE-SPECIFIC COURSE PAGES                                    |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| Course Lists                                                 | When clicking Course title in the courses list, star icon changes from yellow to pink to indicate selection.                                             | Clicked Course title                                                                   | Star icon of selected course turns from yellow to pink                                                                                                                          | PASS      |
| Quantity selector                                            | Clicking plus increments quantity by 1, clicking minus decrements quantity by 1                                                                          | Clicked plus fours times, clicked minus 3 times                                        | Increments quantity to 5, decrements quantity to 2                                                                                                                              | PASS      |
| Book Now button (no course selection)                        | Clicking Book Now without selecting a course first will show an alert box to prompt user to select a course first                                        | Clicked Book Now (no course selected)                                                  | Alert box shows 'Please select course before submitting'                                                                                                                        | PASS      |
| Book Now button (course selected)                            | Select course, Click Book Now button, success message                                                                                                    | Selected course, clicked book now button                                               | Success message to inform that course has been added to bag                                                                                                                     | PASS      |
| CHECKOUT                                                     |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| Complete Order button (form correctly completed)             | Submits form, shows loading image then user taken to checkout success page with a success message.                                                       | Completed form fields correctly and clicked Secure Checkout button.                    | Pink loading page shown then taken to checkout success page with correct summary and Success message.                                                                           | PASS      |
| Adjust Bag button                                            | Takes user back to shopping bag page                                                                                                                     | Click Adjust Bag                                                                       | Taken to shopping bag                                                                                                                                                           | PASS      |
| Secure checkout - incorrectly completed card details         | Shows user a message to say card details are invalid                                                                                                     | Inout an incorrect card number                                                         | Message in red to advise 'Your card number is invalid'                                                                                                                          | PASS      |
| CHECKOUT SUCCESS                                             |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| Send Us An Enquiry button                                    | Takes user to Booking Enquiry page                                                                                                                       | Clicked Send Us an Enquiry button                                                      | Taken to Booking Enquiry page                                                                                                                                                   | PASS      |
| REGISTER                                                     |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| Login button                                                 | Takes user to Login page                                                                                                                                 | Clicked Login button                                                                   | Taken to Login page                                                                                                                                                             | PASS      |
| Error message when passwords do not match                    | Does not submit page, informs user that passwords must match                                                                                             | Completed password fields with passwords that do not match                             | Stayed on Register page and short message to inform user that Passwords must match                                                                                              | PASS      |
| Home button                                                  | Takes user to Home page                                                                                                                                  | Clicked Home button                                                                    | Taken to home page                                                                                                                                                              | PASS      |
| Register (form fields correctly input)                       | Takes user to Verify Email address page and an alert message                                                                                             | Correctly completed form fields and  clicked Register button                           | Taken to Verify Email Address page with an alert message asking me to verify my email                                                                                           | PASS      |
| CONFIRM EMAIL ADDRESS                                        |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| Confirm button                                               | Takes user to login page with success message                                                                                                            | Click confirm button                                                                   | Taken to Login page with success message to inform successful registration                                                                                                      | PASS      |
| LOGIN                                                        |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| Login button                                                 | Takes user to Home page with success message                                                                                                             | Correctly completed form fields and clicked Login                                      | Taken to Home page with successful signin message                                                                                                                               | PASS      |
| Forgot Password button                                       | Takes user to password reset page                                                                                                                        | Clicked Forgotten Password button                                                      | Taken to Password reset page                                                                                                                                                    | PASS      |
| Home Button                                                  | Takes user to home page                                                                                                                                  | Clicked Home button                                                                    | Taken to Home page                                                                                                                                                              | PASS      |
| MEET THE TEAM                                                |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| Name buttons on each instructor image                        | User hovers over Instructor image and clicks button which takes them to the specific instructors page for more info                                      | Clicked each individual instructors name button                                        | Clicked 'Holly', taken to Holly page; Clicked 'Katie', taken to Katie page, Clicked 'Joanne', taken to Joannes page; Clicked 'Janine', taken to Janine page                     | PASS      |
| INSTRUCTOR DETAIL PAGES                                      |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
|                                                              |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| CONTACT                                                      |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |
| Click Contact button in navbar (not logged in)               | User must be logged in to send an enquiry so user is taken to login page with alert message                                                              |                                                                                        | User logs in and is taken directly to Booking Enquiry page                                                                                                                      |           |
| Send button                                                  | Sends a correctly completed form to site admin and redirects user to Home page with a success message                                                    | Completed booking enquiry form and press send                                          | Redirected to Home page with success message and email sent to address provided                                                                                                 | PASS      |
|                                                              |                                                                                                                                                          |                                                                                        |                                                                                                                                                                                 |           |

Each action was tested and found to work as expected. 

- - - 

-   ###  Further Testing

Testing was an ongoing process throughout this project. Google Chrome Developer tools were used to ensure the app was running correctly at each stage and it supported troubleshooting of issues when the project wasnt running as expected or the design required further work. It was particularly useful when adjusting the site styling to improve responsiveness.

<!--The Website was tested on Google Chrome, Microsoft Edge, Firefox and Safari browsers. The site was viewed on a variety of devices such as Desktop, Laptop, Tablets and Phones using dev tools and real devices.-->
The deployed site sent to friends and young family members to review the site and test it from a user perspective.

- - - 

## Automated Testing 
         
-   ### HTML Validation 
    **[W3C]**(https://validator.w3.org/) Markup Validator was used to validate this project to ensure that there were no syntax errors in the project. 
    * [Home page]()
    * [Login page]()
    * [Register page]()
    * [Logout page]()
    * [Shopping Bag page]()
    * [All Courses page]()
    * [Babies Course page]()
    * [Toddler Course page]()
    * [Preschool Course page]()
    * [Early Years Course page]()
    * [Add course page](documentation/testing/images/html_product_management.png)
    * [Edit course page]()
    * [My Profile page page]()
    * [Instructor Info page](documentation/testing/images/html_instructor_info.png)
    * [Instructor Detail page](documentation/testing/images/html_instructor_detail.png)
    * [Add Instructor page](documentation/testing/images/html_team_management.png)
    * [Edit Instructor page]()
    * [Cafe page](documentation/testing/images/html_cafe.png)
    * [Checkout page]()
    * [Checkout Success page]()
    * [Booking Enquiry page](documentation/testing/images/html_contact.png) 
    
    No errors or warnings found
    

- - - 

-   ### CSS Validation 
    All pages were tested using [W3C jigsaw css validator](https://jigsaw.w3.org/css-validator/) 
    * [style.css](documentation/testing/images/css_validation.png)
    * [checkout.css](documentation/testing/images/css_checkout.png)
- - - 
    
-   ### Javascript Validation
    [Jshint](https://jshint.com/) was utilised as the javascript validation tool
    * [base js](documentation/testing/images/base_js.png)- no errors, compatible with ES6

- - - 

-   ### Python Validation
    PEP8 compliant. Used Flake8 and [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code.
    BAG APP
    * [contents.py(bag app)](documentation/testing/images/bag_contents_py.png) 
    * [views.py(bag app)](documentation/testing/images/bag_views.png)
    CHECKOUT APP
    * [signals.py(checkout app)](documentation/testing/images/checkout_signals.png)
    * [views.py(checkout app)](documentation/testing/images/checkout_views.png)
    * [webhook_handler.py(checkout app)](documentation/testing/images/checkout_webhookhandler.png)
    * [webhooks.py(checkout app)](documentation/testing/images/checkout_webhookhandler.png)
    * [models.py(checkout app)](documentation/testing/images/checkout_models.png) 
    * [forms.py(checkout app)](documentation/testing/images/checkout_forms.png)
    * [apps.py(checkout app)](documentation/testing/images/checkout_app_py.png)
    * [admin.py(checkout app)](documentation/testing/images/checkout_admin_py.png)
    * [__init__.py(checkout app)](documentation/testing/images/__init__.png)
    CONTACT APP
    * [admin.py(contact app)](documentation/testing/images/contact_admin.png)
    * [apps.py(contact app)](documentation/testing/images/contact_apps.png) 
    * [forms.py(contact app)](documentation/testing/images/contact_forms.png)
    * [models.py(contact app)](documentation/testing/images/contact_models.png)
    * [views.py(contact app)](documentation/testing/images/contact_views.png)
    HOME APP
    * [apps.py(home app)](documentation/testing/images/home_apps.png)
    * [views.py(home app)](documentation/testing/images/home_views.png)
    INSTRUCTOR APP
    * [apps.py(instructor app)](documentation/testing/images/instructor_apps.png)
    * [forms.py(instructor app)](documentation/testing/images/instructor_forms.png)
    * [models.py(instructor app)](documentation/testing/images/instructor_models.png)
    * [views.py(instructor app)](documentation/testing/images/instructor_views.png)
    * [admin.py(instructor app)](documentation/testing/images/instructor_admin.png)
    * [widgets.py(instructor app)](documentation/testing/images/instructor_widgets.png)
    PRODUCT APP
    * [apps.py(products app)](documentation/testing/images/product_apps.png)
    * [forms.py(products app)](documentation/testing/images/products_forms.png)
    * [models.py(products app)](documentation/testing/images/products_models.png)
    * [views.py(products app)](documentation/testing/images/products_views.png)
    * [admin.py(products app)](documentation/testing/images/product_admin.png)
    * [widgets.py(products app)](documentation/testing/images/products_widgets.png)
    PROFILES APP
    * [apps.py(profiles app)](documentation/testing/images/profiles_apps.png)
    * [forms.py(profiles app)](documentation/testing/images/profiles_forms.png)
    * [models.py(profiles app)](documentation/testing/images/profiles_models.png)
    * [views.py(profiles app)](documentation/testing/images/profiles_views.png)

- - -

-   ### WAVE Testing

    See the WAVE reports for:

    * [Home page]()
    * [Login page]()
    * [Register page]()
    * [Logout page]()
    * [Shopping Bag page]()
    * [All Courses page]()
    * [Babies Course page]()
    * [Toddler Course page]()
    * [Preschool Course page]()
    * [Early Years Course page]()
    * [Add course page]()
    * [Edit course page]()
    * [My Profile page page]()
    * [Instructor Info page]()
    * [Instructor Detail page]()
    * [Add Instructor page]()
    * [Edit Instructor page]()
    * [Cafe page]()
    * [Checkout page]()
    * [Checkout Success page]()
    * [Booking Enquiry page]()

- - -

-   ### Lighthouse 

    Lighthouse within the Chrome Developer Tools was used to test performance, accessibility, best practices and SEO of this website. See the lighthouse reports for each page within the site:
  
    * [Home page]()
    * [Login page]()
    * [Register page]()
    * [Logout page]()
    * [Shopping Bag page]()
    * [All Courses page](documentation/testing/images/all_courses_lighthouse.png)
    * [Babies Course page]()
    * [Toddler Course page]()
    * [Preschool Course page]()
    * [Early Years Course page]()
    * [Add course page]()
    * [Edit course page]()
    * [My Profile page page]()
    * [Instructor Info page]()
    * [Instructor Detail page]()
    * [Add Instructor page]()
    * [Edit Instructor page]()
    * [Cafe page]()
    * [Checkout page]()
    * [Checkout Success page]()
    * [Booking Enquiry page]()

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

    * When submitting the Booking Enquiry form, the user correctly recieves an email from the site confirming that the enquiry has been recieved. The database is also correctly populated with the Booking enquiry info and this can be view within DJango admin. However the user recieves both the error and success messages. When trying to figure out why this could be i checked the Booking Enquiry view again. I wasn't sure what the issue could be. I searched and found a helpful [StackOverflow](https://stackoverflow.com/questions/1508467/log-exception-with-traceback-in-python) thread which helped me to troubleshoot the bug. I added `except Exeption as e` in replacement of the else block to try to catch the error and log it in the string of the error message. Once this change was made the bug was fixed.

    * Instructor images were not rendering after depployment and hosting them within AWS. I added each instructor image via Django admin using the AWS S3 bucket url. They didnt render. I tried a number of things to try to get them to render correctly- cleared the cache, checked the permissions within AWS, checked the image URL was correct by loading the image in a new tab which it did, tried rendering the image in a paragraph outside of the instructor loop which didnt render the image. Checked the DB model to see if I had a mistake in the way the image was being stored. After a quick search of google i found a [Stack Overflow](https://stackoverflow.com/questions/8850535/how-to-get-an-imagefield-url-within-a-template) post which helped me to realise that i was trying to access the empty 'image' field rather than 'image_url', the field i was using to store the image in the database. Once accessing the image_url using `instructors.image_url` the images rendered correctly.

    * I found a bug whereby the Preschool courses, which had been rendering correctly on the Preschool courses page, were suddenly no longer rendering at all. This seemed strange as i hadnt changed any of the code relating to this feature and the other course pages which use the same view and template structure were rendering perfectly. It seemed strange that it was only preschool courses this was affecting. I thought it may have been an issue related to deploying the site as i had just done this. I re-added the data to the database and deleted the old preschool course data. This seemed to fix the issue however about 1 week later when testing the site i ran into the same bug again. This time, when having a closer look at the issue, i checked that the age group choices in the model matched the use of Preschool in the view. I noticed that Preschool file path was the only course of the four that was being passed as a lowercase which seemed to be was causing the issue. To tackle this i ammended the way i fitered the courses using `courses = Course.objects.filter(age_group__iexact=age_group)` to make it case insensitive. This addressed the issue.

- - - 



