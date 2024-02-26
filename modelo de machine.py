import tensorflow as tf
x = tf.constant(1)
for n in range(x,10,1):
    print(f"{n} x {n} = {n * n}")