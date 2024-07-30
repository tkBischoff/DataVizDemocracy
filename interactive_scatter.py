import pandas as pd
import numpy as np
import geopandas as gpd
import plotly.express as px
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import plotly.graph_objects as go
import cv2
import os
import plotly.io as pio
# co2_df = pd.read_pickle("./data/co2_df.pkl")
# rel_df = pd.read_pickle("./data/rel_df.pkl")
# co2_rel_df = pd.read_pickle("./data/co2_rel_df.pkl")

# zabi_scatter(co2_df, "edi", "CO2", title="Electoral Democracy Index vs. CO2 Emissions", year=2000, size="pop", color="continent", uselogy=True)
# zabi_scatter(co2_rel_df, "CO2", "HHI", title="CO2 Emissions vs. Religous Mixedness", year = 2010, size="pop", color="primary_rel", uselogx=True)
# zabi_scatter(rel_df, "edi", "nonreligpct", year=int(year), size="pop", color= "continent", title="Electoral Democracy Index vs. Non-Religious", uselogy=True, savedontshow=True, location="relig_scatter_plots")
# zabi_scatter(rel_df, "edi", "HHI", year=int(year), size="pop", color= "continent", title="Electoral Democracy Index vs. Religious Diversity", uselogy=False, savedontshow=True, location="relig_scatter_plots")
def zabi_scatter(df: pd.DataFrame, name, x: str, y: str, year: int, size: str, color: str, title: str, uselogx=False, uselogy=False, savedontshow=False, location=""):
    if year != 0:
        df = df[df["Year"]==year]
    if size is not None:
        df[size] = df[size].apply(lambda x: 60000000 if x<60000000 else x) / 1e6
    fig = px.scatter(
    df,
    x=x,
    y=y,
    size=size,  # Use the scaled population
    color=color,
    hover_name='Entity',
    size_max=40, # Increase size_max to make points larger -- 200 worked the best
    title=f"{title} {year}",
    )

    # Update the layout
    if uselogx and uselogy:
        fig.update_layout(
            xaxis_title=x,
            yaxis_title=y,
            legend_title=color,
            template='plotly',
            height=800,
            yaxis_type="log",
            xaxis_type="log"
        )
    elif uselogx:
        fig.update_layout(
            xaxis_title=x,
            yaxis_title=y,
            legend_title=color,
            template='plotly',
            height=800,
            xaxis_type="log"
        )
    elif uselogy:
        fig.update_layout(
            xaxis_title=x,
            yaxis_title=y,
            legend_title=color,
            template='plotly',
            height=800,
            yaxis_type="log"
        )        
    fig.update_layout(
        width=700,
        height=500
    )

    # Show the plot
    pio.write_html(fig, f"plots/{name}.html")
    fig.show()
