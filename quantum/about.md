### importing local files in Jupyter notebooks

import os
import sys

sys.path.append(os.getcwd())

from SVM_datasets import sample_ad_hoc_data

# QSVM
