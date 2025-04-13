"""
Configuration settings for the Bangalore Accident Prevention System.

This module contains constants, theme settings, and configuration parameters
used throughout the application.
"""

import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# API Keys
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN", "")

# Bangalore coordinates (default center point)
BANGALORE_LAT = 12.9716
BANGALORE_LON = 77.5946

# Application theme colors (based on the TSX website color scheme)
COLORS = {
    "primary": "#1E88E5",      # Primary blue
    "secondary": "#424242",    # Dark gray
    "accent": "#FF5252",       # Red accent
    "warning": "#FF9800",      # Orange warning
    "success": "#4CAF50",      # Green success
    "info": "#2196F3",         # Info blue
    "background": "#F9F9F9",   # Light background
    "card": "#FFFFFF",         # Card background
    "text": "#212121",         # Main text
    "text_secondary": "#757575", # Secondary text
    "border": "#E0E0E0",       # Border color
    "hazard_high": "#FF5252",  # High hazard (red)
    "hazard_medium": "#FF9800", # Medium hazard (orange)
    "hazard_low": "#FFC107",   # Low hazard (yellow)
    "civic_blue": "#1976D2",   # Civic blue
}

# Custom CSS for styling the application
def load_css():
    """
    Load custom CSS styles for the application.

    Returns:
        None: Injects CSS directly into the Streamlit app
    """
    st.markdown(f"""
    <style>
        /* Main headers */
        .main-header {{
            font-size: 2.5rem;
            color: {COLORS["primary"]};
            font-weight: 700;
        }}

        /* Sub headers */
        .sub-header {{
            font-size: 1.5rem;
            color: {COLORS["secondary"]};
            font-weight: 500;
        }}

        /* Card styling */
        .card {{
            border-radius: 8px;
            padding: 20px;
            background-color: {COLORS["card"]};
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            border: 1px solid {COLORS["border"]};
            color: {COLORS["text"]};
        }}

        /* Warning text */
        .warning {{
            color: {COLORS["hazard_high"]};
            font-weight: 500;
        }}

        /* Info text */
        .info {{
            color: {COLORS["success"]};
            font-weight: 500;
        }}

        /* Streamlit overrides */
        .stApp {{
            background-color: {COLORS["background"]};
            color: {COLORS["text"]};
        }}

        /* Sidebar styling */
        .css-1d391kg {{
            background-color: {COLORS["card"]};
        }}

        /* Button styling */
        .stButton>button {{
            background-color: {COLORS["primary"]};
            color: white;
            border-radius: 4px;
            border: none;
            padding: 0.5rem 1rem;
            font-weight: 500;
        }}

        .stButton>button:hover {{
            background-color: {COLORS["civic_blue"]};
        }}

        /* Metric styling */
        .metric-container {{
            background-color: {COLORS["card"]};
            border-radius: 8px;
            padding: 15px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            color: {COLORS["text"]};
        }}

        .metric-value {{
            font-size: 2rem;
            font-weight: 700;
            margin: 10px 0;
            color: {COLORS["primary"]};
        }}

        .metric-label {{
            font-size: 1rem;
            color: {COLORS["text_secondary"]};
        }}

        /* Alert box styling */
        .alert-box {{
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 15px;
            color: {COLORS["text"]};
        }}

        .alert-box.high {{
            background-color: {COLORS["hazard_high"]}20;
            border-left: 4px solid {COLORS["hazard_high"]};
        }}

        .alert-box.medium {{
            background-color: {COLORS["hazard_medium"]}20;
            border-left: 4px solid {COLORS["hazard_medium"]};
        }}

        .alert-box.low {{
            background-color: {COLORS["hazard_low"]}20;
            border-left: 4px solid {COLORS["hazard_low"]};
        }}

        .alert-box.info {{
            background-color: {COLORS["info"]}20;
            border-left: 4px solid {COLORS["info"]};
        }}

        /* Language selector styling */
        .language-selector {{
            position: absolute;
            top: 0.5rem;
            right: 1rem;
            z-index: 1000;
            display: flex;
            gap: 0.5rem;
        }}

        .language-button {{
            background-color: {COLORS["card"]};
            color: {COLORS["text"]};
            border: 1px solid {COLORS["border"]};
            border-radius: 4px;
            padding: 0.25rem 0.5rem;
            font-size: 0.8rem;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .language-button:hover {{
            background-color: {COLORS["primary"]};
            color: white;
        }}

        .language-button.active {{
            background-color: {COLORS["primary"]};
            color: white;
        }}

        /* Emergency services button */
        .emergency-button {{
            background-color: {COLORS["hazard_high"]};
            color: white;
            border: none;
            border-radius: 4px;
            padding: 0.5rem 1rem;
            font-weight: 500;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            margin-bottom: 1rem;
            width: 100%;
            transition: all 0.2s;
        }}

        .emergency-button:hover {{
            background-color: #d32f2f;
        }}

        /* Risk prediction map */
        .risk-map-container {{
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 20px;
        }}

        .risk-legend {{
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-top: 0.5rem;
            flex-wrap: wrap;
        }}

        .risk-legend-item {{
            display: flex;
            align-items: center;
            gap: 0.25rem;
        }}

        .risk-legend-color {{
            width: 1rem;
            height: 1rem;
            border-radius: 2px;
        }}

        /* Fix for text in all cards and containers */
        p, h1, h2, h3, h4, h5, h6, li, span, div {{
            color: inherit;
        }}

        /* Fix for dataframe text */
        .dataframe {{
            color: {COLORS["text"]};
        }}

        .dataframe th {{
            color: {COLORS["text"]};
            background-color: {COLORS["primary"]}20;
        }}

        .dataframe td {{
            color: {COLORS["text"]};
        }}
    </style>
    """, unsafe_allow_html=True)

# Page configuration
def setup_page():
    """
    Configure the Streamlit page settings.

    Returns:
        None: Sets up the page configuration
    """
    st.set_page_config(
        page_title="Bangalore Accident Prevention System",
        page_icon="🚨",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    load_css()
