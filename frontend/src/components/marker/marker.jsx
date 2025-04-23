import {divIcon} from 'leaflet'
import {Marker} from 'react-leaflet'
import 'leaflet/dist/leaflet.css'
import React from 'react'
import {renderToStaticMarkup} from 'react-dom/server'

export default function MapMarker({icon, position, children}) {
    const htmlIcon = divIcon({
        html: renderToStaticMarkup(icon),
        className: '', // override Leaflet default class
      })
    return <Marker position={position} icon={htmlIcon}>
            {children}
        </Marker>;
    
}