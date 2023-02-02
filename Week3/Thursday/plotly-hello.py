import plotly.express as px

# https://plotly.com/python/plotly-express/

fig = px.line(x=["a","b","c"], y=[1,3,2], title="Hellow world!")
# fig.show()

# # Cross language support
out = fig.show("json")
print(out)