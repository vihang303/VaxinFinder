import requests
import time
from datetime import date

today = date.today()
d1 = today.strftime("%d-%m-%Y")

district = 377 #for-wardha
url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(
    district
, d1)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


def find_Vaccine():
    vac = 0
    result = requests.get(url, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    for i in data:
        if((i["available_capacity"] > 0) & (i["min_age_limit"] == 18)):
            vac += vac
            print('Center Name : ' + i["name"] + ', ' +str(i["pincode"]))
            print('Vaccine : ' + i["vaccine"])
            print('Available Vaccines : ' + str(i["available_capacity"]))
            return True
    if(vac == 0):
        print("No Available Slots")
        return False


while(find_Vaccine() == False):
    time.sleep(5)
    find_Vaccine()