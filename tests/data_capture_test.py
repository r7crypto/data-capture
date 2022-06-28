import unittest
from data_capture.data_capture import DataCapture


class TestDataCapture(unittest.TestCase):
    data_capture = DataCapture()
    data_capture.add(3)
    data_capture.add(9)
    data_capture.add(3)
    data_capture.add(4)
    data_capture.add(6)
    stats = data_capture.build_stats()

    def test_work_flow_less(self):
        self.assertEqual(self.stats.less(4), 2)

    def test_work_flow_greater(self):
        self.assertEqual(self.stats.greater(4), 2)

    def test_work_flow_between(self):
        self.assertEqual(self.stats.between(3, 6), 4)


if __name__ == '__main__':
    unittest.main()
