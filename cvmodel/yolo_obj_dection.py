from ast import Str
from traceback import print_tb
from unittest import result
import cv2
import numpy as np
import glob
import random
import shutil
from PIL.Image import Image


class DarknetModel():
    """ Responsável por carregar o modelo a partir do arquivo de configuração e os pesos. 
    Parâmetros:
        - cfg_path: caminho para o arquivo .cfg do modelo
        - weights_path: caminho para o arquivo .weights do modelo
        - classes_name: o nome das classes. Precisa estar na mesma ordem que a do treinamento
    """
    def __init__(self, cfg_path : Str, weights_path: Str, classes_name: list[Str]) -> None:
        # Load YoloPYT
        self.net = cv2.dnn.readNetFromDarknet(cfg_path, weights_path)
        self.classes = classes_name
        self.layer_names = self.net.getLayerNames()
        self.output_layers = [self.layer_names[i-1] for i in self.net.getUnconnectedOutLayers()]
        
    def detect(self, im: Image) -> list[tuple[int, str, tuple[float,float,float,float]]]:
        """
        Função que recebe uma imagem do tipo Image(PIL) e usa o modelo carregado para 
        detectar os objetos na tela.

        Parâmetros:
            - Image: Imagem do tipo Image(PIL)

        Retorno:
            - Array de objetos reconhecidos: [(class_id, class_name, (box))]
        """
        img = np.asarray(im)
        height, width, channels = img.shape

        # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

        self.net.setInput(blob)
        outs = self.net.forward(self.output_layers)
        
        class_ids = []
        confidences = []
        boxes = []
        # labeldata = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.1:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    # boxes.append([x, y, w, h])
                    boxes.append([detection[0], detection[1], detection[2], detection[3]])
                    # labeldata.append([class_id, detection[0], detection[1], detection[2], detection[3]])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)
        result = []
        for i in indexes:
            box = boxes[i]
            label = str(self.classes[class_ids[i]])
            # print(f"class_id: {class_ids[i]}; classe: {label}; confiança: {confidences[i]}")
            result.append((class_ids[i], label, box))

        return result

        # for conf in confidences:
        #     print(f"class_id: {class_id}; classe: {self.classes[class_id]}; confiança: {conf}")


# # Load YoloPYT
# net = cv2.dnn.readNetFromDarknet("/home/miyamoto/projects/tcc/darknet/nosso-yolo/yolov4-obj.cfg", "/home/miyamoto/projects/tcc/darknet/nosso-yolo/data/backup/yolov4-obj_best.weights")

# # Name custom object
# classes = ["battle", "exploration", "menu"]

# # Images path
# images_path = glob.glob(r"/home/miyamoto/projects/tcc/darknet/nosso-yolo/data/validation/*.jpg")

# layer_names = net.getLayerNames()
# output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]
# colors = np.random.uniform(0, 255, size=(len(classes), 3))

# # Insert here the path of your images
# random.shuffle(images_path)
# print(len(images_path))
# # loop through all the images
# for img_num, img_path in enumerate(images_path):
#     # Loading image
#     img = cv2.imread(img_path)
#     # img = cv2.resize(img, None, fx=0.4, fy=0.4)
#     height, width, channels = img.shape

#     # Detecting objects
#     blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

#     net.setInput(blob)
#     outs = net.forward(output_layers)

#     # Showing informations on the screen
#     class_ids = []
#     confidences = []
#     boxes = []
#     labeldata = []
#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.3:
#                 # Object detected
#                 center_x = int(detection[0] * width)
#                 center_y = int(detection[1] * height)
#                 w = int(detection[2] * width)
#                 h = int(detection[3] * height)

#                 # Rectangle coordinates
#                 x = int(center_x - w / 2)
#                 y = int(center_y - h / 2)

#                 boxes.append([x, y, w, h])
#                 labeldata.append([class_id, detection[0], detection[1], detection[2], detection[3]])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)
                
#     indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
#     font = cv2.FONT_HERSHEY_PLAIN
#     has = False
#     for i in range(len(boxes)):
#         if i in indexes:
#             x, y, w, h = boxes[i]
#             label = str(classes[class_ids[i]])
#             color = colors[class_ids[i]]
#             cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
#             cv2.putText(img, label, (x, y + 30), font, 1, color, 1)
#             has = True

#     if has:
#         cv2.imshow("Image", img)
#         key = cv2.waitKey(0)

#     #     savepath = "./results"

#     #     if key == 113:
#     #         exit()
#     #     elif key == 27:
#     #         continue
#     #     elif key == 32:
#     #         shutil.copyfile(img_path, savepath + "\\ajustar\\" + img_path.split("\\")[-1])
#     #     else:
#     #         shutil.copyfile(img_path, savepath + img_path.split("\\")[-1])
#     #         txtFile = img_path.split("\\")[-1].split(".")[0] + ".txt"
#     #         f = open(savepath + txtFile, 'w')
#     #         for i in range(len(labeldata)):
#     #             if i in indexes:
#     #                 f.write(str(labeldata[i][0]) + " " + str(labeldata[i][1]) + " " + str(labeldata[i][2]) + " " + str(labeldata[i][3]) + " " + str(labeldata[i][4]) + "\n")
#     #         f.close()

#     print(str(img_num) + "/" + str(len(images_path)))

# cv2.destroyAllWindows()





#https://learnopencv.com/deep-learning-based-object-detection-using-yolov3-with-opencv-python-c/