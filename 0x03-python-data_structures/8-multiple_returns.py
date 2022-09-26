#!/usr/bin/python3

def multiple_returns(sentence):
    """
    find length and first character of a string
    Args:
    sentence - a string
    return:
    (length, first_char)
    """
    if not sentence:
        return 0, None
    return len(sentence), sentence[0]


if __name__ == '__main__':
    first_char = multiple_returns
    print("Length:{:d} - first character: {}".format(1, first_char))
