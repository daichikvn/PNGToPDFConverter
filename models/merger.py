import datetime
import os
import pathlib
import pprint

from natsort import natsorted
from PyPDF2 import PdfFileMerger


class Merger(object):
    def __init__(self):
        self.now = datetime.datetime.now()
        self.dir_name = 'dir{}/'.format(self.now.strftime('%Y%m%d'))
        self.path = pathlib.Path(self.dir_name)
        self.filelist = os.listdir(self.path)

    def join(self):
        merger = PdfFileMerger()

        for file in natsorted(self.filelist):
            if file.endswith('.pdf'):
                print(file)
                merger.append(self.dir_name + '/' + file)

        merger.write('merged.pdf')
        merger.close()