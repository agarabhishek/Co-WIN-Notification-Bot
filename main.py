import json
import requests
import os
import time

## Sound Config
duration = 1  # seconds
freq = 440  # Hz

## Slot Config
startDate = "09-05-2021"
minAgeLimit = 18
minAvailCapacity = 1

## Request Headers
headers = {
    'Connection': 'close',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Host': 'cdn-api.co-vin.in',
    'User-Agent': 'Mozilla/5.0 (X11; Untu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5" -H $"Accept-Encoding: gzip, deflate" -H $"DNT: 1',
    'Upgrade-Insecure-Requests': '1',
}

##District IDs List: Delhi and Gautam Budh Nagar
district_id=[141,145,140,146,147,143,148,149,144,150,142,650]

print("[+] Script Started...")
while(True):
    print("[-] Searching...")
    for disID in district_id:
        response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id='+str(disID)+'&date='+startDate, headers=headers)
        if response.status_code == 200:
            # Slot Found
            data = json.loads(response.content)
            for i in data['centers']:
                for j in i['sessions']:
                    if j['min_age_limit'] == minAgeLimit and j['available_capacity'] >=minAvailCapacity:
                        print("")
                        print("[++++] Found Slot. Details are below:")
                        # Play sound to notify
                        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
                        print("Center Name: ",i['name'])
                        print("Pincode: ",i['pincode'])
                        print("Address: ",i['address'])
                        print(json.dumps(j, indent=4, sort_keys=True))
                        print("----------------------------------")
        time.sleep(1) # Rate Limiting to avoid blocking