import requests
import json

url = "https://leetcode.com/graphql"

query = """
query {
  submissionList(
    offset: 0,
    limit: 10,
    lastKey: "",
    status: 10,
    questionSlug: ""
  ) {
    submissions {
      frontendId
      title
      statusDisplay
    }
  }
}
"""

response = requests.post(url, json={"query": query})

print(response.status_code)
print(json.dumps(response.json(), indent=2))