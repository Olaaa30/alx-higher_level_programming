#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_chr = ""
    if length < 1:
        first_chr = "None"
    first_chr = sentence[0]
    tup = length, first_chr
    return(tup)