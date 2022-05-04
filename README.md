## GitHub Advanced Security: API demo

This repository contains a couple of small examples of using the GitHub Advanced Security webhook events and APIs to implement simple workflows.

### `alert_closed.py`

This sample uses a webhook to respond to Code Scanning alerts which are closed by the user.

To configure and run the sample:
 * Install [ngrok](https://ngrok.com/download).
 * Run `ngrok http 4567` and copy the URL
 * Visit the organization or repository on GitHub that you wish to set the webhook up for, and follow the [Setting up a webhook](https://docs.github.com/en/developers/webhooks-and-events/webhooks/creating-webhooks#setting-up-a-webhook) instructions.
 * Choose the `application/json` content type
 * Configure the events by choosing "Let me select individual events", and deselect the "Push" event and instead select the "Code Scanning alerts" event
 * Run `python3 alert_closed.py`, and experiment with opening and closing alerts in the user interface.


### `mttr.py`

This sample demonstrates how to calculate the mean-time-to-remediate for closed alerts.

To run the sample:
 * Create a GitHub PAT with the `security_events` scope.
 * Set your `GITHUB_TOKEN` environment variable to the generated token.
 * Update the `mttr.py` to specify an org and repo of interest (requires a repository with Code Scanning enabled).
 * Run `python3 mttr.py`
