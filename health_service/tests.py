from django.test import TestCase

# Create your tests here.
import os
import sys
import requests
import json

# http get测试
test_url = "http://127.0.0.1:8000/hec/health/"
r = requests.get(test_url)
print(r.text)

# http post测试
test_url = "http://127.0.0.1:8000/hec/health/"
data = {"person_id": 12, "height": "123", "weight": "456", "blood_pressure": "789", "blood_routines": "102",
        "urine_routines": "测试", "diet": "正常", "sleep_info": 123}
r = requests.post(test_url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
print(r.text)
