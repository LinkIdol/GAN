import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])

# 至此，我们得到了两个重要的Tensor：y和y_。
# y是模型的输出，y_是实际的图像标签，不要忘了y_是独热表示的
# 下面我们就会根据y和y_构造损失

# 根据y, y_构造交叉熵损失
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y)))

# 有了损失，我们就可以用随机梯度下降针对模型的参数（W和b）进行优化
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# 创建一个Session。只有在Session中才能运行优化步骤train_step。
sess = tf.InteractiveSession()
# 运行之前必须要初始化所有变量，分配内存。
tf.global_variables_initializer().run()
print('start training...')

# 进行1000步梯度下降
for _ in range(1000):
    print (_)
    # 在mnist.train中取100个训练数据
    # batch_xs是形状为(100, 784)的图像数据，batch_ys是形如(100, 10)的实际标签
    # batch_xs, batch_ys对应着两个占位符x和y_
    batch_xs, batch_ys = tf.keras.datasets.mnist.train.next_batch(100)
    # 在Session中运行train_step，运行时要传入占位符的值
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# 正确的预测结果
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# 计算预测准确率，它们都是Tensor
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# 在Session中运行Tensor可以得到Tensor的值
# 这里是获取最终模型的正确率
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))  # 0.9185