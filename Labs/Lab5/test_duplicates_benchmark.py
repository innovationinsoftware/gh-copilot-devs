import timeit
import unittest

from duplicates import find_duplicates


class FindDuplicatesTests(unittest.TestCase):
    def test_finds_numeric_duplicates_in_first_occurrence_order(self):
        self.assertEqual(find_duplicates([2, 1, 2, 3, 1, 1]), [2, 1])

    def test_finds_string_duplicates(self):
        self.assertEqual(
            find_duplicates(["oak", "elm", "oak", "pine", "elm"]),
            ["oak", "elm"],
        )

    def test_accepts_an_iterator(self):
        self.assertEqual(find_duplicates(value for value in [4, 5, 4]), [4])

    def test_benchmark_reports_runtime_by_input_size(self):
        print("\nfind_duplicates benchmark (best of 5, milliseconds per call)")
        for size in (1_000, 10_000, 100_000):
            values = [index % (size // 2) for index in range(size)]
            expected = list(range(size // 2))
            self.assertEqual(find_duplicates(values), expected)

            number = max(1, 1_000_000 // size)
            samples = timeit.repeat(
                lambda: find_duplicates(values),
                repeat=5,
                number=number,
            )
            per_call_ms = min(samples) / number * 1_000
            print(f"{size:>7,} items: {per_call_ms:.3f} ms/call")


if __name__ == "__main__":
    unittest.main(verbosity=2)
