from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Define color schemes for the layout
colors = {
    'background': '#2c3e50',  # Dark blue
    'text': '#ECF0F1',        # Light grey
    'graph_bg': '#34495E',    # Medium blue
    'accent': '#E74C3C'       # Red accent
}

df = pd.read_csv("data.csv")

regions = ['north', 'east', 'south', 'west', 'all']

def filter_data(region):
    if region == 'all':
        return df
    else:
        return df[df['region'] == region]


# Layout of the app with enhanced styling
app.layout = html.Div(style={'backgroundColor': colors['background'], 'fontFamily': 'Arial'}, children=[
    html.H1(
        children='Soul Foods Sales Analysis: Impact of Pink Morsel Price Increase',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'fontSize': '36px',
            'padding': '20px'
        }
    ),
    
    # Radio button to select region with enhanced styling
    html.Div([
        dcc.RadioItems(
            id='region-selector',
            options=[{'label': region.capitalize(), 'value': region} for region in regions],
            value='all',  # Default selection
            style={
                'color': colors['text'], 
                'fontSize': '18px'
            },
            labelStyle={
                'display': 'inline-block', 
                'margin-right': '20px',
                'padding': '10px',
                'backgroundColor': '#34495E',  # Dark blue background
                'borderRadius': '10px',
                'cursor': 'pointer'
            }
        )
    ], style={'textAlign': 'center', 'marginBottom': '30px'}),

    # Line graph that updates based on region selection
    dcc.Graph(id='graph-1', style={'height': '500px'})
])

@app.callback(
    Output('graph-1', 'figure'),
    Input('region-selector', 'value')
)
def update_graph(selected_region):
    # Filter the data based on the selected region
    filtered_df = filter_data(selected_region)

    # Create a line chart with the filtered data
    fig = px.line(filtered_df, x="date", y="sales")
    
    # Add a vertical line for the price increase date
    fig.add_vline(x="2021-01-15", line_dash="dash", line_color=colors['accent'], 
                  label=dict(
            text="15 - Jan - 2021",
            textposition="top center",
            font=dict(size=20, family="Courier New", color=colors['accent']),
        ),
        fillcolor=colors['graph_bg'],
        line_width=3
    )

    # Update the layout with enhanced styling
    fig.update_layout(
        plot_bgcolor=colors['graph_bg'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],
        xaxis_title="Date",
        yaxis_title="Sales",
        xaxis=dict(showline=True, showgrid=False, showticklabels=True, linecolor=colors['text'], ticks='outside', tickfont=dict(size=14, color=colors['text'])),
        yaxis=dict(showline=True, showgrid=False, showticklabels=True, linecolor=colors['text'], ticks='outside', tickfont=dict(size=14, color=colors['text'])),
        title_font=dict(size=22, color=colors['text'], family="Arial"),
        hoverlabel=dict(bgcolor=colors['graph_bg'], font_size=16, font_family="Arial"),
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)


