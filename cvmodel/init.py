from cvmodel.yolo_ovj_dection import DarknetModel

def init():
    darknet_model = DarknetModel(
        cfg_path= "/home/miyamoto/projects/tcc/darknet/nosso-yolo/yolov4-obj.cfg", 
        weights_path= "/home/miyamoto/projects/tcc/darknet/nosso-yolo/data/backup/yolov4-obj_best.weights",
        classes_name= ["battle", "exploration", "menu"]
    )

    darknet_model.detect("/home/miyamoto/projects/tcc/darknet/nosso-yolo/dataset/va/batalha19442_png.rf.973db3164f20398879f2090e2ed3e412.jpg")