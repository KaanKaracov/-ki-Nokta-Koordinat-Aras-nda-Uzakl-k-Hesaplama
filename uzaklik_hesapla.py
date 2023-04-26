import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from geopy.distance import geodesic

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("İki Nokta Arasındaki Uzaklık Hesaplayıcı"),
        html.Div(
            children=[
                html.Label("Başlangıç Noktası Latitude (Enlem):"),
                dcc.Input(
                    id="start-lat",
                    type="number",
                    placeholder="Enlem girin...",
                    value=0,
                    step=0.1,
                ),
                html.Label("Başlangıç Noktası Longitude (Boylam):"),
                dcc.Input(
                    id="start-lon",
                    type="number",
                    placeholder="Boylam girin...",
                    value=0,
                    step=0.1,
                ),
                html.Label("Hedef Noktası Latitude (Enlem):"),
                dcc.Input(
                    id="end-lat",
                    type="number",
                    placeholder="Enlem girin...",
                    value=0,
                    step=0.1,
                ),
                html.Label("Hedef Noktası Longitude (Boylam):"),
                dcc.Input(
                    id="end-lon",
                    type="number",
                    placeholder="Boylam girin...",
                    value=0,
                    step=0.1,
                ),
                html.Button("Hesapla", id="calculate-button"),
                html.Div(id="result"),
            ],
            style={"max-width": "500px", "margin": "auto"},
        ),
    ],
    style={"text-align": "center", "padding-top": "50px"},
)


@app.callback(
    Output("result", "children"),
    [Input("calculate-button", "n_clicks")],
    [
        Input("start-lat", "value"),
        Input("start-lon", "value"),
        Input("end-lat", "value"),
        Input("end-lon", "value"),
    ],
)
def calculate_distance(n_clicks, start_lat, start_lon, end_lat, end_lon):
    if n_clicks:
        start = (start_lat, start_lon)
        end = (end_lat, end_lon)
        distance = geodesic(start, end).kilometers
        return html.Div(
            children=[
                html.H3("Uzaklık Hesaplandı:"),
                html.P(
                    f"Başlangıç Noktası: Latitude={start_lat}, Longitude={start_lon}"
                ),
                html.P(f"Hedef Noktası: Latitude={end_lat}, Longitude={end_lon}"),
                html.P(f"Uzaklık: {distance} kilometre"),
            ],
            style={"margin-top": "30px"},
        )


if __name__ == "__main__":
    app.run_server(debug=True)
