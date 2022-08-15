import json
import folium,requests

width:int = 650
height:int = 450


mp = folium.Map(tiles=None,location=[26,35],zoom_start=4)

add = '/MapServer/tile/{z}/{y}/{x}.png'
ESRI = dict(World_Ocean_Base='http://services.arcgisonline.com/arcgis/rest/services/Ocean/World_Ocean_Base',
            World_Navigation_Charts='http://services.arcgisonline.com/ArcGIS/rest/services/Specialty/World_Navigation_Charts',
            World_Ocean_Reference='http://services.arcgisonline.com/arcgis/rest/services/Ocean/World_Ocean_Reference',
            NatGeo_World_Map='http://services.arcgisonline.com/arcgis/rest/services/NatGeo_World_Map/MapServer',
            World_Imagery='http://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer',
            World_Physical_Map='http://services.arcgisonline.com/arcgis/rest/services/World_Physical_Map/MapServer',
            World_Shaded_Relief='http://services.arcgisonline.com/arcgis/rest/services/World_Shaded_Relief/MapServer',
            World_Street_Map='http://services.arcgisonline.com/arcgis/rest/services/World_Street_Map/MapServer',
            World_Terrain_Base='http://services.arcgisonline.com/arcgis/rest/services/World_Terrain_Base/MapServer',
            World_Topo_Map='http://services.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer')

attribute = ('&copy GeoBasis-DE /<a href="http://www.bkg.bund.de">BKG</a>')
for tile_name, tile_url in ESRI.items():
    tile_url += add
    folium.TileLayer(name=tile_name,attr=attribute,
                     tiles=tile_url,show=False).add_to(mp)

attribute = ('&copy GeoBasis-DE /<a href="http://www.bkg.bund.de">BKG</a>')

folium.raster_layers.WmsTileLayer(url = 'http://mfsai.xyz/geoserver/trharita/wms',
                                  layers='trharita:ilce',
                                  fmt='image/png',
                                  attr=attribute,
                                  transparent=True).add_to(mp)

# url =  "http://mfsai.xyz/geoserver/trharita/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=trharita%3Ailce&maxFeatures=1050&outputFormat=application%2Fjson"

# folium.GeoJson(url, name="geojson").add_to(mp)

folium.LayerControl().add_to(mp)
mp.save("index.html")