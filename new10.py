import requests
import json

url = "https://leetcode.com/graphql"

query = """
query{
  submissionList(offset:0, limit:5){
    __typename
  }
}
"""

response = requests.post(url, json={"query": query})

print(response.status_code)
print(json.dumps(response.json(), indent=2))