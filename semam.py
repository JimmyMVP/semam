from urllib.request import urlretrieve
from zipfile import ZipFile

DATASET_URL = "http://mlg.ucd.ie/files/datasets/bbc-fulltext.zip"
DATASET_NAME = "dataset.zip"

urlretrieve(DATASET_URL, DATASET_NAME)


zipfile = ZipFile(DATASET_NAME)
zipfile.extractall()



