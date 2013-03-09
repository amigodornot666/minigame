'''
    minigame.tools.dice.dieclass.py

    dice utilitys written in standard python 2.7

    by: aMigod666(KyleJRoux)
'''
import random

class BaseDie(object):
    '''
    BaseDie defines the generic dice behivor

    the standard default 6 sided die is just Die for simplicty
    anything else has a specific name. 
    '''
    _faces = [None, 'One', 'Two', 'Three', 'Four', 'Five', 'Six']
    _nums = [None, 1, 2, 3, 4, 5, 6]
    _face_num_map = {None: None, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6}

    def __init__(self, display=False):
        '''
        assign an inital rolled number, but do not display unless given a seprate flag
        '''
        self.gen_num()
        if (display):
            print self.return_roll()
        
    def __str__(self):
        return str(self.num)

    def __repr__(self):
        return str(self.num)

    def roll(self):
        ''' generates and prints a new random number'''
        self.gen_num()
        x = self.return_num()
        print x
    
    def gen_num(self):
        '''to be complete, define with set_face()'''
        raise NotImplementedError

    def return_num(self):
        ''' return rolled number to other functions'''
        return self.num

    def set_face(self):
        ''' assign the face of die based on the roll '''
        self.face = BaseDie._faces[self.num]

class Die(BaseDie):
    ''' standard 6 sided die '''
    def gen_num(self):
        self.num = random.randrange(1,7)
        self.set_face()

def test():
    #x = BaseDie()
    #x.roll()
    x = Die()
    print x
    for i in range(5):
        x.roll()


if __name__ == "__main__":
    test()

