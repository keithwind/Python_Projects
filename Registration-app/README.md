# Flask User Registration and Login System

This Flask application provides a user registration and login system using MongoDB for storage and bcrypt for password hashing. Users can register for an account, login, and logout. The application uses session management to maintain user authentication.

## Setup

1. **Clone the Repository:** Clone the repository or download the code files.

2. **Install Dependencies:** Install the required dependencies using pip:

   ```
   pip install Flask pymongo bcrypt
   ```

3. **Set Up MongoDB:** Ensure you have MongoDB installed and running.

4. **Update MongoDB Credentials:** Replace the `username` and `password` variables in the code with your MongoDB username and password. Make sure to escape the username and password according to RFC 3986.

5. **Run the Application:** Run the Flask application:

   ```
   python app.py
   ```

6. **Access the Application:** Open a web browser and navigate to `http://localhost:5000` to access the application.

## Features

- **Registration:** Users can register for an account by providing a username, email, and password. Passwords are securely hashed using bcrypt before being stored in the database.

- **Login:** Registered users can log in to their accounts using their email and password. Passwords are verified against the hashed password stored in the database.

- **Session Management:** The application uses Flask's session management to keep users logged in across requests.

- **Logout:** Users can log out of their accounts, terminating the session.

## Files

- `app.py`: Main Flask application file containing route definitions and logic for user registration, login, and session management.

- `base.html`: Base HTML template providing the layout structure for other templates.

- `index.html`: HTML template for the registration form.

- `login.html`: HTML template for the login form.

- `logged_in.html`: HTML template for the page displayed when a user is logged in.

- `signout.html`: HTML template for the page displayed when a user logs out.

## Dependencies

- Flask: Micro web framework for Python.
- pymongo: MongoDB driver for Python.
- bcrypt: Library for hashing passwords.

## Usage

1. Register for a new account by providing a username, email, and password.
2. Log in to your account using your email and password.
3. Once logged in, you can access the logged-in page.
4. Click on the "Logout" button to terminate your session and log out.

## Note

- This application is for demonstration purposes and should not be used in production without further hardening and security measures.

---

This README file provides an overview of the Flask User Registration and Login System, including setup instructions, features, file descriptions, dependencies, usage guidelines, and a note about production use. Adjustments can be made as necessary.

--- 

Let me know if you need anything else!


