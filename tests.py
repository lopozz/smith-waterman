import unittest
from smith_waterman import zeros, water


class TestSmithWaterman(unittest.TestCase):
    def test_zeros(self):
        """Test zeros() function to ensure it creates correct matrices"""
        self.assertEqual(zeros((2, 3)), [[0, 0, 0], [0, 0, 0]])
        self.assertEqual(zeros((3, 2)), [[0, 0], [0, 0], [0, 0]])

    def test_water_basic(self):
        """Test basic sequence alignment cases"""
        seq1 = "ACACACTA"
        seq2 = "AGCACACA"
        align1, align2 = water(seq1, seq2)

        expected_align1 = ["A", "-", "C", "A", "C", "A", "C", "T", "A"]
        expected_align2 = ["A", "G", "C", "A", "C", "A", "C", "-", "A"]

        self.assertEqual(align1, expected_align1)
        self.assertEqual(align2, expected_align2)

    def test_water_gap_insertion(self):
        """Test sequences where gaps are expected in the alignment"""
        seq1 = "GATTACA"
        seq2 = "GCATGCU"
        align1, align2 = water(seq1, seq2)

        # Expected results may vary based on scoring, but it should align correctly
        expected_align1 = ["G", "-", "A", "T", "T", "A", "C", "A"]
        expected_align2 = ["G", "C", "A", "-", "T", "G", "C", "U"]

        self.assertEqual(align1, expected_align1)
        self.assertEqual(align2, expected_align2)

    def test_water_no_alignment(self):
        """Test sequences with no significant alignment"""
        seq1 = "AAAA"
        seq2 = "TTTT"
        align1, align2 = water(seq1, seq2)

        # Since no characters match, alignment should be empty
        self.assertEqual(align1, ["A", "A", "A", "A"])
        self.assertEqual(align2, ["T", "T", "T", "T"])

    def test_water_perfect_alignment(self):
        """Test sequences with no significant alignment"""
        seq1 = "AAAA"
        seq2 = "AAAA"
        align1, align2 = water(seq1, seq2)

        # Since no characters match, alignment should be empty
        self.assertEqual(align1, ["A", "A", "A", "A"])
        self.assertEqual(align2, ["A", "A", "A", "A"])


if __name__ == "__main__":
    unittest.main()
