import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def pw_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

@pytest.fixture
def page(pw_context):
    page = pw_context.new_page()
    yield page
    page.close()
