
import { useEffect, useRef, useState } from 'react';
import mapboxgl from 'mapbox-gl';
import 'mapbox-gl/dist/mapbox-gl.css';
import { Loader2 } from 'lucide-react';

// This is a temporary approach - in a production app, you'd use environment variables or Supabase secrets
const MAPBOX_TOKEN = 'YOUR_MAPBOX_PUBLIC_TOKEN';

interface MapboxMarker {
  id: string;
  lat: number;
  lng: number;
  type: 'pothole' | 'construction' | 'accident' | 'other';
  title: string;
  description: string;
  severity: 'low' | 'medium' | 'high';
  dateReported: string;
}

const DUMMY_MARKERS: MapboxMarker[] = [
  {
    id: '1',
    lat: 40.7128,
    lng: -74.006,
    type: 'pothole',
    title: 'Deep pothole on Main Street',
    description: 'A large pothole that has caused damage to multiple vehicles',
    severity: 'high',
    dateReported: '2023-04-10',
  },
  {
    id: '2',
    lat: 40.7138,
    lng: -74.008,
    type: 'construction',
    title: 'Incomplete sidewalk construction',
    description: 'Sidewalk construction has been abandoned for weeks',
    severity: 'medium',
    dateReported: '2023-04-08',
  },
  {
    id: '3',
    lat: 40.7148,
    lng: -74.009,
    type: 'accident',
    title: 'Frequent accident zone',
    description: 'This intersection has had 5 accidents in the past month',
    severity: 'high',
    dateReported: '2023-04-12',
  },
];

// Function to get marker color based on severity
const getMarkerColor = (severity: MapboxMarker['severity']): string => {
  switch (severity) {
    case 'high':
      return '#DC2626'; // hazard default (red)
    case 'medium':
      return '#F97316'; // hazard orange
    case 'low':
      return '#FBBF24'; // hazard yellow
    default:
      return '#3B82F6'; // civic blue
  }
};

interface CityMapProps {
  centerLat?: number;
  centerLng?: number;
  zoom?: number;
}

const CityMap = ({ centerLat = 40.7128, centerLng = -74.006, zoom = 13 }: CityMapProps) => {
  const mapContainer = useRef<HTMLDivElement>(null);
  const map = useRef<mapboxgl.Map | null>(null);
  const [loading, setLoading] = useState(true);
  const [apiKeyEntered, setApiKeyEntered] = useState(!!MAPBOX_TOKEN);
  const [customMapboxToken, setCustomMapboxToken] = useState('');

  useEffect(() => {
    if (!mapContainer.current) return;
    if (!apiKeyEntered) return;

    const token = MAPBOX_TOKEN !== 'YOUR_MAPBOX_PUBLIC_TOKEN' ? MAPBOX_TOKEN : customMapboxToken;
    if (!token) return;

    // Initialize MapBox
    mapboxgl.accessToken = token;
    
    try {
      map.current = new mapboxgl.Map({
        container: mapContainer.current,
        style: 'mapbox://styles/mapbox/streets-v12',
        center: [centerLng, centerLat],
        zoom: zoom,
      });
      
      map.current.addControl(new mapboxgl.NavigationControl(), 'top-right');
      map.current.addControl(new mapboxgl.GeolocateControl({
        positionOptions: {
          enableHighAccuracy: true
        },
        trackUserLocation: true
      }));
    
      map.current.on('load', () => {
        setLoading(false);
        
        // Add markers after map is loaded
        DUMMY_MARKERS.forEach(marker => {
          const markerColor = getMarkerColor(marker.severity);
          
          // Create a custom marker element
          const markerElement = document.createElement('div');
          markerElement.className = 'custom-marker';
          markerElement.style.width = '24px';
          markerElement.style.height = '24px';
          markerElement.style.backgroundColor = markerColor;
          markerElement.style.borderRadius = '50%';
          markerElement.style.border = '2px solid white';
          markerElement.style.boxShadow = '0 2px 4px rgba(0,0,0,0.3)';
          
          // For high severity, add pulsing animation
          if (marker.severity === 'high') {
            markerElement.style.animation = 'pulse 2s infinite';
          }
  
          // Add a popup
          const popup = new mapboxgl.Popup({ offset: 25 })
            .setHTML(`
              <div>
                <h3 class="font-bold">${marker.title}</h3>
                <p class="text-sm">${marker.description}</p>
                <p class="text-xs mt-2">Reported: ${marker.dateReported}</p>
              </div>
            `);
  
          // Add marker to map
          new mapboxgl.Marker(markerElement)
            .setLngLat([marker.lng, marker.lat])
            .setPopup(popup)
            .addTo(map.current!);
        });
      });
    } catch (error) {
      console.error("Error initializing map:", error);
      setLoading(false);
    }

    return () => {
      map.current?.remove();
    };
  }, [centerLat, centerLng, zoom, apiKeyEntered, customMapboxToken]);

  if (!apiKeyEntered && MAPBOX_TOKEN === 'YOUR_MAPBOX_PUBLIC_TOKEN') {
    return (
      <div className="flex flex-col items-center justify-center p-6 bg-white rounded-lg shadow-sm border min-h-[400px]">
        <h2 className="text-xl font-semibold mb-4">Mapbox API Key Required</h2>
        <p className="text-sm text-gray-600 mb-4 text-center max-w-md">
          Please enter your Mapbox API key to use the map feature. You can get a free API key by signing up at 
          <a href="https://www.mapbox.com/" target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline"> Mapbox.com</a>.
        </p>
        <input
          type="text"
          placeholder="Enter your Mapbox API key"
          className="w-full max-w-md p-2 border rounded mb-4"
          value={customMapboxToken}
          onChange={(e) => setCustomMapboxToken(e.target.value)}
        />
        <button 
          className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
          onClick={() => setApiKeyEntered(true)}
          disabled={!customMapboxToken}
        >
          Submit API Key
        </button>
      </div>
    );
  }

  return (
    <div className="relative w-full h-[70vh] rounded-lg overflow-hidden border">
      {loading && (
        <div className="absolute inset-0 flex items-center justify-center bg-background/80 z-10">
          <Loader2 className="h-8 w-8 animate-spin text-primary" />
          <span className="ml-2">Loading map...</span>
        </div>
      )}
      <div ref={mapContainer} className="absolute inset-0" />
      <style jsx>{`
        @keyframes pulse {
          0% { transform: scale(1); opacity: 1; }
          50% { transform: scale(1.3); opacity: 0.7; }
          100% { transform: scale(1); opacity: 1; }
        }
      `}</style>
    </div>
  );
};

export default CityMap;
