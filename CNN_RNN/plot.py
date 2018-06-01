import matplotlib.pyplot as plt

train_scores=[8.94,80.30, 84.59, 86.78, 90.00, 90.78,91.26]
test_scores=[2.1, 0.64, 0.5, 0.41,0.34,0.32,0.29]
fig = plt.figure()

ax = fig.add_subplot(1, 2, 1)
ax.plot(range(7 * 1), train_scores, label="accuracy ", marker='+')
ax.set_title(" accuracy ")
ax.set_xlabel(r"Epoch")
ax.set_ylabel("score")
ax.set_ylim(0, 100)
ax.legend(loc="best", framealpha=0.5)
ax = fig.add_subplot(1, 2, 2)
ax.plot(range(7 * 1), test_scores, label=" loss ", marker='o')
ax.set_title(" loss ")
ax.set_xlabel(r"Epoch")
# ax.set_ylabel("score")
ax.set_ylim(0, 1.05)
ax.legend(loc="best", framealpha=0.5)

plt.show()
