import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)


def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'


@st.cache
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
    df = df[df["ConvertedComp"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis=1)

    country_map = shorten_categories(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    df = df[df["ConvertedComp"] <= 250000]
    df = df[df["ConvertedComp"] >= 10000]
    df = df[df["Country"] != "Other"]

    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    df = df.rename({"ConvertedComp": "Salary"}, axis=1)
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Software Engineer Salaries")

    st.write(
        """
    ### Stack Overflow Developer Survey 2020
    """
    )

    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Number of Data from different countries""")

    st.pyplot(fig1)
    
    st.write(
        """
    #### Mean Salary Based On Country
    """
    )

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### Mean Salary Based On Experience
    """
    )

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)


def show_explore_page():
    # Inject custom CSS
    st.markdown(
        """
        <style>
        /* Page background */
        .stApp {
            background: linear-gradient(to right, #f0f4f8, #d9e2ec);
            color: #0f111a;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Title style */
        .title {
            color: #1f77b4;
            font-size: 40px;
            font-weight: bold;
            text-align: center;
        }

        /* Subtitle style */
        .subtitle {
            color: #ff7f0e;
            font-size: 22px;
            margin-bottom: 10px;
        }

        /* Chart containers */
        .chart-container {
            background-color: #ffffffcc;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
            margin-bottom: 30px;
        }

        /* Pie chart labels */
        .pie-label {
            #font-weight: bold;
            color: #2c3e50;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="title">Explore Software Engineer Salaries</h1>', unsafe_allow_html=True)

    st.markdown('<p class="subtitle">Stack Overflow Developer Survey 2020</p>', unsafe_allow_html=True)

    # Pie chart for country data
    data = df["Country"].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=False, startangle=180)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.markdown('<div class="chart-container"><h4 class="subtitle">Number of Data from Different Countries</h4></div>', unsafe_allow_html=True)
    st.pyplot(fig1)

    # Bar chart for mean salary by country
    st.markdown('<div class="chart-container"><h4 class="subtitle">Mean Salary Based On Country</h4></div>', unsafe_allow_html=True)
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    # Line chart for mean salary by experience
    st.markdown('<div class="chart-container"><h4 class="subtitle">Mean Salary Based On Experience</h4></div>', unsafe_allow_html=True)
    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)

