#FinancialReportController
from flask import Flask, render_template, request, send_file
from controller.presenter import Presenter
import config

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the home page."""
    return render_template('home.html')

@app.route('/print_presenter')
def print_presenter():
    """Handles the request to generate and download a PDF report."""
    presenter = Presenter()
    presenter.handle_request()
    return send_file(config.OUTPUT_PDF_PATH, as_attachment=True)

@app.route('/screen_presenter')
def screen_presenter():
    """Handles the request to display the report on the screen."""
    presenter = Presenter()
    data= presenter.handle_request()
    return render_template('screen_view.html', reports=data.table, file_data=data.text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
