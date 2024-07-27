import requests
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/hydjobsinfo'
r = requests.get(BASE_URL + END_POINT)
data = r.json()
for job in data:
    print('Company Name:',job['company'])
    print('Eligibility:',job['eligibility'])
    print('Title:',job['title'])
    print('Mail ID:',job['email'])
    print('Phone Number:',job['phonenumber'])
    print()
