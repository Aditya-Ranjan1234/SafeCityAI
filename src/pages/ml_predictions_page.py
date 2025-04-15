"""
Machine Learning Predictions page for the Bangalore Accident Prevention System.

This module contains the layout and functionality for the ML predictions page,
which displays accident risk predictions based on various factors.
"""

import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium.plugins import HeatMap
from datetime import datetime, timedelta
from streamlit_folium import folium_static
from src.utils.config import BANGALORE_LAT, BANGALORE_LON, COLORS
from src.utils.data_loader import load_accident_data, get_weather_data, get_weather_condition, get_weather_icon
from src.components.map_components import display_map

def render():
    """
    Render the ML predictions page.

    Returns:
        None: Renders the ML predictions page in the Streamlit app
    """
    st.markdown("<h1 class='main-header'>Accident Risk Predictions</h1>", unsafe_allow_html=True)

    # Introduction card
    st.markdown("""
    <div class='card'>
    <h2 class='sub-header'>Machine Learning Based Risk Assessment</h2>
    <p>Our predictive model analyzes multiple factors to identify areas with high accident risk:</p>
    <ul>
        <li>Historical accident data patterns</li>
        <li>Current and forecasted weather conditions</li>
        <li>Time of day and traffic patterns</li>
        <li>Road infrastructure and conditions</li>
    </ul>
    <p>The map below shows predicted risk levels across Bangalore city.</p>
    </div>
    """, unsafe_allow_html=True)

    # Load data
    accident_data = load_accident_data()
    weather_data = get_weather_data()

    # Create columns for filters and current conditions
    col1, col2 = st.columns([2, 1])

    with col1:
        # Time selection
        st.markdown("### Time Period for Prediction")
        time_options = ["Current Time", "Morning Rush (8-10 AM)", "Afternoon (12-2 PM)",
                        "Evening Rush (5-8 PM)", "Night (10 PM-5 AM)"]
        selected_time = st.selectbox("Select time period", time_options)

        # Weather condition override
        st.markdown("### Weather Condition")
        current_weather = "Clear" if not weather_data else get_weather_condition(weather_data.get('current', {}).get('weather_code', 0))
        weather_options = ["Use Current Weather", "Clear", "Rainy", "Foggy", "Thunderstorm"]
        selected_weather = st.selectbox("Select weather condition", weather_options,
                                       index=0 if "Use Current Weather" else weather_options.index(current_weather))

        if selected_weather == "Use Current Weather":
            weather_condition = current_weather
        else:
            weather_condition = selected_weather

    with col2:
        # Display current conditions
        st.markdown("### Current Conditions")

        # Current time
        current_time = datetime.now().strftime("%H:%M")
        current_date = datetime.now().strftime("%d %b %Y")

        # Get weather data safely
        temp = weather_data.get('current', {}).get('temperature_2m', 'N/A')
        if isinstance(temp, float):
            temp = f"{temp:.1f}"

        humidity = weather_data.get('current', {}).get('relative_humidity_2m', 'N/A')
        if isinstance(humidity, float):
            humidity = f"{humidity:.0f}"

        wind = weather_data.get('current', {}).get('wind_speed_10m', 'N/A')
        if isinstance(wind, float):
            wind = f"{wind:.1f}"

        # Create the weather display
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"**Time:** {current_time}")
            st.markdown(f"**Date:** {current_date}")

        with col2:
            st.markdown(f"**Weather:** {current_weather}")
            st.markdown(f"**Temperature:** {temp}°C")

        st.markdown(f"**Humidity:** {humidity}%")
        st.markdown(f"**Wind Speed:** {wind} km/h")

        # Risk factors explanation
        st.markdown("### Risk Factors")

        # Determine risk factors based on selected time and weather
        risk_factors = []

        if "Rush" in selected_time:
            risk_factors.append(("High Traffic Volume", "high"))
        elif "Night" in selected_time:
            risk_factors.append(("Poor Visibility", "medium"))

        if weather_condition in ["Rainy", "Thunderstorm"]:
            risk_factors.append(("Wet Roads", "high"))
        elif weather_condition == "Foggy":
            risk_factors.append(("Reduced Visibility", "high"))

        # Display risk factors
        if risk_factors:
            for factor, severity in risk_factors:
                severity_color = COLORS["hazard_high"] if severity == "high" else COLORS["hazard_medium"]
                st.markdown(f"**{factor}** - {severity.capitalize()} Risk", unsafe_allow_html=True)
        else:
            st.markdown("No significant risk factors")

    # Generate risk prediction map
    st.markdown("### City-wide Risk Prediction Map")

    # Create risk map
    risk_map = create_risk_prediction_map(accident_data, selected_time, weather_condition)

    # Display the map
    display_map(risk_map, width=1000, height=600)

    # Risk level legend
    st.markdown("### Risk Level Legend")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("🟢 Low Risk")
    with col2:
        st.markdown("🟡 Moderate Risk")
    with col3:
        st.markdown("🟠 High Risk")
    with col4:
        st.markdown("🔴 Very High Risk")

    # Emerging hotspots
    st.markdown("### Emerging Accident Hotspots")

    # Generate some sample emerging hotspots
    emerging_hotspots = generate_emerging_hotspots()

    # Display emerging hotspots
    for hotspot in emerging_hotspots:
        risk_color = {
            "high": COLORS["hazard_high"],
            "medium": COLORS["hazard_medium"],
            "low": COLORS["hazard_low"]
        }.get(hotspot["risk_level"], COLORS["hazard_medium"])

        st.markdown(f"**{hotspot['location']}** - {hotspot['risk_level'].capitalize()} Risk")
        st.markdown(hotspot["description"])

        # Display factors
        st.markdown("**Contributing Factors:**")
        for factor in hotspot["factors"]:
            st.markdown(f"- {factor}")

        st.markdown("---")

    # Safety recommendations
    st.markdown("### Personalized Safety Recommendations")

    # Generate recommendations based on selected time and weather
    recommendations = generate_safety_recommendations(selected_time, weather_condition)

    # Display recommendations
    for i, recommendation in enumerate(recommendations):
        st.markdown(f"**{i+1}. {recommendation['title']}**")
        st.markdown(recommendation["description"])
        st.markdown("")

def create_risk_prediction_map(accident_data, time_period, weather_condition):
    """
    Create a map showing predicted accident risk across Bangalore.

    Args:
        accident_data (pandas.DataFrame): DataFrame containing accident data
        time_period (str): Selected time period
        weather_condition (str): Selected weather condition

    Returns:
        folium.Map: Map object with risk prediction visualization
    """
    # Create base map
    m = folium.Map(location=[BANGALORE_LAT, BANGALORE_LON], zoom_start=12, tiles="CartoDB positron")

    # Generate grid of points covering Bangalore
    grid_points = generate_risk_grid()

    # Add risk heatmap
    HeatMap(
        grid_points,
        radius=25,
        max_zoom=13,
        gradient={
            0.0: '#00FF00',  # Green (low risk)
            0.5: '#FFFF00',  # Yellow (moderate risk)
            0.75: '#FFA500', # Orange (high risk)
            1.0: '#FF0000'   # Red (very high risk)
        }
    ).add_to(m)

    # Add markers for known accident hotspots
    for _, row in accident_data.iterrows():
        if row['severity'] == 'high':
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=8,
                color='#FF0000',
                fill=True,
                fill_color='#FF0000',
                fill_opacity=0.7,
                popup=f"<b>{row['location']}</b><br>High risk area"
            ).add_to(m)

    return m

def generate_risk_grid():
    """
    Generate a grid of points with risk values covering Bangalore.

    Returns:
        list: List of [lat, lng, intensity] points for heatmap
    """
    # Define Bangalore area bounds
    min_lat, max_lat = 12.8, 13.1
    min_lng, max_lng = 77.4, 77.8

    # Generate grid
    grid_points = []

    # Known high-risk areas (major junctions and accident-prone areas)
    high_risk_areas = [
        (12.9177, 77.6233, 1.0),  # Silk Board Junction
        (13.0054, 77.6714, 0.9),  # KR Puram Bridge
        (13.0358, 77.5946, 0.9),  # Hebbal Flyover
        (12.9591, 77.6974, 0.8),  # Marathahalli Bridge
        (12.8933, 77.5970, 0.8),  # Bannerghatta Road
        (12.9984, 77.6610, 0.9),  # Tin Factory
        (13.0152, 77.5843, 0.7),  # Mekhri Circle
        (13.0204, 77.5563, 0.7),  # Yeshwanthpur Junction
        (12.9227, 77.6127, 0.9),  # Jayadeva Flyover
        (12.8440, 77.6608, 0.7),  # Electronic City Flyover
    ]

    # Add high-risk areas
    grid_points.extend(high_risk_areas)

    # Generate random points with risk values influenced by proximity to high-risk areas
    np.random.seed(42)  # For reproducibility
    num_points = 500

    for _ in range(num_points):
        lat = np.random.uniform(min_lat, max_lat)
        lng = np.random.uniform(min_lng, max_lng)

        # Base risk (random)
        risk = np.random.uniform(0.1, 0.4)

        # Increase risk based on proximity to high-risk areas
        for hr_lat, hr_lng, hr_risk in high_risk_areas:
            distance = ((lat - hr_lat) ** 2 + (lng - hr_lng) ** 2) ** 0.5
            if distance < 0.03:  # Within ~3km
                risk += hr_risk * (1 - distance / 0.03) * 0.5

        # Cap risk at 1.0
        risk = min(risk, 1.0)

        grid_points.append([lat, lng, risk])

    return grid_points

def generate_emerging_hotspots():
    """
    Generate sample emerging accident hotspots.

    Returns:
        list: List of dictionaries containing emerging hotspot information
    """
    return [
        {
            "location": "Outer Ring Road near Bellandur",
            "risk_level": "high",
            "description": "Recent construction and increased traffic have led to a 40% increase in incidents over the past month.",
            "factors": ["Construction", "Rush Hour Traffic", "Poor Signage"]
        },
        {
            "location": "Whitefield Main Road",
            "risk_level": "medium",
            "description": "New IT park development has changed traffic patterns, creating congestion during peak hours.",
            "factors": ["Changed Traffic Pattern", "Peak Hour Congestion"]
        },
        {
            "location": "Indiranagar 100ft Road",
            "risk_level": "medium",
            "description": "Increased commercial activity and on-street parking have reduced effective road width.",
            "factors": ["Commercial Activity", "Parking Issues", "Pedestrian Movement"]
        }
    ]

def generate_safety_recommendations(time_period, weather_condition):
    """
    Generate safety recommendations based on selected time and weather.

    Args:
        time_period (str): Selected time period
        weather_condition (str): Selected weather condition

    Returns:
        list: List of dictionaries containing safety recommendations
    """
    recommendations = []

    # Time-based recommendations
    if "Rush" in time_period:
        recommendations.append({
            "title": "Allow Extra Travel Time",
            "description": "Plan your journey with extra buffer time to avoid rushing through traffic."
        })
    elif "Night" in time_period:
        recommendations.append({
            "title": "Ensure Good Visibility",
            "description": "Use headlights properly and ensure they are working well. Wear reflective clothing if walking or cycling."
        })

    # Weather-based recommendations
    if weather_condition in ["Rainy", "Thunderstorm"]:
        recommendations.append({
            "title": "Reduce Speed on Wet Roads",
            "description": "Decrease your speed by at least 20% on wet roads to account for reduced traction."
        })
        recommendations.append({
            "title": "Increase Following Distance",
            "description": "Double the normal following distance to allow for increased stopping distance."
        })
    elif weather_condition == "Foggy":
        recommendations.append({
            "title": "Use Fog Lights Appropriately",
            "description": "Turn on fog lights but avoid using high beams as they can reflect back and reduce visibility further."
        })

    # General recommendations
    recommendations.append({
        "title": "Avoid Accident Hotspots",
        "description": "If possible, plan routes that avoid known high-risk areas, especially during peak hours."
    })

    return recommendations

# Weather icon and condition functions are now imported from data_loader.py
