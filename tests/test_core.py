import unittest
from insurance_package.core import InsurancePolicy

class TestInsurancePolicy(unittest.TestCase):

    def setUp(self):
        self.policy = InsurancePolicy(policy_holder="John Doe", coverage_amount=100000)

    def test_calculate_premium(self):
        premium = self.policy.calculate_premium()
        self.assertIsInstance(premium, float)
        self.assertGreater(premium, 0)

    def test_validate_policy(self):
        valid = self.policy.validate_policy()
        self.assertTrue(valid)

if __name__ == '__main__':
    unittest.main()