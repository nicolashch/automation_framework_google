@web

Feature: Go to google page

    Scenario: Load Home Page

        When User visits google

        Then User can search desired word
        And User clicks at first link
        And Is redirected to site
