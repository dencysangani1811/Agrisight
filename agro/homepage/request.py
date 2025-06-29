import requests # pip install requests
import re

with open("img2.jpg", "rb") as InputFile:
    file_dict = {"InputImg": InputFile}
    response = requests.post("https://detect-crop-disease.herokuapp.com/", files=file_dict)

response = re.sub("_", " ", response.text)
response = re.sub("   "," ", response)
response = re.sub("  "," ", response)
print("The disease is  ==> ", response)