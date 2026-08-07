import requests
import json

candidate_fields = [
    "id",
    "statusDisplay",
    "status",
    "title",
    "titleSlug",
    "lang",
    "langName",
    "timestamp",
    "question",
    "questionId",
    "frontendQuestionId",
    "runtime",
    "memory",
    "url"
]

url = "https://leetcode.com/graphql"

for field in candidate_fields:
    query = f"""
    query {{
      submissionList(offset:0, limit:1){{
        submissions {{
          {field}
        }}
      }}
    }}
    """

    response = requests.post(url, json={"query": query})
    data = response.json()

    if "errors" in data:
        print(f"{field:20} -> {data['errors'][0]['message']}")
    else:
        print(f"{field:20} -> EXISTS")