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

now = dt.now()
d = now.day
m = now.month
stringD = now.strftime("%A")
hour = now.hour
minute = now.minute
print(now.strftime("%A, %B %d, %Y"))
print(f"Today is {stringD}, {m}/{d}")
print(f"Current time: {hour}:{minute:02d}")

# example: Monday from 11:50 AM to 12:00 PM

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
# monday on zoom 12-2pm : https://csumb.zoom.us/j/82255850123. 
# Thursday in person BIT 203 at 12-2 pm
# Friday on Zoom 4-6 pm: https://csumb.zoom.us/j/83142158374  


message = ""
# print message with zoom link for Monday office hours if the current time is between 11:50 AM and 12:00 PM on Monday
if stringD == "Monday" and hour == 11 and minute >= 50:
    print(f"Hello! <!channel> Today's office hours is about to start.\n{':clock2:'} When: {m}/{d},  12:00 PM – 2:00 PM.\n{':computer:'}Where: Zoom https://csumb.zoom.us/j/82255850123")
    message = (
        f"Hello! <!channel> Today's office hours is about to start.\n"
        f"{':clock2:'} When: {m}/{d}, 12:00 PM – 2:00 PM.\n"
        f"{':computer:'}Where: Zoom https://csumb.zoom.us/j/82255850123"
    )
    #post reminder message to Slack channel before 11:50 AM on Monday.
elif stringD == "Monday" and (hour < 11 or (hour == 11 and minute < 50)):
    # print message without zoom link for Monday office hours if the current time is not between 11:50 AM and 12:00 PM on Monday
    print(f"Hello! <!channel> Just a quick reminder about today's office hours scheduled.\n{':clock2:'} When: {m}/{d},  12:00 PM – 2:00 PM.\n{':computer:'}Where: Zoom")
    message = (
        f"Hello! <!channel> Just a quick reminder about today's office hours scheduled.\n"
        f"{':clock2:'} When: {m}/{d}, 12:00 PM – 2:00 PM.\n"
        f"{':computer:'}Where: in Zoom"
    )
    
    
    
# print message with or without zoom link for Thursday office hours any time
if stringD == "Thursday" and hour == 11 and minute >= 50:
    print(f"Hello! <!channel> Today's office hours is about to start.\n{':clock2:'} When: {m}/{d},  12:00 PM – 2:00 PM.\n{':computer:'}Where: BIT 203")
    message = (
        f"Hello! <!channel> Today's office hours is about to start.\n"
        f"{':clock2:'} When: {m}/{d}, 12:00 PM – 2:00 PM.\n"
        f"{':computer:'}Where: BIT 203"
    )
# print message before 11:50 AM on Thursday for office hours in BIT 203
elif stringD == "Thursday" and (hour < 11 or (hour == 11 and minute < 50)):
    print(f"Hello! <!channel> Just a quick reminder about today's office hours scheduled.\n{':clock2:'} When: {m}/{d}, 12:00 PM – 2:00 PM.\n{':computer:'}Where: BIT 203")
    message = (
        f"Hello! <!channel> Just a quick reminder about today's office hours scheduled.\n"
        f"{':clock2:'} When: {m}/{d}, 12:00 PM – 2:00 PM.\n"
        f"{':computer:'}Where: BIT 203"
    )
    
# print message with zoom link for Friday office hours if the current time is between 3:50 PM and 4:00 PM on Friday
if stringD == "Friday" and hour == 15 and minute >= 50:
    print(f"Hello! <!channel> Today's office hours is about to start.\n{':clock2:'} When: {m}/{d},  4:00 PM – 6:00 PM.\n{':computer:'}Where: Zoom https://csumb.zoom.us/j/83142158374")
    message = (
        f"Hello! <!channel> Today's office hours is about to start.\n"
        f"{':clock2:'} When: {m}/{d}, 4:00 PM – 6:00 PM.\n"
        f"{':computer:'}Where: Zoom https://csumb.zoom.us/j/83142158374"
    )
# print message before 3:50 PM on Friday for office hours in Zoom
elif stringD == "Friday" and (hour < 15 or (hour == 15 and minute < 50)):
    print(f"Hello! <!channel> Just a quick reminder about today's office hours scheduled.\n{':clock2:'} When: {m}/{d},  4:00 PM – 6:00 PM.\n{':computer:'}Where: Zoom  https://csumb.zoom.us/j/83142158374")
    message = (
        f"Hello! <!channel> Just a quick reminder about today's office hours scheduled.\n"
        f"{':clock2:'} When: {m}/{d}, 4:00 PM – 6:00 PM.\n"
        f"{':computer:'}Where: in Zoom"
    )
    
    
# print message with or without Zoom link for Monday, Thursday, and Friday office hours any time
print(f"\n ================================================================= \n This is the message that was posted on slack:\n ================================================================= \n {message}")
# post the message to the slack channel
client.chat_postMessage(channel='#cst-329-fall26', text=message)

# test the bot by posting the message to a test channel
# client.chat_postMessage(channel='#test1', text=message)
