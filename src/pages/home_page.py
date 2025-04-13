"""
Home page for the Bangalore Accident Prevention System.

This module contains the layout and functionality for the home page,
which serves as the main entry point for the application.
"""

import streamlit as st
from src.utils.data_loader import load_accident_data, get_weather_data, get_safety_alerts
from src.components.stats_components import display_key_metrics
from src.components.map_components import create_accident_map, display_map

def render():
    """
    Render the home page.

    Returns:
        None: Renders the home page in the Streamlit app
    """
    st.markdown("<h1 class='main-header'>Bangalore Accident Prevention System</h1>", unsafe_allow_html=True)

    # Introduction card
    st.markdown("""
    <div class='card'>
    <h2 class='sub-header'>Welcome to the Predictive Accident Prevention System</h2>
    <p>This platform integrates multiple data sources to help prevent accidents and improve road safety in Bangalore:</p>
    <ul>
        <li>Real-time weather data and forecasts</li>
        <li>Historical accident records and hotspots</li>
        <li>Crowdsourced safety reports from citizens</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # Load data
    accident_data = load_accident_data()
    weather_data = get_weather_data()
    safety_alerts = get_safety_alerts(weather_data)

    # Display key metrics
    display_key_metrics(accident_data)

    # Quick access to key features
    st.markdown("<h2 class='sub-header'>Quick Access</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='card'>
            <h3>🗺️ Accident Hotspot Map</h3>
            <p>View high-risk areas and accident-prone locations across Bangalore.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Accident Map", key="view_map"):
            st.session_state.page = "Accident Map"
            st.experimental_rerun()

    with col2:
        st.markdown("""
        <div class='card'>
            <h3>🌦️ Weather & Safety Alerts</h3>
            <p>Get real-time weather updates and related safety warnings.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Check Weather Alerts", key="check_weather"):
            st.session_state.page = "Weather & Alerts"
            st.experimental_rerun()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='card'>
            <h3>🤖 ML Risk Predictions</h3>
            <p>View machine learning based accident risk predictions across the city.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Risk Predictions", key="view_predictions"):
            st.session_state.page = "ML Predictions"
            st.experimental_rerun()

    with col2:
        st.markdown("""
        <div class='card'>
            <h3>📝 Report an Issue</h3>
            <p>Report road hazards, infrastructure issues, or dangerous conditions.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Report Issue", key="report_issue"):
            st.session_state.page = "Report Issue"
            st.experimental_rerun()

    # Preview map
    st.markdown("<h2 class='sub-header'>Accident Hotspot Preview</h2>", unsafe_allow_html=True)

    # Filter to just high severity for the preview
    preview_data = accident_data[accident_data['severity'] == 'high']
    preview_map = create_accident_map(preview_data)
    display_map(preview_map, height=400)

    # Recent alerts section
    st.markdown("<h2 class='sub-header'>Recent Alerts</h2>", unsafe_allow_html=True)

    if safety_alerts:
        for alert in safety_alerts[:2]:  # Show only top 2 alerts
            severity = alert.get('severity', 'medium')
            severity_class = {
                'high': 'high',
                'medium': 'medium',
                'low': 'low'
            }.get(severity, 'medium')

            icon = {
                'rain': '🌧️',
                'upcoming_rain': '🌦️',
                'wind': '🌬️',
                'visibility': '🌫️',
                'heat': '🌡️'
            }.get(alert.get('type', ''), '⚠️')

            st.markdown(f"""
            <div class='alert-box {severity_class}'>
                <h3 class='warning'>{icon} {alert.get('title', 'Weather Alert')}</h3>
                <p>{alert.get('description', '')}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class='card'>
            <h4>✅ No Current Alerts</h4>
            <p>There are currently no active safety alerts for Bangalore.</p>
        </div>
        """, unsafe_allow_html=True)

    # Recent updates section
    st.markdown("<h2 class='sub-header'>Recent Updates</h2>", unsafe_allow_html=True)

    with st.container():
        st.markdown("""
        <div class='card'>
            <h4>🚧 Road Work - May 14, 2023</h4>
            <p>Ongoing construction on Outer Ring Road near Marathahalli. Expect delays and plan alternate routes.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='card'>
            <h4>🚦 New Traffic Signal - May 12, 2023</h4>
            <p>New traffic signal operational at the junction of MG Road and Brigade Road. Adjusted timing to improve flow.</p>
        </div>
        """, unsafe_allow_html=True)
