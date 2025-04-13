import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
import numpy as np
import requests
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="Bangalore Accident Prevention System",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        font-weight: 700;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        font-weight: 500;
    }
    .card {
        border-radius: 5px;
        padding: 20px;
        background-color: #f9f9f9;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .warning {
        color: #ff5252;
        font-weight: 500;
    }
    .info {
        color: #4caf50;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Accident Map", "Weather & Alerts", "Report Issue"])

# Load Bangalore accident data
@st.cache_data
def load_accident_data():
    try:
        # Load data from CSV file
        data = pd.read_csv('data/bangalore_accident_data.csv')
        return data
    except Exception as e:
        st.error(f"Error loading accident data: {e}")
        return pd.DataFrame()

# Get current weather data
@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_weather_data(lat=12.9716, lon=77.5946):
    try:
        # Using OpenMeteo API for weather data
        base_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": ["temperature_2m", "relative_humidity_2m", "precipitation", "wind_speed_10m", "weather_code"],
            "hourly": ["temperature_2m", "precipitation_probability", "weather_code"],
            "forecast_days": 3
        }

        response = requests.get(base_url, params=params)
        return response.json()
    except Exception as e:
        st.error(f"Error fetching weather data: {e}")
        return {}

# Weather code to condition mapping
def get_weather_condition(code):
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snow fall",
        73: "Moderate snow fall",
        75: "Heavy snow fall",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    }
    return weather_codes.get(code, "Unknown")

# Home Page
def home_page():
    st.markdown("<h1 class='main-header'>Bangalore Accident Prevention System</h1>", unsafe_allow_html=True)

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

    # Key statistics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='card' style='text-align: center;'>
            <h3>Accident Hotspots</h3>
            <h2 style='color: #ff5252;'>10</h2>
            <p>High-risk areas identified</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='card' style='text-align: center;'>
            <h3>Weather Alerts</h3>
            <h2 style='color: #ff9800;'>3</h2>
            <p>Active weather warnings</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='card' style='text-align: center;'>
            <h3>Citizen Reports</h3>
            <h2 style='color: #2196f3;'>24</h2>
            <p>Safety issues reported this week</p>
        </div>
        """, unsafe_allow_html=True)

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

    # Recent updates section
    st.markdown("<h2 class='sub-header'>Recent Updates</h2>", unsafe_allow_html=True)

    with st.container():
        st.markdown("""
        <div class='card'>
            <h4>⚠️ Heavy Rain Alert - May 15, 2023</h4>
            <p>Heavy rainfall expected in East and South Bangalore. Potential for waterlogging in low-lying areas.</p>
        </div>
        """, unsafe_allow_html=True)

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

# Accident Map Page
def accident_map_page():
    st.markdown("<h1 class='main-header'>Accident Hotspot Map</h1>", unsafe_allow_html=True)

    # Load accident data
    accident_data = load_accident_data()

    # Filter options
    st.sidebar.markdown("### Filter Options")
    severity_filter = st.sidebar.multiselect(
        "Severity Level",
        options=["high", "medium", "low"],
        default=["high", "medium"]
    )

    min_incidents = st.sidebar.slider(
        "Minimum Incidents",
        min_value=0,
        max_value=50,
        value=20
    )

    # Filter data
    filtered_data = accident_data[
        (accident_data['severity'].isin(severity_filter)) &
        (accident_data['incidents'] >= min_incidents)
    ]

    # Create map
    st.markdown("<h2 class='sub-header'>Bangalore Accident Prone Areas</h2>", unsafe_allow_html=True)

    # Create a folium map centered on Bangalore
    m = folium.Map(location=[12.9716, 77.5946], zoom_start=12, tiles="OpenStreetMap")

    # Add markers for accident hotspots
    for idx, row in filtered_data.iterrows():
        # Choose color based on severity
        if row['severity'] == 'high':
            color = 'red'
            icon = 'exclamation-circle'
        elif row['severity'] == 'medium':
            color = 'orange'
            icon = 'exclamation'
        else:
            color = 'blue'
            icon = 'info-sign'

        # Create popup content
        popup_content = f"""
        <div style='width: 200px'>
            <h4>{row['location']}</h4>
            <p><b>Incidents:</b> {row['incidents']}</p>
            <p><b>Severity:</b> {row['severity'].capitalize()}</p>
            <p>{row['description']}</p>
        </div>
        """

        # Add marker to map
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=folium.Popup(popup_content, max_width=300),
            icon=folium.Icon(color=color, icon=icon, prefix='fa')
        ).add_to(m)

    # Display the map
    folium_static(m, width=1000, height=600)

    # Display data table
    st.markdown("<h2 class='sub-header'>Accident Hotspot Details</h2>", unsafe_allow_html=True)
    st.dataframe(
        filtered_data[['location', 'severity', 'incidents', 'description']],
        use_container_width=True,
        hide_index=True
    )

    # Accident statistics
    st.markdown("<h2 class='sub-header'>Accident Statistics</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        # Create a bar chart of incidents by location
        fig = px.bar(
            filtered_data,
            x='location',
            y='incidents',
            color='severity',
            color_discrete_map={'high': '#ff5252', 'medium': '#ff9800', 'low': '#2196f3'},
            title='Number of Incidents by Location',
            labels={'incidents': 'Number of Incidents', 'location': 'Location'}
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Create a pie chart of incidents by severity
        severity_counts = filtered_data.groupby('severity')['incidents'].sum().reset_index()
        fig = px.pie(
            severity_counts,
            values='incidents',
            names='severity',
            color='severity',
            color_discrete_map={'high': '#ff5252', 'medium': '#ff9800', 'low': '#2196f3'},
            title='Incidents by Severity Level'
        )
        st.plotly_chart(fig, use_container_width=True)

# Weather and Alerts Page
def weather_alerts_page():
    st.markdown("<h1 class='main-header'>Weather & Safety Alerts</h1>", unsafe_allow_html=True)

    # Get weather data
    weather_data = get_weather_data()

    if weather_data:
        # Current weather
        current = weather_data.get('current', {})
        hourly = weather_data.get('hourly', {})

        st.markdown("<h2 class='sub-header'>Current Weather Conditions</h2>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div class='card' style='text-align: center;'>
                <h3>Temperature</h3>
                <h2>{current.get('temperature_2m', 'N/A')}°C</h2>
                <p>{get_weather_condition(current.get('weather_code', 0))}</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class='card' style='text-align: center;'>
                <h3>Humidity</h3>
                <h2>{current.get('relative_humidity_2m', 'N/A')}%</h2>
                <p>Relative Humidity</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class='card' style='text-align: center;'>
                <h3>Wind Speed</h3>
                <h2>{current.get('wind_speed_10m', 'N/A')} km/h</h2>
                <p>At 10m height</p>
            </div>
            """, unsafe_allow_html=True)

        # Weather forecast
        st.markdown("<h2 class='sub-header'>3-Day Weather Forecast</h2>", unsafe_allow_html=True)

        if hourly and 'time' in hourly:
            # Prepare forecast data
            forecast_data = {
                'time': hourly['time'][:72],  # 3 days (24 hours * 3)
                'temperature': hourly['temperature_2m'][:72],
                'precipitation_probability': hourly['precipitation_probability'][:72],
                'weather_code': hourly['weather_code'][:72]
            }

            # Convert to DataFrame
            forecast_df = pd.DataFrame(forecast_data)
            forecast_df['time'] = pd.to_datetime(forecast_df['time'])
            forecast_df['date'] = forecast_df['time'].dt.date
            forecast_df['hour'] = forecast_df['time'].dt.hour

            # Create temperature chart
            fig = px.line(
                forecast_df,
                x='time',
                y='temperature',
                title='Temperature Forecast (°C)',
                labels={'temperature': 'Temperature (°C)', 'time': 'Time'}
            )
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)

            # Create precipitation probability chart
            fig = px.bar(
                forecast_df,
                x='time',
                y='precipitation_probability',
                title='Precipitation Probability (%)',
                labels={'precipitation_probability': 'Probability (%)', 'time': 'Time'}
            )
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)

        # Weather alerts
        st.markdown("<h2 class='sub-header'>Weather-Related Safety Alerts</h2>", unsafe_allow_html=True)

        # Check for rain
        has_rain = any(code in [51, 53, 55, 61, 63, 65, 80, 81, 82] for code in hourly.get('weather_code', [])[:24])

        if has_rain:
            st.markdown("""
            <div class='card' style='border-left: 4px solid #ff5252;'>
                <h3 class='warning'>⚠️ Heavy Rain Alert</h3>
                <p>Rain expected in the next 24 hours. Be cautious on roads, especially in these areas:</p>
                <ul>
                    <li>Koramangala - Potential waterlogging</li>
                    <li>Outer Ring Road - Slippery conditions</li>
                    <li>Marathahalli - Poor drainage areas</li>
                </ul>
                <p><b>Safety Tips:</b> Reduce speed, maintain safe distance, use headlights.</p>
            </div>
            """, unsafe_allow_html=True)

        # Check for high winds
        high_wind = current.get('wind_speed_10m', 0) > 20

        if high_wind:
            st.markdown("""
            <div class='card' style='border-left: 4px solid #ff9800;'>
                <h3 class='warning'>⚠️ High Wind Advisory</h3>
                <p>Strong winds may affect vehicle stability, especially for:</p>
                <ul>
                    <li>Two-wheelers and high-profile vehicles</li>
                    <li>Elevated roads and flyovers</li>
                    <li>Areas with construction scaffolding</li>
                </ul>
                <p><b>Safety Tips:</b> Maintain firm grip on steering, be cautious when passing large vehicles.</p>
            </div>
            """, unsafe_allow_html=True)

        # General safety tips
        st.markdown("""
        <div class='card'>
            <h3>Safe Driving Tips During Adverse Weather</h3>
            <ul>
                <li>Reduce speed during wet or foggy conditions</li>
                <li>Maintain safe following distance (3-second rule)</li>
                <li>Turn on headlights in poor visibility</li>
                <li>Avoid driving through standing water</li>
                <li>Check your route for accidents or closures before leaving</li>
                <li>Allow extra time for travel during severe weather</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Unable to fetch weather data. Please try again later.")

# Report Issue Page
def report_issue_page():
    st.markdown("<h1 class='main-header'>Report a Safety Issue</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    <h2 class='sub-header'>Help Improve Road Safety</h2>
    <p>Report road hazards, infrastructure issues, or dangerous conditions to help make Bangalore safer for everyone.</p>
    </div>
    """, unsafe_allow_html=True)

    # Report form
    with st.form("safety_report_form"):
        # Basic information
        issue_title = st.text_input("Issue Title", placeholder="E.g., Pothole on MG Road")

        col1, col2 = st.columns(2)
        with col1:
            issue_type = st.selectbox(
                "Issue Type",
                options=["Pothole", "Broken Traffic Signal", "Waterlogging", "Poor Visibility", "Dangerous Driving", "Other"]
            )

        with col2:
            severity = st.select_slider(
                "Severity",
                options=["Low", "Medium", "High"],
                value="Medium"
            )

        location = st.text_input("Location", placeholder="E.g., Near Forum Mall, Koramangala")

        # Map for location selection
        st.markdown("### Select Location on Map")
        m = folium.Map(location=[12.9716, 77.5946], zoom_start=12, tiles="OpenStreetMap")
        folium_static(m, width=800, height=400)

        # Additional details
        description = st.text_area(
            "Description",
            placeholder="Please provide details about the issue...",
            height=150
        )

        # Photo upload
        photo = st.file_uploader("Upload Photo (optional)", type=["jpg", "jpeg", "png"])

        # Contact information (optional)
        st.markdown("### Contact Information (Optional)")

        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Your Name (Optional)")

        with col2:
            contact = st.text_input("Contact Number (Optional)")

        # Submit button
        submit_button = st.form_submit_button("Submit Report")

    if submit_button:
        if issue_title and location and description:
            st.success("Thank you for your report! City officials have been notified about this issue.")

            # Display submission summary
            st.markdown("### Report Summary")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Issue Title:** {issue_title}")
                st.markdown(f"**Issue Type:** {issue_type}")
                st.markdown(f"**Severity:** {severity}")
                st.markdown(f"**Location:** {location}")

            with col2:
                st.markdown(f"**Description:** {description}")
                if name:
                    st.markdown(f"**Reported By:** {name}")
                if photo:
                    st.image(photo, caption="Uploaded Photo", width=300)
        else:
            st.error("Please fill in all required fields (Title, Location, and Description).")

# Main app logic
if page == "Home":
    home_page()
elif page == "Accident Map":
    accident_map_page()
elif page == "Weather & Alerts":
    weather_alerts_page()
elif page == "Report Issue":
    report_issue_page()
