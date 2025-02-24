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
# print(stringD)yy


if stringD == "Wednesday":
    # client.chat_postMessage(channel='#bot-message', text = f"Hello! @channel Just a quick reminder about our Deep Work Session scheduled for today.\n{':clock2:'} When: {m}/{d}, from 12 pm to 2pm.\n{':computer:'} Where: CSUMB BIT Building (506), Room: 111")
    # print("M")
    print(f"Hello! @channel Just a quick reminder about our Deep Work Session scheduled for today.\n{':clock2:'} When: {m}/{d}, from 4 pm to 6 pm.\n{':computer:'}Where: CSUMB, 045 Coast Hall room 103")

if stringD == "Friday":
    i = input("It the guided: ")
    print(f"Hello! @channel Just a quick reminder about our Deep Work Session scheduled for today.\n{':clock2:'} When: {m}/{d}, from 2 pm to 4pm.\n{':computer:'} Where: CSUMB BIT Building (506), Room: 223")
    # client.chat_postMessage(channel='#bot-message', text = f"Hello! @channel Just a quick reminder about our Deep Work Session scheduled for today.\n{':clock2:'} When: {m}/{d}, from 2 pm to 4pm.\n{':computer:'} Where: CSUMB BIT Building (506), Room: 108")
    
    if i.lower() =="y":
        print(f"Hello! @channel Just a quick reminder about our Guided Session scheduled for today. {':clock2:'} When: {m}/{d} from 4pm to 6pm. {':computer:'} Where: CSUMB BIT Building (506), Room: 223.\n{':pizza:'} Pizza will be offered.\n{':droplet:'} Bring your own beverage")
        # client.chat_postMessage(channel='#bot-message', text = f"Hello! @channel Just a quick reminder about our Guided Session scheduled for today. {':clock2:'} When: {m}/{d} from 4pm to 6pm. {':computer:'} Where: CSUMB BIT Building (506), Room: 111.\n{':pizza:'} Pizza will be offered.\n{':droplet:'} Bring your own beverage")

