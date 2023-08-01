'''API for face recognition'''
import io
from flask import Flask, request, jsonify, send_file
import face_recognition
from PIL import Image, ImageDraw

app = Flask(__name__)

@app.route('/detect_faces', methods=['POST'])
def detect_faces():
    '''Find a face in an image'''
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request."}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected."}), 400

    if file:
        img = face_recognition.load_image_file(file)
        face_locations = face_recognition.face_locations(img)

        if len(face_locations) > 0:
            return jsonify({"message": "positive", "no_of_faces": len(face_locations)})
        else:
            return jsonify({"message": "negative", "no_of_faces": len(face_locations)})

    return jsonify({"error": "An error occurred."}), 500

@app.route('/locate_faces', methods=['POST'])
def locate_faces():
    '''Locate faces in an image'''
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request."}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected."}), 400

    if file:
        img = face_recognition.load_image_file(file)
        face_locations = face_recognition.face_locations(img)

        pil_image = Image.open(file)
        draw = ImageDraw.Draw(pil_image)

        for (top, right, bottom, left) in face_locations:
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

        # Save to a file-like object
        img_byte_array = io.BytesIO()
        pil_image.save(img_byte_array, format='JPEG')
        img_byte_array.seek(0)

        return send_file(img_byte_array, mimetype='image/jpeg')

    return jsonify({"error": "An error occurred."}), 500

if __name__ == "__main__":
    app.run(debug=True)
