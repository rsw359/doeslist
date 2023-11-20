import secrets
SECRET_KEY = secrets.token_hex(32)

DB_PASSWORD = secrets.token_hex(16)

print("secret_key: " + SECRET_KEY)
print("db_password: " + DB_PASSWORD)