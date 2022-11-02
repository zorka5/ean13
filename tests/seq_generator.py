import unittest

from ean13.barcode import Barcode


class TestBarcode(unittest.TestCase):
    def test_sequence(self):
        b = Barcode("8711253001202")
        self.assertEqual(
            b.markers,
            [
                [1, 0, 1],
                [0, 1, 1, 1, 0, 1, 1],
                [0, 1, 1, 0, 0, 1, 1],
                [0, 0, 1, 1, 0, 0, 1],
                [0, 0, 1, 1, 0, 1, 1],
                [0, 1, 1, 1, 0, 0, 1],
                [0, 1, 1, 1, 1, 0, 1],
                [0, 1, 0, 1, 0],
                [1, 1, 1, 0, 0, 1, 0],
                [1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0],
                [1, 1, 0, 1, 1, 0, 0],
                [1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 1, 1, 0, 0],
                [1, 0, 1],
            ],
        )
