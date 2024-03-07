import matplotlib.pyplot as plt

#LINE GRAPH
x = [1,2,3,4,5]
y = [2,3,5,7,11]
plt.plot(x,y)
plt.xlabel("USN")
plt.ylabel("MARKS")
plt.title("Simple Line Graph")
plt.show()

#BAR CHART
x = ["ANURAG", "AKSHAY", "ARKA"]
y = [80, 90, 100]
plt.bar(x,y)
plt.xlabel("NAME")
plt.ylabel("MARKS")
plt.title("Simple Bar Chart")
plt.show()

#SCATTER PLOT
x = [1,2,3]
y = [80, 90, 100]
plt.scatter(x,y)
plt.xlabel("YEAR")
plt.ylabel("SALES")
plt.title("Simple Scatter Plot")
plt.show()

#PIE CHART
size = [30, 20, 15, 35]
labels = ['A', 'B', 'C', 'D']
plt.pie(size,labels=labels)
plt.title("Simple Pie Chart")
plt.show()

#HISTOGRAM
x = [1,2,3,4,5]
y = [2,3,5,7,11]
plt.hist(x,y)
plt.title("Simple Histogram")
plt.show()
