# get()

# string values
my_str_dict = {
      'red': '113a',
      'green': '347b',
      'cyan': '553c'
}

def valueof(colour):
    return 'value is %s' % my_str_dict.get(colour, 'unknown')

valueof('red')
# 'value is 113a'

valueof('purple')
# 'value is unknown'

####################

# numerical values
my_num_dict = {
      'red': 113,
      'green': 347,
      'cyan': 553
}

def valueof(colour):
    return 'value is %d' % my_num_dict.get(colour, 0)

valueof('red')
# 'value is 113'

valueof('purple')
# 'value is 0'
