from ean13.barcode_generator import BarcodeGenerator
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("barcode", type=str, help="the sequence to generate barcode")
args = parser.parse_args()
sequence = args.barcode

barcode = BarcodeGenerator(sequence=sequence)
print(f"checksum: {barcode.barcode.checksum}, sequence: {barcode.barcode.code}")
