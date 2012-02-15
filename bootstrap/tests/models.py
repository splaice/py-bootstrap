import unittest
from bootstrap.models import World


class TestWorld(unittest.TestCase):

    def test_default_world(self):
        world = World()
        print world.get_state()
