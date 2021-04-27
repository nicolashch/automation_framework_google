import pytest
import logging

from google_search import GoogleSearch


def test_visit_google(config, web_browser, context):
    google_home = GoogleSearch(web_browser, config)
    google_home.load()
    google_home.search_input()
    context["browser"] = google_home
    print(context)
    assert "Wikipedia" in google_home.title(), "You are not at Google"


'''def test_search_input(context):
    google_home = context["browser"]
    google_home.search_input()'''
