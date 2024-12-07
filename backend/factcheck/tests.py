from django.test import TestCase
from django.utils import timezone
from .models import Fact

class FactModelTest(TestCase):
    def setUp(self):
        self.fact = Fact.objects.create(
            text="This is a test fact.",
            status="pending",
            source_url="https://example.com"
        )

    def test_fact_creation(self):
        self.assertTrue(isinstance(self.fact, Fact))
        self.assertEqual(self.fact.__str__(), "This is a test fact.")

    def test_fact_fields(self):
        self.assertEqual(self.fact.text, "This is a test fact.")
        self.assertEqual(self.fact.status, "pending")
        self.assertEqual(self.fact.source_url, "https://example.com")
        self.assertTrue(isinstance(self.fact.created_at, timezone.datetime))

    def test_fact_status_choices(self):
        valid_statuses = ['verified', 'pending', 'false']
        for status in valid_statuses:
            fact = Fact.objects.create(text=f"Fact with {status} status", status=status)
            self.assertEqual(fact.status, status)

    def test_fact_str_method(self):
        long_text = "This is a very long fact text that should be truncated in the string representation."
        fact = Fact.objects.create(text=long_text, status="verified")
        self.assertEqual(fact.__str__(), "This is a very long ")
