from playwright.sync_api import sync_playwright, expect
import os

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Get the absolute path to the index.html file
    file_path = os.path.abspath("index.html")

    # Navigate to the local HTML file
    page.goto(f"file://{file_path}")

    # Click the play button to trigger the popup
    page.locator("#play-button").click()

    # Wait for the popup to be visible
    popup = page.locator("#popup-container")
    expect(popup).to_be_visible()

    # Take a screenshot of the page with the popup
    page.screenshot(path="jules-scratch/verification/verification_popup.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)