import sys
from typing import List

from PIL import Image, ImageDraw, ImageFont

from .barcode import Barcode


class BarcodeGenerator:
    sequence: List[int]

    def __init__(self, sequence: str) -> None:
        self.sequence = Barcode(sequence).areas
        self._generate_barcode()

    def _generate_barcode(self) -> None:
        print(len(self.sequence))
        with Image.open("ean13/base.png").convert("RGBA") as base:
            (width, height) = base.size

            max_width = int(width / (95 + 7 + 11))
            print("max_width", max_width)

            draw = ImageDraw.Draw(base)

            width = 3
            start_x = 7 * width
            start_y = 50

            for digit in self.sequence:
                if digit == 1:
                    color = (255, 255, 255, 0)
                else:
                    color = (255, 255, 255, 255)

                draw.line(
                    (start_x, start_y, start_x, start_y + height - 100),
                    fill=color,
                    width=max_width,
                    joint=None,
                )
                start_x += max_width

            base.show()
            # base.save("code.png")
