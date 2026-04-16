import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import joblib
from sklearn.preprocessing import LabelEncoder
import os

# --- Page Config ---
st.set_page_config(
    page_title="EmployeeBay Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Load Data ---
@st.cache_data
def load_data():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    metrics = pd.read_csv(os.path.join(base, 'data', 'processed', 'employee_metrics.csv'))
    tasks = pd.read_csv(os.path.join(base, 'data', 'processed', 'merged_data.csv'))
    return metrics, tasks

metrics, tasks = load_data()

# --- Sidebar Filters ---
st.sidebar.title("🔍 Filters")
selected_dept = st.sidebar.multiselect(
    "Department", options=metrics['department'].unique(), 
    default=metrics['department'].unique()
)
selected_tier = st.sidebar.multiselect(
    "Performance Tier", options=metrics['performance_tier'].unique(),
    default=metrics['performance_tier'].unique()
)
min_exp, max_exp = st.sidebar.slider(
    "Years of Experience", 
    float(metrics['years_experience'].min()), 
    float(metrics['years_experience'].max()), 
    (0.0, 15.0)
)

# Filter data
filtered = metrics[
    (metrics['department'].isin(selected_dept)) &
    (metrics['performance_tier'].isin(selected_tier)) &
    (metrics['years_experience'] >= min_exp) &
    (metrics['years_experience'] <= max_exp)
]

# --- Header ---
st.title("📊 Employee Performance & Productivity Analytics")
st.caption("EmployeeBay Systems — Internal Analytics Dashboard")
st.markdown("---")

# --- KPI Cards Row ---
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Employees", len(filtered))
col2.metric("Avg Performance Score", f"{filtered['performance_score'].mean():.1f}")
col3.metric("Avg Completion Rate", f"{filtered['completion_rate'].mean():.1f}%")
col4.metric("High Performers", len(filtered[filtered['performance_tier'] == 'High Performer']))
col5.metric("At Risk Employees", len(filtered[filtered['performance_tier'] == 'At Risk']))

st.markdown("---")

# --- Charts Row 1 ---
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Performance Tier Distribution")
    tier_fig = px.pie(
        filtered, names='performance_tier',
        color_discrete_sequence=px.colors.qualitative.Set2,
        hole=0.4
    )
    tier_fig.update_layout(margin=dict(t=20, b=20))
    st.plotly_chart(tier_fig, use_container_width=True)

with col_b:
    st.subheader("Performance Score by Department")
    dept_fig = px.box(
        filtered, x='department', y='performance_score',
        color='department', color_discrete_sequence=px.colors.qualitative.Pastel
    )
    dept_fig.update_layout(showlegend=False, margin=dict(t=20, b=20))
    st.plotly_chart(dept_fig, use_container_width=True)

# --- Charts Row 2 ---
col_c, col_d = st.columns(2)

with col_c:
    st.subheader("Completion Rate vs Experience")
    scatter_fig = px.scatter(
        filtered, x='years_experience', y='completion_rate',
        color='performance_tier', size='total_tasks_assigned',
        hover_data=['role', 'department'],
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    st.plotly_chart(scatter_fig, use_container_width=True)

with col_d:
    st.subheader("Deadline Adherence by Department")
    adherence = filtered.groupby('department')['deadline_adherence_rate'].mean().reset_index()
    bar_fig = px.bar(
        adherence, x='department', y='deadline_adherence_rate',
        color='deadline_adherence_rate', color_continuous_scale='RdYlGn',
        labels={'deadline_adherence_rate': 'Adherence Rate (%)'}
    )
    bar_fig.update_layout(coloraxis_showscale=False, margin=dict(t=20))
    st.plotly_chart(bar_fig, use_container_width=True)

# --- Employee Table ---
st.markdown("---")
st.subheader("📋 Employee Performance Table")
display_cols = ['employee_id', 'department', 'role', 'performance_score',
                'performance_tier', 'completion_rate', 'deadline_adherence_rate',
                'avg_efficiency', 'years_experience']

st.dataframe(
    filtered[display_cols].sort_values('performance_score', ascending=False),
    use_container_width=True,
    hide_index=True
)

# --- Prediction Tool ---
st.markdown("---")
st.subheader("🤖 Performance Predictor")
st.caption("Enter an employee's metrics to predict their performance tier")

pred_col1, pred_col2, pred_col3 = st.columns(3)
with pred_col1:
    p_completion = st.slider("Completion Rate (%)", 0.0, 100.0, 75.0)
    p_deadline = st.slider("Deadline Adherence (%)", 0.0, 100.0, 70.0)
    p_efficiency = st.slider("Avg Efficiency Score", 0.0, 100.0, 75.0)
with pred_col2:
    p_satisfaction = st.slider("Avg Satisfaction (1-5)", 1.0, 5.0, 3.5)
    p_experience = st.slider("Years of Experience", 0.0, 20.0, 3.0)
    p_tasks = st.slider("Tasks Assigned", 1, 50, 15)
with pred_col3:
    p_high_priority = st.slider("High Priority Tasks", 0, 20, 5)
    p_time_ratio = st.slider("Time Efficiency Ratio", 0.1, 3.0, 1.0)
    p_dept = st.selectbox("Department", options=metrics['department'].unique())

if st.button("🔍 Predict Performance Tier", type="primary"):
    try:
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model = joblib.load(os.path.join(base, 'src', 'performance_model.pkl'))
        le = LabelEncoder()
        le.fit(metrics['department'])
        dept_enc = le.transform([p_dept])[0]
        
        features = np.array([[p_completion, p_deadline, p_efficiency,
                               p_satisfaction, p_time_ratio, p_experience,
                               p_tasks, p_high_priority, dept_enc]])
        prediction = model.predict(features)[0]
        proba = model.predict_proba(features)[0]
        
        if prediction == 1:
            st.success(f"✅ Predicted: HIGH PERFORMER (Confidence: {proba[1]:.1%})")
        else:
            st.warning(f"⚠️ Predicted: NOT a High Performer (Confidence: {proba[0]:.1%})")
    except Exception as e:
        st.error(f"Model not found. Please run the ML notebook first. Error: {e}")