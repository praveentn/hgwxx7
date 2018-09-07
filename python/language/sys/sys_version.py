# loading modules specific to a Python version

import sys

sys.version_info
# sys.version_info(major=3, minor=6, micro=4, releaselevel='final', serial=0)

if sys.version_info[0]>=3:
    from html.parser import HTMLParser
else:
    from HTMLParser import HTMLParser

