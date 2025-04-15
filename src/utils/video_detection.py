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
    Display a video in Streamlit with crash detection and bounding boxes.

    Args:
        video_path (str): Path to the video file
        width (int, optional): Width of the video display

    Returns:
        None: Displays the video in the Streamlit app
    """
    # For demonstration, we'll use the crash detection model image
    # and simulate a video feed with bounding boxes

    # Create a container for the video
    video_container = st.empty()

    # Create a progress bar to simulate video playback
    progress_bar = st.progress(0)

    # Determine if this is a crash video based on the filename
    is_crash_video = "crash" in video_path.lower() or "accident" in video_path.lower()

    # Simulate video frames with bounding boxes
    num_frames = 100
    crash_frame = random.randint(60, 80) if is_crash_video else -1

    for i in range(num_frames):
        # Update progress bar
        progress_bar.progress(i + 1)

        # Create a simulated frame with bounding boxes
        frame = create_simulated_frame(i, num_frames, is_crash_video, crash_frame)

        # Display the frame
        video_container.image(
            frame,
            caption=f"Video feed from {os.path.basename(video_path)} - Frame {i+1}/{num_frames}",
            width=width
        )

        # Slow down the simulation
        time.sleep(0.05)

    # Display detection result after video playback
    if is_crash_video:
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

def create_simulated_frame(frame_idx, total_frames, is_crash_video, crash_frame):
    """
    Create a simulated video frame with bounding boxes.

    Args:
        frame_idx (int): Current frame index
        total_frames (int): Total number of frames
        is_crash_video (bool): Whether this is a crash video
        crash_frame (int): Frame number where crash occurs

    Returns:
        numpy.ndarray: Simulated video frame with bounding boxes
    """
    from PIL import Image, ImageDraw, ImageFont
    import numpy as np

    # Load the base image (crash detection model diagram)
    try:
        base_img = Image.open("src/data/videos/crash_detection_model.png")
    except:
        # Create a blank image if the model image is not available
        base_img = Image.new('RGB', (640, 480), color=(30, 30, 46))

    # Resize to a standard size
    base_img = base_img.resize((640, 480))

    # Create a drawing context
    draw = ImageDraw.Draw(base_img)

    # Add frame number and timestamp
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    draw.text((10, 10), f"Frame: {frame_idx+1}/{total_frames}", fill="white", font=font)
    draw.text((10, 40), f"Time: {timestamp}", fill="white", font=font)

    # Add simulated vehicles with bounding boxes
    num_vehicles = random.randint(2, 5)

    # Vehicle positions - simulate movement
    progress = frame_idx / total_frames

    # First vehicle (car 1)
    car1_x = int(100 + progress * 400)
    car1_y = 200
    car1_width = 80
    car1_height = 40

    # Second vehicle (car 2)
    car2_x = int(500 - progress * 200)
    car2_y = 240
    car2_width = 80
    car2_height = 40

    # Draw vehicles
    draw.rectangle([car1_x, car1_y, car1_x + car1_width, car1_y + car1_height],
                   outline="yellow", width=2)
    draw.text((car1_x, car1_y - 20), "Vehicle 1: 0.92", fill="yellow", font=font)

    draw.rectangle([car2_x, car2_y, car2_x + car2_width, car2_y + car2_height],
                   outline="yellow", width=2)
    draw.text((car2_x, car2_y - 20), "Vehicle 2: 0.89", fill="yellow", font=font)

    # Add additional vehicles
    for i in range(2, num_vehicles):
        veh_x = random.randint(50, 550)
        veh_y = random.randint(100, 350)
        veh_width = random.randint(60, 100)
        veh_height = random.randint(30, 50)

        draw.rectangle([veh_x, veh_y, veh_x + veh_width, veh_y + veh_height],
                       outline="yellow", width=2)
        draw.text((veh_x, veh_y - 20), f"Vehicle {i+1}: {random.uniform(0.8, 0.95):.2f}",
                  fill="yellow", font=font)

    # Simulate crash if this is a crash video and we're at the crash frame
    if is_crash_video and abs(frame_idx - crash_frame) < 10:
        # Calculate crash intensity based on proximity to crash frame
        crash_intensity = 1.0 - abs(frame_idx - crash_frame) / 10.0

        # Simulate crash between car1 and car2
        crash_x = min(car1_x, car2_x) - 10
        crash_y = min(car1_y, car2_y) - 10
        crash_width = max(car1_x + car1_width, car2_x + car2_width) - crash_x + 20
        crash_height = max(car1_y + car1_height, car2_y + car2_height) - crash_y + 20

        # Draw crash bounding box
        draw.rectangle([crash_x, crash_y, crash_x + crash_width, crash_y + crash_height],
                       outline="red", width=3)

        # Add crash text with confidence
        confidence = 0.7 + 0.3 * crash_intensity
        draw.text((crash_x, crash_y - 25), f"CRASH DETECTED: {confidence:.2f}",
                  fill="red", font=font)

        # Add visual effects for crash
        for _ in range(int(20 * crash_intensity)):
            effect_x = random.randint(crash_x, crash_x + crash_width)
            effect_y = random.randint(crash_y, crash_y + crash_height)
            effect_size = random.randint(2, 8)
            draw.ellipse([effect_x, effect_y, effect_x + effect_size, effect_y + effect_size],
                         fill="red")

    # Convert PIL Image to numpy array for Streamlit
    return np.array(base_img)

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
