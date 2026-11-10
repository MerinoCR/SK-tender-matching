import unittest
from owner_rules import assess

class RulesTests(unittest.TestCase):
    def a(self, topic, **facts):
        return assess(topic, dict(sku_id="SYNTHETIC-1", **facts))
    def test_static_default(self):
        self.assertEqual(self.a("load", static_kg=250, dynamic_kg=135, required_kg=250)["status"], "supported")
    def test_explicit_dynamic(self):
        self.assertEqual(self.a("load", specified_basis="dynamic", static_kg=250, dynamic_kg=135, required_kg=250)["status"], "standard_deviation")
    def test_missing_static(self):
        self.assertEqual(self.a("load", required_kg=250)["status"], "pending_verification")
    def test_equivalences(self):
        for topic, flag in [("vascular_position", "trendelenburg"), ("corner_bumpers", "bumpers"), ("lower_storage", "bottom_plastic_cover"), ("cassette_travel", "full_body_xray")]:
            with self.subTest(topic=topic):
                self.assertEqual(self.a(topic, **{flag: True})["status"], "accepted_owner_rule")
                self.assertEqual(self.a(topic)["status"], "pending_verification")
    def test_sections(self):
        self.assertEqual(self.a("rigid_four_sections", back_adjustment=True, knee_adjustment=True)["status"], "accepted_owner_rule")
        self.assertEqual(self.a("rigid_four_sections", back_adjustment=True)["status"], "pending_verification")
    def test_iv(self):
        self.assertEqual(self.a("iv_pole", pole=True, mounts=True)["status"], "accepted_owner_rule")
    def test_dispositions(self):
        expected = {"backrest_reach": "customization_to_request", "antistatic_wheels": "customization_to_specify", "rail_details": "non_strict", "fifth_wheel_diameter": "pending_verification", "mattress": "separate_customizable_product"}
        for topic, status in expected.items():
            with self.subTest(topic=topic):
                result = self.a(topic)
                self.assertEqual(result["status"], status)
                self.assertFalse(result["engineering_confirmed"])
                self.assertFalse(result["full_offer_approved"])
    def test_range_supported(self):
        self.assertEqual(self.a("backrest_reach", required_range_demonstrated=True)["status"], "supported")
    def test_contradiction_and_conflict(self):
        result = self.a("corner_bumpers", bumpers=True, explicit_contradiction=True, source_conflict=True)
        self.assertEqual(result["status"], "conflict_review_required")
        self.assertTrue(result["source_conflict"])
    def test_no_mutation(self):
        facts = dict(sku_id="SYNTHETIC-1", full_body_xray=True)
        original = facts.copy()
        assess("cassette_travel", facts)
        self.assertEqual(facts, original)
    def test_invalid_inputs(self):
        for facts in ({}, {"sku_id": ""}, {"sku_id": 12}):
            with self.assertRaises(ValueError): assess("mattress", facts)
        for value in (True, -1, float("nan"), "250"):
            with self.assertRaises(ValueError): self.a("load", static_kg=value, required_kg=250)
        with self.assertRaises(ValueError): self.a("unknown")
    def test_no_truthy_strings(self):
        self.assertEqual(self.a("corner_bumpers", bumpers="yes")["status"], "pending_verification")

if __name__ == "__main__":
    unittest.main()
