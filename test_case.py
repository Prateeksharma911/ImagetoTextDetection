import unittest
import imagetotext

class TestImage(unittest.TestCase):

    def test_imgtotext(self):
        result = imagetotext.alltext
        self.assertEqual(result,"HOW TO WRITE AlT TEXT AND IMAGE DESCRIPTIONS FOR THE VISUALLY IMPAIRED ")