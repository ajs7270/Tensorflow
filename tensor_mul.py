import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

a = tf.placeholder("float")
b = tf.placeholder("float")

y = tf.math.multiply(a,b)

sess = tf.Session()

print(sess.run(y, feed_dict={a:4,b:4}))
