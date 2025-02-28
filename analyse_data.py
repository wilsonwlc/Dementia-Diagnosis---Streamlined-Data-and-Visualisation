import dash
from dash import dcc, html, dash_table
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output


app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Dementia Diagnoses Dashboard"),
    dcc.Interval(id="interval-update", interval=30*60*1000, n_intervals=0),

    html.Div([
        html.H3("Age Group"),  # Heading above the dropdown
        dcc.Dropdown(id="age-group-selector", value=None, clearable=False),
    ], style={"padding": "20px 0"}),

    html.Div([

        html.Div([
            html.H3("Table"),
            dash_table.DataTable(
                id="summary-table",
                style_table={'overflowX': 'auto'},
                style_cell={"whiteSpace": "normal", "height": "auto", "textAlign": "center"},
                style_data_conditional=[
                    {"if": {"column_id": "month"}, "width": "80px"},
                    {"if": {"column_id": "year"}, "width": "80px"},
                    {"if": {"column_id": "Male"}, "width": "100px"},
                    {"if": {"column_id": "Female"}, "width": "100px"}])
        ], style={"width": "48%", "display": "inline-block", "verticalAlign": "top"}),

        html.Div(style={"width": "4%"}),

        html.Div([
            html.H3("Graph"),
            dcc.Graph(id="diagnosis-trend")
        ], style={"width": "48%", "display": "inline-block", "verticalAlign": "top"})

    ], style={"display": "flex", "justify-content": "space-between"})
])


def load_data():
    file_path = "dataset.xlsx"
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    df["year_month"] = df["year"].astype(str) + "-" + df["month_num"].astype(str).str.zfill(2)
    df["month"] = df["month"].str.capitalize()
    return df


@app.callback(
    Output("age-group-selector", "options"),
    Output("age-group-selector", "value"),
    Input("interval-update", "n_intervals")
)
def update_dropdown(_):
    df = load_data()
    options = [{"label": ag, "value": ag} for ag in df["age_gp"].unique()]
    return options, df["age_gp"].unique()[0]  # Default value: 0-39


def check_for_update():
    try:
        with open("update_signal.txt", "r") as signal_file:
            last_update_time = signal_file.read().strip()
            return last_update_time
    except FileNotFoundError:
        return None


# Callback to update table and graph
@app.callback([Output("summary-table", "data"),
               Output("summary-table", "columns"),
               Output("diagnosis-trend", "figure")],
              [Input("age-group-selector", "value"),
               Input("interval-update", "n_intervals")])
def update_dashboard(selected_age_group, _):

    df = load_data()
    filtered_df = df[df["age_gp"] == selected_age_group]
    column_names = {"year": "Year", "month": "Month", "Male": "Male Diagnoses", "Female": "Female Diagnoses"}
    summary_table = filtered_df.rename(columns=column_names)[["Year", "Month", "Male Diagnoses", "Female Diagnoses"]]

    table_data = summary_table.to_dict("records")
    table_columns = [{"name": col, "id": col} for col in summary_table.columns]

    fig = px.line(
        filtered_df, x="year_month", y=["Male", "Female"],
        markers=True,
        labels={"value": "Number of Diagnoses", "year_month": "Year-Month", "variable": "Gender"},
        title="Dementia Diagnoses Trend"
    )
    fig.update_layout(xaxis_tickangle=-45)

    return table_data, table_columns, fig


if __name__ == "__main__":
    app.run_server(debug=True)
