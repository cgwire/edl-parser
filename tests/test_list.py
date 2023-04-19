# -*- coding: utf-8 -*-

import unittest
import edl


class ListTestCase(unittest.TestCase):
    """tests the edl.edl.List class"""

    def setup(self):
        """set up the tests"""
        pass

    def testing_to_edl_method_will_output_the_standard_edl_case1(self):
        """testing if to_string will output the EDL as string"""
        p = edl.Parser("24")
        with open("tests/test_data/test_24.edl") as f:
            s = p.parse(f)

        with open("tests/test_data/test_24.edl") as f:
            expected_edl = f.readlines()

        self.maxDiff = None

        with open("tests/test_data/test_24.edl", "w+") as f:
            f.write(s.to_string())

        self.assertEqual(
            "".join(
                [line for line in expected_edl if not line.startswith("AUD")]
            ),
            s.to_string(),
        )

    def testing_to_edl_method_will_output_the_standard_edl_case2(self):
        """testing if to_string will output the EDL as string"""
        p = edl.Parser("25")
        with open("tests/test_data/test.edl") as f:
            s = p.parse(f)

        with open("tests/test_data/test.edl") as f:
            expected_edl = f.readlines()

        with open("tests/test_data/test.edl", "w+") as f:
            f.write(s.to_string())

        self.assertEqual(
            "".join(
                [line for line in expected_edl if not line.startswith("AUD")]
            ),
            s.to_string(),
        )

    def testing_to_edl_method_will_output_the_standard_edl_case3(self):
        """testing if to_string will output the EDL as string"""
        p = edl.Parser("50")
        with open("tests/test_data/test_50.edl") as f:
            s = p.parse(f)

        with open("tests/test_data/test_50.edl") as f:
            expected_edl = f.readlines()

        with open("tests/test_data/test_50.edl", "w+") as f:
            f.write(s.to_string())

        self.assertEqual(
            "".join(
                [line for line in expected_edl if not line.startswith("AUD")]
            ),
            s.to_string(),
        )
