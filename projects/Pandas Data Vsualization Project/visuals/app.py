import pandas as pd
import numpy as np
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("../data/quick_commerce_clean.csv")

df.columns = df.columns.str.strip().str.lower()

# =========================
# APP SETUP
# =========================
app = dash.Dash(__name__)
app.title = "Quick Commerce Dashboard"

# =========================
# LAYOUT
# =========================
app.layout = html.Div(style={'backgroundColor': '#0e0e0e', 'color': 'white'}, children=[

    html.H1("🚀 Executive Quick Commerce Dashboard", style={'textAlign': 'center'}),

    # ================= FILTERS =================
    html.Div([
        html.Div([
            html.Label("Company"),
            dcc.Dropdown(df['company'].unique(), multi=True, id='company_filter')
        ], style={'width': '24%', 'display': 'inline-block'}),

        html.Div([
            html.Label("City"),
            dcc.Dropdown(df['city'].unique(), multi=True, id='city_filter')
        ], style={'width': '24%', 'display': 'inline-block'}),

        html.Div([
            html.Label("Category"),
            dcc.Dropdown(df['product_category'].unique(), multi=True, id='cat_filter')
        ], style={'width': '24%', 'display': 'inline-block'}),

        html.Div([
            html.Label("Payment Method"),
            dcc.Dropdown(df['payment_method'].unique(), multi=True, id='pay_filter')
        ], style={'width': '24%', 'display': 'inline-block'}),
    ]),

    # ================= KPI ROW =================
    html.Div(id='kpi_row', style={'display': 'flex', 'justifyContent': 'space-around', 'marginTop': 20}),

    # ================= CHARTS =================
    html.Div([
        dcc.Graph(id='revenue_chart'),
        dcc.Graph(id='category_chart'),
    ], style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr'}),

    html.Div([
        dcc.Graph(id='city_chart'),
        dcc.Graph(id='delivery_chart'),
    ], style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr'}),

])


# =========================
# FILTER FUNCTION
# =========================
def filter_data(company, city, cat, pay):

    dff = df.copy()

    if company:
        dff = dff[dff['company'].isin(company)]
    if city:
        dff = dff[dff['city'].isin(city)]
    if cat:
        dff = dff[dff['product_category'].isin(cat)]
    if pay:
        dff = dff[dff['payment_method'].isin(pay)]

    return dff


# =========================
# CALLBACK
# =========================
@app.callback(
    Output('kpi_row', 'children'),
    Output('revenue_chart', 'figure'),
    Output('category_chart', 'figure'),
    Output('city_chart', 'figure'),
    Output('delivery_chart', 'figure'),
    Input('company_filter', 'value'),
    Input('city_filter', 'value'),
    Input('cat_filter', 'value'),
    Input('pay_filter', 'value')
)
def update_dashboard(company, city, cat, pay):
    try:
        dff = filter_data(company, city, cat, pay)

        # ================= KPIs =================
        total_orders = len(dff)
        total_revenue = dff['order_value'].sum() if not dff.empty else 0
        avg_order_value = dff['order_value'].mean() if not dff.empty else 0
        avg_delivery = dff['delivery_time_min'].mean() if not dff.empty else 0

        # Handle both boolean (True/False) and string ('Yes'/'No') columns
        if dff.empty:
            refund_rate = 0.0
        elif dff['refund_requested'].dtype == object:
            refund_rate = (dff['refund_requested'].str.strip().str.lower() == 'yes').mean() * 100
        else:
            refund_rate = dff['refund_requested'].mean() * 100

        top_city     = dff['city'].value_counts().idxmax() if not dff.empty else 'N/A'
        top_category = dff['product_category'].value_counts().idxmax() if not dff.empty else 'N/A'

        # Safe formatting (guard NaN)
        def fmt(val, spec):
            try:
                return format(val, spec)
            except (ValueError, TypeError):
                return 'N/A'

        kpis = html.Div([
            html.Div(f"📦 Orders: {total_orders:,}"),
            html.Div(f"💰 Revenue: {fmt(total_revenue, ',.0f')}"),
            html.Div(f"🧾 Avg Order: {fmt(avg_order_value, '.2f')}"),
            html.Div(f"⏱ Avg Delivery: {fmt(avg_delivery, '.2f')} min"),
            html.Div(f"🔁 Refund %: {fmt(refund_rate, '.2f')}%"),
            html.Div(f"📍 Top City: {top_city}"),
            html.Div(f"🍔 Top Category: {top_category}"),
        ], style={'display': 'flex', 'gap': '20px', 'justifyContent': 'center'})

        # ================= CHARTS =================
        fig1 = px.bar(
            dff.groupby('company')['order_value'].sum().reset_index(),
            x='company', y='order_value',
            template='plotly_dark',
            title='Revenue by Company'
        )

        fig2 = px.bar(
            dff['product_category'].value_counts().reset_index(),
            x='product_category', y='count',
            template='plotly_dark',
            title='Orders by Category'
        )

        fig3 = px.bar(
            dff['city'].value_counts().head(10).reset_index(),
            x='city', y='count',
            template='plotly_dark',
            title='Top Cities by Orders'
        )

        fig4 = px.histogram(
            dff,
            x='delivery_time_min',
            nbins=30,
            template='plotly_dark',
            title='Delivery Time Distribution'
        )

        return kpis, fig1, fig2, fig3, fig4

    except Exception as e:
        import traceback
        traceback.print_exc()   # prints full error to terminal
        empty_fig = px.bar(title=f'Error: {str(e)}', template='plotly_dark')
        error_msg = html.Div(f"⚠️ Error: {str(e)}", style={'color': 'red'})
        return error_msg, empty_fig, empty_fig, empty_fig, empty_fig


# =========================
# RUN APP
# =========================
if __name__ == '__main__':
    app.run(debug=True)