import pexpect

cmd_list = ['', '', '']

mod = "--malware_analysis"
child = pexpect.spawn("python3 SecureTea.py " + mod)
for i in range(len(cmd_list)):
    child.expect("(.*)")
    child.sendline(cmd_list[i])
child.expect(pexpect.EOF)
print (child.before.decode('utf-8'))
