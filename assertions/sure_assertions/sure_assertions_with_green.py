# TODO sure assertions
import sure
# import unittest2 as unittest
import unittest as unittest
from sure import expect
from sure.core import Anything, DeepComparison
from sure import AssertionBuilder, AssertionHelper, IdentityAssertion


class TestSimpleAssertions(unittest.TestCase):
    def test_simple_assertions(self):
        (4).should.be.equal(2 + 2)
        (7.5).should.eql(3.5 + 4)

        (3).shouldnt.be.equal(5)

        {'foo': 'bar'}.should.equal({'foo': 'bar'})
        {'foo': 'bar'}.should.have.key('foo').which.should.equal('bar')

        "Awesome ASSERTIONS".lower().split().should.equal(['awesome', 'assertions'])

        # failing
        "Awesome ASSERTIONS".lower().split().shouldnt.equal(['awesome', 'assertions'])
        assert 1==1

    def test_some_more_awesome_assertions(self):
        """
        using sure.expect function
        :return:
        """
        expect(("asd").shouldnt.equal("asd"))
        expect(("asd").should.equal("asd"))

    def test_some_new_assertions(self):
        pass
