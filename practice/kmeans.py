import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import tensorflow.compat.v1 as tf

# Generate random points
num_points = 2000
vectors_set = []

for i in range(num_points):
    if np.random.random() > 0.5:
        vectors_set.append([np.random.normal(0.0,0.9),
                            np.random.normal(0.0,0.9)])

    else:
        vectors_set.append([np.random.normal(3.0,0.5),
                            np.random.normal(1.0,0.5)])

# Draw Graph
df = pd.DataFrame({"x": [v[0] for v in vectors_set],
                    "y": [v[1] for v in vectors_set]})
sns.lmplot("x","y", data=df, fit_reg=False, height=6)
#plt.show()

vectors = tf.constant(vectors_set)
k = 4
centroids = tf.Variable(tf.slice(tf.random_shuffle(vectors),[0,0],[k,-1]))

expanded_vectors = tf.expand_dims(vectors, 0)
expanded_centroids = tf.expand_dims(centroids, 1)

assignments = tf.argmin(tf.reduce_sum(tf.square(tf.subtract(expanded_vectors,
        expanded_centroids)),2 ), 0)

means = tf.concat(0, [tf.reduce_mean(tf.gather(vectors,
        tf.reshape(tf.where(tf.equal(assignments,c)), [1,-1])),
        reduction_indices=[1]) for c in range(k)])

update_centroids = tf.assign(centroids, means)

init_op = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init_op)

for step in range(100):
    _, centroid_values, assignment_values = sess.run([update_centroids,
        centroids, assignment])
