def upper(string):
    '''
    capitalise everything
    '''
    return string.upper()
def upper_first(string):
    '''
    capitalise every word in a string
    '''
    return ' '.join([word.capitalize() for word in string.split()])
