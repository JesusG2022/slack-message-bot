import os
from pathlib import Path
from datetime import datetime as dt

from dotenv import load_dotenv
from slack_sdk import WebClient

env_p = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_p)

slack_token = os.environ.get("SLACK_TOKEN")
if not slack_token:
    raise ValueError("SLACK_TOKEN not found in environment variables. Please check your .env file.")

client = WebClient(token=slack_token)

d = dt.now().day
m = dt.now().month
stringD = dt.now().strftime("%A")
print(dt.now().strftime("%A, %B %d, %Y"))

# client.chat_postMessage(channel='#cst-329-fall26',text="hello world")
 
# if stringD == "Tuesday":
#     print(f"Hello! @channel Just a quick reminder about our Deep Work Session scheduled for today.\n{':clock2:'} When: {m}/{d}, 2:00 PM – 4:00 PM.\n{':computer:'}Where: Zoom http://bit.ly/cti-launch-deep-work ")
# if stringD == "Wednesday":
#     print(f"Hello! @channel Just a quick reminder about our Deep Work Session scheduled for today.\n{':clock2:'} When: {m}/{d}, 2:00 PM – 4:00 PM.\n{':computer:'}Where: Zoom http://bit.ly/cti-launch-deep-work ")
# if stringD == "Thursday":
#     print(f"Hello! @channel Just a quick reminder about our Deep Work Session scheduled for today.\n{':clock2:'} When: {m}/{d},  6:00 PM – 8:00 PM.\n{':computer:'}Where: Zoom http://bit.ly/cti-launch-deep-work ")
# if stringD == "Friday":
#     print(f"Hello! @channel Just a quick reminder about our Deep Work Session scheduled for today.\n{':clock2:'} When: {m}/{d},  2:00 PM – 4:00 PM.\n{':computer:'}Where: <http://bit.ly/cti-launch-deep-work|Zoom>")

#  use cst-329-fall26 for office hours 
# monday on zoom 12-2pm : https://csumb.zoom.us/j/82255850123Links. 
# Thursday in person BIT 203 at 12-2pm
# Friday on zoom 4-6 pm : https://csumb.zoom.us/j/83142158374  

if stringD == "Monday":
    print(f"Hello! @channel Just a quick reminder about today's office hours scheduled.\n{':clock2:'} When: {m}/{d},  12:00 PM – 2:00 PM.\n{':computer:'}Where: Zoom  https://csumb.zoom.us/j/82255850123")
    client.chat_postMessage(channel='#cst-329-fall26', text=f"Hello! @channel Just a quick reminder about today's office hours scheduled.\n{':clock2:'} When: {m}/{d},  12:00 PM – 2:00 PM.\n{':computer:'}Where: Zoom  https://csumb.zoom.us/j/82255850123")
if stringD == "Thursday":
    print(f"Hello! @channel Just a quick reminder about today's office hours scheduled.\n{':clock2:'} When: {m}/{d},  12:00 PM – 2:00 PM.\n{':computer:'}Where: BIT 203")
    client.chat_postMessage(channel='#cst-329-fall26', text=f"Hello! @channel Just a quick reminder about today's office hours scheduled.\n{':clock2:'} When: {m}/{d},  12:00 PM – 2:00 PM.\n{':computer:'}Where: BIT 203")
if stringD == "Friday":
    print(f"Hello! @channel Just a quick reminder about today's office hours scheduled.\n{':clock2:'} When: {m}/{d},  4:00 PM – 6:00 PM.\n{':computer:'}Where: Zoom  https://csumb.zoom.us/j/83142158374")
    client.chat_postMessage(channel='#cst-329-fall26', text=f"Hello! @channel Just a quick reminder about today's office hours scheduled.\n{':clock2:'} When: {m}/{d},  4:00 PM – 6:00 PM.\n{':computer:'}Where: Zoom  https://csumb.zoom.us/j/83142158374")
