import json
#json is JavaScript Object Notation - useful for integration with websites!!
a = [3, 45, 83, 21]
with open('test.txt', 'w') as f:
    f.write(json.dumps(a))

with open('test.txt', 'r') as f:
    a = json.loads(f.read())