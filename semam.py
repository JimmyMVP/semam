from urllib.request import urlretrieve
from zipfile import ZipFile
import os

if(not "bbc" in os.listdir(".")):

    DATASET_URL = "http://mlg.ucd.ie/files/datasets/bbc-fulltext.zip"
    DATASET_NAME = "dataset.zip"

    urlretrieve(DATASET_URL, DATASET_NAME)


    zipfile = ZipFile(DATASET_NAME)
    zipfile.extractall()



