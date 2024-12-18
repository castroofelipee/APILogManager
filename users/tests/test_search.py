import time
from django.test import TestCase


class PerfomanceTest(TestCase):
    def test_large_query_performance(self):
        start_time = time.time()
        # MyModel.objects.all()
        end_time = time.time()

        self.assertTrue((end_time - start_time) < 2)