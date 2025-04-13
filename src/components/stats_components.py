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
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Create a bar chart of incidents by location (top 10)
        top_locations = data.sort_values('incidents', ascending=False).head(10)
        fig = px.bar(
            top_locations,
            x='location',
            y='incidents',
            color='severity',
            color_discrete_map={
                'high': COLORS["hazard_high"], 
                'medium': COLORS["hazard_medium"], 
                'low': COLORS["hazard_low"]
            },
            title='Top 10 Accident Hotspots',
            labels={'incidents': 'Number of Incidents', 'location': 'Location'}
        )
        fig.update_layout(
            xaxis_tickangle=-45,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.1)'),
            margin=dict(l=20, r=20, t=40, b=80),
            legend_title_text='Severity'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Create a pie chart of incidents by severity
        severity_counts = data.groupby('severity')['incidents'].sum().reset_index()
        fig = px.pie(
            severity_counts,
            values='incidents',
            names='severity',
            color='severity',
            color_discrete_map={
                'high': COLORS["hazard_high"], 
                'medium': COLORS["hazard_medium"], 
                'low': COLORS["hazard_low"]
            },
            title='Incidents by Severity Level'
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=40, b=20),
            legend_title_text='Severity'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Additional statistics if we have accident_type in the data
    if 'accident_type' in data.columns:
        # Create a bar chart of incidents by accident type
        accident_type_counts = data.groupby('accident_type')['incidents'].sum().reset_index()
        fig = px.bar(
            accident_type_counts,
            x='accident_type',
            y='incidents',
            color='accident_type',
            title='Incidents by Accident Type',
            labels={'incidents': 'Number of Incidents', 'accident_type': 'Accident Type'}
        )
        fig.update_layout(
            xaxis_tickangle=0,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.1)'),
            margin=dict(l=20, r=20, t=40, b=20),
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Additional statistics if we have peak_hours in the data
    if 'peak_hours' in data.columns:
        # Create a bar chart of incidents by peak hours
        peak_hours_counts = data.groupby('peak_hours')['incidents'].sum().reset_index()
        fig = px.bar(
            peak_hours_counts,
            x='peak_hours',
            y='incidents',
            color='peak_hours',
            title='Incidents by Time of Day',
            labels={'incidents': 'Number of Incidents', 'peak_hours': 'Time of Day'}
        )
        fig.update_layout(
            xaxis_tickangle=0,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.1)'),
            margin=dict(l=20, r=20, t=40, b=20),
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

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
