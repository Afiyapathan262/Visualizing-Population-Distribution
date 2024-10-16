Task 1: Data Visualization - Histogram of Age Distribution

Overview

This task, part of my Data Science internship at Prodigy InfoTech, involved visualizing the distribution of the 'Age' column from a dataset using a histogram. It focused on practicing data cleaning and exploratory data analysis techniques while applying visual representation to communicate insights effectively.

Objective

The main objective of this task was to:

Load, inspect, and clean the dataset to ensure it was prepared for analysis.
Identify and handle missing values and duplicated records.
Visualize the distribution of the numerical 'Age' column using a histogram to gain insights into the data's distribution, helping to identify trends and patterns.

Key Features of the Code

Data Loading:The dataset is loaded from a CSV file using Pandas with low_memory=False to suppress data type warnings.
Histogram for Age Distribution:A histogram is plotted for the 'Age' column, a continuous variable, using plt.hist(). It shows how frequently different ages occur in the dataset, with bins set to 10 for a clear distribution.
Bar Chart for Gender Distribution:A bar chart is plotted for the 'Gender' column, a categorical variable, using sns.countplot() from Seaborn, which helps visualize the count of each gender category.
Plot Customization:Titles, axis labels, colors, and layouts are customized for clear visualization using Matplotlib

Learning Outcomes
Understanding how to inspect and clean data (checking for missing and duplicate values). Visualizing a numerical column using a histogram to observe its distribution. Using Python libraries like Pandas, seaborn, and Matplotlib for data analysis and visualization. Learning to handle in-memory plotting and figure display using io for seamless image handling.


Tools & Technologies :

Python (Version 3.x): Main programming language for data handling and visualization.

Pandas: Used for loading and handling the dataset.

Matplotlib: Used for creating and customizing plots (histogram and figure layout).

Seaborn: Enhances data visualization (bar charts) with aesthetically pleasing themes.

NumPy: Although not explicitly used in this code, it's often important for numerical operations related to data analysis.


Sample Output

The histogram generated from the 'Age' column provides a clear view of its frequency distribution, helping identify patterns and trends in the data.
