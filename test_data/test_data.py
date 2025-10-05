# Test data constants and generators

# Authentication test data
AUTH_VALID_CREDENTIALS = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

AUTH_INVALID_CREDENTIALS = {
    "email": "eve.holt@reqres.in", 
    "password": "wrongpassword"
}

AUTH_MISSING_PASSWORD = {
    "email": "eve.holt@reqres.in"
}

# CRUD test data
POST_CREATE_DATA = {
    "title": "Test Post Title",
    "body": "This is a test post body content for automation testing",
    "userId": 1
}

USER_CREATE_DATA = {
    "name": "John Doe Automation",
    "email": "john.doe.automation@example.com",
    "gender": "male",
    "status": "active"
}