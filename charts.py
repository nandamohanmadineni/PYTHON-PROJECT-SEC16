import matplotlib.pyplot as plt

# Bar Chart
def bar_chart(subjects, marks):
    plt.bar(subjects, marks)
    plt.title("Subject Scores")
    plt.show()

# Pie Chart
def pie_chart(labels, sizes):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Attendance")
    plt.show()

# Line Chart
def line_chart(x, y):
    plt.plot(x, y)
    plt.title("Performance Trend")
    plt.show()

# Histogram
def histogram(data):
    plt.hist(data)
    plt.title("Marks Distribution")
    plt.show()