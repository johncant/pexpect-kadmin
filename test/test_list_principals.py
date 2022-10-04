from pytest import fixture
from pexpect import spawn
from kadmin.client import Client

@fixture
def process():
    return spawn(
        "kadmin.local",
        timeout=1
    )


def test_list_principals(process):
    princs = Client.from_pexpect(process).listprincs()

    expected = 'krbtgt/ATHENA.MIT.EDU@ATHENA.MIT.EDU'
    assert expected in princs
