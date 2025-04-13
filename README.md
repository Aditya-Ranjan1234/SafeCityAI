# Bangalore Accident Prevention System

A Streamlit-based web application for visualizing and analyzing accident-prone areas in Bangalore, providing weather alerts, and allowing citizens to report safety issues.

## Features

- **Interactive Map**: View accident hotspots across Bangalore with detailed information
- **Weather Alerts**: Get real-time weather updates and related safety warnings
- **Reporting System**: Report road hazards and safety issues
- **Data Visualization**: Analyze accident statistics and trends

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Rename `.env.example` to `.env`
   - Add your API keys for weather services (if needed)

## Usage

1. Run the Streamlit application:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:8501
   ```

## Data Sources

- Accident data: Sample dataset based on known accident-prone areas in Bangalore
- Weather data: Open-Meteo API (free and open-source weather API)

## Project Structure

```
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (API keys)
├── data/               # Data files
│   └── bangalore_accident_data.csv  # Accident hotspot data
└── README.md           # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
