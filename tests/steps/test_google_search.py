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


@when('The user visits google')
def visit_google(config, web_browser, context):
    google_home = GoogleSearch(web_browser, config)
    google_home.load()
    context["browser"] = google_home
    assert "Google" in google_home.title(), "You are not at Google"


@then('The user can visualize google search bar')
def search_input(context):
    google_home = context["browser"]
    google_home.search_input()
