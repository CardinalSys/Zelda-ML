from subprocess import Popen, PIPE

p = Popen(['D:\\projects\\ZeldaML\\ZeldaHook\\x64\\Debug\\ZeldaHook.exe'], shell=True, stdout=PIPE, stdin=PIPE)
while True:
    #value = bytes(value, 'UTF-8')  # Needed in Python 3.
    result = p.stdout.readline().strip()
    print(result)
    p.stdin.write(b"8\n")
    p.stdin.flush()
