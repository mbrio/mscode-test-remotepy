"""Test code for remote debugging."""
import time
import ptvsd


ptvsd.enable_attach('my_secret', address=('localhost', 40000))
# ptvsd.wait_for_attach()


def _transform(t):
    return t / 2


t = time.time()
d = _transform(t)

print(d)
