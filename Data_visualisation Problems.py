import matplotlib.pyplot as plt

#HISTOGRAM
x = [18, 8, 19, 19, 20, 20, 20, 20, 20, 21, 22, 22, 23, 23, 25, 25, 30, 35, 45, 50]
plt.hist(x)
plt.xlabel("Age")
plt.title("AGE DISTRIBUTION IN A MUSICAL FESTIVAL")
plt.show()

# LINE GRAPH
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [100, 101, 104, 100, 99, 97, 100, 99, 96, 99, 97, 99, 100, 101, 103, 105, 104, 102, 100, 99, 96, 94, 93, 102, 105, 106, 110, 111, 113, 115]
plt.plot(x, y)
plt.xlabel("DAY")
plt.ylabel("PRICE (IN $)")
plt.title("STOCK PRICE VISUALISATION")
plt.show()

# BAR CHART
plt.title("CAR DEALERSHIP SALES PERFORMANCE")
x = ["GT3 RS", "G-CLASS", "MUSTANG", "LA FERRARI", "AVENTEDOR"]
y = [5, 3, 11, 2, 4]
plt.bar(x,y)
plt.xlabel("Car Model")
plt.ylabel("Monthly sale")
plt.show()

#SCATTER PLOT
plt.title("FUEL EFFICIENCY ON HIGHWAY")
x = [10, 20, 30, 40 ,50]
y = [7.4, 9, 10, 7.9, 5]
plt.scatter(x,y)
plt.xlabel("DISTANCE TRAVELLED (in kms)")
plt.ylabel("Fuel efficieny (km/l)")
plt.show()

#PIE CHART
plt.title("CLASS SURVEY ON FAVOURITE SUBJECT")
size = [25, 15, 18, 12, 5]
labels = ["MATHS", "PYTHON", "JAVA", "DBMS", "TOC"]
plt.pie(size, labels=labels)
plt.show()
