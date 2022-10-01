from pytest import fixture
from subprocess import Popen, PIPE
from kadmin.client import Client

@fixture
def process():
    return Popen(
        "kadmin.local",
        stdout=PIPE,
        stdin=PIPE
    )


def test_list_principals(process):
    princs = Client.from_popen(process).listprincs()

    assert 'foo' in princs
