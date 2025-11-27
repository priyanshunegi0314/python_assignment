import re

text = """
Phone: 9876543210
PAN: ABCDE1234F
Aadhaar: 1234 5678 9123
PIN: 248001
URL: https://www.example.com
IP: 192.168.1.1
Password: Abc@1234
"""

mobile = re.findall(r'\b[6-9]\d{9}\b', text)

pan = re.findall(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b', text)

aadhaar = re.findall(r'\b\d{4}\s\d{4}\s\d{4}\b', text)

pin = re.findall(r'\b\d{6}\b', text)

url = re.findall(r'https?://[A-Za-z0-9./]+\b', text)

ipv4 = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)

password = re.findall(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$', "Abc@1234")

print(mobile)
print(pan)
print(aadhaar)
print(pin)
print(url)
print(ipv4)
print(password)
