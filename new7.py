import requests
import json

url = "https://leetcode.com/graphql"

query = """
query {
  recentAcSubmissionList(username: "Toshu_Pandey") {
    id
    title
    titleSlug
    timestamp
  }
}
"""

response = requests.post(url, json={"query": query})

print(response.status_code)
print(json.dumps(response.json(), indent=2))