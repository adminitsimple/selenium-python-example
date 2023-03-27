import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.smoketest
def test_alhymrec_navigation_test_env(browser):
    browser.get("https://fyl.vqr.mybluehost.me/")
    page_title = WebDriverWait(browser, 10).until(EC.title_contains("Homepage"))
    assert "Homepage" in browser.title
    assert "https://fyl.vqr.mybluehost.me" in browser.current_url



