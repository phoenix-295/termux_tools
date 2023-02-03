from truecallerpy import search_phonenumber
from dotenv import load_dotenv
import os
import sys

load_dotenv()
id = os.environ['id']

# number = sys.argv[2]
number = input("Enter number: ")

search_number = search_phonenumber(number, "IN", id)

# search_number = {'data': [{'id': 'Xnok4b/c5XzuhKuLn/Qq8A==', 'name': 'Nikhil Shirdhankar', 'imId': '1hnox8vlx40e8', 'gender': 'UNKNOWN', 'about': '', 'image': 'https://storage.googleapis.com/tc-images-noneu/myview/1/da920641bda9b0b0126f365e609ef65c/1', 'jobTitle': '', 'score': 0.9, 'access': 'PUBLIC', 'enhanced': True, 'companyName': '', 'phones': [{'e164Format': '+919096546781', 'numberType': 'MOBILE', 'nationalFormat': '090965 46781', 'dialingCode': 91, 'countryCode': 'IN', 'carrier': 'Airtel', 'type': 'openPhone'}], 'addresses': [{'address': 'IN', 'street': '', 'zipCode': '', 'city': 'Maharashtra', 'countryCode': 'IN', 'timeZone': '+05:30', 'type': 'address'}], 'internetAddresses': [{'id': 'nikhil295@gmail.com', 'service': 'email', 'caption': 'Nikhil Shirdhankar', 'type': 'internetAddress'}], 'badges': ['user'], 'tags': [], 'cacheTtl': 1296000000, 'sources': [], 'searchWarnings': [], 'surveys': [{'id': 'd61f74f4-2158-43b0-83de-a4bf056bbc51', 'frequency': 3600, 'passthroughData': 'eyAiOCI6ICIwIiwgIjIiOiAiTmlraGlsIFNoaXJkaGFua2FyIiwgIjMiOiAiOTE5MDk2NTQ2NzgxIiwgIjQiOiAicGYiIH0=', 'perNumberCooldown': 31536000}], 'commentsStats': {'showComments': False}, 'ns': 0}], 'provider': 'ss-nu', 'stats': {'sourceStats': []}}

try:
    print("Name: \t\t", search_number['data'][0]["name"])
except:
    print("Name: \t\t","Not found")
    pass
try:
    print("Carrier: \t", search_number['data'][0]['phones'][0]["carrier"])
except:
    print("Carrier: \t", "Not found")
    pass

try:
    print("Country: \t", search_number['data'][0]["addresses"][0]["countryCode"])
except:
    print("Country: \t", "Not found")
    pass

try:
    print("City: \t\t", search_number['data'][0]["addresses"][0]["city"])
except:
    print("City: \t\t", "Not found")

try:
    print("eMail: \t\t", search_number['data'][0]["internetAddresses"][0]["id"])
except:
    print("eMail: \t\t", "Not found")

