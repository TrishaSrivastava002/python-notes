from matplotlib import pyplot as plt
# Going to create a plot with ages of software developers on x-axis and their median salary on the y-axis
#PLOT 1
age_x=[25,26,27,28,29,30,31,32,33,34,35]
dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320]
plt.plot(age_x,dev_y,label='all devs')
#PLOT 2
age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(age_x,py_dev_y,label='some devs')
plt.xlabel('Developer Age')
plt.ylabel('Median Salary in USD')
plt.title('Median Salary (USD) by Developers Age')
plt.legend()
# plt.legend(['all devs','some devs'])
# 2 different plots but on the same graph which are not differentiable so we use legend func which can only be used if know the order 
# of the plots added which can be avoided if we pass lable func in the plot command as and then give the legend command without any inputs
plt.show()