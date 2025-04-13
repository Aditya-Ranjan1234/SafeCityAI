"""
Weather visualization components for the Bangalore Accident Prevention System.

This module contains functions for displaying weather data and related alerts.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from src.utils.data_loader import get_weather_condition, get_weather_icon
from src.utils.config import COLORS

def display_current_weather(weather_data):
    """
    Display current weather conditions.

    Args:
        weather_data (dict): Weather data from the API

    Returns:
        None: Displays weather information in the Streamlit app
    """
    if not weather_data or 'current' not in weather_data:
        st.error("Weather data not available")
        return

    current = weather_data.get('current', {})

    # Get weather condition and icon
    weather_code = current.get('weather_code', 0)
    is_day = current.get('is_day', 1)
    condition = get_weather_condition(weather_code)
    icon = get_weather_icon(weather_code, is_day)

    # Display current weather in three columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class='card' style='text-align: center;'>
            <h3>Temperature</h3>
            <div style='font-size: 3rem;'>{icon}</div>
            <h2>{current.get('temperature_2m', 'N/A')}°C</h2>
            <p>{condition}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='card' style='text-align: center;'>
            <h3>Humidity</h3>
            <div style='font-size: 3rem;'>💧</div>
            <h2>{current.get('relative_humidity_2m', 'N/A')}%</h2>
            <p>Relative Humidity</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class='card' style='text-align: center;'>
            <h3>Wind Speed</h3>
            <div style='font-size: 3rem;'>🌬️</div>
            <h2>{current.get('wind_speed_10m', 'N/A')} km/h</h2>
            <p>At 10m height</p>
        </div>
        """, unsafe_allow_html=True)

def display_weather_forecast(weather_data):
    """
    Display weather forecast for the next few days.

    Args:
        weather_data (dict): Weather data from the API

    Returns:
        None: Displays forecast in the Streamlit app
    """
    if not weather_data or 'hourly' not in weather_data:
        return

    hourly = weather_data.get('hourly', {})
    daily = weather_data.get('daily', {})

    # Display daily forecast if available
    if daily and 'time' in daily:
        st.markdown("<h3>Daily Forecast</h3>", unsafe_allow_html=True)

        # Create columns for each day
        cols = st.columns(len(daily['time']))

        for i, (day, max_temp, min_temp, weather_code) in enumerate(zip(
            daily['time'],
            daily['temperature_2m_max'],
            daily['temperature_2m_min'],
            daily['weather_code']
        )):
            # Format date
            # For demo purposes, we'll use March-April 2025 dates
            # In a real app, this would use the actual API data
            date_obj = datetime.strptime(day, "%Y-%m-%d")
            day_name = date_obj.strftime("%a")

            # Override with March-April 2025 dates for the demo
            if i == 0:
                date_str = "14 Apr 2025"
                day_name = "Mon"
            elif i == 1:
                date_str = "15 Apr 2025"
                day_name = "Tue"
            elif i == 2:
                date_str = "16 Apr 2025"
                day_name = "Wed"
            else:
                date_str = f"{14 + i} Apr 2025"

            # Get weather icon
            icon = get_weather_icon(weather_code)
            condition = get_weather_condition(weather_code)

            with cols[i]:
                st.markdown(f"""
                <div class='card' style='text-align: center; padding: 10px;'>
                    <h4>{day_name}</h4>
                    <p>{date_str}</p>
                    <div style='font-size: 2rem;'>{icon}</div>
                    <p>{condition}</p>
                    <div style='margin-top: 10px;'>
                        <span style='color: {COLORS["hazard_high"]}; font-weight: bold;'>{max_temp}°</span> /
                        <span style='color: {COLORS["info"]};'>{min_temp}°</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    # Hourly forecast charts
    if hourly and 'time' in hourly:
        st.markdown("<h3>Hourly Forecast</h3>", unsafe_allow_html=True)

        # Prepare forecast data
        forecast_data = {
            'time': hourly['time'][:24],  # Next 24 hours
            'temperature': hourly['temperature_2m'][:24],
            'precipitation_probability': hourly['precipitation_probability'][:24],
            'weather_code': hourly['weather_code'][:24],
            'wind_speed': hourly['wind_speed_10m'][:24]
        }

        # Convert to DataFrame
        forecast_df = pd.DataFrame(forecast_data)
        forecast_df['time'] = pd.to_datetime(forecast_df['time'])
        forecast_df['hour'] = forecast_df['time'].dt.hour
        forecast_df['formatted_time'] = forecast_df['time'].dt.strftime('%H:%M')

        # For demo purposes, update the dates to April 2025
        # In a real app, this would use the actual API data
        base_date = pd.Timestamp('2025-04-14')
        hours = pd.timedelta_range(start='0 hours', periods=24, freq='H')
        forecast_df['time'] = [base_date + hour for hour in hours]

        # Create temperature chart
        fig = px.line(
            forecast_df,
            x='time',
            y='temperature',
            title='Temperature Forecast (°C)',
            labels={'temperature': 'Temperature (°C)', 'time': 'Time'},
            markers=True
        )
        fig.update_layout(
            xaxis_tickangle=-45,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.1)'),
            margin=dict(l=20, r=20, t=40, b=20),
            height=350
        )
        fig.update_traces(line=dict(color=COLORS["primary"], width=3))
        st.plotly_chart(fig, use_container_width=True)

        # Create precipitation probability chart
        fig = px.bar(
            forecast_df,
            x='time',
            y='precipitation_probability',
            title='Precipitation Probability (%)',
            labels={'precipitation_probability': 'Probability (%)', 'time': 'Time'},
            color_discrete_sequence=[COLORS["info"]]
        )
        fig.update_layout(
            xaxis_tickangle=-45,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.1)'),
            margin=dict(l=20, r=20, t=40, b=20),
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)

def display_weather_alerts(alerts):
    """
    Display weather-related safety alerts.

    Args:
        alerts (list): List of alert dictionaries

    Returns:
        None: Displays alerts in the Streamlit app
    """
    if not alerts:
        st.markdown("""
        <div class='card' style='border-left: 4px solid #4CAF50;'>
            <h3 style='color: #4CAF50;'>✅ No Weather Alerts</h3>
            <p>There are currently no weather-related safety alerts for Bangalore.</p>
        </div>
        """, unsafe_allow_html=True)
        return

    for alert in alerts:
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

            <p><strong>Affected Areas:</strong></p>
            <ul>
                {"".join(f"<li>{area}</li>" for area in alert.get('areas', []))}
            </ul>

            <p><strong>Safety Tips:</strong></p>
            <ul>
                {"".join(f"<li>{tip}</li>" for tip in alert.get('safety_tips', []))}
            </ul>
        </div>
        """, unsafe_allow_html=True)

def display_safety_tips():
    """
    Display general safety tips for adverse weather conditions.

    Returns:
        None: Displays safety tips in the Streamlit app
    """
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
            <li>Ensure your vehicle's wipers and lights are in good condition</li>
            <li>Keep emergency contact numbers handy</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
