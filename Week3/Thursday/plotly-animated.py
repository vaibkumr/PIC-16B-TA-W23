import plotly.express as px

# https://www.aei.org/carpe-diem/animated-chart-of-the-day-worlds-top-ten-billionaires-2000-to-2022/

df = px.data.gapminder()
print(df.columns)
fig = px.scatter(
    df, 
    x="gdpPercap", 
    y="lifeExp", 
    animation_frame="year", 
    size="pop", 
    color="continent", 
    hover_name="country",
    log_x=True, 
    size_max=55, 
    range_x=[100,100000], 
    range_y=[25,90]
)

fig.show()