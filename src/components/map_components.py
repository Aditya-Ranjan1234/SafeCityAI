"""
Map visualization components for the Bangalore Accident Prevention System.

This module contains functions for creating and customizing maps to display
accident hotspots and other geographic data.
"""

import folium
from folium.plugins import HeatMap, MarkerCluster
import streamlit as st
from streamlit_folium import folium_static
import pandas as pd
from src.utils.config import BANGALORE_LAT, BANGALORE_LON, COLORS

def create_accident_map(data, center_lat=BANGALORE_LAT, center_lon=BANGALORE_LON, zoom=12):
    """
    Create a folium map with accident hotspot markers.
    
    Args:
        data (pandas.DataFrame): DataFrame containing accident data
        center_lat (float): Latitude for map center
        center_lon (float): Longitude for map center
        zoom (int): Initial zoom level
    
    Returns:
        folium.Map: Map object with accident markers
    """
    # Create a folium map centered on Bangalore
    m = folium.Map(location=[center_lat, center_lon], zoom_start=zoom, tiles="OpenStreetMap")
    
    # Add markers for accident hotspots
    for _, row in data.iterrows():
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
            <p><b>Type:</b> {row.get('accident_type', 'N/A')}</p>
            <p><b>Peak Hours:</b> {row.get('peak_hours', 'N/A')}</p>
            <p><b>Road Condition:</b> {row.get('road_condition', 'N/A')}</p>
            <p>{row['description']}</p>
        </div>
        """
        
        # Add marker to map
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=folium.Popup(popup_content, max_width=300),
            icon=folium.Icon(color=color, icon=icon, prefix='fa')
        ).add_to(m)
    
    return m

def create_heatmap(data, center_lat=BANGALORE_LAT, center_lon=BANGALORE_LON, zoom=12):
    """
    Create a heatmap of accident hotspots.
    
    Args:
        data (pandas.DataFrame): DataFrame containing accident data
        center_lat (float): Latitude for map center
        center_lon (float): Longitude for map center
        zoom (int): Initial zoom level
    
    Returns:
        folium.Map: Map object with heatmap layer
    """
    # Create base map
    m = folium.Map(location=[center_lat, center_lon], zoom_start=zoom, tiles="OpenStreetMap")
    
    # Prepare data for heatmap
    heat_data = []
    for _, row in data.iterrows():
        # Weight by number of incidents
        weight = row['incidents']
        heat_data.append([row['latitude'], row['longitude'], weight])
    
    # Add heatmap layer
    HeatMap(heat_data, radius=15, blur=10).add_to(m)
    
    return m

def create_cluster_map(data, center_lat=BANGALORE_LAT, center_lon=BANGALORE_LON, zoom=12):
    """
    Create a map with clustered accident markers.
    
    Args:
        data (pandas.DataFrame): DataFrame containing accident data
        center_lat (float): Latitude for map center
        center_lon (float): Longitude for map center
        zoom (int): Initial zoom level
    
    Returns:
        folium.Map: Map object with clustered markers
    """
    # Create base map
    m = folium.Map(location=[center_lat, center_lon], zoom_start=zoom, tiles="OpenStreetMap")
    
    # Create marker cluster
    marker_cluster = MarkerCluster().add_to(m)
    
    # Add markers to cluster
    for _, row in data.iterrows():
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
            <p><b>Type:</b> {row.get('accident_type', 'N/A')}</p>
            <p>{row['description']}</p>
        </div>
        """
        
        # Add marker to cluster
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=folium.Popup(popup_content, max_width=300),
            icon=folium.Icon(color=color, icon=icon, prefix='fa')
        ).add_to(marker_cluster)
    
    return m

def display_map(map_object, width=1000, height=600):
    """
    Display a folium map in the Streamlit app.
    
    Args:
        map_object (folium.Map): Map object to display
        width (int): Width of the map in pixels
        height (int): Height of the map in pixels
    
    Returns:
        None: Displays the map in the Streamlit app
    """
    folium_static(map_object, width=width, height=height)

def create_location_selector_map(default_lat=BANGALORE_LAT, default_lon=BANGALORE_LON, zoom=12):
    """
    Create a map for selecting a location.
    
    Args:
        default_lat (float): Default latitude
        default_lon (float): Default longitude
        zoom (int): Initial zoom level
    
    Returns:
        folium.Map: Map object for location selection
    """
    m = folium.Map(location=[default_lat, default_lon], zoom_start=zoom, tiles="OpenStreetMap")
    
    # Add a marker for the default location
    folium.Marker(
        location=[default_lat, default_lon],
        popup="Click on the map to select a location",
        icon=folium.Icon(color="blue", icon="info-sign", prefix='fa'),
        draggable=True
    ).add_to(m)
    
    return m
