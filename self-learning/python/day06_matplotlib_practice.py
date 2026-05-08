# self learning - matplotlib & basic visualization
# just trying to make plots that look decent
# referenced a few youtube videos and the docs

import matplotlib.pyplot as plt
import numpy as np

# ── line chart ────────────────────────────────

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
sales  = [1200,1450,1800,1600,2100,2400,2200,2600,2350,2800,3100,3500]

plt.figure(figsize=(10, 4))
plt.plot(months, sales, marker="o", color="#4C72B0", linewidth=2, markersize=6)
plt.title("Monthly Sales 2024", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.grid(axis="y", alpha=0.4)
plt.tight_layout()
plt.savefig("line_sales.png", dpi=150)
plt.show()
print("Saved line_sales.png")

# ── bar chart ─────────────────────────────────

categories = ["Electronics", "Clothing", "Food", "Books", "Sports"]
revenue    = [45000, 32000, 18000, 8500, 22000]
colors     = ["#4C72B0","#55A868","#C44E52","#8172B2","#CCB974"]

plt.figure(figsize=(8, 5))
bars = plt.bar(categories, revenue, color=colors, edgecolor="white", width=0.6)

# adding value labels on bars
for bar, val in zip(bars, revenue):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500,
             f"₹{val:,}", ha="center", fontsize=9)

plt.title("Revenue by Category", fontsize=14, fontweight="bold")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig("bar_revenue.png", dpi=150)
plt.show()

# ── histogram ─────────────────────────────────

np.random.seed(10)
exam_scores = np.random.normal(65, 15, 200)   # mean=65, std=15

plt.figure(figsize=(7, 4))
plt.hist(exam_scores, bins=20, color="#4C72B0", edgecolor="white", alpha=0.8)
plt.axvline(exam_scores.mean(), color="red", linestyle="--", label=f"Mean: {exam_scores.mean():.1f}")
plt.title("Distribution of Exam Scores", fontsize=13, fontweight="bold")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig("histogram_scores.png", dpi=150)
plt.show()

# ── scatter plot ──────────────────────────────

x = np.random.rand(80) * 100   # study hours (scaled)
y = 40 + 0.5*x + np.random.randn(80)*8   # marks

plt.figure(figsize=(6, 5))
plt.scatter(x, y, alpha=0.6, color="#C44E52", edgecolors="white", s=60)
plt.title("Study Hours vs Exam Marks", fontsize=13, fontweight="bold")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
# adding a trend line
m, b = np.polyfit(x, y, 1)
plt.plot(sorted(x), [m*xi + b for xi in sorted(x)], color="black", linestyle="--", linewidth=1.5)
plt.tight_layout()
plt.savefig("scatter_study.png", dpi=150)
plt.show()

# NOTE: next thing to try - subplots (plt.subplots) to show multiple charts together
