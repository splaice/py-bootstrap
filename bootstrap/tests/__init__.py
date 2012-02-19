import unittest
import bootstrap.tests.models


def test_all():
    return unittest.TestSuite([bootstrap.tests.models.suite, ])

if __name__ == '__main__':
    test_all()
