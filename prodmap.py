from errno import ESTALE
import folium
import pandas
data = pandas.read_csv('E:/vscode prac/web programming lab/milkyway/milkpt.csv')
lat = list(data["LAT"])
lon = list(data["LON"])
plc = list(data["PLACE"])

def color_producer(place):
    if place =='MILKPOINT':
        return 'green'
    else:
         return 'orange'


map = folium.Map(location=[9.9252,78.1198],zoom_start=6,tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name ="milkpoints in madurai")
for lt,ln,p in zip(lat,lon,plc):
      fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=p,tooltip = p,fill_color=color_producer(p),color='grey',fill_opacity=0.7)) 
fgp = folium.FeatureGroup(name="population")
fgp.add_child(folium.GeoJson(data=open('E:/vscode prac/web programming lab/milkyway/world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 
else 'orange' if 10000000<= x['properties']['POP2005']<20000000 else 'red'}))
map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("prodmap.html")
