from bs4 import BeautifulSoup
import urllib2
import sched, time
import os

s = sched.scheduler(time.time, time.sleep)

def getInfo():
    os.system('cls')
    os.system('clear')
    resp = urllib2.urlopen("https://www.reddit.com/r/smashbros/comments/3dmmuq/evo_general_tournament_thread_live_updates_ft/")

    data = resp.read()
    resp.close()

    parsedData = BeautifulSoup(data, "html.parser")

    headers = parsedData.findAll("p")

    shouldDisp = False

    for p in headers:
        if(shouldDisp):
            print p.getText()
        if(p.getText() == "STREAM Link: http://www.twitch.tv/srkevo2"):
            shouldDisp = True
        if(p.getText() == "[8:20 AM]: VGBC ANNOUNCES SALTY SUITE TRAILER"):
            break

s.enter(60, 1, getInfo(), (s,))
s.run()
