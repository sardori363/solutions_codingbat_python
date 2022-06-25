'''
                                            HELLO_NAME


Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'
'''

def hello_name(name):
  return "Hello " + name + "!"

'''
                                            MAKE_ABBA


Given two strings, a and b, return the result of putting them together in the order abba,
e.g. "Hi" and "Bye" returns "HiByeByeHi".


make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'
'''

def make_abba(a, b):
  return a+b+b+a

'''
                                            MAKE_TAGS

The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this
example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and
word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'
'''

def make_tags(tag, word):
  return '<' + tag + '>' + word + '<' + '/' + tag + '>'

'''
                                            MAKE_OUT_WORD


Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".


make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'
'''

def make_out_word(out, word):
  return out[:2] + word + out[2:]

'''
                                            EXTRA_END


Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.


extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
'''

def extra_end(str):
  if len(str) <= 2:
    return str*3
  else:
    return str[-2:]*3

'''
                                            FIRST_TWO

Given a string, return the string made of its first two chars, so the String "Hello" yields
"He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and
the empty string "" yields the empty string "".


first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'
'''

def first_two(str):
  return str[:2]

'''
                                            FIRST_HALF


Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'
'''

def first_half(str):
  return str[:len(str)/2]

'''
                                            


'''