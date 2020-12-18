# Copyright (C) By @StarkGang And @ZeltraxRockz
# Powered By @Nemo_Projects
# Copyright (C) By @UNKNOWN_MEMEBER_69
# IMPORTED TO HYPERUSERBOT-X FROM FRIDAY USER BOT
# THNX MR.STARK SIR AKA MIDHUN SIR
# CREDITS GOES TO RESPECTED OWNERS
import random
import string


# String Finder
def stark_finder(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


# Id Generator
def id_generator(size=64, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))
