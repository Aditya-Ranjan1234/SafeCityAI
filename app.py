"""
Main application file for the Bangalore Accident Prevention System.

This is the entry point for the Streamlit application, which sets up the
page configuration, navigation, and renders the appropriate page based on
user selection.
"""

import streamlit as st

# Set up the page configuration - MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="Bangalore Accident Prevention System",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

import os
import sys

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import utility modules
from src.utils.config import load_css
from src.utils.data_loader import load_accident_data, get_weather_data

# Import page modules
from src.pages import home_page, accident_map_page, weather_page, report_page, ml_predictions_page
from src.pages import route_planning_page, video_surveillance_page

# Import components
from src.components.emergency_services import display_emergency_banner

# Load CSS styles
load_css()

# Add additional CSS to ensure chart text is visible
st.markdown("""
<style>
    /* Force all text in charts to be white and bold */
    .js-plotly-plot text,
    .js-plotly-plot .xtick text,
    .js-plotly-plot .ytick text,
    .js-plotly-plot .gtitle,
    .js-plotly-plot .ztick text,
    .js-plotly-plot .legend text,
    .js-plotly-plot .annotation-text,
    .js-plotly-plot .xaxis .title,
    .js-plotly-plot .yaxis .title,
    .js-plotly-plot .zaxis .title {
        fill: white !important;
        color: white !important;
        font-weight: bold !important;
        text-shadow: 1px 1px 2px black !important;
    }

    /* Ensure chart backgrounds are dark */
    .js-plotly-plot .plotly .main-svg,
    .js-plotly-plot .bg,
    .stPlotlyChart > div > div > div {
        background-color: #1E1E2E !important;
    }

    /* Make axis lines visible */
    .js-plotly-plot .xaxis path.domain,
    .js-plotly-plot .yaxis path.domain {
        stroke: white !important;
        stroke-width: 2px !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for navigation if not already set
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Display emergency services banner at the top
display_emergency_banner()

# Sidebar navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio(
    "Go to",
    ["Home", "Accident Map", "Safe Route Planning", "Video Surveillance", "ML Predictions", "Report Issue"],
    index=["Home", "Accident Map", "Safe Route Planning", "Video Surveillance", "ML Predictions", "Report Issue"].index(st.session_state.page if st.session_state.page in ["Home", "Accident Map", "Safe Route Planning", "Video Surveillance", "ML Predictions", "Report Issue"] else "Home")
)

# Update session state
st.session_state.page = selected_page

# Display app information in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.markdown(
    "The Bangalore Accident Prevention System integrates multiple data sources "
    "to help prevent accidents and improve road safety in Bangalore."
)

# Display data sources in sidebar
st.sidebar.markdown("### Data Sources")
st.sidebar.markdown(
    "- Accident data: Historical records\n"
    "- Weather data: Open-Meteo API\n"
    "- Citizen reports: Crowdsourced"
)

# Render the selected page
if selected_page == "Home":
    home_page.render()
elif selected_page == "Accident Map":
    accident_map_page.render()
elif selected_page == "Safe Route Planning":
    route_planning_page.display_route_planning_page()
elif selected_page == "Video Surveillance":
    video_surveillance_page.display_video_surveillance_page()
elif selected_page == "ML Predictions":
    ml_predictions_page.render()
elif selected_page == "Report Issue":
    report_page.render()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "© 2025 Bangalore Accident Prevention System | "
    "Developed for safer roads and communities | "
    "Created for समAI - Time for AI | "
    "Data updated: April 2025"
    "</div>",
    unsafe_allow_html=True
)
