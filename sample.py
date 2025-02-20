import json
json_str = '''{
  "Name": "MOHAMMAD HUSSAIN",
  "Gender": "Male",
  "Date of Birth": "16-January-2017",
  "Place of Birth": "Gaya",
  "Name of Father": "Shafique Ahmed",
  "Name of Mother": "Farzana Aslam",
  "Permanent Address": "Aliganj, Road No-3, City-Gaya, Dist – Gaya, State-Bihar, India",
  "Address of Parents at the time of Birth of Child": "Aliganj, Road No-3, City-Gaya, Dist – Gaya, State-Bihar, India",
  "Registration Number": "12559/1/7428/2017",
  "Date of Registration": "19-June-2017",
  "Date of Issue": "19-June-2017"
}'''

temp_dict = json.loads(json_str)
print(temp_dict)

