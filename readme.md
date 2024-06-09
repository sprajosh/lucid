### Features
- User signup and login with JWT authentication
- Adding, retrieving, and deleting posts
- Token-based authentication for certain endpoints
- Validation for payload size and user input


### Install dependencies
- pip install -r requirements.txt

### Usage
- uvicorn app.main:app --reload

### Endpoints
- [POST] /signup: Create a new user account.
- [POST] /login: Log in with an existing user account and receive a JWT token.
- [POST] /posts: Add a new post.
- [GET] /posts: Retrieve all posts for the authenticated user.
- [DELETE] /posts/{post_id}: Delete a post by its ID.
