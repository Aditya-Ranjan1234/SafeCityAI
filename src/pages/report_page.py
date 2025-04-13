"""
Report Issue page for the Bangalore Accident Prevention System.

This module contains the layout and functionality for the report page,
which allows users to submit safety issues and hazards.
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from src.components.map_components import create_location_selector_map, display_map
from src.utils.config import BANGALORE_LAT, BANGALORE_LON, COLORS

def render():
    """
    Render the report issue page.
    
    Returns:
        None: Renders the report page in the Streamlit app
    """
    st.markdown("<h1 class='main-header'>Report a Safety Issue</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
    <h2 class='sub-header'>Help Improve Road Safety</h2>
    <p>Report road hazards, infrastructure issues, or dangerous conditions to help make Bangalore safer for everyone.</p>
    <p>Your reports are valuable for identifying and addressing safety concerns in the city.</p>
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
                options=["Pothole", "Broken Traffic Signal", "Waterlogging", "Poor Visibility", 
                         "Dangerous Driving", "Missing Road Signs", "Broken Street Light", 
                         "Illegal Parking", "Other"]
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
        st.markdown("Click on the map to select the exact location of the issue.")
        
        # Create a location selector map
        location_map = create_location_selector_map()
        display_map(location_map, width=800, height=400)
        
        # Coordinates (would be set by map click in a real implementation)
        col1, col2 = st.columns(2)
        with col1:
            latitude = st.number_input("Latitude", value=BANGALORE_LAT, format="%.6f")
        with col2:
            longitude = st.number_input("Longitude", value=BANGALORE_LON, format="%.6f")
        
        # Additional details
        description = st.text_area(
            "Description",
            placeholder="Please provide details about the issue...",
            height=150
        )
        
        # When did you notice this issue?
        col1, col2 = st.columns(2)
        with col1:
            date_noticed = st.date_input("When did you notice this issue?", datetime.now().date())
        with col2:
            time_of_day = st.selectbox(
                "Time of Day",
                options=["Morning (6 AM - 12 PM)", "Afternoon (12 PM - 4 PM)", 
                         "Evening (4 PM - 8 PM)", "Night (8 PM - 6 AM)"]
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
            
            st.markdown(f"""
            <div class='card'>
                <h3>Report Details</h3>
                <table style="width:100%">
                    <tr>
                        <td style="width:30%; font-weight:bold;">Issue Title:</td>
                        <td>{issue_title}</td>
                    </tr>
                    <tr>
                        <td style="font-weight:bold;">Issue Type:</td>
                        <td>{issue_type}</td>
                    </tr>
                    <tr>
                        <td style="font-weight:bold;">Severity:</td>
                        <td>{severity}</td>
                    </tr>
                    <tr>
                        <td style="font-weight:bold;">Location:</td>
                        <td>{location}</td>
                    </tr>
                    <tr>
                        <td style="font-weight:bold;">Coordinates:</td>
                        <td>{latitude}, {longitude}</td>
                    </tr>
                    <tr>
                        <td style="font-weight:bold;">Date Noticed:</td>
                        <td>{date_noticed.strftime('%d %b %Y')}</td>
                    </tr>
                    <tr>
                        <td style="font-weight:bold;">Time of Day:</td>
                        <td>{time_of_day}</td>
                    </tr>
                    <tr>
                        <td style="font-weight:bold;">Description:</td>
                        <td>{description}</td>
                    </tr>
                    {f"<tr><td style='font-weight:bold;'>Reported By:</td><td>{name}</td></tr>" if name else ""}
                </table>
            </div>
            """, unsafe_allow_html=True)
            
            if photo:
                st.image(photo, caption="Uploaded Photo", width=400)
            
            # What happens next
            st.markdown("""
            <div class='card'>
                <h3>What Happens Next?</h3>
                <ol>
                    <li>Your report will be reviewed by city officials within 24-48 hours</li>
                    <li>The issue will be prioritized based on severity and impact</li>
                    <li>Appropriate departments will be notified for action</li>
                    <li>You can track the status of your report using the reference number</li>
                </ol>
                <p>Thank you for contributing to making Bangalore's roads safer!</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Please fill in all required fields (Title, Location, and Description).")
    
    # Display recent reports (static for demo)
    st.markdown("<h2 class='sub-header'>Recent Community Reports</h2>", unsafe_allow_html=True)
    
    # Create sample data for recent reports
    recent_reports = [
        {
            "title": "Large pothole on Outer Ring Road",
            "location": "Near Bellandur Lake, Outer Ring Road",
            "type": "Pothole",
            "severity": "High",
            "date": "May 10, 2023",
            "status": "Under Review"
        },
        {
            "title": "Traffic signal not working",
            "location": "Junction of MG Road and Brigade Road",
            "type": "Broken Traffic Signal",
            "severity": "High",
            "date": "May 12, 2023",
            "status": "Assigned"
        },
        {
            "title": "Waterlogging after rain",
            "location": "Sony World Junction, Koramangala",
            "type": "Waterlogging",
            "severity": "Medium",
            "date": "May 13, 2023",
            "status": "Under Review"
        }
    ]
    
    # Display recent reports
    for report in recent_reports:
        severity_color = {
            "High": COLORS["hazard_high"],
            "Medium": COLORS["hazard_medium"],
            "Low": COLORS["hazard_low"]
        }.get(report["severity"], COLORS["hazard_medium"])
        
        status_color = {
            "Under Review": "#FFC107",
            "Assigned": "#2196F3",
            "In Progress": "#FF9800",
            "Resolved": "#4CAF50",
            "Closed": "#9E9E9E"
        }.get(report["status"], "#9E9E9E")
        
        st.markdown(f"""
        <div class='card' style='border-left: 4px solid {severity_color};'>
            <div style='display: flex; justify-content: space-between; align-items: start;'>
                <h3>{report["title"]}</h3>
                <span style='background-color: {status_color}; color: white; padding: 3px 8px; border-radius: 4px; font-size: 0.8rem;'>{report["status"]}</span>
            </div>
            <p><strong>Location:</strong> {report["location"]}</p>
            <p><strong>Type:</strong> {report["type"]} | <strong>Severity:</strong> {report["severity"]} | <strong>Reported:</strong> {report["date"]}</p>
        </div>
        """, unsafe_allow_html=True)
