import './App.css'
import { MapContainer, TileLayer, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { useState, useEffect } from 'react';
import * as icons from "lucide-react"
import MapMarker from './components/marker/marker';

function App() {
  const [userLocation, setUserLocation] = useState(null);
  const []
  useEffect(() => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const { latitude, longitude } = position.coords;
          setUserLocation([latitude, longitude]);
        },
        (error) => {
          setUserLocation([51.505, -0.09]); // Default location
          // alert("Unable to fetch your location. Please enable location services.");
          console.error("Error fetching location:", error);
        },
        { enableHighAccuracy: true, timeout: 10000, maximumAge: 0 } // Mobile-friendly options
      );
    } else {
      console.error("Geolocation is not supported by this browser.");
    }
  }, [userLocation]);
  return <>
  {userLocation ? <div id="root" style={{ height: "100vh", width: "100%" }}>
      <MapContainer center={userLocation} zoom={17} style={{ height: "100%", width: "100%" }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />
        <MapMarker position={userLocation} icon={<icons.PersonStandingIcon color='green' size={32}/>}>
          <Popup>
            You are here!
          </Popup>
        </MapMarker>
      </MapContainer>
    </div> : <h1>"Couldn't get location"</h1>}
  </>
    
}

export default App

