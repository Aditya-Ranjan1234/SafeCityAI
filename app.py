"""
Main application file for the Bangalore Accident Prevention System.

This is the entry point for the Streamlit application, which sets up the
page configuration, navigation, and renders the appropriate page based on
user selection.
"""

import streamlit as st
import os
import sys

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import utility modules
from src.utils.config import setup_page
from src.utils.data_loader import load_accident_data, get_weather_data

# Import page modules
from src.pages import home_page, accident_map_page, weather_page, report_page, ml_predictions_page

# Import components
from src.components.emergency_services import display_emergency_banner

# Set up the page configuration
setup_page()

# Initialize session state for navigation if not already set
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Display emergency services banner at the top
display_emergency_banner()

# Sidebar navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio(
    "Go to",
    ["Home", "Accident Map", "Weather & Alerts", "ML Predictions", "Report Issue"],
    index=["Home", "Accident Map", "Weather & Alerts", "ML Predictions", "Report Issue"].index(st.session_state.page if st.session_state.page in ["Home", "Accident Map", "Weather & Alerts", "ML Predictions", "Report Issue"] else "Home")
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
elif selected_page == "Weather & Alerts":
    weather_page.render()
elif selected_page == "ML Predictions":
    ml_predictions_page.render()
elif selected_page == "Report Issue":
    report_page.render()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "© 2023 Bangalore Accident Prevention System | "
    "Developed for safer roads and communities"
    "</div>",
    unsafe_allow_html=True
)
