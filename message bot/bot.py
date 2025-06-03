# import slack as s
# import os as o
# from pathlib import Path as p
# from dotenv import load_dotenv as ld
from datetime import datetime as dt

# env_p = p('.')/'.env'
# ld(dotenv_path=env_p)

# client = s.WebClient(token=o.environ['SLACK_TOKEN'])

d = dt.now().day
m = dt.now().month
stringD = dt.now().strftime("%A")
print(dt.now().strftime("%A, %B %d, %Y"))

if stringD == "Tuesday":
    print(f"Hello! @channel Just a quick reminder about our Deep Work Session scheduled for today.\n{':clock2:'} When: {m}/{d}, 2:00 PM – 4:00 PM.\n{':computer:'}Where: Zoom http://bit.ly/cti-launch-deep-work ")
if stringD == "Wednesday":
    print(f"Hello! @channel Just a quick reminder about our Deep Work Session scheduled for today.\n{':clock2:'} When: {m}/{d}, 2:00 PM – 4:00 PM.\n{':computer:'}Where: Zoom http://bit.ly/cti-launch-deep-work ")
if stringD == "Thursday":
    print(f"Hello! @channel Just a quick reminder about our Deep Work Session scheduled for today.\n{':clock2:'} When: {m}/{d},  6:00 PM – 8:00 PM.\n{':computer:'}Where: Zoom http://bit.ly/cti-launch-deep-work ")
if stringD == "Friday":
    print(f"Hello! @channel Just a quick reminder about our Deep Work Session scheduled for today.\n{':clock2:'} When: {m}/{d},  2:00 PM – 4:00 PM.\n{':computer:'}Where: <http://bit.ly/cti-launch-deep-work|Zoom> ")