import requests
import json

queries = [
    "submissionList",
    "submissionHistory",
    "submissionListV2",
    "userSubmissionList",
    "submissions",
    "questionSubmissionList",
    "questionSubmissions",
    "problemsetQuestionList",
    "recentSubmissionList",
    "allSubmissions"
]

url = "https://leetcode.com/graphql"

for q in queries:
    query = f"""
    query {{
        {q}(username:"Toshu_Pandey") {{
            __typename
        }}
    }}
    """

    response = requests.post(url, json={"query": query})

    data = response.json()

    if "errors" in data:
        print(f"{q:30} -> {data['errors'][0]['message']}")
    else:
        print(f"{q:30} -> EXISTS")