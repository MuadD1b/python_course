import cv2 as cv


class Images:

        def __init__(self, path):
            self.path = path

        def show(self):
            if r'.jpg' in self.path:
                self.frame = cv.imread(self.path)
                cv.imshow('image', self.frame)
                cv.waitKey(2000)
            elif r'.mp4' in self.path:
                cap = cv.VideoCapture(self.path)

                while cap.isOpened():
                    read, self.frame = cap.read()
                    if not read:
                        break
                    cv.imshow('frame', self.frame)
                    if cv.waitKey(1) == ord('q'):
                        break
                cap.release()
                cv.destroyAllWindows()

        def resizing(self, new_w=None, new_h=None):
            h, w = self.frame.shape[:2]
            if new_w is None and new_h is None:
                return self.frame
            elif new_w is None:
                ratio = new_h / h
                dim = (int(w * ratio), new_h)
            else:
                ratio = new_w / w
                dim = (new_w, int(h * ratio))
            self.frame = cv.resize(self.frame, dim)
            cv.imshow('image', self.frame)
            cv.waitKey(2000)


        def detect(self):
            face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
            frame_gray = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
            frame_gray = cv.equalizeHist(frame_gray)
            faces = face_cascade.detectMultiScale(frame_gray)
            for (x, y, w, h) in faces:
                center = (x + w // 2, y + h // 2)
                frame = cv.ellipse(self.frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
                cv.imshow('frame', self.frame)
                cv.waitKey(2000)

image = Images('photo.jpg')
image.show()
image.resizing(None,200)
image.detect()