import testify
from bootstrap.models import World


class WorldTestCase(testify.TestCase):
    @testify.setup
    def create_world(self):
        self.world = World()

    @testify.teardown
    def clear_world(self):
        self.world = None

    def test_default_state(self):
        testify.assert_equal(self.world.get_state(), None,
                'incorrect default state')
