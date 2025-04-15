"""
Data loading utilities for the Bangalore Accident Prevention System.

This module contains functions for loading and processing data from various sources,
including accident data, weather data, and other relevant information.
"""

import streamlit as st
import pandas as pd
import requests
from datetime import datetime
from src.utils.config import BANGALORE_LAT, BANGALORE_LON

@st.cache_data
def load_accident_data():
    """
    Load accident data from the CSV file.

    Returns:
        pandas.DataFrame: DataFrame containing accident data
    """
    try:
        # Load data from CSV file
        data = pd.read_csv('src/data/bangalore_accident_data.csv')
        return data
    except Exception as e:
        st.error(f"Error loading accident data: {e}")
        return pd.DataFrame()

@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_weather_data(lat=BANGALORE_LAT, lon=BANGALORE_LON):
    """
    Get current weather data from Open-Meteo API.

    Args:
        lat (float): Latitude coordinate (default: Bangalore's latitude)
        lon (float): Longitude coordinate (default: Bangalore's longitude)

    Returns:
        dict: Weather data from the API
    """
    try:
        # For demo purposes, return mock data instead of making an API call
        # This ensures we have consistent data for the demo

        # Mock current weather data
        current = {
            "temperature_2m": 23.9,
            "relative_humidity_2m": 65,
            "precipitation": 0,
            "wind_speed_10m": 2.5,
            "weather_code": 0,  # Clear sky
            "is_day": 1
        }

        # Mock hourly forecast data
        hourly_times = [f"2025-04-14T{h:02d}:00" for h in range(24)]
        hourly = {
            "time": hourly_times,
            "temperature_2m": [22.5, 22.0, 21.5, 21.0, 20.5, 20.0, 21.0, 22.0,
                             23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 28.5, 28.0,
                             27.5, 27.0, 26.0, 25.0, 24.0, 23.5, 23.0, 22.5],
            "precipitation_probability": [0, 0, 0, 0, 0, 0, 0, 0, 10, 20, 30, 40,
                                       50, 60, 70, 60, 50, 40, 30, 20, 10, 0, 0, 0],
            "weather_code": [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2,
                           3, 61, 61, 61, 3, 2, 1, 0, 0, 0, 0, 0],
            "visibility": [20000] * 24,
            "wind_speed_10m": [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9,
                             3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.4, 3.3, 3.2, 3.1,
                             3.0, 2.9, 2.8, 2.7]
        }

        # Mock daily forecast data
        daily = {
            "time": ["2025-04-14", "2025-04-15", "2025-04-16"],
            "weather_code": [61, 3, 95],  # Light rain, Overcast, Thunderstorm
            "temperature_2m_max": [28.5, 27.8, 26.5],
            "temperature_2m_min": [20.0, 19.5, 18.8],
            "precipitation_sum": [2.5, 0.0, 15.0],
            "precipitation_probability_max": [70, 30, 90]
        }

        return {
            "current": current,
            "hourly": hourly,
            "daily": daily
        }

        # Uncomment below to use the actual API in a production environment
        '''
        base_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": ["temperature_2m", "relative_humidity_2m", "precipitation",
                       "wind_speed_10m", "weather_code", "is_day"],
            "hourly": ["temperature_2m", "precipitation_probability", "weather_code",
                      "visibility", "wind_speed_10m"],
            "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min",
                     "precipitation_sum", "precipitation_probability_max"],
            "timezone": "auto",
            "forecast_days": 3
        }

        response = requests.get(base_url, params=params)
        return response.json()
        '''
    except Exception as e:
        st.error(f"Error fetching weather data: {e}")
        return {}

def get_weather_condition(code):
    """
    Convert weather code to human-readable condition.

    Args:
        code (int): Weather code from Open-Meteo API

    Returns:
        str: Human-readable weather condition
    """
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

def get_weather_icon(code, is_day=1):
    """
    Get appropriate weather icon based on weather code and time of day.

    Args:
        code (int): Weather code from Open-Meteo API
        is_day (int): Whether it's daytime (1) or nighttime (0)

    Returns:
        str: Icon name for the weather condition
    """
    if is_day:
        icons = {
            0: "☀️",  # Clear sky
            1: "🌤️",  # Mainly clear
            2: "⛅",  # Partly cloudy
            3: "☁️",  # Overcast
            45: "🌫️",  # Fog
            48: "🌫️",  # Depositing rime fog
            51: "🌦️",  # Light drizzle
            53: "🌦️",  # Moderate drizzle
            55: "🌧️",  # Dense drizzle
            56: "🌨️",  # Light freezing drizzle
            57: "🌨️",  # Dense freezing drizzle
            61: "🌦️",  # Slight rain
            63: "🌧️",  # Moderate rain
            65: "🌧️",  # Heavy rain
            66: "🌨️",  # Light freezing rain
            67: "🌨️",  # Heavy freezing rain
            71: "🌨️",  # Slight snow fall
            73: "🌨️",  # Moderate snow fall
            75: "❄️",  # Heavy snow fall
            77: "❄️",  # Snow grains
            80: "🌦️",  # Slight rain showers
            81: "🌧️",  # Moderate rain showers
            82: "🌧️",  # Violent rain showers
            85: "🌨️",  # Slight snow showers
            86: "❄️",  # Heavy snow showers
            95: "⛈️",  # Thunderstorm
            96: "⛈️",  # Thunderstorm with slight hail
            99: "⛈️",  # Thunderstorm with heavy hail
        }
    else:
        icons = {
            0: "🌙",  # Clear sky
            1: "🌙",  # Mainly clear
            2: "☁️",  # Partly cloudy
            3: "☁️",  # Overcast
            45: "🌫️",  # Fog
            48: "🌫️",  # Depositing rime fog
            51: "🌧️",  # Light drizzle
            53: "🌧️",  # Moderate drizzle
            55: "🌧️",  # Dense drizzle
            56: "🌨️",  # Light freezing drizzle
            57: "🌨️",  # Dense freezing drizzle
            61: "🌧️",  # Slight rain
            63: "🌧️",  # Moderate rain
            65: "🌧️",  # Heavy rain
            66: "🌨️",  # Light freezing rain
            67: "🌨️",  # Heavy freezing rain
            71: "🌨️",  # Slight snow fall
            73: "🌨️",  # Moderate snow fall
            75: "❄️",  # Heavy snow fall
            77: "❄️",  # Snow grains
            80: "🌧️",  # Slight rain showers
            81: "🌧️",  # Moderate rain showers
            82: "🌧️",  # Violent rain showers
            85: "🌨️",  # Slight snow showers
            86: "❄️",  # Heavy snow showers
            95: "⛈️",  # Thunderstorm
            96: "⛈️",  # Thunderstorm with slight hail
            99: "⛈️",  # Thunderstorm with heavy hail
        }

    return icons.get(code, "❓")

def get_safety_alerts(weather_data):
    """
    Generate safety alerts based on weather conditions.

    Args:
        weather_data (dict): Weather data from the API

    Returns:
        list: List of safety alerts with severity and descriptions
    """
    alerts = []

    if not weather_data:
        return alerts

    current = weather_data.get('current', {})
    hourly = weather_data.get('hourly', {})
    daily = weather_data.get('daily', {})

    # Check for rain
    if current.get('precipitation', 0) > 0:
        alerts.append({
            'type': 'rain',
            'severity': 'high' if current.get('precipitation', 0) > 5 else 'medium',
            'title': 'Heavy Rain Alert' if current.get('precipitation', 0) > 5 else 'Rain Alert',
            'description': 'Heavy rainfall currently occurring. Be cautious on roads, especially in low-lying areas.'
                          if current.get('precipitation', 0) > 5
                          else 'Light rain currently occurring. Roads may be slippery.',
            'areas': ['Koramangala', 'Outer Ring Road', 'Marathahalli'],
            'safety_tips': ['Reduce speed', 'Maintain safe distance', 'Use headlights']
        })

    # Check for upcoming rain
    if hourly and 'precipitation_probability' in hourly:
        next_12_hours = hourly['precipitation_probability'][:12]
        if any(prob > 70 for prob in next_12_hours):
            alerts.append({
                'type': 'upcoming_rain',
                'severity': 'medium',
                'title': 'Rain Expected Soon',
                'description': 'High probability of rain in the next 12 hours. Plan your travel accordingly.',
                'areas': ['City-wide'],
                'safety_tips': ['Check weather before travel', 'Carry rain gear', 'Plan for delays']
            })

    # Check for high winds
    if current.get('wind_speed_10m', 0) > 20:
        alerts.append({
            'type': 'wind',
            'severity': 'medium',
            'title': 'High Wind Advisory',
            'description': 'Strong winds may affect vehicle stability, especially for two-wheelers and high-profile vehicles.',
            'areas': ['Elevated roads', 'Flyovers', 'Open areas'],
            'safety_tips': ['Maintain firm grip on steering', 'Be cautious when passing large vehicles']
        })

    # Check for poor visibility
    if 'visibility' in hourly and any(vis < 5000 for vis in hourly['visibility'][:12]):
        alerts.append({
            'type': 'visibility',
            'severity': 'high',
            'title': 'Poor Visibility Alert',
            'description': 'Reduced visibility expected in some areas. Drive with caution.',
            'areas': ['Highway sections', 'Low-lying areas'],
            'safety_tips': ['Use headlights', 'Reduce speed', 'Maintain safe distance']
        })

    # Check for extreme temperatures
    if daily and 'temperature_2m_max' in daily:
        max_temp = max(daily['temperature_2m_max'])
        if max_temp > 35:
            alerts.append({
                'type': 'heat',
                'severity': 'medium',
                'title': 'High Temperature Alert',
                'description': f'High temperatures expected (up to {max_temp}°C). Stay hydrated and avoid prolonged exposure.',
                'areas': ['City-wide'],
                'safety_tips': ['Stay hydrated', 'Avoid prolonged sun exposure', 'Check vehicle cooling systems']
            })

    return alerts
