# load libraries
import os
import time
import random
from math import pi
import webbrowser as wb
from random import shuffle

# from __future__ import braces

# antigravity
import antigravity
print("plying...!", pi)


class PaperGrid():
    def __init__(self):
        self.chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        self.firefox = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
        self.browsers = [self.chrome, self.firefox, ]
        self.browser = random.choice(self.browsers)
        self.search_engines = ["https://www.bing.com/", "https://duckduckgo.com/", "https://www.google.co.in/", ]
        self.search_engine = random.choice(self.search_engines)
        self.pdf_reader = r'""C:\\Program Files\\Tracker Software\\PDF Editor\\PDFXEdit.exe""'
        
        self.books_directory = {
                               'ai': "C:\\Users\\Praveen.TN\\Desktop\\contributions\\Books\\AI\\",
                               'classics': "C:\\Users\\Praveen.TN\\Desktop\\contributions\\Books\\Classics\\",
                               #'qcomics': "C:\\Users\\Praveen.TN\\Desktop\\docs\\Q\\Resources\\QM-Comics-MS-Present\\",
                               'quantum': "C:\\Users\\Praveen.TN\\Desktop\\contributions\\Books\\Q\\",
                               }

        self.reading_list = []

        self.watch_list = [ "https://www.youtube.com/playlist?list=PLmRxgFnCIhaMgvot-Xuym_hn69lmzIokg",
                            
                          ]

        self.prior_urls = [ "http://shaey.in/",
                            "http://nautil.us/",
                            "https://aeon.co/",
                            "https://scienceillustrated.com.au/blog/",
                            "https://cmt3.research.microsoft.com/Conference/Recent",
                          ]

        self.socia_urls = [ "https://twitter.com/",
                            "https://www.quora.com/",                            
                          ]

        self.cours_urls = [ "https://www.coursera.org/",
                            "https://www.edx.org/",
                          ]

        self.aimls_urls = [ "https://syncedreview.com/",
                            "http://www.roboticmagazine.com/",
                            "https://www.artificialintelligence-news.com/",
                            "https://distill.pub", 
                            "https://ai.google/",
                            "https://arxiv.org/",
                            "https://www.analyticsinsight.net/",
                          ]

        self.artis_urls = [ "http://abstractions.nautil.us/",
                            "http://poetry.nautil.us/",
                          ]

        self.rando_urls = [ "https://c.xkcd.com/random/comic/",
                            "https://en.wikipedia.org/wiki/Special:Random",
                            "https://www.explainxkcd.com/wiki/index.php/Special:Random",
                            "http://www.irregularwebcomic.net/random.php",
                          ]

        self.astro_urls = [ "https://cosmosmagazine.com/",
                            "https://apod.nasa.gov/apod/astropix.html",
                            "https://dailygalaxy.com/",
                            "http://cosmos.nautil.us/",
                          ]

        self.talks_urls = [ "https://www.brighttalk.com/",
                            #"https://anchor.fm/",
                          ]

        self.facts_urls = [ "https://www.nngroup.com/",
                            "https://www.rd.com/",
                            "https://reportswatch.com/",
                            "https://www.pewresearch.org/",
                            "https://fivethirtyeight.com/",
                            "https://www.frontiersin.org/",
                          ]

        self.footb_urls = [ "https://www.espn.in/football/league/_/name/eng.1",
                            "https://footystats.org/england/premier-league/",
                          ]

        self.natur_urls = [ "https://www.nationalgeographic.com/",
                            
                          ]

        self.scien_urls = [ "https://phys.org/",
                            "https://www.sciencefocus.com/",
                            "https://www.nature.com/",
                            "https://spectrum.ieee.org/computing",
                            "https://www.livescience.com/",
                            "http://tlas.nautil.us/",
                            "https://scitechdaily.com/",
                            "https://longreads.com/",
                            "https://thebrowser.com/",
                            "https://www.wired.com/",
                            "https://futurism.com/",
                            "https://www.scientificamerican.com/",
                            "https://science.sciencemag.org/",
                            "http://maxplanck.nautil.us/",
                            "https://www.worldscientific.com/",
                            "http://alliance.nautil.us/",
                            "https://www.the-scientist.com/",
                          ]

        self.quant_urls = [ "https://quantumzeitgeist.com/",
                            "https://quantum-computing.ibm.com/",
                            "https://qiskit.org/textbook/ch-states/introduction.html",
                            "https://hackaday.io",
                            "https://www.twitch.tv/crazy4pi314/schedule",
                            "https://www.youtube.com/playlist?list=PLmRxgFnCIhaMgvot-Xuym_hn69lmzIokg",
                            "https://qiskit.org/documentation/tutorials/circuits/2_plotting_data_in_qiskit.html",
                            "http://quantumapalooza.com/",
                            "https://www.scottaaronson.com/",
                            "http://quantumcatalog.com/",
                            "https://quantum.country/qcvc",
                            #"https://www.youtube.com/watch?v=zHKdx13iD1o",
                            #"https://theoreticalminimum.com/courses",
                            #"https://www.youtube.com/watch?v=b0EChbwSuuQ&feature=emb_logo",
                            #"https://www.youtube.com/watch?v=F_Riqjdh2oM&list=PLWJPmidafEvy9TiFeQevjFzUSU5mFxRoa&index=10&t=0s",
                          ]

        self.reads_urls = [ "https://www.t3.com/",
                            "https://hedgehogreview.com/",
                            "https://www.popularmechanics.com/",
                            "https://www.lrb.co.uk/",
                            "https://benjaminreinhardt.com/",
                            "https://www.nybooks.com/",
                            "https://www.tabletmag.com/",
                            "https://restofworld.org/",
                            "http://www.openculture.com/",
                            "https://wingedexpress.com/",
                            "https://cphmag.com/",
                            "https://thenextweb.com/",
                            "https://archpaper.com/",
                            "https://thereader.mitpress.mit.edu/",
                          ]

        self.newes_urls = [ "https://www.wsj.com/news/us/",
                            "https://www.bloomberg.com/",
                            
                          ]

        self.inter_urls = [ "https://www.academia.edu/",
                            "https://www.syfy.com/",
                            "http://mitp.nautil.us/",
                            "https://venturebeat.com/",
                            "https://www.technologyreview.com/",
                          ]

        self.stack_urls = [ "https://datascience.stackexchange.com/questions?sort=newest",
                            "https://stackoverflow.com/questions/tagged/python?sort=newest&pageSize=10", 
                            "https://stats.stackexchange.com/questions?sort=newest",
                            "https://quantumcomputing.stackexchange.com/",
                          ]

        self.eandy_urls = [ "https://www.yammer.com/ey.com/#/home",
                            "https://eylearning.udemy.com/home/my-courses/learning/",
                            "https://sites.ey.com/sites/globalinnovationteam/sitepages/ai@ey.aspx",
                            "https://portal.azure.com/",
                            "https://www.office.com/",
                            "https://aiatey.cognistreamer.com/",
                            "https://studio.azureml.net/",
                          ]

        self.skype_urls = [ "https://algorithmia.com/",
                            "https://developerblog.myo.com/",
                            "https://ghost.org/",
                            "http://www.patentsview.org/",
                            "https://towardsdatascience.com/solving-nlp-task-using-sequence2sequence-model-from-zero-to-hero-c193c1bd03d1",
                            "https://theaisummit.com/",
                            "https://www.superdatascience.com/",
                            "https://analyticsvidhya.com/",
                            "https://link.springer.com/journal/11336",
                            "https://www.adasci.org/",
                            "http://sci-hub.tw/",
                            "https://www.livejournal.com/",
                            "https://skymind.ai/wiki/",
                            "http://www.research.att.com/",
                            "https://www.cnet.com/",
                            "https://hai.stanford.edu/",
                            "http://www.yalescientific.org/",
                            "https://mechanixillustrated.technicacuriosa.com/",
                            "https://www.skeptic.com/",
                            "https://www.techexplorist.com/",
                            "https://wazirx.com/",
                          ]

        self.qubits_url = [ self.watch_list, self.prior_urls, self.socia_urls, self.cours_urls, 
                            self.aimls_urls, self.artis_urls, self.rando_urls, self.astro_urls,
                            self.talks_urls, self.facts_urls, self.footb_urls, self.natur_urls,
                            self.scien_urls, self.quant_urls, self.reads_urls, self.newes_urls,
                            self.inter_urls, self.stack_urls, self.eandy_urls, self.skype_urls,
                            
                          ]


    def get_random_num(self, ):
        return random.randint(39,59)

    def get_browser(self, ):
        self.browser = random.choice(self.browsers)

    def get_search_engine(self, ):
        self.search_engine = random.choice(self.search_engines)

    def get_papergrid(self, ):
        pg = 0
        for i in range(1,5):
            p = pow(10,i)
            r = self.get_random_num()
            pg += p * r
        return pg

    def open_urls(self, urls, st=3):
        shuffle(urls)
        for url in urls:
            # sleep time in seconds
            s = (pi**2) * self.get_random_num()
            self.get_browser()
            print("Sleep: " + str(s) + ' seconds')
            print("Web browser: " + self.browser)
            print("URL: " + url)
            time.sleep(s)

            # open browser and url
            wb.get(self.browser).open(url)

    def open_folders(self, folder):
        try:
            path = os.path.realpath(folder)
            os.startfile(path)
        except  BaseException as e:
            print("encountered exception", e)
            pass

    def read_books(self, subjects):
        # open pdf exchange editor
        os.system('start cmd /k ' + self.pdf_reader)

        for subject in subjects:
            root_dir = self.books_directory[subject]

            self.reading_list = os.listdir(root_dir) 
            for file in self.reading_list:
                os.startfile(os.path.join(root_dir, file))

                time.sleep(pi**2)

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
        #os.system('start \"\" cmd /k \"cd /D C:\\ & C:\\Python37\\envs\\innventure\\Scripts\\activate\"')
        #os.system('start \"\" cmd /k \"cd /D C:\\ & C:\\Python37\\envs\\innventure\\Scripts\\activate & cd /D C:\\Users\\Praveen.TN\\Workspaces\\workspace-dtccstock\\dtcc\"')
        #os.system('start \"\" cmd /k \"cd /D C:\\ & C:\\Python37\\envs\\quoted\\Scripts\\activate & cd /D C:\\Users\\Praveen.TN\\Workspaces\\workspace-quoted\\quoted\"')
        os.system('start \"\" cmd /k \"cd /D C:\\ & C:\\Python37\\envs\\dream\\Scripts\\activate & cd /D C:\\Users\\Praveen.TN\\Workspaces\\workspace-dream\\dream\"')
        os.system('start \"\" cmd /k \"cd /D C:\\ & C:\\Python37\\envs\\qiskit\\Scripts\\activate & cd /D C:\\Users\\Praveen.TN\\Workspaces\\workspace-qiskit\\qiskit\"')
        os.system('start \"\" cmd /k \"cd /D C:\\ & C:\\Python37\\envs\\dream\\Scripts\\activate & cd /D C:\\Users\\Praveen.TN\\Workspaces\\workspace-dream\\dream\"')
        os.system('start \"\" cmd /k \"cd /D C:\\ & C:\\Python37\\envs\\qiskit\\Scripts\\activate & cd /D C:\\Users\\Praveen.TN\\Workspaces\\workspace-qiskit\\qiskit\"')
        time.sleep(pi*2)

        # ey toolbox
        toolbox = r'"C:\Program Files\EY\EY Toolbox\EYToolbox.exe"'
        os.system('start cmd /k ' + toolbox)
        #os.system('start \"\" cmd /k \"C:\\Program Files\\EY\\EY Toolbox\\EYToolbox.exe & exit\"')
        time.sleep(pi**2)
