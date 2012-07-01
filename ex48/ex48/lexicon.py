class lexicon(object):

    def __init__(self, words):
        self.words = words
                          
    def convert_numbers(self, s):
        try:
            return int(s)
        except ValueError:
            return None
        
    def scan(self, words):
        split_words = words.split(' ')
        parsed_words = []
        word_list = [('direction', 'north'),
                     ('direction', 'south'),
                     ('direction', 'east'),
                     ('verb', 'go'),
                     ('verb', 'kill'),
                     ('verb', 'eat'),
                     ('stop', 'the'),
                     ('stop', 'in'),
                     ('stop', 'of'),
                     ('noun', 'bear'),
                     ('noun', 'princess')]
        for item in split_words:
            if item in word_list:
                parsed_words.append(item)
            elif convert_numbers(item):
                parsed_words.append(('number', convert_numbers(item)))
            else:
                parsed_words.append(('error', item))
                
        return parsed_words