from flask import Blueprint, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from .models import detect_defects

main_routes = Blueprint('main_routes', __name__)

# Homepage route
@main_routes.route('/')
def index():
    return render_template('index.html')

# Handle image upload and redirect to result page
@main_routes.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect(url_for('main_routes.index'))

    image_file = request.files['image']
    if image_file.filename == '':
        return redirect(url_for('main_routes.index'))

    # Save the uploaded image temporarily
    upload_folder = os.path.join(os.getcwd(), 'uploads')
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, secure_filename(image_file.filename))
    image_file.save(file_path)

    # Detect defects (replace with your model logic)
    result = detect_defects(file_path)

    # Clean up: Delete the uploaded image after processing
    os.remove(file_path)

    # Redirect to result page and pass data via query parameters
    return redirect(url_for('main_routes.result', result=result))

# Result page route
@main_routes.route('/result')
def result():
    result_data = request.args.get('result', "No defects detected")  # Default message
    return render_template('result.html', result=result_data)

# Dashboard page route
@main_routes.route('/dashboard')
def dashboard():
    dashboard_data = request.args.get('dashboard', "Dashboard Metrics Unavailable")
    return render_template('dashboard.html', result=dashboard_data)
