import os
import sys
import time

import pyautogui as pg
from termcolor import colored


class ScreenCapture(object):
    def __init__(self):
        self.pages = 0
        self.upperleft = (0, 0)
        self.lowerright = (0, 0)
        self.color = 'blue'
        self.question = 'red'
        self.border = ("\n=================================next=================================")

    def size_check(self):
        print(colored(self.border, self.color))
        print(colored("search screen size of your book, so you follow next instructions", self.color))
        print(colored("your screen size : ", self.color), pg.size())
        time.sleep(1)

    def display_set(self):
        print(colored(self.border, self.color))

        set_by_mouse = input(colored("use mouse ? [y/n] : ", self.question))

        if (set_by_mouse == 'y'):
            print(colored(self.border, self.color))
            ready = input(colored("Set your mouse cursor in upper_left corner.\n After finishig your preparetions ? [ok] : ", self.question))
            if (ready == "ok"):
                self.upperleft = pg.position()
                print(colored("upper_left corner : ", self.color), self.upperleft)
                print(colored(self.border, self.color))
                ready = input(colored("Set your mouse cursor in lower_right corner.\n After finishig your preparetions ? [ok] : ", self.question))
                if (ready == "ok"):
                    self.lowerright = pg.position()
                    print(colored("upper_right corner : ", self.color), self.lowerright)
                else:
                    print(colored("error", self.color))
                    sys.exit()
            else:
                print(colored("error", self.color))
                sys.exit()
        else:
            self.upperleft = (0, 0)
            self.lowerright = pg.size()
            print(colored("upper_left corner : ", self.color), self.upperleft)
            print(colored("upper_right corner : ", self.color), self.lowerright)

    def screen_shot(self):
        ##### warning : change double scale in Macbookpro #####
        left = 2*int(self.upperleft[0])
        upper = 2*int(self.upperleft[1])
        width = 2*int(self.lowerright[0]) - 2*int(self.upperleft[0])
        height = 2*int(self.lowerright[1]) - 2*int(self.upperleft[1])
        region = (left, upper, width, height)

        print(colored("region : ", self.color), region)
        print(colored("Finish defining region", self.color))
        time.sleep(1)

        print(colored(self.border, self.color))
        pages = input(colored("Please input number of pages ? [INT] : ", self.question))
        self.pages = int(pages)
        print(colored("pages : ", self.color), self.pages)
        print(colored("Finish defining pages", self.color))
        time.sleep(1)

        print(colored(self.border, self.color))
        print(colored("Set first page of your book with full screen within 3 seconds", self.color))
        ready = input(colored("Can I start shooting ? [ok] : ", self.question))
        if (ready == "ok"):
            time.sleep(3)
            for i in range(self.pages):
                sc = pg.screenshot(region=region)
                sc.save('target/' + str(i + 1) + '.png')
                time.sleep(0.5)
                # pg.press("left")
                pg.press("right")
                time.sleep(0.5)
        else:
            print(colored("cancel.......", self.color))
            sys.exit()
