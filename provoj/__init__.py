#!/usr/bin/env python
import math
import datetime

class NewTest(object):
    def __init__(self, title=None):
        # define the scores dictionary, and initialize
        self.scores = {}
        self.scores["success"] = 0
        self.scores["error"] = 0
        self.time = datetime.datetime.now()
        if title != None:
            self.title = title
            print("")
            pc.blue("- " + title)
        else:
            self.title = ""
            print("")
            pc.blue("- unnamed test")
    def equal(self, action, a, b):
        if a != b:
            pc.error(action + " - Error, '" + str(a) + "' should be equal to '" + str(b) + "'")
            self.scores["error"] += 1
        else:
            pc.checked(action)
            self.scores["success"] += 1
    def notequal(self, action, a, b):
        if a == b:
            pc.error(action + " - Error, '" + str(a) + "' should be not equal to '" + str(b) + "'")
            self.scores["error"] += 1
        else:
            pc.checked(action)
            self.scores["success"] += 1
    def bigger(self, action, a, b):
        if a < b:
            pc.error(action + " - Error, '" + str(a) + "' should be bigger than '" + str(b) + "'")
            self.scores["error"] += 1
        else:
            pc.checked(action)
            self.scores["success"] += 1
    def smaller(self, action, a, b):
        if a > b:
            pc.error(action + " - Error, '" + str(a) + "' should be smaller than '" + str(b) + "'")
            self.scores["error"] += 1
        else:
            pc.checked(action)
            self.scores["success"] += 1

    def length(self, action, a, l):
        if len(a) != l:
            pc.error(action + " - Error, actual length is '" + str(len(a)) + "', expected to be '" + str(l) + "'")
            self.scores["error"] += 1
        else:
            pc.checked(action)
            self.scores["success"] += 1

    def rStatus(self, action, r, verbose=False):
        if r.status_code < 200 or r.status_code > 299:
            if verbose:
                pc.error(action + " - Error " + str(r.status_code) + ": " + r.text)
            else:
                pc.error(action + " - Error " + str(r.status_code))

            self.scores["error"] += 1
        else:
            pc.checked(action)
            self.scores["success"] += 1

    def printScores(self):
        pc.purple("     Test title: " + self.title)
        score = math.ceil(( self.scores["success"]/(self.scores["success"]+self.scores["error"]) )*100)
        elapsed = datetime.datetime.now() - self.time
        pc.purple("     Score: " + str(score)
            + "% (" + str(self.scores["success"]) + "/" + str(self.scores["success"] + self.scores["error"]) + ")"
            + " Time benchmark: " + str(elapsed))


'''
code to print the colors in the terminal
'''
checkIcon = "✓ "
errorIcon = "❌ "

class pc:
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    END = '\033[0m'

    @classmethod
    def red(cls, s, **kwargs):
        print(cls.RED + s + cls.END, **kwargs)

    @classmethod
    def green(cls, s, **kwargs):
        print(cls.GREEN + s + cls.END, **kwargs)

    @classmethod
    def blue(cls, s, **kwargs):
        print(cls.BLUE + s + cls.END, **kwargs)

    @classmethod
    def purple(cls, s, **kwargs):
        print(cls.PURPLE + s + cls.END, **kwargs)

    @classmethod
    def checked(cls, s, **kwargs):
        print("     " + cls.GREEN + checkIcon + s + cls.END, **kwargs)

    @classmethod
    def error(cls, s, **kwargs):
        print("     " + cls.RED + errorIcon + s + cls.END, **kwargs)
