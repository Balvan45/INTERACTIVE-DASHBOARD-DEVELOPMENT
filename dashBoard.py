import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

df = pd.read_csv("sales_data.csv")

app = dash.Dash(__name__)


region_sales = df.groupby("region")["sales"].sum().reset_index()
region_fig = px.bar(region_sales, x="region", y="sales",
                    title="Total Sales by Region", color="region")

product_avg = df.groupby("product")["sales"].mean().reset_index()
product_fig = px.pie(product_avg, names="product", values="sales",
                     title="Average Sales by Product")

top_sales = df.sort_values(by="sales", ascending=False).head(5)
top_fig = px.bar(top_sales, x="product", y="sales",
                 title="Top 5 Sales Records")

app.layout = html.Div([
    html.H1("Interactive Sales Analytics Dashboard",
            style={"textAlign": "center"}),

    dcc.Graph(figure=region_fig),
    dcc.Graph(figure=product_fig),
    dcc.Graph(figure=top_fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
