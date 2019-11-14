import os, signal, sys, time
with open('python.pid', 'w') as pidfile:
    pidfile.write(str(os.getpid()))

def clean(*args):
    os.unlink('python.pid')
    sys.exit()
signal.signal(signal.SIGINT, clean)
sys.atexit=clean
while True:
    time.sleep(0.0005)
