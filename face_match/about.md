https://docs.microsoft.com/en-us/azure/cognitive-services/Face/Quickstarts/client-libraries?pivots=programming-language-python

# Detect the faces in an image that contains multiple faces
# Each detected face gets assigned a new ID
    
    multi_face_image_url = "http://www.historyplace.com/kennedy/president-family-portrait-closeup.jpg"
    multi_image_name = os.path.basename(multi_face_image_url)
    detected_faces2 = face_client.face.detect_with_url(url=multi_face_image_url)

