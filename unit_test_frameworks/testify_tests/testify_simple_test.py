# TODO testify tests
import testify

class AdditionTestCase(testify.TestCase):

    @testify.class_setup
    def init_the_variable(self):
        self.variable = 0

    @testify.setup
    def increment_the_variable(self):
        self.variable += 1

    def test_the_variable(self):
        testify.assert_equal(self.variable,
                             1)

    @testify.suite('disabled', reason='ticket #123, not equal to 2 places')
    def test_broken(self):
        # raises 'AssertionError: 1 !~= 1.01'
        testify.assert_almost_equal(1, 1.01, digits=2)

    def test_passing_almost_equal(self):
        testify.assert_almost_equal(1, 1.001, digits=2)

    @testify.teardown
    def decrement_the_variable(self):
        self.variable -= 1

    @testify.class_teardown
    def get_rid_of_the_variable(self):
        self.variable = None


if __name__ == "__main__":
    testify.run()
