#!/usr/bin/env python
# coding: utf-8

# <h1 style="text-align:center; font-weight:bold;">
#  📊Real Estate Sales Dataset Visualization By Ali Ahmad🏢 
# 
# </h1>
# 

# In[22]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Excel file
file_path = r"C:\Users\Ali Ahmad\Documents\Al Kabir all data\power bi\Al kabir excel format true latest.xlsx"
df = pd.read_excel(file_path)

# Show first 5 rows
print(df.head())


# In[23]:


print(df.info)


# In[24]:


print(df.describe())



# In[51]:


total_sales = df["Sale"].sum()
sales_target = df["Sales Target"].sum()

Values = [total_sales, sales_target]
labels = ["Achieved Sales", "Sales Target"]

plt.bar(labels, Values, color=["Yellow", "green"])

for i, v in enumerate (values):
    plt.text(i, v +(v * 0.01), f"{int(v):,}", ha="center" , fontsize=10, fontweight="bold")


plt.title("Sales vs Sales Target")
plt.ylabel("Number of Sales and Sales Targets")

plt.show()


# In[59]:


# Manager-wise total sales
Manager_Sales = df.groupby("Manager")["Sale"].sum().reset_index()

# Plot bar chart
plt.bar(Manager_Sales["Manager"], Manager_Sales["Sale"], color="cyan", edgecolor="red")

# Add value labels on bars
for i, v in enumerate(Manager_Sales["Sale"]):
    plt.text(i, v + (v * 0.01), f"{int(v):,}", ha="center", fontsize=10, fontweight="bold")

# Chart formatting
plt.title("Sales by Manager")
plt.xlabel("Manager")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)  # rotate labels if too many managers

# Show chart
plt.show()


# In[60]:


# Group sales by Sales Person
sales_by_person = df.groupby("Sales Person")["Sale"].sum().sort_values(ascending=False)

# Plot bar chart
plt.figure(figsize=(10,6))
bars = sales_by_person.plot(kind="bar", color="skyblue", edgecolor="black")

# Add value labels on top of each bar
for i, v in enumerate(sales_by_person):
    plt.text(i, v + (v * 0.01), f"{int(v):,}", ha="center", fontsize=9, fontweight="bold")

# Formatting
plt.title("Total Sales by Sales Person", fontsize=16)
plt.xlabel("Sales Person", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()


# In[70]:


# Convert Book Value and Book Value Target to numeric (ignore errors, turn non-numeric into NaN)
df["Book Value"] = pd.to_numeric(df["Book Value"], errors="coerce")
df["Book Value Target"] = pd.to_numeric(df["Book Value Target"], errors="coerce")

# --- Calculate KPIs ---
total_sales = df["Sale"].sum()
sales_target = df["Sales Target"].sum()
revenue_achieved = df["Book Value"].sum()
revenue_target = df["Book Value Target"].sum()

# Achievement percentages
sales_achievement = (total_sales / sales_target * 100) if sales_target > 0 else 0
revenue_achievement = (revenue_achieved / revenue_target * 100) if revenue_target > 0 else 0

# --- Create KPI Dashboard ---
import matplotlib.pyplot as plt
import matplotlib

# ✅ Use emoji-supported font (Windows: Segoe UI Emoji, Mac: Apple Color Emoji, Linux: Noto Color Emoji)
matplotlib.rcParams['font.family'] = 'Segoe UI Emoji'  

plt.figure(figsize=(10,6))
plt.axis("off")  # hide axes

# Add KPI texts
plt.text(0.1, 0.8, f"📊 Total Sales: {total_sales:,.0f}", fontsize=14, fontweight="bold", color="green")
plt.text(0.1, 0.7, f"🎯 Sales Target: {sales_target:,.0f}", fontsize=14, fontweight="bold", color="orange")
plt.text(0.1, 0.6, f"💰 Revenue Achieved: {revenue_achieved:,.0f}", fontsize=14, fontweight="bold", color="blue")
plt.text(0.1, 0.5, f"🏆 Revenue Target: {revenue_target:,.0f}", fontsize=14, fontweight="bold", color="purple")
plt.text(0.1, 0.4, f"✅ Sales Achievement: {sales_achievement:.1f}%", fontsize=14, fontweight="bold", color="darkgreen")
plt.text(0.1, 0.3, f"✅ Revenue Achievement: {revenue_achievement:.1f}%", fontsize=14, fontweight="bold", color="darkblue")

plt.title("📊 KPI Dashboard", fontsize=18, fontweight="bold")
plt.show()


# In[76]:


# --- Ensure Date column is datetime ---
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# --- Filter only 2025 data ---
df_2025 = df[df["Date"].dt.year == 2025]

# --- Group by Month ---
monthly_sales = df_2025.groupby(df_2025["Date"].dt.to_period("M"))["Sale"].sum().reset_index()
monthly_sales["Date"] = monthly_sales["Date"].dt.to_timestamp()

# --- Calculate MoM Growth % ---
monthly_sales["Growth %"] = monthly_sales["Sale"].pct_change() * 100

# --- Plot ---
plt.figure(figsize=(8,5))

# Sales Trend
plt.plot(monthly_sales["Date"], monthly_sales["Sale"], marker="o", color="blue", label="Total Sales")

# Growth %
plt.bar(monthly_sales["Date"], monthly_sales["Growth %"], alpha=0.4, color="red", label="MoM Growth %")

# Labels on sales line
for i, v in enumerate(monthly_sales["Sale"]):
    plt.text(monthly_sales["Date"].iloc[i], v + (v*0.02), f"{v:,.0f}", ha="center", fontsize=9, color="blue")

plt.title("📈 Monthly Sales Growth - 2025", fontsize=16, fontweight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales & Growth %", fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.grid(linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()


# In[79]:


import matplotlib.pyplot as plt

# group and sort
project_sales = df.groupby("Project")["Sale"].sum().sort_values(ascending=False)

# plot
fig, ax = plt.subplots(figsize=(12,6))
bars = ax.bar(project_sales.index, project_sales.values, color="teal", edgecolor="black")

# add horizontal value labels above each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(
        f"{int(height):,}",                      # label text with thousands separator
        xy=(bar.get_x() + bar.get_width() / 2, height),  # point to annotate
        xytext=(0, 6),                           # offset label by 6 points above the bar
        textcoords="offset points",
        ha="center", va="bottom", fontsize=9, fontweight="bold", rotation=0
    )

# formatting
ax.set_title("Project-wise Sales Performance", fontsize=16, fontweight="bold")
ax.set_xlabel("Project")
ax.set_ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
ax.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

print("🏆 Top 5 Projects by Sales:")
print(project_sales.head(5))


# In[84]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Example dataframe
# df = pd.DataFrame({"Salesperson": ["Ali", "Ahmed", "Sara", "Usman"],
#                    "Sale": [120000, 95000, 180000, 110000]})

# 1. Find top performer
top_sales = df.groupby("Sales Person")["Sale"].sum().sort_values(ascending=False)
top_name = top_sales.index[0]
top_value = top_sales.iloc[0]

# 2. Create a gradient background (for 3D/pro look)
fig, ax = plt.subplots(figsize=(7,7))
x = np.linspace(0, 1, 100).reshape(-1,1)
ax.imshow(x, cmap="coolwarm", interpolation="bicubic", extent=[0,1,0,1], alpha=0.3)

# 3. Add 3D trophy-like emoji
ax.text(0.5, 0.8, "🏆", fontsize=100, ha="center", va="center")

# 4. Add cartoon-like decorations
ax.text(0.2, 0.7, "💰", fontsize=40, alpha=0.8)
ax.text(0.8, 0.7, "📈", fontsize=40, alpha=0.8)
ax.text(0.2, 0.4, "🎯", fontsize=40, alpha=0.8)
ax.text(0.8, 0.4, "🔥", fontsize=40, alpha=0.8)

# 5. Add main text
ax.text(0.5, 0.55, f"Top Performer", fontsize=20, fontweight="bold", color="darkred", ha="center")
ax.text(0.5, 0.45, f"{top_name}", fontsize=26, fontweight="bold", color="black", ha="center")
ax.text(0.5, 0.35, f"Sales: {int(top_value):,}", fontsize=18, color="blue", ha="center")

# 6. Add animation effect (simulate with sparkles ✨)
for pos in [(0.3,0.9),(0.7,0.9),(0.25,0.2),(0.75,0.2)]:
    ax.text(pos[0], pos[1], "✨", fontsize=20, ha="center", va="center", alpha=0.7)

# Formatting
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.axis("off")

plt.tight_layout()
plt.show()


# In[103]:


import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

# --- Setup figure ---
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis("off")

# Doraemon-like head
head = patches.Circle((0,0), 1.2, facecolor="skyblue", edgecolor="black", lw=2)
face = patches.Circle((0,0), 1.0, facecolor="white", edgecolor="black", lw=2)
ax.add_patch(head)
ax.add_patch(face)

# Eyes
eye_left = patches.Circle((-0.3,0.3), 0.2, facecolor="white", edgecolor="black")
eye_right = patches.Circle((0.3,0.3), 0.2, facecolor="white", edgecolor="black")
pupil_left = ax.plot(-0.3,0.3, "o", color="black")[0]
pupil_right = ax.plot(0.3,0.3, "o", color="black")[0]
ax.add_patch(eye_left)
ax.add_patch(eye_right)

# Nose
nose = patches.Circle((0,0.1), 0.1, facecolor="red", edgecolor="black")
ax.add_patch(nose)

# Mouth
mouth = patches.Arc((0,-0.2), 0.8, 0.5, theta1=200, theta2=-20, edgecolor="black", lw=2)
ax.add_patch(mouth)

# Hand (to wave)
hand = patches.Circle((1.5,0.2), 0.25, facecolor="white", edgecolor="black")
ax.add_patch(hand)

# Text with proper emoji font
msg = ax.text(0, -1.6, "See you in next project 👋", 
              ha="center", fontsize=14, fontweight="bold", fontname="Segoe UI Emoji")

# --- Animation function ---
def animate(frame):
    # Make the hand wave (move up and down)
    y = 0.2 + 0.1 * ((frame % 20) / 10 - 1)  # wave motion
    hand.set_center((1.5, y))
    return [hand, pupil_left, pupil_right]

# Run animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=100, blit=True)

plt.show()

