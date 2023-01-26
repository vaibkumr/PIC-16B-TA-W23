import numpy as np

# https://plotly.com/python/plotly-express/

s = """Basics: scatter, line, area, bar, funnel, timeline
Part-of-Whole: pie, sunburst, treemap, icicle, funnel_area
1D Distributions: histogram, box, violin, strip, ecdf
2D Distributions: density_heatmap, density_contour
Matrix or Image Input: imshow
3-Dimensional: scatter_3d, line_3d
Multidimensional: scatter_matrix, parallel_coordinates, parallel_categories
Tile Maps: scatter_mapbox, line_mapbox, choropleth_mapbox, density_mapbox
Outline Maps: scatter_geo, line_geo, choropleth
Polar Charts: scatter_polar, line_polar, bar_polar
Ternary Charts: scatter_ternary, line_ternary"""

lines = [l.split(":")[-1].strip() for l in s.split("\n")]
plots = [plot.strip() for plot in ",".join(lines).split(",")]
print(np.random.choice(plots))