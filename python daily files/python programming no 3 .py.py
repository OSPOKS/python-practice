class RegexPractice:
    """
    Regular expression:
    * lookahead
        1. positive
        2. negative
    * lookbehind
        1. positive
        2. negative
    """
    @classmethod
    def reg(cls, pattern = '', text = ''):
        return re.compile(pattern, re.VERBOSE).search(text)
    @classmethod
    def lookahead_positive(cls):
        return cls.reg('g(?=oo)', text = 'google search.')
    @classmethod
    def lookahead_negative(cls): 
        return cls.reg('goo(?!ggg)', text = 'google search.')
    @classmethod
    def lookbehind_positive(cls):
        return cls.reg('(?<=g)oo', text = 'google search.')
    @classmethod
    def lookbehind_negative(cls):
        return cls.reg('(?<!g)gle', text = 'google search.')
