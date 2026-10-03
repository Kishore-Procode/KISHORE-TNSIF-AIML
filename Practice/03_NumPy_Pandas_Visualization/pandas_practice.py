# pandas practice

import pandas as pd

# creating a dataframe
student_data = {
    "name": ["Kishore", "Arun", "Bala", "Charan", "Divya",
             "Esha", "Fathima", "Gokul"],
    "department": ["CSE", "ECE", "CSE", "IT",
                    "EEE", "CSE", "IT", "ECE"],
    "marks": [88, 72, 91, 68, 77, 95, 54, 81],
    "attendance": [92, 75, 88, 82, 78, 95, 70, 85],
    "cgpa": [8.8, 7.2, 9.1, 6.8, 7.7, 9.5, 5.4, 8.1]
}

df = pd.DataFrame(student_data)
print(df)
print("\nshape:", df.shape)
print("columns:", list(df.columns))
print("data types:\n", df.dtypes)


# basic stuff
print("\nfirst 3 rows:")
print(df.head(3))

print("\nlast 3 rows:")
print(df.tail(3))

print("\nstatistical summary:")
print(df.describe())


# selecting and filtering
print("\nnames:")
print(df["name"])

print("\nname and marks:")
print(df[["name", "marks"]])

# students with marks > 80
print("\nstudents with marks > 80:")
print(df[df["marks"] > 80])

# cse students only
print("\ncse students:")
print(df[df["department"] == "CSE"])

# cse students with marks > 80
print("\ncse students with marks > 80:")
print(df[(df["department"] == "CSE") & (df["marks"] > 80)])

# low attendance
print("\nstudents with low attendance (< 80):")
print(df[df["attendance"] < 80][["name", "department", "attendance"]])


# sorting
print("\nsorted by marks (ascending):")
print(df.sort_values("marks"))

print("\nsorted by marks (descending):")
print(df.sort_values("marks", ascending=False))

print("\nsorted by department, then marks:")
print(df.sort_values(["department", "marks"], ascending=[True, False]))


# adding new columns
df["grade"] = df["marks"].apply(
    lambda x: "A+" if x >= 90 else
              "A" if x >= 80 else
              "B" if x >= 70 else
              "C" if x >= 60 else "F"
)

df["result"] = df["marks"].apply(lambda x: "pass" if x >= 50 else "fail")
print("\nwith new columns:")
print(df)


# groupby
print("\naverage marks by department:")
print(df.groupby("department")["marks"].mean())

print("\ncount of students per department:")
print(df.groupby("department")["name"].count())

print("\nmultiple aggregations:")
print(df.groupby("department").agg({
    "marks": ["mean", "max", "min"],
    "attendance": "mean",
    "cgpa": "mean"
}))


# product sales analysis
products = pd.DataFrame({
    "product": ["Laptop", "Phone", "Tablet", "Keyboard",
                "Mouse", "Monitor", "Headphones", "Webcam"],
    "category": ["Electronics", "Electronics", "Electronics",
                 "Accessories", "Accessories", "Electronics",
                 "Accessories", "Accessories"],
    "price": [60000, 30000, 20000, 1500, 800, 25000, 3000, 2500],
    "quantity": [20, 60, 40, 70, 100, 30, 80, 50]
})

products["revenue"] = products["price"] * products["quantity"]
print("\nproducts:")
print(products)

print("\ntotal revenue:", products["revenue"].sum())

print("\nrevenue by category:")
print(products.groupby("category")["revenue"].sum())

print("\ntop 3 products by revenue:")
print(products.nlargest(3, "revenue")[["product", "revenue"]])
