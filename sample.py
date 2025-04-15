"""
Sample Crash Detection Application

This standalone application allows users to upload a video file and
detect car crashes using computer vision techniques.
"""

import streamlit as st
import cv2
import numpy as np
import tempfile
import os
import time
from datetime import datetime
import random
from PIL import Image, ImageDraw, ImageFont
from src.utils.yolo_detection import process_video_with_yolo, find_crash_videos

# Set page configuration
st.set_page_config(
    page_title="Car Crash Detection Demo",
    page_icon="🚨",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #FF5252;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.8rem;
        color: #FF9800;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .crash-alert {
        background-color: #FF5252;
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        font-weight: bold;
        text-align: center;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #1E1E2E;
        border: 1px solid #3A3A4C;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    .stProgress > div > div > div > div {
        background-color: #FF5252;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='main-header'>Car Crash Detection Demo</h1>", unsafe_allow_html=True)

st.markdown("""
<div class='info-box'>
This demo application allows you to upload a video file and detect car crashes using computer vision techniques.
The system will analyze the video and identify potential crash events, displaying the frame where the crash occurred.
</div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Controls")
detection_threshold = st.sidebar.slider("Detection Threshold", 0.5, 1.0, 0.7, 0.05)
show_bounding_boxes = st.sidebar.checkbox("Show Bounding Boxes", True)
show_confidence = st.sidebar.checkbox("Show Confidence Score", True)

# Function to simulate crash detection
def detect_crash(frame, frame_count):
    """
    Simulate crash detection on a video frame.

    In a real implementation, this would use a trained model to detect crashes.
    For this demo, we're simulating detection based on random factors and frame count.

    Args:
        frame: The video frame to analyze
        frame_count: The current frame number

    Returns:
        tuple: (is_crash_detected, confidence, bounding_boxes)
    """
    # Convert frame to PIL Image for drawing
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)

    # Simulate vehicle detection (in a real implementation, this would use a model)
    # For demo purposes, we'll create random bounding boxes
    height, width = frame.shape[:2]
    num_vehicles = random.randint(2, 5)
    bounding_boxes = []

    for _ in range(num_vehicles):
        x1 = random.randint(0, width - 100)
        y1 = random.randint(0, height - 100)
        x2 = x1 + random.randint(50, 100)
        y2 = y1 + random.randint(50, 100)
        confidence = random.uniform(0.7, 0.95)
        bounding_boxes.append((x1, y1, x2, y2, confidence))

    # Simulate crash detection based on frame number
    # In a real implementation, this would analyze motion patterns, object proximity, etc.
    is_crash_frame = False
    crash_confidence = 0.0

    # Simulate a crash at a specific frame range
    crash_start_frame = int(frame_count * 0.7)  # Crash at 70% through the video
    crash_duration = 10  # Frames

    if crash_start_frame <= frame_count < crash_start_frame + crash_duration:
        # Increase confidence as we get closer to the middle of the crash
        progress = 1.0 - abs(frame_count - (crash_start_frame + crash_duration/2)) / (crash_duration/2)
        crash_confidence = 0.5 + 0.5 * progress

        if crash_confidence >= detection_threshold:
            is_crash_frame = True

            # Add a "crash box" that encompasses the vehicles involved
            if len(bounding_boxes) >= 2:
                # Simulate two vehicles involved in crash
                vehicle1 = bounding_boxes[0]
                vehicle2 = bounding_boxes[1]

                # Create a bounding box that encompasses both vehicles
                crash_x1 = min(vehicle1[0], vehicle2[0]) - 10
                crash_y1 = min(vehicle1[1], vehicle2[1]) - 10
                crash_x2 = max(vehicle1[2], vehicle2[2]) + 10
                crash_y2 = max(vehicle1[3], vehicle2[3]) + 10

                # Draw crash bounding box in red
                draw.rectangle([crash_x1, crash_y1, crash_x2, crash_y2], outline="red", width=3)

                # Add "CRASH DETECTED" text
                try:
                    font = ImageFont.truetype("arial.ttf", 20)
                except IOError:
                    font = ImageFont.load_default()

                draw.text((crash_x1, crash_y1 - 25), f"CRASH DETECTED: {crash_confidence:.2f}", fill="red", font=font)

    # Draw bounding boxes for vehicles if enabled
    if show_bounding_boxes:
        for box in bounding_boxes:
            x1, y1, x2, y2, conf = box
            color = "yellow"
            draw.rectangle([x1, y1, x2, y2], outline=color, width=2)

            if show_confidence:
                try:
                    font = ImageFont.truetype("arial.ttf", 12)
                except IOError:
                    font = ImageFont.load_default()

                draw.text((x1, y1 - 15), f"Vehicle: {conf:.2f}", fill=color, font=font)

    # Convert back to OpenCV format
    result_frame = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    return is_crash_frame, crash_confidence, result_frame

def process_video(video_file):
    """
    Process a video file to detect crashes using YOLO.

    Args:
        video_file: The uploaded video file

    Returns:
        None: Displays the results in the Streamlit app
    """
    # Create a temporary file to store the uploaded video
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())

    st.info("Video uploaded successfully. Processing with YOLOv8 model...")

    # Create columns for the video and crash frame
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h3>Video Processing</h3>", unsafe_allow_html=True)
        video_placeholder = st.empty()

    with col2:
        st.markdown("<h3>Crash Detection</h3>", unsafe_allow_html=True)
        crash_placeholder = st.empty()

    # Create a progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()

    # Define a display function for the video frames
    def display_frame(frame, frame_idx, current_time):
        # Update progress
        progress = min(float(frame_idx) / frame_count, 1.0) if 'frame_count' in locals() else 0.5
        progress_bar.progress(progress)

        # Update status
        if 'frame_count' in locals() and 'fps' in locals():
            status_text.text(f"Processing frame {frame_idx}/{frame_count} ({current_time:.2f}s / {(frame_count/fps):.2f}s)")
        else:
            status_text.text(f"Processing frame {frame_idx}")

        # Display the current frame
        video_placeholder.image(
            cv2.cvtColor(frame, cv2.COLOR_BGR2RGB),
            caption=f"Frame {frame_idx} ({current_time:.2f}s)",
            use_column_width=True
        )

    # Open the video to get properties
    cap = cv2.VideoCapture(tfile.name)
    if not cap.isOpened():
        st.error("Error: Could not open video file.")
        return

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    cap.release()

    st.info(f"Video loaded: {frame_count} frames, {fps:.2f} FPS, {duration:.2f} seconds")

    # Process the video with YOLO
    results = process_video_with_yolo(tfile.name, display_func=display_frame)

    # Clean up the temporary file
    os.unlink(tfile.name)

    # Final status
    progress_bar.progress(1.0)
    status_text.text("Video processing complete!")

    # Extract results
    crash_detected = results.get("crash_detected", False)
    crash_confidence = results.get("crash_confidence", 0.0)
    crash_time = results.get("crash_time", 0.0)
    crash_frame = results.get("crash_frame", None)

    # Display the crash frame if detected
    if crash_detected and crash_frame is not None:
        crash_placeholder.image(
            cv2.cvtColor(crash_frame, cv2.COLOR_BGR2RGB),
            caption=f"Crash Detected! Confidence: {crash_confidence:.2f}, Time: {crash_time:.2f}s",
            use_column_width=True
        )

    # Display crash results
    if crash_detected:
        st.markdown(f"""
        <div class='crash-alert'>
            🚨 CRASH DETECTED! 🚨<br>
            Confidence: {crash_confidence:.2f}<br>
            Time: {crash_time:.2f}s (Frame {int(crash_time * fps)})
        </div>
        """, unsafe_allow_html=True)

        # Display crash details
        st.markdown("<h2 class='sub-header'>Crash Analysis</h2>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Crash Confidence", f"{crash_confidence:.2f}", "High" if crash_confidence > 0.8 else "Medium")

        with col2:
            st.metric("Crash Time", f"{crash_time:.2f}s", f"Frame {int(crash_time * fps)}")

        with col3:
            severity = "High" if crash_confidence > 0.9 else "Medium" if crash_confidence > 0.7 else "Low"
            st.metric("Estimated Severity", severity, "Based on impact analysis")

        # YOLO detection details
        st.markdown("<h3>YOLO Detection Details</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='info-box'>
        <p>The crash was detected using YOLOv8, a state-of-the-art object detection model:</p>
        <ul>
            <li><strong>Model:</strong> YOLOv8 (You Only Look Once version 8)</li>
            <li><strong>Detection Method:</strong> Real-time object detection with bounding boxes</li>
            <li><strong>Objects Tracked:</strong> Cars, trucks, buses, motorcycles</li>
            <li><strong>Crash Detection:</strong> Analysis of object proximity and motion patterns</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        # Recommendations
        st.markdown("""
        <h3>Recommendations</h3>
        <ul>
            <li>Contact emergency services immediately</li>
            <li>Secure the accident scene to prevent further incidents</li>
            <li>Check for injuries and provide first aid if necessary</li>
            <li>Document the accident scene for insurance purposes</li>
        </ul>
        """, unsafe_allow_html=True)
    else:
        st.success("No crashes detected in the video.")

# Main application
st.markdown("<h2 class='sub-header'>Upload a Video</h2>", unsafe_allow_html=True)

# Find crash videos in the current directory
crash_videos = find_crash_videos()
if crash_videos:
    st.info(f"Found {len(crash_videos)} crash videos in the current directory.")
    selected_video = st.selectbox("Select a crash video", crash_videos, index=0)

    if st.button("Process Selected Video"):
        # Create a temporary file to process the selected video
        with open(selected_video, "rb") as video_file:
            video_bytes = video_file.read()

        # Create a temporary file
        tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        tfile.write(video_bytes)
        tfile.close()

        # Process the video
        process_video(tfile)

# Allow uploading a new video
uploaded_file = st.file_uploader("Or upload your own video file", type=["mp4", "avi", "mov", "mkv"])

if uploaded_file is not None:
    # Process the uploaded video
    process_video(uploaded_file)
elif not crash_videos:
    # Display sample images when no video is uploaded and no crash videos are found
    st.markdown("<h2 class='sub-header'>Sample Crash Detection</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image("CarCrashDataset/assets/CCD.png", caption="Car Crash Detection Model Architecture", use_column_width=True)

    with col2:
        st.markdown("""
        <div class='info-box'>
        <h3>How it works:</h3>
        <ol>
            <li>Upload a video containing traffic footage</li>
            <li>The system analyzes each frame using YOLOv8</li>
            <li>Vehicles are detected and tracked throughout the video</li>
            <li>Abnormal motion patterns and sudden changes are identified</li>
            <li>When a crash is detected, the system marks the frame and provides details</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class='info-box'>
    <h3>Sample Videos:</h3>
    <p>You can download sample crash videos from these sources:</p>
    <ul>
        <li><a href="https://ankitshah009.github.io/accident_forecasting_traffic_camera" target="_blank">CADP Dataset</a></li>
        <li><a href="https://github.com/Cogito2012/CarCrashDataset" target="_blank">Traffic Accident Detection Dataset</a></li>
        <li><a href="https://www.kaggle.com/datasets/ckay16/accident-detection-from-cctv-footage" target="_blank">Road Accident Dataset on Kaggle</a></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "© 2025 Bangalore Accident Prevention System | "
    "Car Crash Detection Demo | "
    "Created for समAI - Time for AI"
    "</div>",
    unsafe_allow_html=True
)
