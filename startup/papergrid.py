# Copyright 2017 The PaperGrid Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

# startup script

# load libraries
import os
import time
import this
import random
import logging
import subprocess as sp
import webbrowser as wb
from math import pi
from random import shuffle

# from __future__ import braces

# antigravity
import antigravity
print("plying...!", pi)


logname = 'papergrid.log'
#logname = os.path.join(os.getcwd(), 'papergrid.log')
logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%d-%m-%y %H:%M:%S',
                            level=logging.INFO)

class PaperGrid():
    def __init__(self):
        self.chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        self.firefox = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
        self.browsers = [self.chrome, self.firefox, ]
        self.browser = random.choice(self.browsers)
        self.search_engines = ["https://www.bing.com/", "https://duckduckgo.com/", "https://www.google.co.in/", ]
        self.search_engine = random.choice(self.search_engines)

        self.definite_urls = [ "https://quantum-computing.ibm.com/", "https://qiskit.org/textbook/ch-states/introduction.html", \
                               "https://www.youtube.com/watch?v=b0EChbwSuuQ&feature=emb_logo", 
                             ]

        self.interesting_urls = ["https://studio.azureml.net/", "http://tlas.nautil.us/", "https://www.livescience.com/", "https://scitechdaily.com/", \
                "https://longreads.com/", "https://thebrowser.com/", "https://spectrum.ieee.org/computing", "https://www.pewresearch.org/", \
                "https://ai.google/", "https://www.wsj.com/news/us/", "https://www.bloomberg.com/", "https://www.academia.edu/", \
                "http://nautil.us/", "https://aeon.co/", "https://apod.nasa.gov/apod/astropix.html", "https://www.techexplorist.com/", \
                "https://cosmosmagazine.com/", "http://www.roboticmagazine.com/", "https://scienceillustrated.com.au/blog/", \
                "http://www.yalescientific.org/", "https://datascience.stackexchange.com/questions?sort=newest", \
                "https://distill.pub", "https://arxiv.org/", "https://fivethirtyeight.com/", "https://www.syfy.com/", \
                "https://stackoverflow.com/questions/tagged/python?sort=newest&pageSize=10", "https://stats.stackexchange.com/questions?sort=newest", \
                "https://eylearning.udemy.com/home/my-courses/learning/", "https://www.wired.com/", "https://futurism.com/", \
                "https://twitter.com/", "http://mitp.nautil.us/", "https://venturebeat.com/", \
                "http://abstractions.nautil.us/", "http://poetry.nautil.us/", "https://archpaper.com/", \
                "http://maxplanck.nautil.us/", "https://www.worldscientific.com/", "https://www.artificialintelligence-news.com/",\
                "http://www.irregularwebcomic.net/random.php", "http://cosmos.nautil.us/", "http://alliance.nautil.us/", "https://phys.org/",\
                "https://www.scientificamerican.com/", "https://science.sciencemag.org/", "https://dailygalaxy.com/", \
                "https://www.skeptic.com/", "https://mechanixillustrated.technicacuriosa.com/", "https://www.the-scientist.com/", \
                "https://www.technologyreview.com/", "https://www.t3.com/", "https://www.explainxkcd.com/wiki/index.php/Special:Random", \
                "https://footystats.org/england/premier-league/", 
                ]

        self.skip_urls = ["https://algorithmia.com/", "https://developerblog.myo.com/", "https://ghost.org/", \
            "https://towardsdatascience.com/solving-nlp-task-using-sequence2sequence-model-from-zero-to-hero-c193c1bd03d1", \
            "https://theaisummit.com/", "https://www.superdatascience.com/", "https://analyticsvidhya.com/", \
            "https://www.office.com/", "http://www.patentsview.org/", "http://sci-hub.tw/", "https://www.livejournal.com/", \
            "https://link.springer.com/journal/11336", "https://www.adasci.org/", "https://portal.azure.com/", "https://medium.com/", \
            "https://skymind.ai/wiki/", "http://www.research.att.com/", "https://www.cnet.com/", "https://hai.stanford.edu/", \
            ]

    def get_random_num(self, ):
        return random.randint(39,59)

    def get_papergrid(self, ):
        pg = 0
        for i in range(1,5):
            p = pow(10,i)
            r = self.get_random_num()
            pg += p * r
        return pg

    def open_urls(self, urls):
        shuffle(urls)
        for url in urls:
            # sleep time in seconds
            s = (pi**2) * self.get_random_num()
            browser = self.browser
            logging.info("Sleep: " + str(s) + ' seconds')
            logging.info("Web browser: " + browser)
            logging.info("URL: " + url)
            time.sleep(s)

            # open browser and url
            wb.get(self.browser).open(url)

    def run_commands(self, ):
        # open outlook
        os.startfile("outlook")
        time.sleep(pi**2)

        # one note
        onenote = r'"C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\ONENOTE.exe"'
        os.system('start cmd /k ' + onenote)
        time.sleep(pi**2)

        # open command prompt
        #os.system('start cmd /k "cd\\"')
        os.system('start \"\" cmd /k \"cd /D C:\\ & C:\\Python37\\envs\\qiskit\\Scripts\\activate & cd /D C:\\Users\\Praveen.TN\\Workspaces\\workspace-qiskit\\qiskit\"')


if __name__ == "__main__":

    print("PaperGrid")
    logging.info("Running PaperGrid")

    pg = PaperGrid()
    logging.info("Today's PaperGrid: " + str(pg.get_papergrid()))

    time.sleep(pi**2)
    wb.get(pg.browser).open(pg.search_engine)
    logging.info("Web browser: " + pg.browser)
    logging.info("Search engine: " + pg.search_engine)

    pg.run_commands()

    pg.open_urls(pg.definite_urls)
    pg.open_urls(pg.interesting_urls)
    pg.open_urls(pg.skip_urls)


