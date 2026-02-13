import os

EMAIL = os.getenv("TEST_EMAIL")
PASSWORD = os.getenv("TEST_PASSWORD")

if not EMAIL or not PASSWORD:
    raise ValueError("Environment variables TEST_EMAIL or TEST_PASSWORD not set!")
