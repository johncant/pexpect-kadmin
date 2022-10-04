from select import select
import pexpect


def kadmin_escape_arg(val):
    # TODO - implement security check
    return val


class Client:

    def __init__(self, pexpect, timeout=1):
        self.pexpect = pexpect
        self.timeout = timeout
        self.prompts = [
            "kadmin:  ",
            "kadmin.local:  ",
        ]

    @classmethod
    def from_pexpect(cls, pexpect):
        kadmin = cls(pexpect)
        kadmin.pexpect.expect(kadmin.prompts)
        return kadmin

    def listprincs(self, expr=None):
        expr = kadmin_escape_arg(expr)
        cmd = "listprincs"

        if expr:
            cmd = cmd + " " + expr

        output = self.command(cmd)
        return [
            line.decode('utf8')
            for line in output.splitlines()
        ]

    def command(self, cmd):
        self.pexpect.sendline(cmd)
        self.pexpect.expect([cmd+r"\r\n\x1b\[\?2004l\r"])
        self.pexpect.expect([r'\x1b\[\?2004h'])
#        self.pexpect.expect(self.prompts)
        output = self.pexpect.before
        return output

