import unittest
from tempfile import TemporaryFile
from test import *
from context import mp4box
from mp4box.box_parser import BoxParser

class TestBoxParser(unittest.TestCase):
    # def test_ftyp(self):
    #     b = 0
    #     with  TemporaryFile() as f:
    #         f.write(b"\x00\x00\x00\x18\x66\x74\x79\x70\x69\x73\x6f\x36\x00\x00\x00\x01\x69\x73\x6f\x36\x64\x61\x73\x68")
    #         f.seek(0)
    #         bp = BoxParser(f)
    #         bp.parse()
    #         boxes = bp.get_boxes()
    #         self.assertEqual(len(boxes.keys()), 1)

    # def test_second_box_size(self):
    #     b = 0
    #     with  TemporaryFile() as f:
    #         f.write(b"\x00\x00\x00\x18\x66\x74\x79\x70\x69\x73\x6f\x6d\x00\x00\x00\x01\x69\x73\x6f\x6d\x61\x76\x63\x31")
    #         f.seek(0)
    #         bp = BoxParser(f)
    #         bp.parse()
    #         boxes = bp.get_boxes()
    #         self.assertIsNot(boxes['ftyp'], None) 

    def test_file_writing(self):
        with TemporaryFile() as f:
            f.write((48).to_bytes(4, 'big'))
            f.seek(0)
            self.assertEqual(f.read(4), b'\x00\x00\x00\x30')

if __name__ == "__main__":
    unittest.main()

