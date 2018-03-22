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
            pc.error("{} - Error, {} should be equal to {}".format(action, a, b))
            self.scores["error"] += 1
        else:
            pc.checked(action)
            self.scores["success"] += 1
    def notequal(self, action, a, b):
        if a == b:
            pc.error("{} - Error, {} should be not equal to {}".format(action, a, b))
            self.scores["error"] += 1
        else:
            pc.checked(action)
            self.scores["success"] += 1
    def bigger(self, action, a, b):
        if a < b:
            pc.error("{} - Error, {} should be bigger than {}".format(action, a, b))
            self.scores["error"] += 1
        else:
            pc.checked(action)
            self.scores["success"] += 1
    def smaller(self, action, a, b):
        if a > b:
            pc.error("{} - Error, {} should be smaller than {}".format(action, a, b))
            self.scores["error"] += 1
        else:
            pc.checked(action)
            self.scores["success"] += 1

    def length(self, action, a, l):
        if len(a) != l:
            pc.error("{} - Error, actual length is {}, expected to be {}".format(action, a, l))
            self.scores["error"] += 1
        else:
            pc.checked(action)
            self.scores["success"] += 1

    def rStatus(self, action, r, verbose=False):
        if r.status_code < 200 or r.status_code > 299:
            if verbose:
                pc.error("{} - Error {}: {}".format(action, r.status_code, r.text))
            else:
                pc.error("{} - Error {}".format(action, r.status_code))

            self.scores["error"] += 1
        else:
            pc.checked(action)
            self.scores["success"] += 1

    def printScores(self):
        pc.purple("     Test title: " + self.title)
        success = self.scores["success"]
        error = self.scores["error"]
        score = math.ceil((success/(success+error))*100)
        elapsed = datetime.datetime.now() - self.time
        pc.purple("     Score: {} % ({}/{}) Time benchmark: {}".format(score, success, success+error, elapsed))


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
