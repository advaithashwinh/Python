import unittest
from gamefunction import game,MismatchError,CharacterError
class testgame(unittest.TestCase):
    def testg1(self):
        a=[2,5,7]
        b=[3,6,9]
        self.assertEqual(game(a,b),"WIN")

    def testg2(self):
        a=[2,5,7]
        b=[3,6,2]
        self.assertEqual(game(a,b),"LOSE")

    def testg3(self):
        a=['e,@',3,'f']
        b=['vn6',2,'w']
        self.assertRaises(CharacterError,game,a,b)

    def testg4(self):
        a=[2,3]
        b=[3,2,100]
        self.assertRaises(MismatchError,game,a,b)

    def testg5(self):
        a=[2,5,9,23]
        b=[2,5,9,23]
        self.assertEqual(game(a,b),"LOSE")

if __name__ == '__main__':
    unittest.main()