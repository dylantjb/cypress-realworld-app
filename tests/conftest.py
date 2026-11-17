import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Set the default base URL for all tests."""
    return {
        **browser_context_args,
        "base_url": "http://localhost:3000",
    }

@pytest.fixture(autouse=True, scope="session")
def setup_playwright_test_id(playwright: Playwright):
    """Configure Playwright to use data-test instead of data-testid."""
    playwright.selectors.set_test_id_attribute("data-test")
