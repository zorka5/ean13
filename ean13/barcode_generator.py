import argparse
from typing import List

from PIL import Image, ImageDraw, ImageFont

from .barcode import Barcode


class BarcodeGenerator:
    sequence: List[int]
    barcode_str: str

    def __init__(self, sequence: str) -> None:
        self.barcode = Barcode(sequence)
        self.sequence = self.barcode.areas
        self._generate_barcode(self, filename=sequence)

    @staticmethod
    def _generate_barcode(self, filename) -> None:
        with Image.open("ean13/base.png").convert("RGBA") as base:
            (width, height) = base.size

            max_line_width = int(width / (95 + 7 + 11))
            max_line_height = int(height) * 0.9
            image_new_width = (95 + 7 + 11) * max_line_width
            newsize = (image_new_width, height)
            base = base.resize(newsize)

            draw = ImageDraw.Draw(base)

            start_x = 7 * max_line_width
            start_y = int(height) * (1 - 0.9) / 2

            for digit in self.sequence:
                if digit == 1:
                    color = (255, 255, 255, 0)
                else:
                    color = (255, 255, 255, 255)

                draw.line(
                    (start_x, start_y, start_x, start_y + max_line_height),
                    fill=color,
                    width=max_line_width,
                    joint=None,
                )
                start_x += max_line_width

            base.show()
            base.save(f"./barcodes/{filename}.png")
