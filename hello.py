from playwright.sync_api import sync_playwright
import re

USERNAME = "Toshu_Pandey"

with sync_playwright() as p:

    # Opens a visible browser
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    # Open LeetCode profile problems page
    page.goto(f"https://leetcode.com/u/{USERNAME}/")

    print("Login if required...")
    input("Press ENTER after the solved problems page is visible...")

    # Get all text from page
    text = page.locator("body").inner_text()

    # Find question numbers
    numbers = re.findall(r"\b\d+\b", text)

    # Remove duplicates and sort
    solved = sorted(set(map(int, numbers)))

    print("\nPossible question numbers found:")
    print("-------------------------------")

    for x in solved:
        print(x)

    print("\nTotal:", len(solved))

    browser.close()