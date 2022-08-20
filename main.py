import cv2
from PIL import Image
import pathlib

def check_paths(img_path, face_path, result_path):
    def is_image(path):
        if path.endswith('.png') or path.endswith('.jpeg') or path.endswith('.jpg') or path.endswith('.gif') or path.endswith('.tiff'): return True
        else: return False
    if not pathlib.Path(img_path).exists():
        print("image path isn't exist")
        return False
    elif not pathlib.Path(face_path).exists():
        print("face path isn't exist")
        return False
    elif not pathlib.Path(result_path).parent.exists():
        print("result path isn't exist")
    elif not is_image(img_path):
        print("your image path isn't image")
        return False
    elif not is_image(face_path):
        print("your face path isn't image")
        return False
    elif not is_image(result_path):
        print("result path isn't image")
    return True

def get_faces(img):
    face_cascade = cv2.CascadeClassifier('face.xml')
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    coords_ = face_cascade.detectMultiScale(gray, 1.1, 4)
    coords = [[] for _ in range(len(coords_))]
    for i in range(len(coords_)):
        for n in range(len(coords_[i])):
            coords[i].append(int(coords_[i][n]))

    return coords

def change_faces(img, face, coords):
    img = Image.open(img)
    face = Image.open(face)

    for coord in coords:
        img.paste(face, coord[:2])

    return img

def save_img(result_filename, img):
    img.save(result_filename)

def main():
    img_path = input('Path to image: ')
    face_path = input('Path to image that must replace face: ')
    result_path = input("Path to image that will be result of code: ")
    if not check_paths(img_path, face_path, result_path): return
    coords = get_faces(img_path)
    img = change_faces(img_path, face_path, coords)
    save_img(result_path, img)

if __name__ == '__main__':
    main()
