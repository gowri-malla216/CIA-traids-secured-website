# Job Post Generating Website
A secure Job Posting Platform built with Django, integrating advanced security measures to protect user data and prevent cyber threats. This platform enables users to create, edit, and manage job listings while maintaining high standards of Confidentiality, Integrity, and Availability (CIA Triad).

## Features
- Secure User Authentication – Login with OTP-based authentication and encrypted passwords.
- On-Screen Keyboard Rendering – Prevents keylogging attacks during login.
- Password Encryption – Uses bcrypt with salts for enhanced security.
- CSRF Protection – Secure handling of CSRF tokens to prevent attacks.
- Asymmetric Encryption – Public-private key cryptography for data security.
- Job Posting & Editing – Easily add, edit, and manage job listings.
- Role-Based Access Control – Limits access based on user roles.
- Error Handling & Logging – Custom 404 & 500 error pages with logging.

## Tech Stack
### Backend – Django Framework
- Security: CSRF Tokens, bcrypt encryption, OTP-based login
- Data Encryption: Public-Private Key Cryptography
- Job Management: Django Models & Views
- Logging & Monitoring: Django Logging
### Frontend – HTML, CSS, JavaScript
- On-Screen Keyboard for login security
- Secure Form Submissions with CSRF protection

##  Security Implementations
1. OTP-Based Authentication
- Users receive a one-time password (OTP) via email for secure login.
- Ensures no password leaks by avoiding static credentials.

1. Password Hashing with Salt
- Uses bcrypt for encrypting passwords before storage.
- Each password is hashed with a unique salt to prevent rainbow table attacks.

1. On-Screen Keyboard for Login Security
- Prevents keyloggers from capturing user credentials.
- Randomized layout on every login attempt.

1. CSRF Protection
- Cross-Site Request Forgery (CSRF) tokens used for all form submissions.
- Prevents unauthorized actions from malicious websites.

1. Public-Private Key Encryption
- Uses asymmetric encryption for sensitive data transmission.
- Prevents MITM (Man-in-the-Middle) attacks on login sessions.

## Setup & Installation
### Prerequisites
- Python 3.x installed
- Django Framework installed
- PostgreSQL / SQLite for database

### Apply Migrations
```
python manage.py migrate
```
### Run the Development Server
```
python manage.py runserver
```
#### Visit: http://127.0.0.1:8000/
