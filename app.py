import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Netflix Analytics Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("netflix_final_clean.csv")
    df['date_added'] = pd.to_datetime(df['date_added'])
    return df

df = load_data()

st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg", width=200)
st.sidebar.title("Dashboard Filters")

content_type = st.sidebar.multiselect("Select Content Type", options=df["type"].unique(), default=df["type"].unique())
selected_genres = st.sidebar.multiselect("Select Genres", options=df["main_genre"].unique(), default=df["main_genre"].unique())
year_range = st.sidebar.slider("Release Year", int(df["release_year"].min()), 2021, (2010, 2021))

filtered_df = df[
    (df["type"].isin(content_type)) & 
    (df["main_genre"].isin(selected_genres)) & 
    (df["release_year"].between(year_range[0], year_range[1]))
]

st.title("🎬 Netflix Movies & TV Shows Analytics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Titles", len(filtered_df))
with col2:
    st.metric("Avg Runtime", f"{int(filtered_df['runtime_minutes'].mean())} min")
with col3:
    st.metric("Countries", filtered_df['country'].nunique())
with col4:
    st.metric("Genres", filtered_df['main_genre'].nunique())

st.markdown("---")

row1_col1, row1_col2 = st.columns([2, 1])

with row1_col1:
    st.subheader("Content Growth Over Time")
    trend_data = filtered_df.groupby("release_year").size().reset_index(name="Count")
    fig_trend = px.area(trend_data, x="release_year", y="Count", color_discrete_sequence=['#E50914'])
    st.plotly_chart(fig_trend, use_container_width=True)

with row1_col2:
    st.subheader("Movies vs TV Shows")
    fig_donut = px.pie(filtered_df, names="type", hole=0.5, color_discrete_map={'Movie':'#E50914', 'TV Show':'#333333'})
    st.plotly_chart(fig_donut, use_container_width=True)

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("Top 10 Genres Distribution")
    genre_data = filtered_df['main_genre'].value_counts().head(10).reset_index()
    fig_genre = px.bar(genre_data, x='count', y='main_genre', orientation='h', color_discrete_sequence=['#E50914'])
    st.plotly_chart(fig_genre, use_container_width=True)

with row2_col2:
    st.subheader("Rating Breakdown")
    fig_sunburst = px.sunburst(filtered_df, path=['type', 'rating'], color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig_sunburst, use_container_width=True)

if st.checkbox("Show Raw Cleaned Data"):
    st.dataframe(filtered_df)
