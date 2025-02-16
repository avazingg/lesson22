import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def driver():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir="videos/")
        page = context.new_page()
        yield page

        browser.close()
