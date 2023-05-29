import pandas as pd
import geopandas as gpd
import folium

input=pd.read_csv('C:/Users/Impana/Downloads/archive/world_population.csv')

print(input)


world=gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
new_input=world.merge(input, how='left', left_on=['name'], right_on=['Country/Territory'])
final_input=new_input.dropna(subset=['2022 Population'])

my_map = folium.Map()
folium.Choropleth(
    geo_data=final_input,
    name="choropleth",
    data=final_input,
    columns=["Country/Territory", "2022 Population"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="2022 Populations",
).add_to(my_map)
my_map.save('1pop.html')