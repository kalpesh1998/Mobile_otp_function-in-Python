
import requests
import random

a=random.randint(1000,9999)
print(a)
message="Welecome to the testing.com and the one time password for the registration is {}. Please do not share this otp to anyone else.This is only for testing purpose".format(a)




url = "https://www.fast2sms.com/dev/bulk"

payload = "sender_id=FSTSMS&message={}&language=english&route=p&numbers=99XXXXXXXXX".format(message)
headers = {
    'authorization': "XXXXt9h2eYUC0Pjp1xnL58uA3gVJlHk7XIrZdvafz6SmTNhXvH37k5YFLmdrCTgK0IfR81apjcsD",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)


