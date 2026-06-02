# Netflix Movies & TV Shows Analytics Dashboard

An interactive data analytics dashboard built with Python and Streamlit that explores Netflix's content library — uncovering trends in genres, ratings, content growth, and more.

---

## Features

- **Interactive Filters** — Filter by content type, genre, and release year range
- **4 KPI Cards** — Total titles, average runtime, countries, and genres at a glance
- **Content Growth Trend** — Area chart showing Netflix content growth over the years
- **Movies vs TV Shows** — Donut chart breakdown of content type
- **Top 10 Genres** — Horizontal bar chart of most popular genres
- **Rating Breakdown** — Sunburst chart showing ratings by content type
- **Raw Data View** — Toggle to explore the cleaned dataset directly

---

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Oooommmmm/netflix-analytics-dashboard.git
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the cleaning script (optional)**
```bash
python data_cleaning.py
```

**4. Launch the dashboard**
```bash
streamlit run app.py
```

---

## Data Cleaning Steps

The raw Netflix dataset was cleaned using the following steps:

- Removed duplicate entries
- Handled missing values in `country`, `director`, and `cast` columns
- Parsed and standardized the `date_added` column to datetime format
- Extracted `main_genre` from the `listed_in` column
- Extracted `runtime_minutes` from the `duration` column
- Removed rows with missing `rating` and `date_added` values

---
