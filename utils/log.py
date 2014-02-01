__author__ = 'thor'

import datetime


def log_to_file(filename, msg):
    with open(filename, "a") as myfile:
        myfile.write(hms_message() + msg + "\n")

def hms_message(msg=''):
    t = datetime.now().time()
    return "%02.0f:%02.0f:%02.0f - %s" % (t.hour, t.minute, t.second, msg)