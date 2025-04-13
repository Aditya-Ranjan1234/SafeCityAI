"""
Emergency Services component for the Bangalore Accident Prevention System.

This module contains functions for displaying emergency services contact information
and one-click contact functionality.
"""

import streamlit as st
from src.utils.config import COLORS

def display_emergency_services():
    """
    Display emergency services contact information with one-click contact buttons.
    
    Returns:
        None: Displays emergency services in the Streamlit app
    """
    # Create a container for emergency services
    with st.container():
        st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 20px;">
            <a href="tel:112" class="emergency-button" style="flex: 1; min-width: 150px; text-decoration: none;">
                <span style="font-size: 1.2rem;">🚨</span> Emergency: 112
            </a>
            <a href="tel:108" class="emergency-button" style="flex: 1; min-width: 150px; text-decoration: none;">
                <span style="font-size: 1.2rem;">🚑</span> Ambulance: 108
            </a>
            <a href="tel:100" class="emergency-button" style="flex: 1; min-width: 150px; text-decoration: none;">
                <span style="font-size: 1.2rem;">👮</span> Police: 100
            </a>
            <a href="tel:101" class="emergency-button" style="flex: 1; min-width: 150px; text-decoration: none;">
                <span style="font-size: 1.2rem;">🚒</span> Fire: 101
            </a>
        </div>
        """, unsafe_allow_html=True)

def display_emergency_banner():
    """
    Display a compact emergency services banner at the top of the page.
    
    Returns:
        None: Displays emergency banner in the Streamlit app
    """
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 8px 16px; border-radius: 8px; margin-bottom: 16px; 
                display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
        <div style="font-weight: bold; color: #d32f2f;">Emergency Services:</div>
        <div style="display: flex; gap: 16px; flex-wrap: wrap;">
            <a href="tel:112" style="text-decoration: none; color: #d32f2f; display: flex; align-items: center; gap: 4px;">
                <span>🚨</span> 112
            </a>
            <a href="tel:108" style="text-decoration: none; color: #d32f2f; display: flex; align-items: center; gap: 4px;">
                <span>🚑</span> 108
            </a>
            <a href="tel:100" style="text-decoration: none; color: #d32f2f; display: flex; align-items: center; gap: 4px;">
                <span>👮</span> 100
            </a>
            <a href="tel:101" style="text-decoration: none; color: #d32f2f; display: flex; align-items: center; gap: 4px;">
                <span>🚒</span> 101
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
