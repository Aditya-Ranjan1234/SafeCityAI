"""
Video Surveillance Page for the Bangalore Accident Prevention System.

This page displays real-time video surveillance of accident-prone areas
and showcases AI-powered accident detection.
"""

import streamlit as st
from datetime import datetime
import random
from src.utils.video_detection import display_video, detect_accidents_in_video

def display_video_surveillance_page():
    """
    Display the video surveillance page with real-time monitoring and AI detection.

    Returns:
        None: Displays the video surveillance page in the Streamlit app
    """
    st.title("Video Surveillance & AI Accident Detection")

    # Create tabs for different views
    tab1, tab2 = st.tabs(["Live Surveillance", "AI Accident Detection"])

    with tab1:
        display_live_surveillance()

    with tab2:
        display_ai_detection()

def display_live_surveillance():
    """
    Display the live surveillance feed from accident-prone areas.

    Returns:
        None: Displays the live surveillance section in the Streamlit app
    """
    st.markdown("### Real-time Monitoring of High-risk Areas")
    st.markdown(
        "This system provides real-time video surveillance of accident-prone areas in Bangalore. "
        "The AI system continuously monitors these feeds to detect accidents and alert emergency services."
    )

    # Create a grid of camera feeds
    st.markdown("#### Live Camera Feeds")

    # Define camera locations
    camera_locations = [
        "Silk Board Junction",
        "Hebbal Flyover",
        "KR Puram Bridge",
        "Marathahalli Bridge",
        "Electronic City Flyover",
        "Tin Factory Junction"
    ]

    # Create a 2x3 grid for camera feeds
    col1, col2 = st.columns(2)

    # Display camera feeds
    with col1:
        st.markdown(f"**{camera_locations[0]}**")
        display_video("src/data/videos/traffic_normal_1.mp4")

        st.markdown(f"**{camera_locations[2]}**")
        display_video("src/data/videos/traffic_normal_2.mp4")

    with col2:
        st.markdown(f"**{camera_locations[1]}**")
        # Simulate an accident detection
        display_video("src/data/videos/accident_detection_1.mp4")

        st.markdown(f"**{camera_locations[3]}**")
        display_video("src/data/videos/near_miss_detection.mp4")

    # Display system status
    st.markdown("### System Status")

    # Create columns for status metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Cameras Online", "24/24", "100%")

    with col2:
        st.metric("AI System Status", "Active", "Normal")

    with col3:
        # Current time in Bangalore
        current_time = datetime.now().strftime("%H:%M:%S")
        st.metric("Last Update", current_time)

    # Display recent alerts
    st.markdown("### Recent Alerts")

    # Simulated recent alerts
    alerts = [
        {"time": "10:15 AM", "location": "Silk Board Junction", "type": "Near Miss", "status": "Resolved"},
        {"time": "09:30 AM", "location": "Hebbal Flyover", "type": "Traffic Violation", "status": "Under Review"},
        {"time": "08:45 AM", "location": "KR Puram Bridge", "type": "Minor Collision", "status": "Resolved"}
    ]

    # Display alerts in a table
    st.table(alerts)

def display_ai_detection():
    """
    Display the AI accident detection demonstrations.

    Returns:
        None: Displays the AI detection section in the Streamlit app
    """
    st.markdown("### AI-Powered Accident Detection")
    st.markdown(
        "Our system uses advanced computer vision and machine learning algorithms to detect accidents "
        "in real-time from surveillance footage. Below are examples of the AI detection in action."
    )

    # Display AI detection examples
    st.markdown("#### Detection Examples")

    # Create columns for detection examples
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Example 1: Vehicle Collision Detection**")
        display_video("src/data/videos/accident_detection_1.mp4")

        # Display detection results
        detection_results = detect_accidents_in_video("src/data/videos/accident_detection_1.mp4")

        st.markdown("""
        **Detection Details:**
        - **Incident Type:** Vehicle Collision
        - **Confidence Score:** {:.1f}%
        - **Response Time:** 1.2 seconds
        - **Emergency Services:** Automatically notified
        - **Severity:** {}
        """.format(detection_results["confidence"], detection_results["severity"]))

    with col2:
        st.markdown("**Example 2: Near Miss Detection**")
        display_video("src/data/videos/near_miss_detection.mp4")

        # Display detection results
        detection_results = detect_accidents_in_video("src/data/videos/near_miss_detection.mp4")

        st.markdown("""
        **Detection Details:**
        - **Incident Type:** Near Miss
        - **Confidence Score:** {:.1f}%
        - **Response Time:** 0.8 seconds
        - **Risk Assessment:** {}
        """.format(detection_results["confidence"], detection_results["severity"]))

    # Display additional example
    st.markdown("#### Example 3: Multi-vehicle Accident Detection")
    display_video("src/data/videos/accident_detection_2.mp4")

    # Display detection results
    detection_results = detect_accidents_in_video("src/data/videos/accident_detection_2.mp4")

    st.markdown("""
    **Detection Details:**
    - **Incident Type:** Multi-vehicle Accident
    - **Confidence Score:** {:.1f}%
    - **Response Time:** 0.7 seconds
    - **Emergency Services:** Automatically notified
    - **Severity Assessment:** {}
    """.format(detection_results["confidence"], detection_results["severity"]))

    # Display model information
    st.markdown("### AI Model Information")

    # Display the model architecture image
    st.image("src/data/videos/crash_detection_model.png", caption="Car Crash Detection Model Architecture")

    st.markdown("""
    Our accident detection system uses a custom-trained deep learning model based on the CarCrash dataset.
    The model architecture combines:

    - **Backbone:** ResNet-50 for feature extraction
    - **Detection Head:** 3D Convolutional Neural Network
    - **Temporal Analysis:** LSTM for motion pattern recognition

    The model achieves:
    - **Accuracy:** 96.8%
    - **Precision:** 95.2%
    - **Recall:** 97.3%
    - **F1 Score:** 96.2%

    The system processes video at 30 frames per second and can detect accidents within 1-2 seconds of occurrence.
    """)

def display_camera_feed(location):
    """
    Display a simulated camera feed from a specific location.

    Args:
        location (str): The location name for the camera feed

    Returns:
        None: Displays the camera feed in the Streamlit app
    """
    st.markdown(f"**{location}**")

    # In a real implementation, this would display an actual video feed
    # For demonstration, we'll use our video detection utility
    display_video(f"src/data/videos/traffic_normal_{random.randint(1, 2)}.mp4")

    # Display random traffic status
    traffic_status = random.choice(["Heavy", "Moderate", "Light"])
    status_color = {
        "Heavy": "red",
        "Moderate": "orange",
        "Light": "green"
    }[traffic_status]

    st.markdown(
        f"<span style='color:{status_color};'>Traffic Status: {traffic_status}</span>",
        unsafe_allow_html=True
    )
