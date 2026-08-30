# This is how I build this slack bot

*  1 go to https://api.slack.com/apps and choose From scratch.
*  add scopes bot and user:  chat:write
*  go to install app and install to workspace
*  copy the bot token to .env file
*  app channel by "Agents & apps"
*  Install the Python packages: slack_sdk and python-dotenv
  *   -> py -m pip show slack_sdk python-dotenv
  *   code it and run
