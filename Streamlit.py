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

# In[ ]:


#sidebar
st.set_page_config(layout="wide")
rad = st.sidebar.radio(options=('Home','Current weather map','Plotting current weather','Forecast weather map','Plotting forecast weather'),label='Selecteer')

st.sidebar.markdown('#')
st.sidebar.markdown('#')

st.sidebar.subheader('Gemaakt door:')
st.sidebar.write('Mara van Boeckel')
st.sidebar.write('Maarten van der Veer')


# In[ ]:


if rad == 'Plotting current weather':

    current_weather = pd.read_csv('Weather_compleet.csv')
    
    city_color_map = {'Netherlands': 'rgb(240,128,128)','United Kingdom': 'rgb(135,206,235)','France': 'rgb(216, 191,216)',
                      'Belgium': 'rgb(127,255,212)','Denmark': 'rgb(238,106,80)','Portugal': 'rgb(205,41,144)',
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
                       labels={'humidity':'Humidity', 'country':'Country'})
    fig1.update_layout(title = "Humidity levels for each country", yaxis_title="Frequency")
    fig1.update_layout({'updatemenus':[{'type': "dropdown",'showactive': True,'active': 0,'buttons': dropdown_buttons}]})
    #fig.update_xaxes(scaleanchor = "x",scaleratio = 1)
    st.plotly_chart(fig)


    fig2 = px.box(data_frame=current_weather, x='country',y='temp_c', title="Boxplots of the temperature per country ",
                 labels={"temp_c": "Temperature (°C)",
                         "country": "Country"},
    category_orders = {'country':['Netherlands','France','Germany','Portugal','United Kingdom','Belgium','Denmark','Spain','Ireland','Italy','Greece','Croatia','Austria','Turkey','Romania','Hungary','Bulgaria']},
                color='country',color_discrete_map =city_color_map)

    st_plotly_chart(fig2)


    fig3=px.scatter(current_weather,x='lat',y='temp_c',color='country',color_discrete_map =city_color_map,trendline="ols",trendline_scope='overall',trendline_color_override="grey",title='nog bedenken',labels={'lat':'Latitude','temp_c':'Temperature (°C)'})
    st_plotly_chart(fig3)
    
    
    model1=ols('temp_c~lat',data=current_weather)
    model1=model1.fit()
    print(model1.summary())


# In[ ]:


if rad == 'Current weather map':
    
    current_weather = pd.read_csv('Weather_compleet.csv')
    
    def colorspressure(pressure):
        if pressure < 1009:
            color = 'blue'
            return color
        elif pressure >= 1009 and pressure < 1022:
            color = 'green'
            return color
        elif pressure >= 1022:
            color = 'red'
            return color


    def colorstemp(temp):
        if temp < 10:
            color = 'blue'
            return color
        elif temp >= 10 and temp < 20:
            color = 'orange'
            return color
        elif temp >= 20 and temp <28:
            color = 'orange'
            return color
        elif temp >=28:
            color = 'red'
            return color

    current_weather_map = folium.map(location=[52.0893191, 5.1101691], zoom_start = 4)



    data = ['Measurements','Wind','Temperature','Pressure','"feels like" temperature']



    effecten = [folium.FeatureGroup(name=x)for x in data]
    tooltip = "Click for information"



    for row in current_weather.iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        popup = ('<strong>' + row_values['City'] + '</strong>' + '<br>'+
        'Temperature: '+ str(round(row_values['temp_c'],2)) + '<br>'+
        'Windspeed: ' + str(round(row_values['speed'],2)) + '<br>' +
        'Pressure: ' + str(round(row_values['pressure'],2)) + '<br>'+
        'Rain: ' + str(row_values['rain']) + '<br>' +
        'Sunrise: ' + str(row_values['sunrise'],) + '<br>' +
        'Sunset: ' + str(row_values['sunset']) + '<br>')
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
        marker = folium.Marker(location=location,tooltip = tooltip)
        marker.add_to(effecten[2])
        effecten[2].add_to(current_weather_map)

    for row in current_weather.iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.CircleMarker(location=location,tooltip = str(round(row_values['pressure'],2)),radius=6,fill=True,opacity=1,color=colorspressure(row_values['pressure']))
        marker.add_to(effecten[3])
        effecten[3].add_to(current_weather_map)

    for row in current_weather.iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.CircleMarker(location=location,tooltip = str(round(row_values['feels_like_c'],2)),radius=6,fill=True,opacity=1,color=colorstemp(row_values['feels_like_c']))
        marker.add_to(effecten[4])
        effecten[4].add_to(current_weather_map)



    evenaar=[[-0,-720], [0,720]]



    folium.LayerControl(position='topleft').add_to(current_weather_map)

    folium.PolyLine(evenaar,color="red").add_to(current_weather_map)

    folium_static(current_weather_map)


# In[ ]:


if rad == 'Weather forecast map':
    
    forecast_weather = pd.read_csv('forecast_sorted.csv')
    
    map = folium.Map(location=[52.0893191, 5.1101691], zoom_start = 4)



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
    popup = ('<strong>' + row_values['name'] + '</strong>' + '<br>'+
                ' Temperature: '+ str(round(row_values['temp_c'],2))+ '°C' + '<br>'+
                'Windspeed: ' + str(round(row_values['speed'],2)) + 'km/h'+ '<br>' +
                'Pressure: ' + str(round(row_values['pressure'],2))+ 'hPa' + '<br>'+
                'Sunrise: ' + str(row_values['sunrise'],) + 'UTC'+ '<br>' +
                'Sunset: ' + str(row_values['sunset'])+ 'UTC' + '<br>')
    start=147


    for row in forecast_weather.iloc[start*0:start*1].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[0])
        effecten[0].add_to(map)


    for row in forecast_weather.iloc[start*1:start*2].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[1])
        effecten[1].add_to(map)

    for row in forecast_weather.iloc[start*2:start*3].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[2])
        effecten[2].add_to(map)


    for row in forecast_weather.iloc[start*3:start*4].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[3])
        effecten[3].add_to(map)

    for row in forecast_weather.iloc[start*4:start*5].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[4])
        effecten[4].add_to(map)

    for row in forecast_weather.iloc[start*5:start*6].iterrows():
        row_values=row[1]
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
        location=[row_values['lat'], row_values['lon']]

        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[7])
        effecten[7].add_to(map)

    for row in forecast_weather.iloc[start*8:start*9].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[8])
        effecten[8].add_to(map)


    for row in forecast_weather.iloc[start*9:start*10].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[9])
        effecten[9].add_to(map)


    for row in forecast_weather.iloc[start*10:start*11].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[10])
        effecten[10].add_to(map)

    for row in forecast_weather.iloc[start*11:start*12].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[11])
        effecten[11].add_to(map)

    for row in forecast_weather.iloc[start*12:start*13].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[12])
        effecten[12].add_to(map)

    for row in forecast_weather.iloc[start*13:start*14].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[13])
        effecten[13].add_to(map)

    for row in forecast_weather.iloc[start*14:start*15].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[14])
        effecten[14].add_to(map)

    for row in forecast_weather.iloc[start*15:start*16].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[15])
        effecten[15].add_to(map)


    for row in forecast_weather.iloc[start*16:start*17].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[16])
        effecten[16].add_to(map)

    for row in forecast_weather.iloc[start*17:start*18].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[17])
        effecten[17].add_to(map)

    for row in forecast_weather.iloc[start*18:start*19].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[18])
        effecten[18].add_to(map)

    for row in forecast_weather.iloc[start*19:start*20].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[19])
        effecten[19].add_to(map)

    for row in forecast_weather.iloc[start*20:start*21].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[20])
        effecten[20].add_to(map)

    for row in forecast_weather.iloc[start*21:start*22].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[21])
        effecten[21].add_to(map)

    for row in forecast_weather.iloc[start*22:start*23].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[22])
        effecten[22].add_to(map)

    for row in forecast_weather.iloc[start*23:start*24].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[23])
        effecten[23].add_to(map)

    for row in forecast_weather.iloc[start*24:start*25].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[24])
        effecten[24].add_to(map)



    for row in forecast_weather.iloc[start*25:start*26].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[25])
        effecten[25].add_to(map)


    for row in forecast_weather.iloc[start*26:start*27].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[26])
        effecten[26].add_to(map)    


    for row in forecast_weather.iloc[start*27:start*28].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[27])
        effecten[27].add_to(map)    

    for row in forecast_weather.iloc[start*28:start*29].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[28])
        effecten[28].add_to(map)       

    for row in forecast_weather.iloc[start*29:start*30].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[29])
        effecten[29].add_to(map)      

    for row in forecast_weather.iloc[start*30:start*3].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[30])
        effecten[30].add_to(map)  

    for row in forecast_weather.iloc[start*31:start*32].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[31])
        effecten[31].add_to(map)  

    for row in forecast_weather.iloc[start*32:start*33].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[32])
        effecten[32].add_to(map) 

    for row in forecast_weather.iloc[start*33:start*34].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[33])
        effecten[33].add_to(map)  


    for row in forecast_weather.iloc[start*34:start*35].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[34])
        effecten[34].add_to(map)   


    for row in forecast_weather.iloc[start*35:start*36].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[35])
        effecten[35].add_to(map) 

    for row in forecast_weather.iloc[start*36:start*37].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[36])
        effecten[36].add_to(map)

    for row in forecast_weather.iloc[start*37:start*38].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[37])
        effecten[37].add_to(map) 

    for row in forecast_weather.iloc[start*38:start*39].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[38])
        effecten[38].add_to(map) 

    for row in forecast_weather.iloc[start*39:start*40].iterrows():
        row_values=row[1]
        location=[row_values['lat'], row_values['lon']]
        marker = folium.Marker(location=location,popup=popup,tooltip = tooltip)
        marker.add_to(effecten[39])
        effecten[39 ].add_to(map)


    folium.LayerControl(position='topleft', title='Dagen').add_to(map)


    map
    
    


# In[ ]:



if rad == 'Plotting weather forecast':

    fig4 = go.Figure()
    for x in list(forecast['Date'].unique()):
            df11 = forecast[forecast['Date'] == x]
            fig4.add_trace(go.Bar(x=df11['name'], y=df11['temp_c'], name=x))

    hour_to_filter = st.slider('Date', '2021-11-08 12:00:00', '2021-11-13 09:00:00', '2021-11-08 12:00:00')  
    filtered_data = Forecast_compleet[Forecast_compleet['Date']== hour_to_filter]        
    st.map(filtered_data)

