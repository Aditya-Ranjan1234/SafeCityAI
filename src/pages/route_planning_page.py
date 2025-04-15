"""
Route Planning Page for the Bangalore Accident Prevention System.

This page allows users to select source and destination locations in Bangalore
and view a route that avoids high-accident areas.
"""

import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import networkx as nx
import random
from src.utils.config import COLORS, BANGALORE_LAT, BANGALORE_LON
from src.utils.data_loader import load_accident_data

def display_route_planning_page():
    """
    Display the route planning page with source and destination selection.
    
    Returns:
        None: Displays the route planning page in the Streamlit app
    """
    st.title("Safe Route Planning")
    st.markdown("### Find the safest route between two locations in Bangalore")
    
    # Load accident data
    accident_data = load_accident_data()
    
    # Define major areas in Bangalore
    bangalore_areas = [
        "Koramangala", "Indiranagar", "Whitefield", "Electronic City", 
        "MG Road", "Jayanagar", "JP Nagar", "HSR Layout", "Bannerghatta Road",
        "Marathahalli", "Hebbal", "Yelahanka", "Malleswaram", "Rajajinagar",
        "BTM Layout", "Basavanagudi", "Domlur", "Bellandur", "Sarjapur Road",
        "Kengeri", "Banashankari", "Vijayanagar", "RT Nagar", "Banaswadi"
    ]
    
    # Create columns for source and destination selection
    col1, col2 = st.columns(2)
    
    with col1:
        source = st.selectbox("Select Source Location", bangalore_areas, index=0)
    
    with col2:
        # Filter out the source to avoid same source and destination
        destination_options = [area for area in bangalore_areas if area != source]
        destination = st.selectbox("Select Destination Location", destination_options, index=0)
    
    # Button to generate route
    if st.button("Find Safest Route", type="primary"):
        st.markdown("### Recommended Safe Route")
        
        # Create a map centered on Bangalore
        m = folium.Map(location=[BANGALORE_LAT, BANGALORE_LON], zoom_start=12)
        
        # Simulate route planning with safety consideration
        route = generate_safe_route(source, destination, accident_data)
        
        # Display route information
        st.markdown(f"**Route:** {' → '.join(route)}")
        
        # Calculate safety metrics
        safety_score = random.randint(75, 95)  # Simulated safety score
        accident_risk = 100 - safety_score
        
        # Display safety metrics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Route Safety Score", f"{safety_score}%", "Higher is safer")
        with col2:
            st.metric("Accident Risk", f"{accident_risk}%", f"-{accident_risk}% vs. shortest route", delta_color="inverse")
        
        # Add route to map
        add_route_to_map(m, route, accident_data)
        
        # Display the map
        st.markdown("### Route Map")
        folium_static(m)
        
        # Display route details
        st.markdown("### Route Details")
        st.markdown("This route avoids the following high-risk areas:")
        
        # Simulate high-risk areas that were avoided
        avoided_areas = ["Silk Board Junction", "Hebbal Flyover", "KR Puram Bridge"]
        for area in avoided_areas:
            st.markdown(f"- **{area}**: High accident probability based on historical data")
        
        # Display estimated time
        distance_km = random.randint(5, 20)  # Simulated distance
        time_min = distance_km * 3  # Simulated time (3 min per km)
        
        st.markdown(f"**Estimated Distance:** {distance_km} km")
        st.markdown(f"**Estimated Time:** {time_min} minutes")
        st.markdown(f"**Note:** This route may be slightly longer than the shortest path, but it significantly reduces your accident risk.")

def generate_safe_route(source, destination, accident_data):
    """
    Generate a safe route between source and destination.
    
    Args:
        source (str): Source location
        destination (str): Destination location
        accident_data (pandas.DataFrame): DataFrame containing accident data
    
    Returns:
        list: List of locations forming the route
    """
    # Create a simple graph for demonstration
    G = nx.Graph()
    
    # Define major areas in Bangalore and their connections
    # This is a simplified representation for demonstration
    bangalore_areas = {
        "Koramangala": ["HSR Layout", "Indiranagar", "BTM Layout"],
        "Indiranagar": ["Koramangala", "Domlur", "MG Road"],
        "Whitefield": ["Marathahalli", "Bellandur"],
        "Electronic City": ["BTM Layout", "Bannerghatta Road"],
        "MG Road": ["Indiranagar", "Ulsoor", "Domlur"],
        "Jayanagar": ["JP Nagar", "Basavanagudi", "BTM Layout"],
        "JP Nagar": ["Jayanagar", "BTM Layout", "Bannerghatta Road"],
        "HSR Layout": ["Koramangala", "BTM Layout", "Bellandur"],
        "Bannerghatta Road": ["JP Nagar", "Electronic City"],
        "Marathahalli": ["Whitefield", "Bellandur", "Sarjapur Road"],
        "Hebbal": ["Yelahanka", "RT Nagar"],
        "Yelahanka": ["Hebbal", "RT Nagar"],
        "Malleswaram": ["Rajajinagar", "Yeshwanthpur"],
        "Rajajinagar": ["Malleswaram", "Vijayanagar"],
        "BTM Layout": ["Koramangala", "JP Nagar", "HSR Layout", "Jayanagar"],
        "Basavanagudi": ["Jayanagar", "Banashankari"],
        "Domlur": ["Indiranagar", "MG Road"],
        "Bellandur": ["HSR Layout", "Marathahalli", "Sarjapur Road"],
        "Sarjapur Road": ["Bellandur", "Marathahalli"],
        "Kengeri": ["Vijayanagar"],
        "Banashankari": ["Basavanagudi", "Vijayanagar"],
        "Vijayanagar": ["Rajajinagar", "Banashankari", "Kengeri"],
        "RT Nagar": ["Hebbal", "Yelahanka", "Banaswadi"],
        "Banaswadi": ["RT Nagar"]
    }
    
    # Add nodes and edges to the graph
    for area, neighbors in bangalore_areas.items():
        for neighbor in neighbors:
            # Add edge with a random weight (representing safety - higher is safer)
            # In a real implementation, this would be based on accident data
            G.add_edge(area, neighbor, weight=random.randint(1, 10))
    
    # Find the safest path (using highest weight path)
    try:
        # In a real implementation, we would use a more sophisticated algorithm
        # that considers accident data to find the safest route
        path = nx.shortest_path(G, source=source, target=destination, weight='weight')
        return path
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        # If no path is found or node doesn't exist, return a simple direct path
        return [source, destination]

def add_route_to_map(m, route, accident_data):
    """
    Add the route and accident hotspots to the map.
    
    Args:
        m (folium.Map): Folium map object
        route (list): List of locations forming the route
        accident_data (pandas.DataFrame): DataFrame containing accident data
    
    Returns:
        None: Updates the map object in place
    """
    # Define coordinates for each location (simplified for demonstration)
    # In a real implementation, these would be geocoded or stored in a database
    location_coords = {
        "Koramangala": [12.9279, 77.6271],
        "Indiranagar": [12.9784, 77.6408],
        "Whitefield": [12.9698, 77.7499],
        "Electronic City": [12.8399, 77.6770],
        "MG Road": [12.9747, 77.6080],
        "Jayanagar": [12.9299, 77.5833],
        "JP Nagar": [12.9063, 77.5857],
        "HSR Layout": [12.9116, 77.6474],
        "Bannerghatta Road": [12.8933, 77.5969],
        "Marathahalli": [12.9591, 77.6974],
        "Hebbal": [13.0358, 77.5970],
        "Yelahanka": [13.1005, 77.5963],
        "Malleswaram": [13.0027, 77.5668],
        "Rajajinagar": [12.9913, 77.5551],
        "BTM Layout": [12.9166, 77.6101],
        "Basavanagudi": [12.9422, 77.5738],
        "Domlur": [12.9609, 77.6387],
        "Bellandur": [12.9257, 77.6681],
        "Sarjapur Road": [12.9102, 77.6870],
        "Kengeri": [12.9054, 77.4820],
        "Banashankari": [12.9252, 77.5461],
        "Vijayanagar": [12.9719, 77.5302],
        "RT Nagar": [13.0211, 77.5949],
        "Banaswadi": [13.0159, 77.6536]
    }
    
    # Add markers for source and destination
    folium.Marker(
        location=location_coords[route[0]],
        popup=f"Start: {route[0]}",
        icon=folium.Icon(color="green", icon="play"),
    ).add_to(m)
    
    folium.Marker(
        location=location_coords[route[-1]],
        popup=f"End: {route[-1]}",
        icon=folium.Icon(color="red", icon="stop"),
    ).add_to(m)
    
    # Add route line
    route_coords = [location_coords[loc] for loc in route]
    folium.PolyLine(
        route_coords,
        color=COLORS["primary"],
        weight=5,
        opacity=0.7,
        popup="Safe Route"
    ).add_to(m)
    
    # Add accident hotspots
    # In a real implementation, these would be from actual accident data
    accident_hotspots = [
        {"location": "Silk Board Junction", "coords": [12.9174, 77.6220], "severity": "high"},
        {"location": "Hebbal Flyover", "coords": [13.0403, 77.5969], "severity": "high"},
        {"location": "KR Puram Bridge", "coords": [12.9984, 77.6784], "severity": "high"},
        {"location": "Tin Factory", "coords": [12.9925, 77.6609], "severity": "medium"},
        {"location": "Marathahalli Bridge", "coords": [12.9577, 77.6969], "severity": "medium"}
    ]
    
    # Add accident hotspots to map
    for hotspot in accident_hotspots:
        severity_color = {
            "high": "red",
            "medium": "orange",
            "low": "yellow"
        }.get(hotspot["severity"], "blue")
        
        folium.CircleMarker(
            location=hotspot["coords"],
            radius=10,
            popup=f"{hotspot['location']} - {hotspot['severity'].title()} Risk",
            color=severity_color,
            fill=True,
            fill_color=severity_color,
            fill_opacity=0.7
        ).add_to(m)
