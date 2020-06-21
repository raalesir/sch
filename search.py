#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import platform
import os
import re

import io

def rank(lst):
    """
    takes a list of results and returns a sorted list by rank.
    [ { 'name': file1, 'content': set1}, {'name': file2, 'content': set2}]

    Each item of a list is a dict with the key being name of the file and the value -- the fraction of
    matched words

    :param lst: list with unsorted results
    :return: sorted list
    """
    newlist = sorted(lst, key=lambda k: k['match_fraction'], reverse=True)

    return  newlist


def calculate_fraction(lst, words_to_find_):
    """
    Calculates a score for each item of the list, where each element is a dictionary with two elements.
    The first element is a name of the file, and the second is the document's vocabulary

    :param lst: list with text files contents
    :param words_to_find_:
    :return: list where each element is a dict: {'name' : fname1, 'match_fraction': match fraction}
    """

    results = []
    for item in lst:
        found = []
        for word in words_to_find_:
            if word in item['filtered_content']:
                found.append(word)
        # print("%s out of  %i  words were found in doc %s " % (found, len(words_to_find_), item['name']))
        results.append({'name': item['name'], 'match_fraction': 100. * len(found) / len(words_to_find_)})

    return  results


def filter_content(lst):
    """
    takes  a list, where each element  is a dict with two elements: {'name': path, 'content' : file content as string}.
    The content of each file is being transformed from a string to set. i.e. creating a vocabulary, where each element  is a unique word.

    The  word definition: every element of a string separated by space, where any characters not in '[^A-Za-z\s-]' being removed.

    The  set in Python has O(1) complexity when performing search like "elem in set".

    :param lst:
    :return: list  with filtered content.
    """

    clean_content = []
    for item in lst:
        tmp = re.sub(r'[^A-Za-z\s-]', '', item['content']).lower()
        tmp = re.sub(r'\n', ' ', tmp)
        clean_content.append({'name': item['name'], 'filtered_content': set((tmp.split()))}
                             )

    return  clean_content


def read_files(data_dir):
    """
    reads files in 'data_dir' and returns a list   of dicts. Each dict  has two elements:
    {'name': path, 'content' : file content as string}

    :param data_dir: data directory to go through
    :return: list of dicts.
    """

    files_content = []
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            path = os.path.join('data', file)
            print(path)
            with open(path) as f:
                files_content.append({'name': path, 'content': f.read()})

    return files_content



def test_clean_content():
    """
    testing `filter_content` function
    :return: True/False
    """
    f = io.StringIO("some initial 1text data!")

    tmp = [{'name': f, 'content': f.read()}]
    clean_content_ = filter_content(tmp)

    assert clean_content_[0]['filtered_content'] ==  set('some initial text data'.split())



def test_calculate_fraction():
    """
    testing calculate_fraction
    {'name' : fname1, 'match_fraction': match fraction}
    :return:
    """
    tmp = set('testing tested test ok one one'.split())
    flt = [{'name': 'test', "filtered_content": tmp}]
    wtf = set(['one', 'ok', 'five', 'test'])

    res = calculate_fraction(flt, wtf)

    assert res[0]['match_fraction'] == 75.0






if __name__=="__main__":
    print("hello from python %s" % platform.python_version())


    words_to_find = set(['a', 'over', 'by', 'the', 'test'])

    while True:
        words_to_find = set(input("input  words separated by space\nto quit type  'q'\nsearch> ").split())
        if 'q' not in words_to_find:
            print(words_to_find)
            data_dir = 'data'
            files_content = read_files(data_dir)

            # print("===================")
            # print(type(files_content[0]),files_content[0] )
            # print("===================")

            clean_content = filter_content(files_content)

            results = calculate_fraction(clean_content, words_to_find)
            for line in rank(results):
                print(line)
            print(30*"=")

        else:
            break
