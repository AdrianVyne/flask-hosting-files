from flask import Flask, render_template, send_from_directory, send_file
import os

app = Flask(__name__)

MOVIE_FOLDER = 'E:/New folder'

@app.route('/')
def index():
    movie_folders = [folder for folder in os.listdir(MOVIE_FOLDER) if os.path.isdir(os.path.join(MOVIE_FOLDER, folder))]
    return render_template('index.html', movie_folders=movie_folders)

@app.route('/movies/<path:folder_name>')
def serve_movie(folder_name):
    folder_path = os.path.join(MOVIE_FOLDER, folder_name)
    movie_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.mkv', '.mp4'))]

    if not movie_files:
        return "No movie file found in the specified folder."

    movie_filename = movie_files[0]
    return send_file(os.path.join(folder_path, movie_filename), as_attachment=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
