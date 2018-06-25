import re


def process_chapter_num(content):
    word_num = len(re.sub('\W', '', content)) / 10000
    return "%.2f" % word_num
