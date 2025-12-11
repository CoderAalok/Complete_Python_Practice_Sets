import json

# convert JSON into python dictionary(Deserialization)
# data = '{"files":["music","photos"],"fruits":["banana","apple","coconut"]}'
# print(data) # by this way can't access value using key
# result = json.loads(data)
# print(result)
# print(result['files'])
# print(type(result))

# ======================================================================

# Convert dictionry  into JSON file(Seralization)
# data = {
#     "Python":"JSON",
#     "dict":"object",
#     "list tuple":"array",
#     "None":"null",
#     "file":[10,True,None,90.12,('python','machine learning')]
# }

# parsed = json.dumps(data)
# print(parsed)


# parsed1 = json.dumps(data, indent=4)
# print(parsed1)

# ======================================================================

# Read JSON from file
with open("data.json","r")as f:
    add_data = (json.load(f))

# ======================================================================
    
# # Write JSON from file
# data = {
#     "Python":"JSON",
#     "dict":"object",
#     "list tuple":"array",
#     "None":"null",
#     "file":[10,True,None,90.12,('python','machine learning')]
# }

# append on file
# data = {
#     "Computer":"vision",
#     "Compitative":"Programming",
#     "Data Analytics":"Data Sciencetist"
# }
# add_data.append(data)
# with open("data.json","w+")as f:
#     print(json.dump(add_data, f, indent=4))

