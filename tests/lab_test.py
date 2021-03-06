import unittest
import timeout_decorator

from PittAPI import lab
from . import PittServerError, DEFAULT_TIMEOUT


class LabTest(unittest.TestCase):
    @timeout_decorator.timeout(DEFAULT_TIMEOUT, timeout_exception=PittServerError)
    def test_get_status_alumni(self):
        self.assertIsInstance(lab.get_status("ALUMNI"), dict)

    @timeout_decorator.timeout(DEFAULT_TIMEOUT, timeout_exception=PittServerError)
    def test_get_status_benedum(self):
        self.assertIsInstance(lab.get_status("BENEDUM"), dict)

    @timeout_decorator.timeout(DEFAULT_TIMEOUT, timeout_exception=PittServerError)
    def test_get_status_cathg27(self):
        self.assertIsInstance(lab.get_status("CATH_G27"), dict)

    @timeout_decorator.timeout(DEFAULT_TIMEOUT, timeout_exception=PittServerError)
    def test_get_status_cathg62(self):
        self.assertIsInstance(lab.get_status("CATH_G62"), dict)

    @timeout_decorator.timeout(DEFAULT_TIMEOUT, timeout_exception=PittServerError)
    def test_get_status_lawrence(self):
        self.assertIsInstance(lab.get_status("LAWRENCE"), dict)

    @timeout_decorator.timeout(DEFAULT_TIMEOUT, timeout_exception=PittServerError)
    def test_get_status_hillman(self):
        self.assertIsInstance(lab.get_status("HILLMAN"), dict)

    @timeout_decorator.timeout(DEFAULT_TIMEOUT, timeout_exception=PittServerError)
    def test_get_status_sutherland(self):
        self.assertIsInstance(lab.get_status("SUTH"), dict)

    def test_fetch_labs(self):
        self.assertIsInstance(lab._fetch_labs(), list)

    def test_lab_name_validation(self):
        valid, fake = lab.LOCATIONS[0].lower(), 'test'
        self.assertTrue(lab._validate_lab(valid), lab.LOCATIONS[0])
        self.assertRaises(ValueError, lab._validate_lab, fake)

    def test_make_status(self):
        keys = ['status', 'windows', 'mac', 'linux']
        closed = lab._make_status('closed')
        open = lab._make_status('open', 1, 1, 1)

        self.assertIsInstance(closed, dict)
        self.assertIsInstance(open, dict)

        self.assertEqual(closed[keys[0]], 'closed')
        self.assertEqual(open[keys[0]], 'open')

        for key in keys[1:]:
            self.assertEqual(closed[key], 0)
            self.assertEqual(open[key], 1)

    def test_extract_machines(self):
        data = '123 hello_world, 456 macOS, 789 cool, 3 nice'
        info = lab._extract_machines(data)
        self.assertIsInstance(info, list)
        self.assertEqual(info, [123, 456, 789, 3])