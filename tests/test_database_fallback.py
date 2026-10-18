import unittest

from core.adaat import conjugate


class DatabaseFallbackTestCase(unittest.TestCase):
    def test_unknown_verb_is_conjugated_and_marked_not_in_database(self):
        result = conjugate("قثب", {
            "all": True,
            "future_type": "كسرة",
            "transitive": True,
        })

        self.assertIn("يَقْثِبُ", str(result["table"]))
        self.assertIn("غير موجود في قاعدة البيانات", result["verb_info"])

    def test_explicit_suggestion_class_is_not_overridden_by_database(self):
        for verb, expected_future in (
            ("هابَ", "يَهَابُ"),
            ("طَوَى", "يَطْوَى"),
        ):
            with self.subTest(verb=verb):
                result = conjugate(verb, {
                    "all": True,
                    "future_type": "فتحة",
                    "transitive": True,
                    "force_future_type": True,
                })

                self.assertIn(expected_future, str(result["table"]))
                self.assertIn("[موجود في قاعدة البيانات]", result["verb_info"])


if __name__ == "__main__":
    unittest.main()
