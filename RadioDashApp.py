from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv("data.csv")

regions = ['north', 'east', 'south', 'west', 'all']

def filter_data(region):
    if region == 'all':
        return df
    else:
        return df[df['region'] == region]


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Soul Foods Sales Analysis: Impact of Pink Morsel Price Increase',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    
    # Radio button to select region
    dcc.RadioItems(
        id='region-selector',
        options=[{'label': region.capitalize(), 'value': region} for region in regions],
        value='all',  # Default selection
        style={'color': colors['text']},
        labelStyle={'display': 'inline-block', 'margin-right': '10px'}
    ),

    # Line graph that updates based on region selection
    dcc.Graph(id='graph-1')
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
    fig.add_vline(x="2021-01-15", line_dash="dash", line_color="yellow", 
                  label=dict(
            text="15 - Jan - 2021",
            textposition="top center",
            font=dict(size=20, family="Times New Roman"),
        ),
        fillcolor="green",
        line_width=3
    )

    # Update the layout with background and text colors
    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],
        xaxis_title="Date",
        yaxis_title="Sales"
    )

    return fig


fig = px.line(df, x="date", y="sales")
fig.add_vline(x="2021-01-15", line_dash="dash", line_color="yellow", 
              label=dict(
        text="15 - jan - 2021",
        textposition="top center",
        font=dict(size=20, family="Times New Roman"),
    ),
    fillcolor="green",
    line_width=3
)

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])


if __name__ == '__main__':
    app.run(debug=True)


