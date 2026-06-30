import smtplib
from config import *

print("EMAIL =", EMAIL_FROM)
print("PASSWORD LENGTH =", len(APP_PASSWORD))

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_FROM, APP_PASSWORD)

    print("로그인 성공!")

except Exception as e:
    print(e)