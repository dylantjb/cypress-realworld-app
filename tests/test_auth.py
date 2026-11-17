from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    page.goto("/signin")

    page.get_by_test_id("signin-username").locator("input").fill("Heath93")
    page.get_by_test_id("signin-password").locator("input").fill("s3cret")
    page.get_by_test_id("signin-submit").click()

    expect(page).to_have_url("http://localhost:3000/")
    expect(page.get_by_test_id("sidenav-username")).to_contain_text("Heath93")

def test_login_failure_shows_error(page: Page):
    page.goto("/signin")

    page.get_by_test_id("signin-username").locator("input").fill("invalid_user")
    page.get_by_test_id("signin-password").locator("input").fill("wrong_password")
    page.get_by_test_id("signin-submit").click()

    error_alert = page.get_by_test_id("signin-error")
    expect(error_alert).to_be_visible()
    expect(error_alert).to_contain_text("Username or password is invalid")
