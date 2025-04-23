import './App.css'
import { MapContainer, TileLayer, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { QueryClient,  QueryClientProvider } from 'react-query';
import { ReactQueryDevtools } from 'react-query/devtools';
import Map from './components/map/map';


function App() {
  const queryClient = new QueryClient();
  return <div id="root" style={{ height: "100vh", width: "100%" }}>
    <QueryClientProvider client={queryClient}>
      <ReactQueryDevtools/>
      <Map/>
    </QueryClientProvider>
    </div>
 

}

export default App  

