import tensorflow as tf
import ptvsd

ptvsd.enable_attach('my_special_secret', address=('192.168.86.156', 3000))
ptvsd.wait_for_attach()

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0)
node3 = node1 * node2

sess = tf.Session()
print(sess.run([node3]))