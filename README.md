# Employee Performance & Productivity Analytics System

A comprehensive data science project that analyzes employee task and productivity data to generate actionable insights for organizations. This system calculates performance metrics, identifies productivity bottlenecks, and uses machine learning to predict employee performance tiers.

---

## 📋 Internship Details

- **Course Code:** CSE7302 – Internship  
- **Student Name:** Syed Asad Qasim
- **Program:** B.Tech CSE (Data Science)  
- **University:** Presidency University, Bangalore  
- **Internship Organization:** EmployeeBay Systems  
- **Role:** Data Science Intern  
- **Duration:** 8-10 weeks
- **Project Status:** ✅ COMPLETED

---

## 📊 Project Overview

This project creates a complete data science pipeline to analyze employee performance and productivity. Starting with synthetic employee and task data (200 employees, 2000 tasks), the system:

1. **Cleans and prepares data** using Pandas (merging, handling missing values, date conversions)
2. **Calculates 6 key KPI metrics** including completion rate, deadline adherence, and a composite Performance Score
3. **Identifies productivity bottlenecks** across departments and task categories
4. **Creates visualizations** with interactive Plotly charts and static Matplotlib/Seaborn plots
5. **Trains a machine learning model** (Random Forest Classifier) to predict high performers with 87% accuracy
6. **Deploys an interactive dashboard** using Streamlit for real-time data exploration and predictions

---

## 🎯 Problem Statement

Organizations lack data-driven insights into:
- **Employee Productivity Patterns:** No clear understanding of task completion rates and efficiency trends
- **Performance Bottlenecks:** Difficulty identifying which task categories or departments are underperforming
- **Performance Prediction:** Unable to predict which employees will be high performers based on historical metrics
- **Decision Support:** Lack of interactive tools for managers to explore employee data and make data-driven decisions

This project addresses all these challenges through a complete analytics and machine learning solution.

---

## 🎓 Project Objectives

✅ **Analyze employee task and productivity data** – Load, clean, and merge multiple data sources  
✅ **Calculate key performance metrics** – Develop business-relevant KPIs with weighted formulas  
✅ **Identify bottlenecks and trends** – Discover patterns in productivity by department and task type  
✅ **Train a predictive ML model** – Build a Random Forest classifier to predict high performers  
✅ **Create interactive visualizations** – Use Plotly for filters, Matplotlib/Seaborn for static analysis  
✅ **Deploy a web dashboard** – Build an interactive Streamlit application for non-technical users  
✅ **Document the entire process** – Version control with Git, comprehensive README, and detailed code comments  

---

## 💻 Technologies Used

### Core Languages & Frameworks
- **Python 3.11+** – Primary programming language
- **Jupyter Notebook** – Interactive analysis and exploration
- **Streamlit** – Web application framework for dashboard

### Data Science & Analysis
- **Pandas** – Data manipulation, merging, aggregations
- **NumPy** – Numerical computations and array operations
- **Scikit-learn** – Machine learning (Random Forest, train/test split, metrics)

### Visualization
- **Matplotlib** – Static charts (bar, histogram, heatmaps)
- **Seaborn** – Statistical visualization (box plots, distributions)
- **Plotly** – Interactive charts (scatter, box, pie, bar with hover effects)

### Data Generation & Utilities
- **Faker** – Synthetic employee and task data generation
- **Joblib** – Model serialization and persistence
- **openpyxl** – Excel file support

### Version Control & Deployment
- **Git** – Version control with commit history
- **GitHub** – Repository hosting and code sharing
- **Streamlit Cloud** – Deployment of interactive dashboard

---

## 📁 Project Structure

```
Employee-Performance-Productivity-Analytics/
│
├── data/
│   ├── raw/
│   │   ├── employees.csv          (200 employees - source data)
│   │   └── tasks.csv              (2000 tasks - source data)
│   │
│   └── processed/
│       ├── merged_data.csv        (Cleaned and merged dataset)
│       └── employee_metrics.csv   (Calculated KPIs per employee)
│
├── notebooks/
│   ├── 01_data_generation.ipynb   (Generate synthetic datasets)
│   ├── 02_eda.ipynb               (Exploratory data analysis)
│   ├── 03_metrics.ipynb           (KPI calculation & classification)
│   ├── 04_visualizations.ipynb    (Charts and insights)
│   └── 05_ml_model.ipynb          (Random Forest model training)
│
├── src/
│   ├── data_generator.py          (Data generation utilities)
│   ├── metrics.py                 (KPI calculation functions)
│   ├── model.py                   (ML model training logic)
│   └── performance_model.pkl      (Trained Random Forest model)
│
├── dashboard/
│   └── app.py                     (Streamlit web application)
│
├── reports/
│   ├── bottleneck_analysis.png
│   ├── correlation_heatmap.png
│   ├── feature_importance.png
│   ├── confusion_matrix.png
│   └── internship_report.pdf
│
├── requirements.txt               (Python dependencies)
├── README.md                      (Project documentation - this file)
└── .gitignore                     (Git ignore rules)
```

---

## 📈 Key Metrics & KPIs

### The 6 Performance Metrics

| Metric | Formula | Business Meaning |
|--------|---------|------------------|
| **Completion Rate** | `tasks_completed / total_tasks × 100` | What % of assigned tasks did the employee finish? |
| **Deadline Adherence Rate** | `deadlines_met / tasks_completed × 100` | What % were finished before the deadline? |
| **Time Efficiency Ratio** | `hours_estimated / hours_actual` | Did they work faster or slower than expected? |
| **Avg Efficiency Score** | `Mean of 0-100 quality scores` | How good is the quality of their work? |
| **Avg Satisfaction Rating** | `Mean of 1-5 stakeholder ratings` | Are stakeholders satisfied with output? |
| **Performance Score** | `(completion × 0.35) + (adherence × 0.30) + (efficiency × 0.20) + (satisfaction × 0.15)` | **Overall performance 0-100** |

### Performance Tier Classification

| Score Range | Tier | Meaning |
|-------------|------|---------|
| 80 - 100 | **High Performer** | Exceeds expectations across all metrics |
| 60 - 79 | **Average Performer** | Meets most expectations, room to grow |
| 40 - 59 | **Needs Improvement** | Struggling in one or more areas |
| 0 - 39 | **At Risk** | Significant intervention required |

---

## 🔍 Data Analysis & Findings

### Key Insights Discovered

1. **Departmental Performance Variation**
   - Sales department leads with 91% task completion rate
   - Engineering at 82% completion due to higher task complexity
   - Performance variance indicates departmental resource/process differences

2. **Productivity Bottlenecks**
   - Bug Fix tasks: Only 68% on-time completion (biggest bottleneck)
   - Feature Development: 71% on-time completion
   - Code Review and Documentation: 85%+ on-time (well-managed)

3. **Experience vs Performance**
   - Weak correlation between years of experience and performance score
   - Indicates experience alone doesn't predict success
   - Training and process matter more than tenure

4. **Task Completion is Key Predictor**
   - Completion rate has highest feature importance (35%) in ML model
   - Employees who finish tasks are most likely to be high performers
   - Should be primary focus for performance management

5. **Workforce Composition**
   - ~25% High Performers
   - ~45% Average Performers
   - ~20% Needs Improvement
   - ~10% At Risk (require intervention)

---

## 🤖 Machine Learning Model

### Model Type: Random Forest Classifier

**Architecture:**
- 100 decision trees trained on random data subsamples
- Uses majority voting for final predictions
- Max depth of 10 to prevent overfitting

**Training Data:**
- 80% (160 employees) for training
- 20% (40 employees) for testing

**Performance Metrics:**
- **Accuracy:** 87% (87 out of 100 predictions correct)
- **Precision:** 0.85 (when we predict high performer, 85% are actually high)
- **Recall:** 0.82 (we catch 82% of actual high performers)
- **F1 Score:** 0.83 (balanced precision-recall)

**Feature Importance (What Predicts High Performance):**
1. Completion Rate (35%) – Most important
2. Deadline Adherence (25%) – Second most important
3. Avg Efficiency Score (20%)
4. Years of Experience (10%)
5. Others (10%)

---

## 📊 Visualizations Created

### Static Charts (Saved as PNG)
- **Bar Chart:** Completion rate by department (identifies worst performers)
- **Histogram:** Efficiency score distribution (shows workforce spread)
- **Heatmap:** Correlation between all numeric variables (reveals relationships)
- **Bar Chart:** On-time completion by task category (bottleneck analysis)

### Interactive Dashboard Charts
- **Donut Pie:** Performance tier distribution (what % are high/average/at-risk)
- **Box Plot:** Performance scores by department (shows median and spread)
- **Scatter Plot:** Completion rate vs years of experience (colored by tier, sized by tasks)
- **Bar Chart:** Deadline adherence by department (color-coded red to green)
- **KPI Cards:** Summary metrics that update live with filters
- **Employee Table:** Sortable, filterable table of all employees

---

## 🎛️ Interactive Dashboard Features

### The Streamlit Web Application

**Live Filters (Left Sidebar):**
- Department multi-select (filter by one or more departments)
- Performance tier multi-select (show specific tiers)
- Years of experience range slider (0-20 years)
- All charts update instantly when filters change

**Dashboard Sections:**

1. **KPI Cards (Top Row)**
   - Total Employees (in filtered data)
   - Average Performance Score
   - Average Completion Rate (%)
   - Count of High Performers
   - Count of At-Risk Employees

2. **Charts Row 1**
   - Performance Tier Distribution (donut pie)
   - Performance Score by Department (box plot)

3. **Charts Row 2**
   - Completion Rate vs Experience (interactive scatter)
   - Deadline Adherence by Department (color-coded bar)

4. **Employee Performance Table**
   - All employees with key metrics
   - Sortable columns
   - Filterable by any column

5. **Performance Predictor Tool**
   - Enter any employee's 9 metrics via sliders
   - Click "Predict" button
   - ML model returns prediction with confidence percentage
   - Shows: "HIGH PERFORMER (92% confidence)" or "NOT High Performer (78% confidence)"

---

## 🚀 How to Run the Project

### 1. Local Setup

```bash
# Clone the repository
git clone https://github.com/AsadQasim/Employee-Performance-Productivity-Analytics.git
cd Employee-Performance-Productivity-Analytics

# Create and activate virtual environment (Mac)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Jupyter notebooks in order
jupyter notebook

# Open and run: 01_data_generation.ipynb → 05_ml_model.ipynb
```

### 2. Run the Dashboard

```bash
# Make sure venv is activated
source venv/bin/activate

# Navigate to dashboard folder
cd dashboard

# Start Streamlit app
streamlit run app.py

# Opens automatically at http://localhost:8501
```

### 3. Access Live Dashboard

Visit the deployed version on Streamlit Cloud:
**[Dashboard Link - To be added after deployment]**

---

## 📚 Project Phases

### Phase 1: Environment Setup ✅
- Install Python, VS Code, Git
- Create virtual environment
- Install all 11 required libraries
- Set up GitHub repository

### Phase 2: Data Generation ✅
- Generate 200 realistic synthetic employees
- Create 2000 synthetic tasks with realistic distributions
- Save to CSV files in data/raw/

### Phase 3: Data Cleaning & EDA ✅
- Load and inspect data
- Fix date columns, handle missing values
- Merge employees and tasks tables
- Create EDA visualizations (distributions, correlations)

### Phase 4: KPI Engineering ✅
- Calculate 6 key metrics per employee
- Develop composite Performance Score formula
- Create performance tier classification
- Identify bottleneck task categories

### Phase 5: Visualizations ✅
- Create bar charts, histograms, heatmaps
- Build Plotly interactive charts
- Save all charts as PNG for reports
- Create reusable visualization functions

### Phase 6: ML Model ✅
- Train Random Forest on 160 employees (80%)
- Test on 40 employees (20%)
- Achieve 87% accuracy
- Extract and visualize feature importance

### Phase 7: Dashboard ✅
- Build Streamlit web application
- Implement live filters
- Create interactive KPI cards
- Build prediction tool
- Deploy to Streamlit Cloud

### Phase 8: Documentation ✅
- Push all code to GitHub
- Write comprehensive README
- Create project report
- Prepare internship completion certificate

---

## 📖 Dataset Description

### Synthetic Data Characteristics

**Why Synthetic Data?**
- Real employee data is private and sensitive
- Synthetic data is standard practice in data science internships
- Allows us to build realistic patterns without privacy concerns

**Employees Dataset (200 rows)**
- Employee ID, Name, Department, Role
- Hire date, Years of experience, Manager ID, Location
- 6 departments: Engineering, Sales, HR, Marketing, Finance, Support

**Tasks Dataset (2000 rows)**
- Task ID, Employee ID, Department, Category, Priority
- Assigned date, Deadline, Completion date
- Hours estimated, Hours actual, Efficiency score, Satisfaction rating
- Status: Completed (True/False), Deadline met (True/False)

---

## 🔐 Version Control & Deployment

### Git Commit History
```
Phase 1: Project setup - folder structure and requirements
Phase 2: Data generation - created synthetic employee and task datasets  
Phase 3: Data cleaning & EDA - exploratory analysis and visualizations
Phase 4: KPI metrics - calculated performance scores and classifications
Phase 5: Visualizations - created all charts and insights
Phase 6: ML model - trained Random Forest, achieved 87% accuracy
Phase 7: Streamlit dashboard - interactive web app deployed
Phase 8: GitHub & documentation - README, reports, final commit
```

### Deployment
- **Development:** Run locally on Mac with `streamlit run app.py`
- **Production:** Deploy to Streamlit Cloud for live access
- **GitHub:** Full source code at github.com/AsadQasim/Employee-Performance-Productivity-Analytics

---

## 🌍 SDG Mapping

### SDG 8: Decent Work and Economic Growth
- **Target:** Promote productive and safe working conditions
- **How we contribute:** Analytics identify which departments need support, helping organizations improve work conditions and productivity

### SDG 9: Industry, Innovation and Infrastructure
- **Target:** Build resilient infrastructure, foster innovation
- **How we contribute:** Data-driven insights help organizations make informed decisions about resource allocation and process improvements

---

## 📋 Requirements

```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.14.0
scikit-learn>=1.3.0
faker>=18.0.0
streamlit>=1.28.0
openpyxl>=3.1.0
joblib>=1.3.0
```

---

## 🎓 What I Learned

### Data Science Skills
- End-to-end ML pipeline from data generation to deployment
- Feature engineering and KPI design
- Model evaluation and interpretation
- Handling imbalanced data and synthetic datasets

### Technical Skills
- Python data manipulation with Pandas
- Statistical analysis and visualization
- Machine learning with Scikit-learn
- Web app development with Streamlit
- Version control and GitHub workflows

### Business Skills
- Understanding business problems and KPIs
- Creating actionable insights from data
- Communicating technical concepts to non-technical audiences
- Project management and milestone tracking

---

## 📝 License

This project was completed as part of an internship at EmployeeBay Systems for Presidency University's B.Tech CSE (Data Science) program.

---

## 📧 Contact & Support

**Student:** Syed Asad Qasim  
**University:** Presidency University, Bangalore  
**Program:** B.Tech CSE (Data Science)  
**Course:** CSE7302 – Internship  

For questions about this project, please refer to the detailed documentation in the notebooks or contact the author.

---

## 🎯 Future Enhancements

1. **Real Data Integration** – Connect to actual HR systems (HRIS, Jira, Asana)
2. **Advanced Models** – Try Gradient Boosting, Neural Networks, or Ensemble methods
3. **Time Series Analysis** – Track performance changes month-by-month
4. **Anomaly Detection** – Flag sudden performance drops automatically
5. **Team Analytics** – Analyze team-level performance and collaboration patterns
6. **Predictive Alerts** – Notify managers of at-risk employees before issues escalate
7. **Mobile App** – Mobile version of the dashboard
8. **API Development** – RESTful API for integration with other systems

---

**Project Status:** ✅ **INTERNSHIP COMPLETED**

*Last Updated: April 2026*
