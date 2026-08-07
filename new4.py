import requests
import json

url = "https://leetcode.com/graphql"

query = """
{
  __type(name: "MatchedUser") {
    name
    fields {
      name
      type {
        name
        kind
        ofType {
          name
          kind
        }
      }
    }
  }
}
"""

response = requests.post(url, json={"query": query})

print(response.status_code)
print(json.dumps(response.json(), indent=2))