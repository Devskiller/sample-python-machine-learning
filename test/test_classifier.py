import unittest

import numpy as np

from app.classifier import Classifier


class TestClassifier(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_cases = [
            (([0, 1], [0, 1]), [-1, 2], [-1, 0]),
            (
                ([-1, 0], [-1, 0]),
                [-5, 0],
                [5, 0],
            ),
            (
                ([-1, 0], [-5, 0]),
                [-6, 0],
                [-4, 0],
            ),
            (
                ([1, -1], [1, -1]),
                [2, -2],
                [0, 0],
            ),
            (
                ([1, 1, 1], [5, 5, 5]),
                [10, 10, 10],
                [0, 0, 0],
            ),
        ]

    def test_classifier_outputs_correct_labels(self):
        for (normal, translation), above, below in self.test_cases:
            with self.subTest(
                normal=normal, translation=translation, above=above, below=below
            ):
                classifier = Classifier(np.array(normal), np.array(translation))
                self.assertTrue(classifier.classify(np.array(above)))
                self.assertFalse(classifier.classify(np.array(below)))
