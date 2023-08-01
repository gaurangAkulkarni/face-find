Of course! Here's the updated `README.md`:

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

### Heroku:

1. **Login to Heroku**:
   ```
   heroku login
   ```

2. **Create a new app on Heroku**:
   ```
   heroku create your-app-name
   ```

3. **Add Heroku remote**:
   ```
   git remote add heroku https://git.heroku.com/your-app-name.git
   ```

4. **Commit your changes**:
   ```
   git add .
   git commit -m "Prepare for Heroku deployment"
   ```

5. **Push to Heroku**:
   ```
   git push heroku master
   ```

6. **Scale your app**:
   ```
   heroku ps:scale web=1
   ```

### Azure:

1. **Login to Azure**:
   ```
   az login
   ```

2. **Create a new Web App**:
   ```
   az webapp up -n your-app-name
   ```

3. **Set the deployment user** (if not done previously):
   ```
   az webapp deployment user set --user-name <username> --password <password>
   ```

4. **Deploy**:
   ```
   git add .
   git commit -m "Prepare for Azure deployment"
   git push azure master
   ```

5. **Browse to the application**:
   ```
   az webapp browse --name your-app-name --resource-group your-resource-group
   ```

---

Replace placeholders like `your-app-name`, `<username>`, and `<password>` with appropriate values.
