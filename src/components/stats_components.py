"""
Statistical visualization components for the Bangalore Accident Prevention System.

This module contains functions for creating charts, graphs, and other visualizations
of accident data and statistics.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.utils.config import COLORS

def display_accident_stats(data):
    """
    Display accident statistics visualizations.

    Args:
        data (pandas.DataFrame): DataFrame containing accident data

    Returns:
        None: Displays statistics in the Streamlit app
    """
    if data.empty:
        st.error("No accident data available for statistics")
        return

    # Display text-based statistics instead of charts
    st.markdown("<h3>Accident Statistics</h3>", unsafe_allow_html=True)

    # Create columns for key metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        # Total incidents
        total_incidents = data['incidents'].sum()
        st.metric("Total Incidents", f"{total_incidents:,}")

    with col2:
        # High severity incidents
        high_severity = data[data['severity'] == 'high']['incidents'].sum()
        high_pct = (high_severity / total_incidents) * 100 if total_incidents > 0 else 0
        st.metric("High Severity", f"{high_severity:,}", f"{high_pct:.1f}%")

    with col3:
        # Most common accident type
        if 'accident_type' in data.columns:
            accident_types = data.groupby('accident_type')['incidents'].sum().reset_index()
            most_common_type = accident_types.loc[accident_types['incidents'].idxmax(), 'accident_type']
            st.metric("Most Common Type", most_common_type)
        else:
            st.metric("Most Common Type", "N/A")

    # Display top accident locations in a table
    st.markdown("<h4>Top 5 Accident Hotspots</h4>", unsafe_allow_html=True)
    top_locations = data.sort_values('incidents', ascending=False).head(5)

    # Format the table data
    table_data = {
        "Location": top_locations['location'],
        "Incidents": top_locations['incidents'],
        "Severity": top_locations['severity'].str.capitalize()
    }

    # Display as a table
    st.table(pd.DataFrame(table_data))

    # Display time-based statistics
    st.markdown("<h4>Time-based Statistics</h4>", unsafe_allow_html=True)

    # Create columns for time-based metrics
    col1, col2 = st.columns(2)

    with col1:
        # Peak hours data
        if 'peak_hours' in data.columns:
            peak_hours = data.groupby('peak_hours')['incidents'].sum().reset_index()
            peak_time = peak_hours.loc[peak_hours['incidents'].idxmax(), 'peak_hours']
            peak_incidents = peak_hours.loc[peak_hours['incidents'].idxmax(), 'incidents']

            st.markdown(f"**Peak Time:** {peak_time}")
            st.markdown(f"**Incidents during peak time:** {peak_incidents:,}")
        else:
            st.markdown("**Peak Time:** N/A")
            st.markdown("**Incidents during peak time:** N/A")

    with col2:
        # Weather-related incidents
        weather_related = data[data['weather_related'] == True]['incidents'].sum() if 'weather_related' in data.columns else 0
        weather_pct = (weather_related / total_incidents) * 100 if total_incidents > 0 else 0

        st.markdown(f"**Weather-related incidents:** {weather_related:,}")
        st.markdown(f"**Percentage of total:** {weather_pct:.1f}%")

    # Display accident types in a table if available
    if 'accident_type' in data.columns:
        st.markdown("<h4>Incidents by Accident Type</h4>", unsafe_allow_html=True)
        accident_type_counts = data.groupby('accident_type')['incidents'].sum().reset_index()
        accident_type_counts = accident_type_counts.sort_values('incidents', ascending=False)

        # Calculate percentages
        accident_type_counts['percentage'] = (accident_type_counts['incidents'] / total_incidents * 100).round(1)

        # Format the table data
        accident_table = {
            "Accident Type": accident_type_counts['accident_type'],
            "Incidents": accident_type_counts['incidents'],
            "Percentage": accident_type_counts['percentage'].apply(lambda x: f"{x}%")
        }

        # Display as a table
        st.table(pd.DataFrame(accident_table))

def display_key_metrics(data):
    """
    Display key metrics about accident data.

    Args:
        data (pandas.DataFrame): DataFrame containing accident data

    Returns:
        None: Displays metrics in the Streamlit app
    """
    if data.empty:
        return

    # Calculate metrics
    total_incidents = data['incidents'].sum()
    high_severity = data[data['severity'] == 'high']['incidents'].sum()
    high_severity_percentage = (high_severity / total_incidents) * 100 if total_incidents > 0 else 0

    # Get top hotspot
    top_hotspot = data.loc[data['incidents'].idxmax()]

    # Display metrics in columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class='metric-container'>
            <h3>Total Accident Hotspots</h3>
            <div class='metric-value'>{len(data)}</div>
            <div class='metric-label'>Identified high-risk areas</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='metric-container'>
            <h3>High Severity Incidents</h3>
            <div class='metric-value' style='color: {COLORS["hazard_high"]};'>{high_severity_percentage:.1f}%</div>
            <div class='metric-label'>Of total reported incidents</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class='metric-container'>
            <h3>Top Accident Hotspot</h3>
            <div class='metric-value'>{top_hotspot['location']}</div>
            <div class='metric-label'>{top_hotspot['incidents']} incidents reported</div>
        </div>
        """, unsafe_allow_html=True)

def display_data_table(data, columns=None):
    """
    Display a formatted data table.

    Args:
        data (pandas.DataFrame): DataFrame to display
        columns (list): List of columns to include (None for all)

    Returns:
        None: Displays table in the Streamlit app
    """
    if data.empty:
        st.warning("No data available to display")
        return

    # Filter columns if specified
    if columns:
        display_data = data[columns].copy()
    else:
        display_data = data.copy()

    # Format column names for display
    display_data.columns = [col.replace('_', ' ').title() for col in display_data.columns]

    # Display the table
    st.dataframe(
        display_data,
        use_container_width=True,
        hide_index=True
    )
