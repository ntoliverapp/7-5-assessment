import matplotlib.pyplot as plt 

plt.style.use('seaborn-notebook')

μs_x = [20, 50, 100, 5000, 1000000]

μsInsert_y = [47.316, 49.685, 168.513, 7555.614, 945321.118]

plt.plot(μs_x, μsInsert_y, marker='D',label='Insert')

μsAppend_y = [113.196, 105.269, 157.719, 701.384, 3957.207]

plt.plot(μs_x, μsAppend_y, marker='D',label='Append')

plt.xlabel('μs X')
plt.ylabel('μs Y')
plt.title('Array Time Complexity')

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig('runtime_chart.png')

plt.show()


