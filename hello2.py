from playwright.sync_api import sync_playwright
import pandas as pd
import re
import time


USERNAME = "Toshu_Pandey"


def main():

    solved_questions = []


    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()


        # Open profile page
        page.goto(
            f"https://leetcode.com/u/{USERNAME}/",
            wait_until="domcontentloaded"
        )


        print("\nBrowser opened.")
        print("Login to LeetCode manually if required.")
        print("Open your profile solved problems section.")
        
        input("\nPress ENTER after solved problems are visible...")


        # Scroll to load all problems
        for i in range(20):
            page.mouse.wheel(0, 3000)
            time.sleep(1)


        # Find problem links
        links = page.locator('a[href*="/problems/"]')


        print("\nProblem links found:", links.count())


        problems = set()


        for i in range(links.count()):

            href = links.nth(i).get_attribute("href")

            if href:

                match = re.search(
                    r"/problems/([^/]+)",
                    href
                )

                if match:
                    problems.add(match.group(1))


        print("\nTotal problems found:", len(problems))


        # Convert slug to readable names
        for slug in sorted(problems):

            name = slug.replace("-", " ").title()

            solved_questions.append(
                {
                    "Problem": name,
                    "Slug": slug
                }
            )


        browser.close()



    # Export Excel

    df = pd.DataFrame(solved_questions)

    df.to_excel(
        "leetcode_solved.xlsx",
        index=False
    )


    print("\nExcel created: leetcode_solved.xlsx")

    print("\nSolved Problems:")
    print("----------------")

    for i, q in enumerate(solved_questions, 1):
        print(i, q["Problem"])



if __name__ == "__main__":
    main()