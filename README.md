Certainly! Here's a `README.md` for the `find-face` API:

---

# Find-Face API

The Find-Face API provides endpoints for detecting and marking faces within uploaded images. Built with Flask and utilizing the face_recognition library, the API offers a straightforward approach to integrate face detection and marking into your applications.

## Endpoints

1. **/find_face**
    - Detects if the uploaded image contains a human face.
    - **Method**: POST
    - **Response**: 'Positive' if a face is detected, 'Negative' otherwise.

2. **/locate_faces**
    - Identifies and marks the locations of faces within the uploaded image.
    - **Method**: POST
    - **Response**: A JPEG image with faces marked.

## Setup & Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/gaurangAkulkarni/face-find.git
   ```

2. **Navigate to the project directory**:
   ```
   cd find-face
   ```

3. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the API**:
   With Flask:
   ```
   FLASK_APP=main.py flask run
   ```
   With Gunicorn:
   ```
   gunicorn -w 4 main:app
   ```

## Usage

1. **Find Face**:
   ```
   curl -X POST -F "file=@path_to_image.jpg" http://localhost:5000/find_face
   ```

2. **Locate Faces**:
   ```
   curl -X POST -F "file=@path_to_image.jpg" http://localhost:5000/locate_faces
   ```

## Deployment

The application is ready for deployment on platforms like Heroku, AWS, GCP, etc. Ensure you have the necessary configurations in place for the deployment platform of your choice.

---
