# data visualization practice - matplotlib

import numpy as np
import matplotlib.pyplot as plt

# line chart - monthly sales
months = ["jan", "feb", "mar", "apr", "may", "jun",
          "jul", "aug", "sep", "oct", "nov", "dec"]
sales_2025 = [45, 52, 48, 61, 55, 67, 72, 68, 75, 80, 85, 92]
sales_2026 = [50, 58, 55, 65, 70, 75, 78, 82, 88, 90, 95, 100]

plt.figure(figsize=(10, 5))
plt.plot(months, sales_2025, marker="o", linewidth=2, label="2025", color="#3498db")
plt.plot(months, sales_2026, marker="s", linewidth=2, label="2026", color="#e74c3c")
plt.title("monthly sales trend (in thousands)")
plt.xlabel("month")
plt.ylabel("sales")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# bar chart - department wise student count
departments = ["CSE", "ECE", "IT", "EEE", "Mech"]
student_count = [120, 95, 80, 65, 70]
colors = ["#2ecc71", "#3498db", "#9b59b6", "#e74c3c", "#f39c12"]

plt.figure(figsize=(8, 5))
bars = plt.bar(departments, student_count, color=colors, edgecolor="black")

for bar, count in zip(bars, student_count):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
             str(count), ha="center", fontweight="bold")

plt.title("department wise student count")
plt.xlabel("department")
plt.ylabel("number of students")
plt.tight_layout()
plt.show()


# pie chart - grade distribution
grades = ["A+ (90-100)", "A (80-89)", "B (70-79)", "C (60-69)", "F (<60)"]
counts = [15, 25, 30, 20, 10]
colors = ["#2ecc71", "#3498db", "#f39c12", "#e67e22", "#e74c3c"]
explode = (0.05, 0.05, 0, 0, 0.1)

plt.figure(figsize=(8, 6))
plt.pie(counts, labels=grades, autopct="%1.1f%%", colors=colors,
        explode=explode, shadow=True, startangle=140)
plt.title("student grade distribution")
plt.tight_layout()
plt.show()


# scatter plot - marks vs attendance
np.random.seed(42)
marks = np.random.randint(40, 100, 30)
attendance = marks * 0.8 + np.random.randint(-10, 15, 30)
attendance = np.clip(attendance, 50, 100)

plt.figure(figsize=(8, 6))
plt.scatter(attendance, marks, c=marks, cmap="coolwarm", s=80, alpha=0.8, edgecolors="black")
plt.colorbar(label="marks")
plt.title("marks vs attendance")
plt.xlabel("attendance (%)")
plt.ylabel("marks")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# histogram - marks distribution
np.random.seed(42)
all_marks = np.random.normal(70, 15, 200)
all_marks = np.clip(all_marks, 0, 100)

plt.figure(figsize=(8, 5))
plt.hist(all_marks, bins=15, color="#3498db", edgecolor="black", alpha=0.7)
plt.axvline(all_marks.mean(), color="red", linestyle="--", label=f"mean: {all_marks.mean():.1f}")
plt.title("distribution of student marks")
plt.xlabel("marks")
plt.ylabel("frequency")
plt.legend()
plt.tight_layout()
plt.show()


# subplot - putting multiple charts together
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("student performance dashboard", fontsize=16, fontweight="bold")

axes[0, 0].plot(months[:6], sales_2026[:6], marker="o", color="#3498db")
axes[0, 0].set_title("sales trend (h1 2026)")
axes[0, 0].set_ylabel("sales")
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].bar(departments, student_count, color=colors)
axes[0, 1].set_title("dept wise students")
axes[0, 1].set_ylabel("count")

axes[1, 0].pie(counts, labels=grades, autopct="%1.0f%%", colors=colors)
axes[1, 0].set_title("grade distribution")

axes[1, 1].hist(all_marks, bins=12, color="#9b59b6", edgecolor="black", alpha=0.7)
axes[1, 1].set_title("marks distribution")
axes[1, 1].set_xlabel("marks")
axes[1, 1].set_ylabel("frequency")

plt.tight_layout()
plt.show()
