import pexpect

class Runner:
    def __init__(self) -> None:
        pass

    def run_command(self, cmd_list, modulename):
        print(cmd_list)
        print(modulename)

        modulename = "--" + modulename

        child = pexpect.spawn("python3 ../SecureTea.py " + modulename)
        for i in range(len(cmd_list)):
            child.expect("(.*)")
            child.sendline(cmd_list[i])
        child.expect(pexpect.EOF)

        output = child.before.decode('utf-8')
        print (output)

        return output

