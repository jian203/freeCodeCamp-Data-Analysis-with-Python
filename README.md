# freeCodeCamp-Data-Analysis-with-Python
A collection of data analysis projects developed using Python (Pandas, Numpy, Matplotlib, and Seaborn) as part of the freeCodeCamp Data Analysis with Python Certification. This repository showcases my ability to manipulate, visualize, and extract insights from various datasets.

# 📊 freeCodeCamp: Data Analysis with Python

Welcome to my data analysis portfolio! This repository tracks my hands-on progress through the **freeCodeCamp Data Analysis with Python Certification**. 

Bridging the structured, analytical mindset of an engineering background with the dynamic world of data science, I created this space to document my journey. Here, you'll find a collection of projects that showcase my ability to wrangle messy data, build clear visualizations, and extract actionable insights using Python.

### 🛠️ Tech Stack & Tools
Throughout these projects, I heavily utilize:
* **Python** (Core logic and scripting)
* **Numpy** (Numerical computing and matrix operations)
* **Pandas** (Data manipulation and cleaning)
* **Matplotlib & Seaborn** (Data visualization)

---

## 📈 Certification Progress
- [x] Project 1: Mean-Variance-Standard Deviation Calculator
- [x] Project 2: Demographic Data Analyzer
- [ ] Project 3: Medical Data Visualizer (In Progress)
- [ ] Project 4: Page View Time Series Visualizer
- [ ] Project 5: Sea Level Predictor

---

## 📂 Project Details

### 1. Mean-Variance-Standard Deviation Calculator
**Folder:** `[Mean-Variance-Standard-Deviation-Calculator](./Mean-Variance-Standard-Deviation-Calculator)`

#### Description:
The goal was to create a function named `calculate()` that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a $3 \times 3$ matrix.

#### Key Skills & Learning Outcomes:
* **Array Manipulation:** Converting a 1D list into a 2D $3 \times 3$ Numpy array using `.reshape()`.
* **Axis-Based Operations:** Mastering the difference between `axis=0` (columns), `axis=1` (rows), and flattened calculations.
* **Data Structure Mapping:** Returning results in a nested dictionary format for structured data access.
* **Robust Programming:** Implementing `try-except` blocks to handle input errors (e.g., raising a `ValueError` if the list contains fewer than 9 elements).

#### Insights:
* Understanding the **axis** concept is fundamental for all future data manipulation in Pandas.
* Learned that Numpy is significantly more efficient for statistical calculations compared to standard Python loops.
* Gained experience in writing code that must pass pre-defined unit tests (`test_module.py`).

---

### 2. Demographic Data Analyzer
**Folder:** `[Demographic-Data-Analyzer](./Demographic-Data-Analyzer)`

#### Description:
Analyzed demographic data extracted from the 1994 Census database using Pandas to answer specific questions regarding race, age, education, work hours, and salary.

#### Key Skills & Learning Outcomes:
* **Data Filtering & Boolean Indexing:** Extracting specific subsets of data using conditions (e.g., `df[df['sex'] == 'Male']`) and combining multiple criteria using logical operators (`&`, `~`).
* **Data Aggregation:** Using `.value_counts()` to count unique categorical values and automatically generate Pandas Series with index labels.
* **Series Operations:** Dividing two Pandas Series to calculate demographic ratios and percentages.
* **Statistical Methods:** Applying `.mean()`, `.min()`, `.max()`, and `.idxmax()` to extract numerical insights and identify peak categories.

#### Insights:
* Discovered the power of **Index Alignment** in Pandas. When dividing two Series, Pandas automatically aligns the data based on matching index labels (e.g., country names), eliminating the need for complex manual loops.
* Mastered the concept of zero-based indexing for DataFrame dimensions; recognizing that `.shape[0]` acts as a reliable "row counter" to find the exact number of individuals meeting specific criteria.
* Realized the importance of floating-point precision (`round(..., 1)`) when formatting analytical outputs to pass strict automated testing environments.

---
*Status: Gaining momentum with data wrangling. Next step: Entering the world of data visualization with the Medical Data Visualizer.*
