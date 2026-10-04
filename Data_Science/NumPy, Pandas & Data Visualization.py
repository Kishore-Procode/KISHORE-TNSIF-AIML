import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# NUMPY - PROBLEM 1: STUDENT MARKS ANALYSIS
# ============================================================

marks = np.array([85, 72, 91, 68, 77, 95, 54, 81, 73, 88])

print("\n========== NUMPY - PROBLEM 1 ==========")
print("Marks:", marks)

print("Total marks:", marks.sum())
print("Average marks:", marks.mean())
print("Highest marks:", marks.max())
print("Lowest marks:", marks.min())

print("Marks greater than 75:", marks[marks > 75])


# ============================================================
# NUMPY - PROBLEM 2: TEMPERATURE ANALYSIS
# ============================================================

temperatures = np.array([28, 31, 29, 33, 35, 27, 32])
days = np.array(["Monday", "Tuesday", "Wednesday",
                 "Thursday", "Friday", "Saturday", "Sunday"])

print("\n========== NUMPY - PROBLEM 2 ==========")
print("Temperatures:", temperatures)

print("Average temperature:", temperatures.mean())
print("Highest temperature:", temperatures.max())
print("Lowest temperature:", temperatures.min())

print("Days with temperature above 30°C:")
print(days[temperatures > 30])

updated_temperatures = temperatures + 2
print("Temperatures after increasing by 2°C:")
print(updated_temperatures)


# ============================================================
# PANDAS - PROBLEM 3: STUDENT PERFORMANCE
# ============================================================

student_data = {
    "Name": ["Arun", "Bala", "Charan", "Divya",
             "Esha", "Fathima", "Gokul", "Hari"],

    "Department": ["CSE", "ECE", "CSE", "IT",
                   "EEE", "CSE", "IT", "ECE"],

    "Marks": [85, 72, 91, 68, 77, 95, 54, 81],

    "Attendance": [90, 75, 88, 82, 78, 95, 70, 85]
}

students = pd.DataFrame(student_data)

print("\n========== PANDAS - PROBLEM 3 ==========")

print("\nComplete DataFrame:")
print(students)

print("\nFirst 5 students:")
print(students.head())

print("\nAverage marks:")
print(students["Marks"].mean())

print("\nStudents who scored more than 75:")
print(students[students["Marks"] > 75])

print("\nStudents whose attendance is below 80%:")
print(students[students["Attendance"] < 80])

print("\nStudents sorted by marks:")
print(students.sort_values("Marks"))


# ============================================================
# PANDAS - PROBLEM 4: PRODUCT SALES ANALYSIS
# ============================================================

product_data = {
    "Product Name": ["Laptop", "Phone", "Tablet", "Keyboard", "Mouse"],
    "Category": ["Electronics", "Electronics", "Electronics",
                 "Accessories", "Accessories"],
    "Price": [60000, 30000, 20000, 1500, 800],
    "Quantity Sold": [20, 60, 40, 70, 100]
}

products = pd.DataFrame(product_data)

# Calculate total sales for each product
products["Total Sales"] = products["Price"] * products["Quantity Sold"]

print("\n========== PANDAS - PROBLEM 4 ==========")

print("\nProduct DataFrame:")
print(products)

print("\nTotal sales amount for each product:")
print(products[["Product Name", "Total Sales"]])

highest_sales_product = products.loc[
    products["Total Sales"].idxmax()
]

print("\nProduct with highest sales:")
print(highest_sales_product)

print("\nAverage product price:")
print(products["Price"].mean())

print("\nProducts where quantity sold is greater than 50:")
print(products[products["Quantity Sold"] > 50])

print("\nProducts sorted based on total sales:")
print(products.sort_values("Total Sales"))


# ============================================================
# DATA VISUALIZATION - PROBLEM 5
# MONTHLY SALES VISUALIZATION
# ============================================================

months = ["January", "February", "March",
          "April", "May", "June"]

sales = [50000, 60000, 55000, 70000, 75000, 80000]

print("\n========== DATA VISUALIZATION - PROBLEM 5 ==========")

# Line chart
plt.figure()
plt.plot(months, sales, marker="o", label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

# Bar chart
plt.figure()
plt.bar(months, sales, label="Sales")
plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

student_names = ["A", "B", "C", "D", "E",
                 "F", "G", "H", "I", "J"]

student_marks = np.array([85, 72, 91, 68, 77,
                          95, 35, 81, 55, 30])

print("\n========== DATA VISUALIZATION - PROBLEM 6 ==========")

plt.figure()
plt.bar(student_names, student_marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

excellent = np.sum((student_marks >= 80) & (student_marks <= 100))
good = np.sum((student_marks >= 60) & (student_marks <= 79))
average = np.sum((student_marks >= 40) & (student_marks <= 59))
needs_improvement = np.sum(student_marks < 40)

categories = [
    "Excellent",
    "Good",
    "Average",
    "Needs Improvement"
]

category_counts = [
    excellent,
    good,
    average,
    needs_improvement
]

plt.figure()
plt.pie(
    category_counts,
    labels=categories,
    autopct="%1.1f%%"
)

plt.title("Student Performance Distribution")
plt.show()