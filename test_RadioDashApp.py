import pytest
from dash import Dash, html, dcc
import RadioDashApp as app

# Test for header presence
def test_header_is_present(dash_duo):
    dash_duo.start_server(app, timeout=60)
    header = dash_duo.find_element("H1")
    assert header is not None

# Test for graph presence
def test_graph_is_present(dash_duo):
    dash_duo.start_server(app, timeout=60)
    graph = dash_duo.find_element("graph-1")
    assert graph is not None

# Test for radio items presence
def test_radio_items_is_present(dash_duo):
    dash_duo.start_server(app, timeout=60)
    radio = dash_duo.find_element("region-selector")
    assert radio is not None