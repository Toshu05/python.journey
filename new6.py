import requests
import json

username = "Toshu_Pandey"

query = """
query{
  matchedUser(username:"%s"){
    recentAcSubmissionList{
      id
      title
      titleSlug
      timestamp
    }
  }
}
""" % username

response = requests.post(
    "https://leetcode.com/graphql",
    json={"query": query}
)

print(response.status_code)
print(json.dumps(response.json(), indent=2))