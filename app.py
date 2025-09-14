import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# ----------------- Data (from your matter) -----------------
matter_sections = {
    "Interactive Charts and Graphs": [
        "Enhanced Understanding: Interactive charts and graphs make complex data more accessible and easier to understand.",
        "Engagement: Interactive elements engage users more effectively, encouraging them to delve deeper into the data.",
        "Customization: Users can customize views to focus on specific data points or metrics."
    ],
    "Audience-Specific Visualizations": [
        "Relevance: Tailoring visualizations to the specific needs and knowledge level of the audience ensures that the information is relevant and comprehensible.",
        "Clarity: Different audiences may require different levels of detail. For example, executives might need high-level summaries, while analysts might require detailed data.",
        "Actionable Insights: When visualizations are designed with the audience in mind, they are more likely to provide actionable insights that can drive decision-making and strategy."
    ],
    "Structured Data Presentation": [
        "Clarity and Consistency: Organized data and reporting ensure that information is presented clearly and consistently.",
        "Efficiency: Well-organized reports save time for the audience, as they can quickly find and understand the information they need.",
        "Credibility: Structured and well-organized reports enhance the credibility of the data and the insights derived from it."
    ],
    "Conclusion": [
        "Choosing data visualization which is effective requires you to choose the appropriate chart types, simplifying designs, and providing clear context.",
        "Reporting involves structuring content, combining text and visuals, and offering detailed analysis, all contributing towards improved understanding as well as faster decision-making."
    ]
}

# ----------------- Streamlit UI -----------------
st.set_page_config(page_title="Data Visualization App", layout="wide")
st.title("📊 Data Visualization from Matter")

# Sidebar choice
st.sidebar.header("Choose Visualization")
option = st.sidebar.radio("Select:", ["Pie Chart", "Word Cloud", "Show Both"])

# ----------------- Pie Chart -----------------
if option in ["Pie Chart", "Show Both"]:
    st.subheader("🍰 Pie Chart: Number of Key Points per Section")

    data = {"Section": list(matter_sections.keys()),
            "Points": [len(points) for points in matter_sections.values()]}
    df = pd.DataFrame(data)

    fig, ax = plt.subplots()
    ax.pie(df["Points"], labels=df["Section"], autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

# ----------------- Word Cloud -----------------
if option in ["Word Cloud", "Show Both"]:
    st.subheader("☁️ Word Cloud: Most Frequent Terms")

    # Combine all text
    text_blob = " ".join([" ".join(points) for points in matter_sections.values()])

    wordcloud = WordCloud(width=1000, height=500, background_color="white", colormap="viridis").generate(text_blob)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)