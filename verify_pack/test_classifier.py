import unittest

import numpy as np

from app.classifier import Classifier


class VerifyTestClassifier(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_cases = [
            (
                ([0, 0, 1], [0, 0, 1]),
                [0, 0, 2],
                [0, 0, 0],
            ),
            (
                ([0, 0, 0, 1], [0, 0, 0, 1]),
                [0, 0, 0, 2],
                [0, 0, 0, 0],
            ),
            (
                ([0, 0, 0, 0, 1], [0, 0, 0, 0, 1]),
                [0, 0, 0, 0, 2],
                [0, 0, 0, 0, 0],
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

    def test_classifier_outputs_correct_labels_for_point_on_hyperplane(self):
        normal, translation = [1, 1], [0, 0]
        classifier = Classifier(np.array(normal), np.array(translation))
        points = [[0, 0], [-1, 1], [1, -1]]
        for point in points:
            self.assertTrue(classifier.classify(np.array(point)))
