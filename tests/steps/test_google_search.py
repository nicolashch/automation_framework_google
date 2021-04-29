import pytest
import logging

from pytest_bdd import (
    scenarios,
    given,
    then,
    when,
    parsers
)
from google_search import GoogleSearch

scenarios('../features/search.feature')


@given('User is at Google')
def visit_google(config, web_browser, context):
    google_home = GoogleSearch(web_browser, config)
    google_home.load()
    context["browser"] = google_home
    assert "Google" in google_home.title(), "You are not at Google"


@when('User searches desired word')
def search_input(context):
    google_home = context["browser"]
    google_result = google_home.search_input()
    context["browser"] = google_result


@then('User clicks at first link')
def click_on_link(context):
    google_result = GoogleSearch(*context["browser"])
    context["browser"] = google_result.click_on()


@then('Is redirected to site')
def validate_redirection(context):
    site = GoogleSearch(*context["browser"])
    assert 'Wikipedia' in site.title(), "Wrong redirection"

