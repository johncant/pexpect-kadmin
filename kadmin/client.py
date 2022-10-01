from select import select
from .utils.mit import MITUtils


class Client:

    def __init__(self, popen, timeout=1):
        self.popen = popen
        self.timeout = timeout
        self.utils = MITUtils()

    @classmethod
    def from_popen(cls, popen):
        kadmin = cls(popen)
        kadmin.recv_output()
        return kadmin

    def listprincs(self):
        output = self.command("listprincs")
        return output

    def send_input(self, command):
        bcommand = command.encode('utf8')
        self.popen.stdin.write(
            bcommand.strip()+b"\n")
        self.popen.stdin.flush()

    def recv_output(self):
        self.popen.stdout.flush()
        output = []
        while(True):
            readable_streams = select(
                [self.popen.stdout], [], [], self.timeout
            )[0]

            if not readable_streams:
                break
                raise ValueError('kadmin read timeout')

            stdout, = readable_streams

            raw_line = stdout.read1()
            line = raw_line.decode('utf-8').strip()
            print(output)
            output.append(line)

        r = "".join(output).splitlines()
        print(r)
        return r

 #       return stdout.readline()

    def command(self, command):
        self.send_input(command)
        output = self.recv_output()
        return self.utils.remove_prompt(output)
