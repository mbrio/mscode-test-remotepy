"""Test code for remote debugging."""
import time
import ptvsd


ptvsd.enable_attach(None, address=('localhost', 5678))
# ptvsd.wait_for_attach()


def _transform(t):
    return t / 2


t = time.time()
d = _transform(t)

print(d)
