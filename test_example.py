import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
#    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("se")
    page.get_by_role("textbox", name="What needs to be done?").press("CapsLock")
    page.get_by_role("textbox", name="What needs to be done?").fill("see u tomoro")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("checkbox", name="Toggle Todo").check()
    page.get_by_role("link", name="Completed").click()
    page.get_by_test_id("todo-title").click()
#    context.tracing.stop(path = "trace.zip")
#    time.sleep(60)
    

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

