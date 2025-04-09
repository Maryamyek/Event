import requests

# URL endpoint برای لاگ اوت
url = 'http://127.0.0.1:8000/auth/logout/'

# توکن Access که شما قبلاً دریافت کرده‌اید
access_token = '<eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0MTU2MDk3LCJpYXQiOjE3NDQxNTU3OTcsImp0aSI6IjI5NzZlZDVjNzNjNzRlMjRhYTM1NjEyOTY4MWY5YjZlIiwidXNlcl9pZCI6MX0.uYErAiGEdxPYk2k7PGPLlJJnRDP7HroFCwmhbh4zles>'  # به جای این قسمت توکن واقعی را قرار دهید

# هدر Authorization
headers = {
    'Authorization': f'Bearer {access_token}'
}

# ارسال درخواست POST به لاگ اوت
response = requests.post(url, headers=headers)

# چاپ پاسخ دریافتی
print(response.json())
