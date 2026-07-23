from uuid import uuid4

class LoginData:

    INVALID_EMAIL="wrong@test.com"
    INVALID_PASSWORD="wrongpassword"
    
    INVALID_EMAIL_FORMAT="invalid-format.com"
    
    VALID_EMAIL_FORMAT="validformat@test.com"
    VALID_PASSWORD_FORMAT="0123456789"
    
class SignUpData:
    
    VALID_NAME = "John Doe"
    VALID_EMAIL = "john.doe@test.com"
    VALID_PASSWORD = "Password123!"

    @staticmethod
    def unique_email():

        return f"test_{uuid4().hex[:8]}{SignUpData.VALID_EMAIL}"

    # Invalid passwords
    SHORT_PASSWORD="Ab1!"
    NO_UPPERCASE_PASSWORD="password123!"
    NO_LOWERCASE_PASSWORD="PASSWORD123!"
    NO_NUMBER_PASSWORD="Password!"
    NO_SPECIAL_CHARACTER_PASSWORD="Password123"
    TOO_LONG_PASSWORD="A" * 65 + "a1!"

    # Invalid emails
    INVALID_EMAIL="invalid-email"

    # Empty fields
    EMPTY_NAME=""
    EMPTY_EMAIL=""
    EMPTY_PASSWORD=""
    