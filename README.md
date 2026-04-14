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
- [x] Project 3: Medical Data Visualizer
- [ ] Project 4: Page View Time Series Visualizer (In Progress)
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

#### Insights:
* Understanding the **axis** concept is fundamental for all future data manipulation in Pandas.
* Learned that Numpy is significantly more efficient for statistical calculations compared to standard Python loops.

---

### 2. Demographic Data Analyzer
**Folder:** `[Demographic-Data-Analyzer](./Demographic-Data-Analyzer)`

#### Description:
Analyzed demographic data extracted from the 1994 Census database using Pandas to answer specific questions regarding race, age, education, work hours, and salary.

#### Key Skills & Learning Outcomes:
* **Data Filtering & Boolean Indexing:** Extracting specific subsets of data using conditions and combining multiple criteria.
* **Data Aggregation:** Using `.value_counts()` to count unique categorical values.
* **Series Operations:** Dividing two Pandas Series to calculate demographic ratios and percentages.

#### Insights:
* Discovered the power of **Index Alignment** in Pandas. When dividing two Series, Pandas automatically aligns the data based on matching index labels.
* Mastered the concept of zero-based indexing for DataFrame dimensions; recognizing that `.shape[0]` acts as a reliable "row counter".

---

### 3. Medical Data Visualizer
**Folder:** `[Medical-Data-Visualizer](./Medical-Data-Visualizer)`

#### Description:
Visualized and explored a medical examination dataset to identify relationships between cardiac disease, body measurements, and lifestyle choices using categorical plots and heatmaps.

#### Key Skills & Learning Outcomes:
* **Feature Engineering:** Creating an 'overweight' column by calculating BMI ($kg/m^2$) using vectorized operations.
* **Data Normalization:** Standardizing categorical health markers (cholesterol and glucose) into binary values (0 for good, 1 for bad).
* **Data Reshaping (Tidy Data):** Using `pd.melt()` to transform the DataFrame into a long format suitable for Seaborn's multi-panel plotting.
* **Advanced Visualizations:** Implementing `sns.catplot()` for categorical comparisons and `sns.heatmap()` for correlation matrices.
* **Advanced Data Cleaning:** Filtering out physiological outliers based on height/weight percentiles and blood pressure logic.

#### Insights:
* Learned how to use `np.triu()` to create a mask for the upper triangle of a correlation matrix, making the heatmap much cleaner and easier to interpret.
* Recognized that `pd.melt()` is essential for visual comparisons; it allows us to "stack" different variables like smoking, alcohol, and activity into a single chart against cardiovascular health.
* Understood that in medical datasets, data cleaning is not just about missing values, but also about filtering "impossible" data (like diastolic pressure being higher than systolic).

---
*Status: Moving from static statistics to time-series analysis. Next step: Visualizing website traffic patterns in the Page View Time Series Visualizer.*
