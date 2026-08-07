import requests
import json

username = "Toshu_Pandey"

url = "https://leetcode.com/graphql"

query = """
query {
    matchedUser(username: "%s") {
        username
    }
}
""" % username

response = requests.post(url, json={"query": query})

print(response.status_code)
print(json.dumps(response.json(), indent=4))