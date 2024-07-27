import webbrowser
import time
import random

while True:
    sites = random.choice(["google.com","youtube.com","doddle.com","samsung.com"])
    visit = "http://www.{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 20)
    time.sleep(seconds)
