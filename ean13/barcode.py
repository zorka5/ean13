import itertools
from typing import List

from .encoding import G_code, L_code, R_code, encoding_dict


class Barcode:

    # https://en.wikipedia.org/wiki/International_Article_Number

    # Barcode consists of 95 areas (modules)
    start_marker: List[int]
    first_digit_markers: List[List[int]] = [[0] * 7] * 6
    center_marker: List[int]
    last_digit_markers: List[List[int]] = [[0] * 7] * 6
    end_marker: List[int]

    _markers: List[List[int]] = []
    _checksum: int
    _code: str

    def __init__(self, code: str) -> None:
        if len(code) != 12:
            raise AttributeError("Len is not 12")
        checksum = str(self._generate_checksum(code))
        self._checksum = checksum
        self._code = code + checksum

        # 3 areas for the start marker (101)
        self.start_marker = [1, 0, 1]
        self._markers.append(self.start_marker)

        enc = encoding_dict[code[0]]

        # 42 areas (seven per digit) to encode digits 2–7
        for i in range(1, 7):
            current_digit = self.code[i]
            current_code = enc["first_group"][i - 1]
            if current_code == "L":
                self.first_digit_markers[i - 1] = [
                    int(i) for i in [*L_code[current_digit]]
                ]
            elif current_code == "G":
                self.first_digit_markers[i - 1] = [
                    int(i) for i in [*G_code[current_digit]]
                ]
            self._markers.append(self.first_digit_markers[i - 1])

        # 5 areas for the center marker (01010)
        self.center_marker = [0, 1, 0, 1, 0]
        self._markers.append(self.center_marker)

        # 42 areas (seven per digit) to encode digits 8–13
        for i in range(7, 13):
            current_digit = self.code[i]
            current_code = enc["last_group"][i - 7]
            self.last_digit_markers[i - 7] = [int(i) for i in [*R_code[current_digit]]]
            self._markers.append(self.last_digit_markers[i - 7])

        # 3 areas for the end marker (101)
        self.end_marker = [1, 0, 1]
        self._markers.append(self.end_marker)

    @property
    def code(self) -> str:
        return self._code

    @property
    def markers(self) -> List[List[int]]:
        return self._markers

    @property
    def areas(self) -> List[int]:
        return list(itertools.chain.from_iterable(self._markers))

    @property
    def checksum(self) -> int:
        return self._checksum

    def _generate_checksum(self, code: str) -> int:
        odd = [int(i) for i in code[-1::-2]]
        sum_odd = sum(odd)
        even = [int(i) for i in code[-2::-2]]
        sum_even = sum(even)
        # ( 10 - [ (3 * Odd + Even) modulo 10 ] ) modulo 10
        return (10 - (3 * sum_odd + sum_even) % 10) % 10
