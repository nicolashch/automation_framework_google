@web

Feature: Go to google page and search for wikipedia

    Scenario: Load Home Page

        Given User is at Google

        When User searches desired word

        Then User clicks at first link
        And Is redirected to site
