"""
Weather and Alerts page for the Bangalore Accident Prevention System.

This module contains the layout and functionality for the weather page,
which displays current weather conditions, forecasts, and related safety alerts.
"""

import streamlit as st
from src.utils.data_loader import get_weather_data, get_safety_alerts
from src.components.weather_components import (
    display_current_weather, 
    display_weather_forecast, 
    display_weather_alerts,
    display_safety_tips
)

def render():
    """
    Render the weather and alerts page.
    
    Returns:
        None: Renders the weather page in the Streamlit app
    """
    st.markdown("<h1 class='main-header'>Weather & Safety Alerts</h1>", unsafe_allow_html=True)
    
    # Introduction
    st.markdown("""
    <div class='card'>
    <p>Get real-time weather updates and related safety warnings for Bangalore. 
    Weather conditions can significantly impact road safety and traffic conditions.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Get weather data
    with st.spinner("Fetching latest weather data..."):
        weather_data = get_weather_data()
    
    if weather_data:
        # Current weather section
        st.markdown("<h2 class='sub-header'>Current Weather Conditions</h2>", unsafe_allow_html=True)
        display_current_weather(weather_data)
        
        # Weather forecast section
        st.markdown("<h2 class='sub-header'>Weather Forecast</h2>", unsafe_allow_html=True)
        display_weather_forecast(weather_data)
        
        # Weather alerts section
        st.markdown("<h2 class='sub-header'>Weather-Related Safety Alerts</h2>", unsafe_allow_html=True)
        
        # Generate safety alerts based on weather data
        safety_alerts = get_safety_alerts(weather_data)
        display_weather_alerts(safety_alerts)
        
        # Safety tips section
        st.markdown("<h2 class='sub-header'>Driving Safety Tips</h2>", unsafe_allow_html=True)
        display_safety_tips()
        
        # Weather impact on traffic
        st.markdown("<h2 class='sub-header'>Weather Impact on Traffic</h2>", unsafe_allow_html=True)
        
        # Check for rain or other adverse conditions
        current = weather_data.get('current', {})
        has_precipitation = current.get('precipitation', 0) > 0
        has_poor_visibility = False
        
        if 'hourly' in weather_data and 'visibility' in weather_data['hourly']:
            has_poor_visibility = any(vis < 5000 for vis in weather_data['hourly']['visibility'][:6])
        
        if has_precipitation or has_poor_visibility:
            st.markdown("""
            <div class='card' style='border-left: 4px solid #FF9800;'>
                <h3 style='color: #FF9800;'>⚠️ Adverse Weather Impact</h3>
                <p>Current weather conditions may affect traffic in the following areas:</p>
                <ul>
                    <li><strong>Outer Ring Road:</strong> Reduced visibility and slippery conditions</li>
                    <li><strong>Low-lying areas:</strong> Potential for water accumulation</li>
                    <li><strong>Flyovers and bridges:</strong> Extra caution advised due to slippery surfaces</li>
                </ul>
                <p>Allow extra travel time and maintain greater following distance.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class='card' style='border-left: 4px solid #4CAF50;'>
                <h3 style='color: #4CAF50;'>✅ Favorable Weather Conditions</h3>
                <p>Current weather conditions are favorable for travel. Normal traffic patterns expected.</p>
                <p>Still, always follow traffic rules and maintain safe driving practices.</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Weather-related accident statistics
        st.markdown("<h2 class='sub-header'>Weather-Related Accident Statistics</h2>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='card'>
            <p>Weather conditions can significantly impact road safety. Historical data shows:</p>
            <ul>
                <li>Accidents increase by approximately 30% during heavy rainfall in Bangalore</li>
                <li>Poor visibility conditions account for 15% of all traffic incidents</li>
                <li>Two-wheeler accidents are 2.5x more likely during wet road conditions</li>
                <li>Morning fog in winter months reduces visibility on highways and major roads</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Unable to fetch weather data. Please try again later.")
        
        # Display offline safety tips
        st.markdown("<h2 class='sub-header'>General Safety Tips</h2>", unsafe_allow_html=True)
        display_safety_tips()
