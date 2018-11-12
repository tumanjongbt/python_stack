Build a Flask application that allows login and registration.

Note
One of the major components to every website is a login and registration.

Registration
The user inputs their information, we verify that the information is correct, insert it into the database and return back with a success message. If the information is not valid, redirect to the registration page and show the following requirements:

Validations and Fields to Include
1. First Name - letters only, at least 2 characters and that it was submitted

2. Last Name - letters only, at least 2 characters and that it was submitted

3. Email - valid Email format, does not already exist in the database, and that it was submitted

4. Password - at least 8 characters, and that it was submitted

5. Password Confirmation - matches password

Login
When the user initially registers we would log them in automatically, but the process of "logging in" is simply just verifying that the email and password the user is providing matches up with one of the records that we have in our database table for users.

But how do we keep track of them once they've logged in? I think you might already know... It's using session! We can create a session variable that holds the user's id. From our study in Database Design, we know that if we have the id of any table we can gather the rest of the information that is associated with that id. Storing a single session variable with the user's id is all we need to access all the information associated with that user.

Once we have already identified the places on our site that we wish to be dynamic for users that are logged in, then we just need to check to see if that session variable has been set and display the content accordingly.
