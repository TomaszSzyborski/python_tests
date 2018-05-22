# TODO sure assertions
import sure
from sure import expect
from sure.core import Anything, DeepComparison
from sure import AssertionBuilder, AssertionHelper, IdentityAssertion

def test_simple_assertions():
    (4).should.be.equal(2 + 2)
    (7.5).should.eql(3.5 + 4)

    (3).shouldnt.be.equal(5)
    expect({"2":"3"}).have.key("2").which.should.equal("4")
    {'foo': 'bar'}.should.equal({'foo': 'bar'})
    {'foo': 'bar'}.should.have.key('foo').which.should.equal('bar')

    "Awesome ASSERTIONS".lower().split().should.equal(['awesome', 'assertions'])

    # failing
    "Awesome ASSERTIONS".lower().split().shouldnt.equal(['awesome', 'assertions'])


def test_some_more_awesome_assertions():
    """
    using sure.expect function
    :return:
    """
    expect(("asd").shouldnt.equal("asd"))
    expect(("asd").should.equal("asd"))


def test_some_new_assertions():
    pass


if __name__ == '__main__':
    test_simple_assertions()
    test_some_more_awesome_assertions()
    test_some_new_assertions()
