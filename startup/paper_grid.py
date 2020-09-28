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

# C:\Program Files\Mozilla Firefox



# startup script
# startup script to
# open folders
# run commands
# open url's
# open applications
# activate python environments
# ==============================================================================

# load libraries
import os
import sys
import time
import this
import random
import logging
import threading
import PaperGrid
import subprocess as sp
import webbrowser as wb
from math import pi

logname = 'C:\\Users\\Praveen.TN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\papergrid.log'
#logname = os.path.join(os.getcwd(), 'papergrid.log')
logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%d-%m-%y %H:%M:%S',
                            level=logging.INFO)

if __name__ == "__main__":

    print("PaperGrid")
    logging.info("Running PaperGrid")

    startup = True
    #startup = False # runs all from start; else picks up URL's only!!
    logging.info("Startup: " + str(startup))

    # instantiate the class
    pg = PaperGrid.PaperGrid()
    logging.info("Today's PaperGrid: " + str(pg.get_papergrid()))

    #time.sleep(pi**2)
    try:
        pg.get_browser()
    except BaseException as e:
        logging.info("Encounter: ", e)

    for i in range(3):
        pgx = PaperGrid.PaperGrid()
        pgx.get_browser()
        pgx.get_search_engine()
        print(pgx.search_engine, pgx.browser)
        wb.register("wb", None, wb.BackgroundBrowser(pgx.browser))
        wb.get(pgx.browser).open(pgx.search_engine)
        time.sleep(3)

        logging.info("Web browser: " + pgx.browser)
        logging.info("Search engine: " + pgx.search_engine)

    if startup:
        # open folders
        folders = [ "C:/Users/Praveen.TN/Workspaces/workspace-dream/dream",
                    "C:/Users/Praveen.TN/Workspaces",
                    "C:/Users/Praveen.TN/Workspaces/workspace-qiskit/qiskit",
                    "C:/Users/Praveen.TN/Downloads",
                    "C:/Users/Praveen.TN/Desktop/contributions",
                  ]
        for folder in folders:
            pg.open_folders(folder)

        # run commands
        pg.run_commands()

        # open books in pdf reader
        subjects = ['quantum', 'classics', ]
        pg.read_books(subjects)

    # open urls
    for bucket in pg.qubits_url:
        pg.open_urls(bucket)
        

    print("PaperGrid Bye Dhwani!")
