import unittest
from bootstrap.models import World


class WorldTestCase(unittest.TestCase):
    def setUp(self):
        self.world = World()

    def tearDown(self):
        self.world = None


    def test_default_state(self):
        self.assertEqual(self.world.get_state(), None,
                'incorrect default state')


suite = unittest.TestLoader().loadTestsFromTestCase(WorldTestCase)
