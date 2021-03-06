import unittest
from word_count import words


class TestWordCounts(unittest.TestCase):

    """
        Counts the occurrences or characters in a word
    """
    # @unittest.skip("to work on")
    def test_word_occurance1(self):
        self.assertDictEqual(
            {'word': 1},
            words('word'),
            msg='should count one word'
        )

    # @unittest.skip("to work on")
    def test_word_occurance2(self):
        self.assertDictEqual(
            {'one': 1, 'of': 1, 'each': 1},
            words("one of each"),
            msg='should count one of each'
        )

    # @unittest.skip("to work on")
    def test_word_occurance3(self):
        self.assertDictEqual(
            {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1},
            words("one fish two fish red fish blue fish"),
            msg='should count multiple occurrences'
        )

    # @unittest.skip("to work on")
    def test_word_occurance4(self):
        self.assertDictEqual(
            {'car': 1,
                ":": 2,
                'carpet': 1,
                'as': 1,
                'java': 1,
                'javascript!!&@$%^&': 1
             },
            words('car : carpet as java : javascript!!&@$%^&'),
            msg='should include punctuation'
        )

    # @unittest.skip("to work on")
    def test_word_occurance5(self):
        self.assertDictEqual(
            {'testing': 2, 1: 1, 2: 1},
            words('testing 1 2 testing'),
            msg='should include numbers'
        )

    # @unittest.skip("to work on")
    def test_word_occurance6(self):
        self.assertDictEqual(
            {'go': 1, 'Go': 1, 'GO': 1},
            words('go Go GO'),
            msg='should respect case'
        )

    # @unittest.skip("to work on")
    def test_word_occurance7(self):
        self.assertDictEqual(
            {"¡Hola!": 1, "¿Qué": 1, "tal?": 1, "Привет!": 1},
            words('¡Hola! ¿Qué tal? Привет!'),
            msg='should count international characters properly'
        )

    # @unittest.skip("to work on")
    def test_word_occurance8(self):
        self.assertDictEqual(
            {'hello': 1, 'world': 1},
            words('hello\nworld'),
            msg='should not count multilines'
        )
    # @unittest.skip("to work on")
    def test_word_occurance9(self):
        self.assertDictEqual(
            {'hello': 1, 'world': 1},
            words('hello\tworld'),
            msg='should not count tabs'
        )

    # @unittest.skip("to work on")
    def test_word_occurance0(self):
        self.assertDictEqual(
            {'hello': 1, 'world': 1},
            words('hello  world'),
            msg='should count multiple spaces as one'
        )


if __name__ == '__main__':
    unittest.main()