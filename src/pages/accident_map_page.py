"""
Accident Map page for the Bangalore Accident Prevention System.

This module contains the layout and functionality for the accident map page,
which displays accident hotspots and related statistics.
"""

import streamlit as st
import pandas as pd
from src.utils.data_loader import load_accident_data
from src.components.map_components import create_accident_map, create_heatmap, create_cluster_map, display_map
from src.components.stats_components import display_accident_stats, display_data_table

def render():
    """
    Render the accident map page.
    
    Returns:
        None: Renders the accident map page in the Streamlit app
    """
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
    
    # Additional filters if we have the columns
    accident_type_filter = None
    if 'accident_type' in accident_data.columns:
        accident_types = accident_data['accident_type'].unique().tolist()
        accident_type_filter = st.sidebar.multiselect(
            "Accident Type",
            options=accident_types,
            default=accident_types
        )
    
    peak_hours_filter = None
    if 'peak_hours' in accident_data.columns:
        peak_hours = accident_data['peak_hours'].unique().tolist()
        peak_hours_filter = st.sidebar.multiselect(
            "Time of Day",
            options=peak_hours,
            default=peak_hours
        )
    
    # Map visualization options
    st.sidebar.markdown("### Map Options")
    map_type = st.sidebar.radio(
        "Map Type",
        options=["Markers", "Heatmap", "Clustered"],
        index=0
    )
    
    # Filter data
    filtered_data = accident_data[
        (accident_data['severity'].isin(severity_filter)) &
        (accident_data['incidents'] >= min_incidents)
    ]
    
    if accident_type_filter:
        filtered_data = filtered_data[filtered_data['accident_type'].isin(accident_type_filter)]
    
    if peak_hours_filter:
        filtered_data = filtered_data[filtered_data['peak_hours'].isin(peak_hours_filter)]
    
    # Create map
    st.markdown("<h2 class='sub-header'>Bangalore Accident Prone Areas</h2>", unsafe_allow_html=True)
    
    if filtered_data.empty:
        st.warning("No data matches the selected filters. Please adjust your filter criteria.")
    else:
        # Create the appropriate map based on selection
        if map_type == "Markers":
            m = create_accident_map(filtered_data)
        elif map_type == "Heatmap":
            m = create_heatmap(filtered_data)
        else:  # Clustered
            m = create_cluster_map(filtered_data)
        
        # Display the map
        display_map(m, width=1000, height=600)
        
        # Display data table
        st.markdown("<h2 class='sub-header'>Accident Hotspot Details</h2>", unsafe_allow_html=True)
        
        # Determine which columns to display
        display_columns = ['location', 'severity', 'incidents', 'description']
        if 'accident_type' in filtered_data.columns:
            display_columns.insert(3, 'accident_type')
        if 'peak_hours' in filtered_data.columns:
            display_columns.insert(4, 'peak_hours')
        if 'road_condition' in filtered_data.columns:
            display_columns.insert(5, 'road_condition')
        
        display_data_table(filtered_data, display_columns)
        
        # Accident statistics
        st.markdown("<h2 class='sub-header'>Accident Statistics</h2>", unsafe_allow_html=True)
        display_accident_stats(filtered_data)
        
        # Safety recommendations based on data
        st.markdown("<h2 class='sub-header'>Safety Recommendations</h2>", unsafe_allow_html=True)
        
        # Count accident types if available
        if 'accident_type' in filtered_data.columns:
            top_accident_type = filtered_data.groupby('accident_type')['incidents'].sum().idxmax()
            
            if top_accident_type == "Vehicle Collision":
                st.markdown("""
                <div class='card'>
                    <h3>Vehicle Collision Prevention</h3>
                    <ul>
                        <li>Maintain safe distance from vehicles ahead</li>
                        <li>Follow lane discipline and traffic signals</li>
                        <li>Avoid distractions like mobile phones while driving</li>
                        <li>Use turn signals when changing lanes</li>
                        <li>Be extra cautious at intersections</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            elif top_accident_type == "Pedestrian Accident":
                st.markdown("""
                <div class='card'>
                    <h3>Pedestrian Safety</h3>
                    <ul>
                        <li>Always use pedestrian crossings and footpaths</li>
                        <li>Make eye contact with drivers before crossing</li>
                        <li>Avoid using mobile phones while crossing roads</li>
                        <li>Wear bright/reflective clothing at night</li>
                        <li>Drivers should slow down in areas with high pedestrian activity</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            elif top_accident_type == "Two-wheeler Accident":
                st.markdown("""
                <div class='card'>
                    <h3>Two-wheeler Safety</h3>
                    <ul>
                        <li>Always wear a helmet and protective gear</li>
                        <li>Avoid lane splitting and weaving through traffic</li>
                        <li>Be extra visible with bright clothing and proper lights</li>
                        <li>Maintain safe distance from larger vehicles</li>
                        <li>Be cautious on wet roads and near potholes</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class='card'>
                <h3>General Road Safety</h3>
                <ul>
                    <li>Follow traffic rules and signals</li>
                    <li>Maintain safe speed according to road conditions</li>
                    <li>Avoid distractions while driving</li>
                    <li>Be extra cautious during peak hours and in high-risk areas</li>
                    <li>Plan your route to avoid accident-prone areas when possible</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
