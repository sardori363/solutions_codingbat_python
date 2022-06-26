'''
string_times


Given a string and a non-negative int n, return a larger string that is n copies of the original string.


string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
'''


def string_times(str, n):
    result = ""
    for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
        result = result + str  # could use += here
    return result


'''
front_times


Given a string and a non-negative int n, we'll say that the front of the string is
 the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;


front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
'''


def front_times(str, n):
    result = ""
    s = str[:3]
    for i in range(n):
        result += s
    return result


'''
string_bits

Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
'''


def string_bits(str):
    result = ""
    l1 = list(range(0, len(str), 2))
    for i in l1:
        result += str[i]
    return result


'''
string_splosion

Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''


def string_splosion(str):
    result = ''
    for n in range(0, len(str) + 1):
        result += str[:n]
    return result
