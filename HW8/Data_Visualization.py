import csv
from BeautifulSoup import BeautifulSoup
import geopandas as gp
import pandas as pd
import os
import json
import pylab as pl
import numpy as np
import statsmodels.api as sm

s = json.load( open(os.getenv('PUI2015')+'/fbb_matplotlibrc.json') )


# Read in carbon emissions data by county

# carbon = gp.GeoDataFrame.from_csv(os.getenv('PUI2015')+'/data/CountiesBySector.csv')
carbon = csv.reader(open(os.getenv('PUI2015')+'/data/CountiesBySector.csv'), delimiter=",")

ce = {}

for row in carbon:
    try:
        fips = row[3]
        carbon_capita = float(row[18])
        ce[fips] = carbon_capita
    except:
        pass
print ce


# Load the SVG map
svg = open(os.getenv('PUI2015')+'/data/USA_Counties_with_FIPS_and_names.svg','r').read()

# Load into Beautiful Soup
soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])

# Find counties
paths = soup.findAll('path')

# Map colors
colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]

# County style
path_style = 'font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'


# Color the counties based on carbon emission per capita
for p in paths:
     
    if p['id'] not in ["State_Lines", "separator"]:
        # pass
        try:
            carbon_capita = ce[p['id']]
        except:
            continue
             
        if carbon_capita > 10:
            color_class = 5
        elif carbon_capita > 8:
            color_class = 4
        elif carbon_capita > 6:
            color_class = 3
        elif carbon_capita > 4:
            color_class = 2
        elif carbon_capita > 2:
            color_class = 1
        else:
            color_class = 0
 
        color = colors[color_class]
        p['style'] = path_style + color

# Output map
fo = open(os.getenv('PUI2015')+'/data/USA_Counties_with_FIPS_and_names.svg', "wb")
fo.write(soup.prettify());
fo.close()

