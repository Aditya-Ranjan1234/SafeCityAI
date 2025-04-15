"""
Video detection utilities for the Bangalore Accident Prevention System.

This module contains functions for processing video feeds and detecting accidents.
"""

import streamlit as st
import cv2
import numpy as np
import base64
from pathlib import Path
import os
import time
import random
from datetime import datetime

def get_base64_video(video_path):
    """
    Convert a video file to base64 encoding.
    
    Args:
        video_path (str): Path to the video file
    
    Returns:
        str: Base64 encoded video
    """
    with open(video_path, "rb") as video_file:
        return base64.b64encode(video_file.read()).decode()

def display_video(video_path, width=None):
    """
    Display a video in Streamlit.
    
    Args:
        video_path (str): Path to the video file
        width (int, optional): Width of the video display
    
    Returns:
        None: Displays the video in the Streamlit app
    """
    # For demonstration, we'll use a placeholder image
    # In a real implementation, this would display an actual video
    st.image(
        "src/data/videos/crash_detection_model.png",
        caption=f"Video feed from {os.path.basename(video_path)}",
        width=width
    )
    
    # Add a progress bar to simulate video playback
    progress_bar = st.progress(0)
    for i in range(100):
        # Update progress bar
        progress_bar.progress(i + 1)
        time.sleep(0.05)
    
    # Display detection result
    if "crash" in video_path.lower() or "accident" in video_path.lower():
        st.error("🚨 ACCIDENT DETECTED! Emergency services notified.")
        
        # Display detection details
        detection_time = datetime.now().strftime("%H:%M:%S")
        confidence = random.uniform(90.0, 99.9)
        
        st.markdown(f"""
        **Detection Details:**
        - **Time:** {detection_time}
        - **Confidence:** {confidence:.1f}%
        - **Location:** Silk Board Junction
        - **Severity:** Medium
        - **Response:** Ambulance dispatched
        """)
    else:
        st.success("✅ No incidents detected")

def get_video_files():
    """
    Get a list of available video files.
    
    Returns:
        list: List of video file paths
    """
    # In a real implementation, this would return actual video files
    # For demonstration, we'll return simulated file paths
    return [
        "src/data/videos/traffic_normal_1.mp4",
        "src/data/videos/traffic_normal_2.mp4",
        "src/data/videos/accident_detection_1.mp4",
        "src/data/videos/accident_detection_2.mp4",
        "src/data/videos/near_miss_detection.mp4"
    ]

def detect_accidents_in_video(video_path):
    """
    Process a video to detect accidents.
    
    Args:
        video_path (str): Path to the video file
    
    Returns:
        dict: Detection results
    """
    # In a real implementation, this would use a trained model to detect accidents
    # For demonstration, we'll return simulated results
    
    # Simulate detection based on filename
    if "accident" in video_path.lower() or "crash" in video_path.lower():
        return {
            "detected": True,
            "confidence": random.uniform(90.0, 99.9),
            "frame_number": random.randint(50, 150),
            "timestamp": f"{random.randint(0, 2)}:{random.randint(10, 59)}:{random.randint(10, 59)}",
            "severity": random.choice(["Low", "Medium", "High"])
        }
    elif "near_miss" in video_path.lower():
        return {
            "detected": True,
            "confidence": random.uniform(70.0, 89.9),
            "frame_number": random.randint(50, 150),
            "timestamp": f"{random.randint(0, 2)}:{random.randint(10, 59)}:{random.randint(10, 59)}",
            "severity": "Low"
        }
    else:
        return {
            "detected": False,
            "confidence": random.uniform(0.0, 10.0)
        }
