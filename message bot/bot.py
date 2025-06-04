import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime as dt

env_p = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_p)

slack_token = os.environ.get('SLACK_TOKEN')
if not slack_token:
    raise ValueError("SLACK_TOKEN not found in environment variables. Please check your .env file.")

client = slack.WebClient(token=slack_token)

d = dt.now().day
m = dt.now().month
stringD = dt.now().strftime("%A")
print(dt.now().strftime("%A, %B %d, %Y"))

client.chat_postMessage(channel='#test1',text="hello world")
 
if stringD == "Tuesday":
    print(f"Hello! @channel Just a quick reminder about our Deep Work Session scheduled for today.\n{':clock2:'} When: {m}/{d}, 2:00 PM – 4:00 PM.\n{':computer:'}Where: Zoom http://bit.ly/cti-launch-deep-work ")
if stringD == "Wednesday":
    print(f"Hello! @channel Just a quick reminder about our Deep Work Session scheduled for today.\n{':clock2:'} When: {m}/{d}, 2:00 PM – 4:00 PM.\n{':computer:'}Where: Zoom http://bit.ly/cti-launch-deep-work ")
if stringD == "Thursday":
    print(f"Hello! @channel Just a quick reminder about our Deep Work Session scheduled for today.\n{':clock2:'} When: {m}/{d},  6:00 PM – 8:00 PM.\n{':computer:'}Where: Zoom http://bit.ly/cti-launch-deep-work ")
if stringD == "Friday":
    print(f"Hello! @channel Just a quick reminder about our Deep Work Session scheduled for today.\n{':clock2:'} When: {m}/{d},  2:00 PM – 4:00 PM.\n{':computer:'}Where: <http://bit.ly/cti-launch-deep-work|Zoom>")
