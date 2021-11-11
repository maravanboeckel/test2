#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import plotly.express as px
import folium
from folium import plugins
from statsmodels.formula.api import ols
import numpy as np
import streamlit as st
from streamlit_folium import folium_static
import plotly.graph_objects as go
from PIL import Image
from folium.plugins import FloatImage
# In[ ]:


#sidebar
st.set_page_config(layout="wide")
rad = st.sidebar.radio(options=('Home','Current weather map','Plotting current weather','Forecast weather map','Plotting forecast weather'),label='Select category')

st.sidebar.markdown('#')
st.sidebar.markdown('#')

st.sidebar.subheader('Made by:')
st.sidebar.write('Mara van Boeckel')
st.sidebar.write('Maarten van der Veer')


# In[ ]:
if rad== 'Home':
    st.title('Dashboard (forecast) weather')
    imghome = Image.open("weer.png")
    st.image(imghome, width=800)
    st.markdown('#')
    st.markdown('#')
    st.markdown('#')
    st.markdown('#')
    st.markdown('#')
    st.subheader('Bibliography')
    '- Max Vandaag. (2021, 20 maart). [Hoge en lage drukgebieden]. Het weer: het maken van een weersverwachting. https://www.maxvandaag.nl/sessies/themas/natuur-milieu/het-maken-van-een-weersverwachting/'
    '- RapidAPI. (z.d.). OpenWeatherMap API - Free Weather Data (for Developers). Geraadpleegd op 11 november 2021, van https://community-open-weather-map.p.rapidapi.com/weather'
    '- RapidAPI. (z.d.). OpenWeatherMap API - Free Weather Data (for Developers). Geraadpleegd op 11 november 2021, van https://community-open-weather-map.p.rapidapi.com/forecast'

if rad == 'Plotting current weather':
    st.header('Plotting current weather')
    st.markdown('#')
  
    'The figure below shows the histograms of the humidity for each country on 6 november 2021. You can select the countries with de dropdown. '
    current_weather = pd.read_csv('Weather_compleet.csv')
    
    city_color_map = {'Netherlands': 'rgb(240,128,128)','United Kingdom': 'rgb(135,206,235)','France': 'rgb(216, 191,216)',
                      'Belgium': 'rgb(127,255,212)','Denmark': 'rgb(255,211,155)','Portugal': 'rgb(205,41,144)',
                      'Germany' : 'rgb(255,246,143)','Spain':'rgb(162,205,90)','Ireland':'rgb(205,200,177)',
                      'Italy':'rgb(255,99,71)','Greece':'rgb(0,238,118)','Croatia':'rgb(99,184,255)',
                      'Austria':'rgb(198,113,113)','Turkey':'rgb(135,38,87)','Romania':'rgb(255,130,171)',
                      'Hungary':'rgb(192,255,62)','Bulgaria':'rgb(255,128,0)'}


    dropdown_buttons = [{'label': 'All','method': 'update','args': [{'visible': [True, True, True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]}]},
                        {'label': 'Netherlands','method': 'update','args': [{'visible': [True, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
                        {'label': 'France','method': 'update','args': [{'visible': [False, True, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
                        {'label': "Germany",'method': "update",'args': [{"visible": [False, False, True,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
                        {'label': "Portugal",'method': "update",'args': [{"visible": [False, False, False,True,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
                        {'label': "United Kingdom",'method': "update",'args': [{"visible":[False, False, False,False,True,False,False,False,False,False,False,False,False,False,False,False,False]}]},
                        {'label': "Belgium",'method': "update",'args': [{"visible": [False, False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False]}]},
                        {'label': "Denmark",'method': "update",'args': [{"visible": [False, False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False]}]},
                        {'label': "Spain",'method': "update",'args': [{"visible": [False, False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False]}]},
                        {'label': "Ireland",'method': "update",'args': [{"visible": [False, False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False]}]},
                        {'label': "Italy",'method': "update",'args': [{"visible": [False, False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False]}]},
                        {'label': "Greece",'method': "update",'args': [{"visible": [False, False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False]}]},
                        {'label': "Croatia",'method': "update",'args': [{"visible": [False, False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False]}]},
                        {'label': "Austria",'method': "update",'args': [{"visible": [False, False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False]}]},
                        {'label': "Turkey",'method': "update",'args': [{"visible": [False, False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False]}]},
                        {'label': "Romania",'method': "update",'args': [{"visible": [False, False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False]}]},
                        {'label': "Hungary",'method': "update",'args': [{"visible": [False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False]}]},
                        {'label': "Bulgaria",'method': "update",'args': [{"visible": [False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True]}]}
                       ]
    fig1 = px.histogram(data_frame=current_weather, x='humidity', color_discrete_map =city_color_map,
                       color='country', nbins=15,
                       labels={'humidity':'Humidity (%)', 'country':'Country'})
    fig1.update_layout(title = "Humidity levels for each country", yaxis_title="Frequency")
    fig1.update_layout({'updatemenus':[{'type': "dropdown",'showactive': True,'active': 0,'buttons': dropdown_buttons}]})
    fig1.update_xaxes(fixedrange=True)
    fig1.update_yaxes(fixedrange=True)
    st.plotly_chart(fig1)

    'The figure below shows the boxplots of the temperature for each country. '
    fig2 = px.box(data_frame=current_weather, x='country',y='temp_c', title="Boxplots of the temperature per country ",
                 labels={"temp_c": "Temperature (°C)",
                         "country": "Country"},
    category_orders = {'country':['Netherlands','France','Germany','Portugal','United Kingdom','Belgium','Denmark','Spain','Ireland','Italy','Greece','Croatia','Austria','Turkey','Romania','Hungary','Bulgaria']},
                color='country',color_discrete_map =city_color_map)

    st.plotly_chart(fig2)
    ##############################################################################################################
    st.markdown('#')
    st.subheader('Scatterplots with predictions')
    fig3=px.scatter(current_weather,x='lat',y='temp_c',color='country',color_discrete_map =city_color_map,trendline="ols",trendline_scope='overall',trendline_color_override="grey",title='Scatterplot of the temperature vs latitude',labels={'lat':'Latitude','temp_c':'Temperature (°C)',"country": "Country"})
    st.plotly_chart(fig3)
    img = Image.open("summary lat.png")
    st.image(img, width=800)
    ##############################################################################################################
    st.markdown('#')
    
    fig4=px.scatter(current_weather,x='temp_diff',y='speed',color='country',color_discrete_map =city_color_map,trendline="ols",trendline_color_override="grey",trendline_scope='overall',title='Scatterplot of the windspeed difference vs temperature',labels={'temp_diff':'Temperature difference','speed':'Windspeed (km/h)',"country": "Country"})
    st.plotly_chart(fig4)
    img1 = Image.open("summary speed.png")
    st.image(img1, width=800)
    ##############################################################################################################
    st.markdown('#')
    st.subheader('Correlation for each variable')
    st.markdown('#')
    img2 = Image.open("corr.png")
    st.image(img2, width=800)

# In[ ]:


if rad == 'Current weather map':
    st.header('Current weather map')
    st.markdown('#')
  
    'The figure below shows the map of the weather on 6 november 2021. With the layer control you can select the information of your choice.'
    current_weather = pd.read_csv('Weather_compleet.csv')
    
    def colorspressure(pressure):
        if pressure < 1009:
            color = 'blue'
            return color
        elif pressure >= 1009 and pressure < 1022:
            color = 'green'
            return color
        elif pressure >= 1022:
            color = 'orange'
            return color


    def colorstemp(temp):
        if temp < 10:
            color = 'blue'
            return color
        elif temp >= 10 and temp < 20:
            color = 'yellow'
            return color
        elif temp >= 20 and temp <28:
            color = 'orange'
            return color
        elif temp >=28:
            color = 'red'
            return color

    
    current_weather_map = folium.Map(location=[45.07033935, 7.686864], zoom_start = 4)



    data = ['Measurements','Wind','Temperature','Pressure','"Feels like" temperature']



    effecten = [folium.FeatureGroup(name=x)for x in data]
    tooltip = "Click for information"



    for row in current_weather.iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        popup = ('<strong>' + row_values['City'] + '</strong>' + '<br>'+
        'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
        'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
        'Pressure: ' + str(round(row_values['pressure'],2))+'hPa' + '<br>'+
        'Rain: ' + str(row_values['rain']) + '<br>' +
        'Sunrise: ' + str(row_values['sunrise'],)+ 'UTC' + '<br>' +
        'Sunset: ' + str(row_values['sunset']) + 'UTC'+ '<br>')
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[0])
        effecten[0].add_to(current_weather_map)

    for row in current_weather.iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.plugins.BoatMarker(location=location,heading = row_values['deg'],tooltip = tooltip)
        marker.add_to(effecten[1])
        effecten[1].add_to(current_weather_map)

    for row in current_weather.iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,tooltip =str(round(row_values['temp_c'],2))+ '°C')
        marker.add_to(effecten[2])
        effecten[2].add_to(current_weather_map)

    for row in current_weather.iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.CircleMarker(location=location,tooltip = str(round(row_values['pressure'],2))+'hPa',radius=6,fill=True,opacity=1,color=colorspressure(row_values['pressure']))
        marker.add_to(effecten[3])
        effecten[3].add_to(current_weather_map)

    for row in current_weather.iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.CircleMarker(location=location,tooltip = str(round(row_values['feels_like_c'],2))+ '°C',radius=6,fill=True,opacity=1,color=colorstemp(row_values['feels_like_c']))
        marker.add_to(effecten[4])
        effecten[4].add_to(current_weather_map)



    evenaar=[[-0,-720], [0,720]]



    folium.LayerControl(position='topleft').add_to(current_weather_map)

    folium.PolyLine(evenaar,color="red").add_to(current_weather_map)
   
    folium_static(current_weather_map)
    
    imglegend = Image.open("legenda2.png")
    st.image(imglegend)
    
  

# In[ ]:


if rad == 'Forecast weather map':
    st.header('Forecast weather map')
    st.markdown('#')
  
    'The figure below shows the map of the forecast weather from 8 november to 13 november 2021. There is a measuring point every 3 hours. With the layer control you can select the day and time of your choice.'
    forecast_weather = pd.read_csv('forecast_sorted.csv')
    
   
    map = folium.Map(location=[45.07033935, 7.686864], zoom_start = 4)


    data =['11-08 12h', '11-08 15h',
           '11-08 18h', '11-08 21h',
           '11-09 00h', '11-09 03h',
           '11-09 06h', '11-09 09h',
           '11-09 12h', '11-09 15h',
           '11-09 18h', '11-09 21h',
           '11-10 00h', '11-10 03h',
           '11-10 06h', '11-10 09h',
           '11-10 12h', '11-10 15h',
           '11-10 18h', '11-10 21h',
           '11-11 00h', '11-11 03h',
           '11-11 06h', '11-11 09h',
           '11-11 12h', '11-11 15h',
           '11-11 18h', '11-11 21h',
           '11-12 00h', '11-12 03h',
           '11-12 06h', '11-12 09h',
           '11-12 12h', '11-12 15h',
           '11-12 18h', '11-12 21h',
           '11-13 00h', '11-13 03h',
           '11-13 06h', '11-13 09h']


    effecten = [folium.FeatureGroup(name=x,show=False)for x in data]
    tooltip = "Click for information"

    start=147


    for row in forecast_weather.iloc[start*0:start*1].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')       
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        
        marker.add_to(effecten[0])
        effecten[0].add_to(map)


    for row in forecast_weather.iloc[start*1:start*2].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[1])
        effecten[1].add_to(map)

    for row in forecast_weather.iloc[start*2:start*3].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[2])
        effecten[2].add_to(map)


    for row in forecast_weather.iloc[start*3:start*4].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[3])
        effecten[3].add_to(map)

    for row in forecast_weather.iloc[start*4:start*5].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[4])
        effecten[4].add_to(map)

    for row in forecast_weather.iloc[start*5:start*6].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[5])
        effecten[5].add_to(map)

    for row in forecast_weather.iloc[start*6:start*7].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[6])
        effecten[6].add_to(map)


    for row in forecast_weather.iloc[start*7:start*8].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]

        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[7])
        effecten[7].add_to(map)

    for row in forecast_weather.iloc[start*8:start*9].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[8])
        effecten[8].add_to(map)


    for row in forecast_weather.iloc[start*9:start*10].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[9])
        effecten[9].add_to(map)


    for row in forecast_weather.iloc[start*10:start*11].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[10])
        effecten[10].add_to(map)

    for row in forecast_weather.iloc[start*11:start*12].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[11])
        effecten[11].add_to(map)

    for row in forecast_weather.iloc[start*12:start*13].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[12])
        effecten[12].add_to(map)

    for row in forecast_weather.iloc[start*13:start*14].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[13])
        effecten[13].add_to(map)

    for row in forecast_weather.iloc[start*14:start*15].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[14])
        effecten[14].add_to(map)

    for row in forecast_weather.iloc[start*15:start*16].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[15])
        effecten[15].add_to(map)


    for row in forecast_weather.iloc[start*16:start*17].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[16])
        effecten[16].add_to(map)

    for row in forecast_weather.iloc[start*17:start*18].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[17])
        effecten[17].add_to(map)

    for row in forecast_weather.iloc[start*18:start*19].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[18])
        effecten[18].add_to(map)

    for row in forecast_weather.iloc[start*19:start*20].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[19])
        effecten[19].add_to(map)

    for row in forecast_weather.iloc[start*20:start*21].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[20])
        effecten[20].add_to(map)

    for row in forecast_weather.iloc[start*21:start*22].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[21])
        effecten[21].add_to(map)

    for row in forecast_weather.iloc[start*22:start*23].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[22])
        effecten[22].add_to(map)

    for row in forecast_weather.iloc[start*23:start*24].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[23])
        effecten[23].add_to(map)

    for row in forecast_weather.iloc[start*24:start*25].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[24])
        effecten[24].add_to(map)



    for row in forecast_weather.iloc[start*25:start*26].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[25])
        effecten[25].add_to(map)


    for row in forecast_weather.iloc[start*26:start*27].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[26])
        effecten[26].add_to(map)    


    for row in forecast_weather.iloc[start*27:start*28].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[27])
        effecten[27].add_to(map)    

    for row in forecast_weather.iloc[start*28:start*29].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[28])
        effecten[28].add_to(map)       

    for row in forecast_weather.iloc[start*29:start*30].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[29])
        effecten[29].add_to(map)      

    for row in forecast_weather.iloc[start*30:start*3].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[30])
        effecten[30].add_to(map)  

    for row in forecast_weather.iloc[start*31:start*32].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[31])
        effecten[31].add_to(map)  

    for row in forecast_weather.iloc[start*32:start*33].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[32])
        effecten[32].add_to(map) 

    for row in forecast_weather.iloc[start*33:start*34].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[33])
        effecten[33].add_to(map)  


    for row in forecast_weather.iloc[start*34:start*35].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[34])
        effecten[34].add_to(map)   


    for row in forecast_weather.iloc[start*35:start*36].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[35])
        effecten[35].add_to(map) 

    for row in forecast_weather.iloc[start*36:start*37].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[36])
        effecten[36].add_to(map)

    for row in forecast_weather.iloc[start*37:start*38].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[37])
        effecten[37].add_to(map) 

    for row in forecast_weather.iloc[start*38:start*39].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[38])
        effecten[38].add_to(map) 

    for row in forecast_weather.iloc[start*39:start*40].iterrows():
        row_values=row[1]
        popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                    'Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                    'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                    'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                    'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                    'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')    
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[39])
        effecten[39 ].add_to(map)


    folium.LayerControl(position='topleft', title='Dagen').add_to(map)


    folium_static(map)
    
    


# In[ ]:



if rad == 'Plotting forecast weather':
    forecast_weather = pd.read_csv('forecast_sorted.csv')
    st.header("Plotting forecast weather")
    'NOG EEN TEKST'
    st.markdown('#')
  
    
    
    data_nl = forecast_weather[forecast_weather['country'].str.contains("Netherlands")].reset_index()
    data_fr = forecast_weather[forecast_weather['country'].str.contains("France")].reset_index()
    data_ge = forecast_weather[forecast_weather['country'].str.contains("Germany")].reset_index()
    data_pt = forecast_weather[forecast_weather['country'].str.contains("Portugal")].reset_index()
    data_uk = forecast_weather[forecast_weather['country'].str.contains("United Kingdom")].reset_index()
    data_be = forecast_weather[forecast_weather['country'].str.contains("Belgium")].reset_index()
    data_dk = forecast_weather[forecast_weather['country'].str.contains("Denmark")].reset_index()                           
    data_es = forecast_weather[forecast_weather['country'].str.contains("Spain")].reset_index()                           
    data_ie = forecast_weather[forecast_weather['country'].str.contains("Ireland")].reset_index()                           
    data_it = forecast_weather[forecast_weather['country'].str.contains("Italy")].reset_index()                            
    data_gr = forecast_weather[forecast_weather['country'].str.contains("Greece")].reset_index()                           
    data_au = forecast_weather[forecast_weather['country'].str.contains("Austria")].reset_index()                           
    data_tu = forecast_weather[forecast_weather['country'].str.contains("Turkey")].reset_index()      
    data_ro = forecast_weather[forecast_weather['country'].str.contains("Romania")].reset_index()                           
    data_hu = forecast_weather[forecast_weather['country'].str.contains("Hungary")].reset_index()                           
    data_bu = forecast_weather[forecast_weather['country'].str.contains("Bulgaria")].reset_index()                          
    data_cr = forecast_weather[forecast_weather['country'].str.contains("Croatia")].reset_index()
                               
    dropdown = st.selectbox('Select country', ("Netherlands","France", "Germany","Portugal","United Kingdom","Belgium","Denmark","Spain","Ireland","Italy", "Greece","Austria","Turkey","Romania", "Hungary","Bulgaria","Croatia"))                          
   
    sliders = [
    {'steps':[
    {'method': 'update', 'label': '2021-11-08 12:00:00', 'args': [{'visible': [True, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-08 15:00:00', 'args': [{'visible': [False, True, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-08 18:00:00', 'args': [{'visible': [False, False, True, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-08 21:00:00', 'args': [{'visible': [False, False, False, True, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-09 00:00:00', 'args': [{'visible': [False, False, False, False, True, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-09 03:00:00', 'args': [{'visible': [False, False, False, False, False, True, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-09 06:00:00', 'args': [{'visible': [False, False, False, False, False, False, True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-09 09:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-09 12:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-09 15:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-09 18:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-09 21:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-10 00:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-10 03:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-10 06:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-10 09:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-10 12:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-10 15:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-10 18:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-10 21:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-11 00:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-11 03:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-11 06:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-11 09:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-11 12:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-11 15:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-11 18:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-11 21:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-12 00:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-12 03:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-12 06:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-12 09:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-12 12:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-12 15:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-12 18:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-12 21:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-13 00:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False]}]},
    {'method': 'update', 'label': '2021-11-13 03:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False]}]},
    {'method': 'update', 'label': '2021-11-13 06:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False]}]},
    {'method': 'update', 'label': '2021-11-13 09:00:00', 'args': [{'visible': [False, False, False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True]}]}
    ]}]
        
        
        
    
                       
                 
    if dropdown=="Netherlands" :
        fignl = go.Figure()
        for x in list(data_nl['dt_txt'].unique()):
            df11 = data_nl[data_nl['dt_txt'] == x]
            fignl.add_trace(go.Bar(x=df11['name'], y=df11['temp_c'], name=x))
        fignl.update_layout({'sliders': sliders})  
        #fig.update_layout(xaxis_range=[["Amsterdam", "Provincie Utrecht","Rotterdam","Middelburg","Gemeente Eindhoven","Maastricht","Gemeente Arnhem","Zwolle","Lelystad","Assen","Province of Groningen","Leeuwarden"]])
        fignl.update_xaxes(fixedrange=True)
        st.plotly_chart(fignl)
    if dropdown=="France" :
        figfr = go.Figure()
        for x in list(data_fr['dt_txt'].unique()):
            df12 = data_fr[data_fr['dt_txt'] == x]
            figfr.add_trace(go.Bar(x=df12['name'], y=df12['temp_c'], name=x))
        figfr.update_layout({'sliders': sliders})  
        figfr.update_xaxes(fixedrange=True)
        st.plotly_chart(figfr)                        
    if dropdown=="Germany" :
        figge = go.Figure()
        for x in list(data_ge['dt_txt'].unique()):
            df13 = data_ge[data_ge['dt_txt'] == x]
            figge.add_trace(go.Bar(x=df13['name'], y=df13['temp_c'], name=x))
        figge.update_layout({'sliders': sliders})    
        figge.update_xaxes(fixedrange=True)
        st.plotly_chart(figge)                       
    if dropdown=="Portugal" :
        figpt = go.Figure()
        for x in list(data_pt['dt_txt'].unique()):
            df14 = data_pt[data_pt['dt_txt'] == x]
            figpt.add_trace(go.Bar(x=df14['name'], y=df14['temp_c'], name=x))
        figpt.update_layout({'sliders': sliders}) 
        figpt.update_xaxes(fixedrange=True)
        st.plotly_chart(figpt)                            
    if dropdown=="United Kingdom" :
        figuk = go.Figure()
        for x in list(data_uk['dt_txt'].unique()):
            df15 = data_uk[data_uk['dt_txt'] == x]
            figuk.add_trace(go.Bar(x=df15['name'], y=df15['temp_c'], name=x))
        figuk.update_layout({'sliders': sliders})  
        figuk.update_xaxes(fixedrange=True)
        st.plotly_chart(figuk)                            
    if dropdown=="Belgium" :
        figbe = go.Figure()
        for x in list(data_be['dt_txt'].unique()):
            df16 = data_be[data_be['dt_txt'] == x]
            figbe.add_trace(go.Bar(x=df16['name'], y=df16['temp_c'], name=x))
        figbe.update_layout({'sliders': sliders})   
        fig.update_xaxes(fixedrange=True)
        st.plotly_chart(figbe)                          
    if dropdown=="Denmark" :
        figdk = go.Figure()
        for x in list(data_dk['dt_txt'].unique()):
            df17 = data_dk[data_dk['dt_txt'] == x]
            figdk.add_trace(go.Bar(x=df17['name'], y=df17['temp_c'], name=x))
        figdk.update_layout({'sliders': sliders})  
        figdk.update_xaxes(fixedrange=True)
        st.plotly_chart(figdk)                           
    if dropdown=="Spain" :
        figes = go.Figure()
        for x in list(data_es['dt_txt'].unique()):
            df18 = data_es[data_es['dt_txt'] == x]
            figes.add_trace(go.Bar(x=df18['name'], y=df18['temp_c'], name=x))
        figes.update_layout({'sliders': sliders}) 
        figes.update_xaxes(fixedrange=True)
        st.plotly_chart(figes)                            
    if dropdown=="Ireland" :
        figie= go.Figure()
        for x in list(data_ie['dt_txt'].unique()):
            df19 = data_ie[data_ie['dt_txt'] == x]
            figie.add_trace(go.Bar(x=df19['name'], y=df19['temp_c'], name=x))
        figie.update_layout({'sliders': sliders}) 
        figie.update_xaxes(fixedrange=True)
        st.plotly_chart(figie)                            
    if dropdown=="Italy" :
        figit = go.Figure()
        for x in list(data_it['dt_txt'].unique()):
            df20 = data_it[data_it['dt_txt'] == x]
            figit.add_trace(go.Bar(x=df20['name'], y=df20['temp_c'], name=x))
        figit.update_layout({'sliders': sliders}) 
        figit.update_xaxes(fixedrange=True)
        st.plotly_chart(figit)                           
    if dropdown=="Greece" :
        figgr = go.Figure()
        for x in list(data_gr['dt_txt'].unique()):
            df21 = data_gr[data_gr['dt_txt'] == x]
            figgr.add_trace(go.Bar(x=df21['name'], y=df21['temp_c'], name=x))
        figgr.update_layout({'sliders': sliders})  
        figgr.update_xaxes(fixedrange=True)
        st.plotly_chart(figgr)                            
    if dropdown=="Austria" : 
        figau = go.Figure()
        for x in list(data_au['dt_txt'].unique()):
            df22 = data_au[data_au['dt_txt'] == x]
            figau.add_trace(go.Bar(x=df22['name'], y=df22['temp_c'], name=x))
        figau.update_layout({'sliders': sliders})      
        figau.update_xaxes(fixedrange=True)
        st.plotly_chart(figau)                            
    if dropdown=="Turkey" :
        figtu = go.Figure()
        for x in list(data_tu['dt_txt'].unique()):
            df23 = data_tu[data_tu['dt_txt'] == x]
            figtu.add_trace(go.Bar(x=df23['name'], y=df23['temp_c'], name=x))
        figtu.update_layout({'sliders': sliders})   
        figtu.update_xaxes(fixedrange=True)
        st.plotly_chart(figtu)                            
    if dropdown=="Romania" :
        figro = go.Figure()
        for x in list(data_ro['dt_txt'].unique()):
            df24 = data_ro[data_ro['dt_txt'] == x]
            figro.add_trace(go.Bar(x=df24['name'], y=df24['temp_c'], name=x))
        figro.update_layout({'sliders': sliders})  
        figro.update_xaxes(fixedrange=True)
        st.plotly_chart(figro)                            
    if dropdown=="Hungary" :
        fighu = go.Figure()
        for x in list(data_hu['dt_txt'].unique()):
            df25 = data_hu[data_hu['dt_txt'] == x]
            fighu.add_trace(go.Bar(x=df25['name'], y=df25['temp_c'], name=x))
        fighu.update_layout({'sliders': sliders}) 
        fighu.update_xaxes(fixedrange=True)
        st.plotly_chart(fighu)                            
                         
    if dropdown=="Croatia" :  
        figcr = go.Figure()
        for x in list(data_cr['dt_txt'].unique()):
            df27 = data_cr[data_cr['dt_txt'] == x]
            figcr.add_trace(go.Bar(x=df27['name'], y=df27['temp_c'], name=x))
        figcr.update_layout({'sliders': sliders}) 
        figct.update_xaxes(fixedrange=True)
        st.plotly_chart(figcr)                        
                              
