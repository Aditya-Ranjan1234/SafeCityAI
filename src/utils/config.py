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
    "background": "#1E1E2E",   # Dark background
    "card": "#2A2A3C",         # Dark card background
    "text": "#FFFFFF",         # White text for dark mode
    "text_secondary": "#B0B0B0", # Light gray secondary text
    "border": "#3A3A4C",       # Dark border color
    "hazard_high": "#FF5252",  # High hazard (red)
    "hazard_medium": "#FF9800", # Medium hazard (orange)
    "hazard_low": "#FFC107",   # Low hazard (yellow)
    "civic_blue": "#1976D2",   # Civic blue
    "sidebar_bg": "#121212",   # Sidebar background
    "sidebar_text": "#FFFFFF", # Sidebar text
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
            color: {COLORS["text"]};
            font-weight: 500;
        }}

        /* Card styling */
        .card {{
            border-radius: 8px;
            padding: 20px;
            background-color: {COLORS["card"]};
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
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
        .css-1d391kg, [data-testid="stSidebar"] {{
            background-color: {COLORS["sidebar_bg"]} !important;
            color: {COLORS["sidebar_text"]} !important;
        }}

        /* Fix sidebar text color */
        [data-testid="stSidebar"] .stRadio label,
        [data-testid="stSidebar"] .stRadio div,
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] li,
        [data-testid="stSidebar"] .stMarkdown,
        [data-testid="stSidebar"] .stMarkdown p {{
            color: {COLORS["sidebar_text"]} !important;
        }}

        /* Fix sidebar radio buttons */
        [data-testid="stSidebar"] .stRadio label span p {{
            color: {COLORS["sidebar_text"]} !important;
            font-weight: 400;
        }}

        /* Fix sidebar radio button selected state */
        [data-testid="stSidebar"] .stRadio input:checked + div {{
            border-color: {COLORS["primary"]} !important;
            background-color: rgba(30, 136, 229, 0.2) !important;
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
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            color: {COLORS["text"]};
            border: 1px solid {COLORS["border"]};
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

        /* Fix for streamlit widgets */
        .stSelectbox label, .stMultiSelect label, .stSlider label {{
            color: {COLORS["text"]} !important;
        }}

        .stSelectbox > div > div, .stMultiSelect > div > div {{
            background-color: {COLORS["card"]} !important;
            color: {COLORS["text"]} !important;
            border: 1px solid {COLORS["border"]} !important;
        }}

        /* Fix for streamlit tabs */
        .stTabs [data-baseweb="tab-list"] {{
            background-color: {COLORS["background"]} !important;
            border-bottom: 1px solid {COLORS["border"]} !important;
        }}

        .stTabs [data-baseweb="tab"] {{
            color: {COLORS["text"]} !important;
        }}

        .stTabs [aria-selected="true"] {{
            background-color: {COLORS["primary"]}30 !important;
            color: {COLORS["text"]} !important;
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
            background-color: {COLORS["card"]};
            border: 1px solid {COLORS["border"]};
        }}

        .dataframe th {{
            color: {COLORS["text"]};
            background-color: {COLORS["primary"]}50 !important;
            border-bottom: 1px solid {COLORS["border"]};
        }}

        .dataframe td {{
            color: {COLORS["text"]};
            border-bottom: 1px solid {COLORS["border"]}30;
        }}

        /* Fix for plotly charts */
        .js-plotly-plot .plotly {{
            background-color: {COLORS["card"]} !important;
        }}

        .js-plotly-plot .plotly .main-svg {{
            background-color: {COLORS["card"]} !important;
        }}

        /* Fix text colors in plotly charts */
        .js-plotly-plot .plotly .xtick text,
        .js-plotly-plot .plotly .ytick text,
        .js-plotly-plot .plotly .gtitle,
        .js-plotly-plot .plotly .ztick text,
        .js-plotly-plot .plotly .legend text,
        .js-plotly-plot .plotly .annotation-text,
        .js-plotly-plot .plotly .pie-label {{
            fill: {COLORS["text"]} !important;
            color: {COLORS["text"]} !important;
        }}

        .js-plotly-plot .plotly .xaxis .title,
        .js-plotly-plot .plotly .yaxis .title,
        .js-plotly-plot .plotly .zaxis .title,
        .js-plotly-plot .plotly .legend .title {{
            fill: {COLORS["text"]} !important;
            color: {COLORS["text"]} !important;
            font-weight: 600 !important;
        }}

        /* Fix for all charts and visualizations */
        .stPlotlyChart, .stDataFrame {{
            background-color: {COLORS["card"]};
            border-radius: 8px;
            padding: 10px;
            border: 1px solid {COLORS["border"]};
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

    # Set Plotly configuration to ensure charts are visible
    st.markdown("""
    <style>
        /* Ensure Plotly charts are visible */
        .js-plotly-plot, .plotly, .plot-container {
            background-color: #1E1E2E !important;
        }

        .js-plotly-plot .main-svg {
            background-color: #1E1E2E !important;
        }

        .js-plotly-plot .svg-container {
            background-color: #1E1E2E !important;
        }

        /* Make sure text in charts is visible */
        .js-plotly-plot text,
        .js-plotly-plot .xtick text,
        .js-plotly-plot .ytick text,
        .js-plotly-plot .xaxislayer-above text,
        .js-plotly-plot .yaxislayer-above text,
        .js-plotly-plot .zaxislayer-above text,
        .js-plotly-plot .overaxes-above text,
        .js-plotly-plot .xaxislayer text,
        .js-plotly-plot .yaxislayer text,
        .js-plotly-plot .zaxislayer text,
        .js-plotly-plot .layer text,
        .js-plotly-plot .legend text {
            fill: white !important;
            color: white !important;
            font-weight: bold !important;
            text-shadow: 0px 0px 2px rgba(0,0,0,0.8) !important;
        }

        /* Ensure axis lines are visible */
        .js-plotly-plot .xaxis .zerolinelayer path,
        .js-plotly-plot .yaxis .zerolinelayer path,
        .js-plotly-plot .xaxis path,
        .js-plotly-plot .yaxis path {
            stroke: white !important;
            stroke-width: 1.5px !important;
        }

        /* Fix for chart containers */
        .element-container iframe {
            border: 1px solid #3A3A4C !important;
            border-radius: 8px !important;
        }

        /* Ensure chart background is dark */
        .stPlotlyChart > div > div > div {
            background-color: #1E1E2E !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Set dark theme for Plotly charts
    st.markdown("""
    <script>
        const setPlotlyDarkMode = () => {
            const style = document.createElement('style');
            style.innerHTML = `
                .js-plotly-plot .plotly .main-svg {
                    background-color: #1E1E2E !important;
                }
                .js-plotly-plot .plotly .bg {
                    fill: #1E1E2E !important;
                }
                .js-plotly-plot .plotly .xtick text,
                .js-plotly-plot .plotly .ytick text,
                .js-plotly-plot .plotly .gtitle,
                .js-plotly-plot .plotly .ztick text,
                .js-plotly-plot .plotly .annotation-text,
                .js-plotly-plot .plotly .pie-label {
                    fill: #FFFFFF !important;
                    color: #FFFFFF !important;
                    font-weight: bold !important;
                    font-size: 14px !important;
                    text-shadow: 0px 0px 2px rgba(0,0,0,0.8) !important;
                }
                .js-plotly-plot .plotly .xaxis .title,
                .js-plotly-plot .plotly .yaxis .title,
                .js-plotly-plot .plotly .zaxis .title {
                    fill: #FFFFFF !important;
                    color: #FFFFFF !important;
                    font-weight: 600 !important;
                    font-size: 16px !important;
                }
                .js-plotly-plot .plotly .legend .bg {
                    fill: #1E1E2E !important;
                    stroke: #FFFFFF !important;
                    stroke-width: 1px !important;
                }
                .js-plotly-plot .plotly .legend text {
                    fill: #FFFFFF !important;
                    color: #FFFFFF !important;
                    font-weight: bold !important;
                }
                .js-plotly-plot .plotly path.xgrid,
                .js-plotly-plot .plotly path.ygrid {
                    stroke: rgba(255,255,255,0.2) !important;
                }
                /* Make sure all text elements are visible */
                .js-plotly-plot text {
                    fill: #FFFFFF !important;
                    color: #FFFFFF !important;
                }
                /* Ensure axis lines are visible */
                .js-plotly-plot .plotly .xaxis path.domain,
                .js-plotly-plot .plotly .yaxis path.domain {
                    stroke: #FFFFFF !important;
                    stroke-width: 2px !important;
                }
                /* Fix for chart containers */
                .element-container iframe {
                    border: 1px solid #FFFFFF !important;
                    border-radius: 8px !important;
                }
            `;
            document.head.appendChild(style);

            // Force redraw of all Plotly charts
            setTimeout(() => {
                const charts = document.querySelectorAll('.js-plotly-plot');
                charts.forEach(chart => {
                    if (chart && chart._fullLayout) {
                        window.Plotly.relayout(chart, {
                            'xaxis.color': '#FFFFFF',
                            'yaxis.color': '#FFFFFF',
                            'paper_bgcolor': '#1E1E2E',
                            'plot_bgcolor': '#1E1E2E',
                            'font.color': '#FFFFFF'
                        });
                    }
                });
            }, 1000);
        };

        if (window.parent.document.readyState === 'complete') {
            setPlotlyDarkMode();
        } else {
            window.parent.addEventListener('load', setPlotlyDarkMode);
        }

        // Also run after a short delay to catch dynamically loaded charts
        setTimeout(setPlotlyDarkMode, 2000);
    </script>
    """, unsafe_allow_html=True)

    load_css()
