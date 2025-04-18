# SafeCityAI: Bangalore Accident Prevention System

## Application Screenshots

The following screenshots showcase the key features and interfaces of the SafeCityAI application:

### Home Page
![Home Page](images/home_page.png)
*The main dashboard provides an overview of accident statistics, emergency service contacts, and key metrics for quick assessment of road safety in Bangalore.*

A comprehensive AI-powered platform for accident prevention and road safety in Bangalore. This system integrates real-time weather data, historical accident records, and machine learning predictions to help citizens navigate safely and report hazardous conditions.

## 🏆 Created for समAI - Time for AI Competition

This project is developed as part of the [समAI - Time for AI](https://wequity.acehacker.com/samai/) competition, which challenges participants to code, create, and innovate with Artificial Intelligence. SafeCityAI demonstrates how AI can be leveraged to create safer urban environments and potentially save lives through predictive analytics and community engagement.

## ✨ Key Features

### 🗺️ Interactive Accident Hotspot Map
- **Detailed Visualization**: View accident-prone areas across Bangalore with severity indicators
- **Filtering Options**: Filter hotspots by severity, incident count, accident type, and time of day
- **Multiple Map Views**: Switch between marker, heatmap, and cluster visualizations
- **Detailed Information**: Click on markers to see comprehensive accident data and contributing factors

![Accident Map](images/accident_map.png)
*The interactive map visualizes accident hotspots across Bangalore with color-coded markers indicating severity levels, allowing users to identify high-risk areas at a glance.*

### 🛣️ Safe Route Planning
- **Source-Destination Selection**: Choose starting and ending points in Bangalore
- **Safety-Optimized Routes**: Get routes that avoid high-accident areas
- **Risk Assessment**: View safety scores for suggested routes
- **Accident Hotspot Avoidance**: Automatically routes around known dangerous areas
- **Time and Distance Estimates**: Compare safety vs. convenience trade-offs

### 📹 Video Surveillance & YOLO-based Accident Detection
- **Real-time Monitoring**: Live camera feeds from high-risk areas across Bangalore
- **YOLOv8 Detection**: State-of-the-art object detection for vehicles and crashes
- **Bounding Box Visualization**: Real-time tracking of vehicles with confidence scores
- **Crash Analysis**: Automatic identification of accidents based on vehicle proximity and motion
- **Multi-Camera Support**: Simultaneous monitoring of multiple locations with different video feeds
- **Instant Alerts**: Immediate notification when incidents are detected
- **Emergency Response**: Automatic dispatch of emergency services
- **Incident Analytics**: Review and analysis of detected incidents with detailed metrics
- **Local Video Processing**: Automatic detection and use of videos from the Crash-1500 directory

![Video Surveillance](Screenshot%202025-04-15%20142906.png)
*Real-time video surveillance with YOLO-based crash detection across multiple camera feeds in Bangalore*

### 🤖 Machine Learning Predictions
- **Risk Prediction**: AI-powered prediction of accident likelihood based on multiple factors
- **City-wide Risk Map**: Color-coded visualization of risk levels across the entire city
- **Emerging Hotspot Detection**: Identification of new high-risk areas before they become problematic
- **Personalized Safety Recommendations**: Contextual safety advice based on current conditions

![Risk Prediction Map](images/risk_prediction_map.png)
*The city-wide risk prediction map uses AI to visualize accident risk levels across Bangalore with a heat map overlay. Red areas indicate high-risk zones, yellow shows moderate risk, and green represents lower risk areas. Red markers pinpoint specific accident hotspots.*

### Recent Updates Section
![Recent Updates](images/recent_updates.png)
*The recent updates section keeps users informed about road work, traffic signal changes, and other important traffic-related announcements with timestamps.*

### 🌦️ Weather & Safety Alerts
- **Real-time Weather Data**: Current weather conditions and forecasts for Bangalore
- **Weather-related Safety Alerts**: Automatic warnings when weather conditions may affect road safety
- **Forecast Integration**: 7-day weather forecast to help plan safer travel
- **Condition-specific Safety Tips**: Tailored advice for different weather conditions

![Current Weather Conditions](images/weather_current.png)
*Real-time weather data showing temperature (23.9°C), humidity (65%), and wind speed (2.5 km/h) with clear sky conditions.*

![Weather Forecast](images/weather_forecast.png)
*3-day weather forecast for March-April 2025 showing upcoming conditions: slight rain showers on Monday (April 14), overcast on Tuesday (April 15), and thunderstorm with slight hail on Wednesday (April 16).*

![Driving Safety Tips](images/driving_safety_tips.png)
*Context-aware driving safety tips that update based on current and forecasted weather conditions, helping drivers navigate safely during adverse weather.*

### 📝 Citizen Reporting System
- **Issue Reporting**: Allow citizens to report road hazards and safety issues
- **Location Selection**: Interactive map for precise location reporting
- **Media Upload**: Support for uploading photos of hazardous conditions
- **Status Tracking**: Follow the status of reported issues

![Community Reports](images/community_reports.png)
*Recent community reports showing citizen-submitted hazards with location details, issue type, severity level, and report status. Reports from April 2025 include a pothole on Outer Ring Road, a broken traffic signal, and waterlogging after rain.*

### 🚨 Emergency Services Integration
- **One-click Emergency Contact**: Quick access to emergency services at the top of every page
- **Direct Calling**: Integrated calling functionality for immediate assistance
- **Multiple Services**: Access to Police, Fire, Ambulance, and General Emergency services

*The emergency services bar at the top of the application provides quick access to important contact numbers (112 for Police, 108 for Ambulance, 100 for Emergency, 101 for Fire) for immediate assistance in case of accidents.*

### 🌐 Multilingual Support (Planned)
- Support for English, Hindi, and Kannada languages
- Easy language switching via the top navigation bar
- Localized emergency information and safety tips

### Footer
*The application footer displays copyright information (© 2025) and acknowledges that the system was created for the समAI - Time for AI competition, reinforcing the project's forward-looking vision.*

## 📊 Data & AI Components

### Data Sources
- **Accident Data**: Historical records of accident-prone areas in Bangalore
- **Weather Data**: Real-time and forecast data from Open-Meteo API
- **Citizen Reports**: Crowdsourced information about road hazards and safety issues

### AI & Machine Learning
- **Risk Prediction Model**: Analyzes multiple factors to predict accident likelihood
- **Hotspot Identification**: Uses clustering algorithms to identify accident-prone areas
- **Weather Impact Analysis**: Correlates weather conditions with accident frequency
- **Emerging Risk Detection**: Identifies new patterns in accident data to predict future hotspots

## 🔧 Technical Implementation

### Technology Stack
- **Frontend**: Streamlit for interactive web interface
- **Data Processing**: Pandas for data manipulation and analysis
- **Visualization**: Folium for maps, Plotly for interactive charts
- **Machine Learning**: Scikit-learn for predictive models
- **APIs**: Open-Meteo for weather data

### Architecture
The application follows a modular architecture with clear separation of concerns:
- **Data Layer**: Handles data loading, processing, and storage
- **Logic Layer**: Implements business logic, predictions, and data analysis
- **Presentation Layer**: Manages the user interface and visualization components

## 📝 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Git

### Installation Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/Aditya-Ranjan1234/SafeCityAI.git
   cd SafeCityAI
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

   Note: The application uses several key dependencies:
   - **Streamlit**: For the interactive web interface
   - **Folium**: For interactive maps and route visualization
   - **NetworkX**: For route planning algorithms
   - **OpenCV**: For video processing and accident detection
   - **Plotly**: For data visualization
   - **Scikit-learn**: For machine learning predictions

4. Download the CarCrash dataset for accident detection (optional):
   ```bash
   git clone https://github.com/Cogito2012/CarCrashDataset.git
   ```

5. Configure environment variables (if needed):
   - Rename `.env.example` to `.env`
   - Add your API keys for weather services

## 🚀 Usage

### Local Development

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:8501
   ```

### Streamlit Cloud Deployment

To deploy on Streamlit Cloud and avoid the `libGL.so.1` error:

1. Make sure your `requirements.txt` file includes all necessary dependencies.

2. The application has built-in fallback mechanisms to handle missing OpenCV dependencies.

3. If you encounter the `libGL.so.1` error, you can install the required system packages on your server:
   ```bash
   # For Ubuntu/Debian
   apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

   # For Amazon Linux/CentOS
   yum update -y && yum install -y mesa-libGL
   ```

4. Alternatively, use the provided Dockerfile for containerized deployment:
   ```bash
   # Build and run using Docker
   docker build -t safecityai .
   docker run -p 8501:8501 safecityai
   ```

5. Access the application at:
   ```
   http://localhost:8501
   ```

## 📁 Project Structure

```
├── app.py                      # Main Streamlit application
├── sample.py                    # Standalone crash detection interface
├── requirements.txt            # Python dependencies
├── Dockerfile                   # Docker configuration for containerized deployment
├── docker-compose.yml           # Docker Compose configuration for easy deployment
├── WORKFLOW.md                  # Detailed workflow documentation
├── .env                        # Environment variables (API keys)
├── src/                        # Source code
│   ├── components/             # UI components
│   │   ├── emergency_services.py  # Emergency services components
│   │   ├── map_components.py   # Map visualization components
│   │   ├── stats_components.py # Statistical visualization components
│   │   └── weather_components.py # Weather visualization components
│   ├── data/                   # Data files
│   │   ├── bangalore_accident_data.csv  # Accident hotspot data
│   │   └── videos/              # Video files for surveillance demo
│   ├── pages/                  # Application pages
│   │   ├── home_page.py        # Home page
│   │   ├── accident_map_page.py # Accident map page
│   │   ├── ml_predictions_page.py # ML predictions page
│   │   ├── route_planning_page.py # Safe route planning page
│   │   ├── video_surveillance_page.py # Video surveillance page
│   │   ├── weather_page.py     # Weather and alerts page
│   │   └── report_page.py      # Issue reporting page
│   └── utils/                  # Utility modules
│       ├── config.py           # Configuration settings
│       ├── data_loader.py      # Data loading utilities
│       ├── video_detection.py  # Video processing and accident detection
│       └── yolo_detection.py   # YOLOv8-based crash detection
├── CarCrashDataset/            # Reference dataset for accident detection
├── screenshots/                # Application screenshots for documentation
└── images/                     # Application screenshots for README
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [समAI - Time for AI](https://wequity.acehacker.com/samai/) for the opportunity to showcase this project
- [Open-Meteo](https://open-meteo.com/) for providing free weather API
- [Streamlit](https://streamlit.io/) for the excellent web application framework
- [Folium](https://python-visualization.github.io/folium/) for the interactive mapping capabilities
- [CarCrashDataset](https://github.com/Cogito2012/CarCrashDataset) for providing reference data for accident detection
- [NetworkX](https://networkx.org/) for the graph algorithms used in route planning
- [YOLOv8](https://github.com/ultralytics/ultralytics) for state-of-the-art object detection

## 🔍 Standalone Crash Detection Interface

In addition to the main application, this project includes a standalone crash detection interface (`sample.py`) that allows users to upload and analyze traffic videos for crashes.

### Features

- **Video Upload**: Upload any traffic video for crash analysis
- **YOLOv8 Processing**: Frame-by-frame analysis with state-of-the-art object detection
- **Real-time Visualization**: Watch the detection process with bounding boxes
- **Crash Frame Identification**: Pinpoints the exact moment of collision
- **Detailed Analysis**: Provides confidence scores, timestamps, and severity assessment
- **Emergency Recommendations**: Suggests actions to take when a crash is detected

### Usage

To run the standalone crash detection interface:

```bash
streamlit run sample.py
```

This will open a web interface where you can upload traffic videos for crash analysis.
