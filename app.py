"""Test code for remote debugging."""
import time
import ptvsd


ptvsd.enable_attach(None, address=('192.168.86.156', 3000))
# ptvsd.wait_for_attach()


def _transform(t):
    return t / 2


t = time.time()
d = _transform(t)

print(d)
