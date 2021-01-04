import datetime
import os
import pathlib
import pprint

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from natsort import natsorted
import numpy as np
from PIL import Image


class Converter(object):
    def __init__(self, path, ext):
        self.path = pathlib.Path(path)
        self.ext = ext
        self.count = 0
        self.now = datetime.datetime.now()
        self.file_name = '{}.pdf'.format(self.now.strftime('%Y%m%d'))
        self.dir_name = 'dir{}/'.format(self.now.strftime('%Y%m%d'))

    def png_to_pdf(self):
        os.makedirs(self.dir_name, exist_ok=True)
        images = os.listdir(self.path)
        for i in natsorted(images):
            if i.endswith(self.ext):
                print(i)
                image = Image.open(str(self.path) + '/' + i)
                image = np.asarray(image)
                fig = plt.figure()
                plt.axis('off')
                plt.imshow(image, interpolation="lanczos")
                self.count += 1
                pp = PdfPages(self.dir_name + str(self.count) + '_' + self.file_name)
                pp.savefig(fig, dpi=500, facecolor='azure', bbox_inches='tight', pad_inches=0)
                pp.close()


