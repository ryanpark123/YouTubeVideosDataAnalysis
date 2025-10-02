import matplotlib.pyplot as plt
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

df = pd.read_csv('output/USvideos_clean.csv')

category_counts = df['category_id'].value_counts()

top_categories = category_counts.head(10)
#plt.bar(top_categories.index, top_categories.values)
#plt.xticks(rotation=0)
#plt.title("Top 10 Trending Categories")
#plt.show()

app = dash.Dash(__name__)
fig = px.bar(top_categories, x=top_categories.index, y=top_categories.values)
fig.update_layout(
    xaxis_title="Video Category",
    yaxis_title="Number of Trending Videos",
    title="Top YouTube Categories"
)

app.layout = html.Div([dcc.Graph(figure=fig)])
app.run(debug=True)