from ultralytics import YOLO


if __name__ == "__main__":
    # 加载YOLOv8模型
    model = YOLO("best.pt")
    # 视频路径
    file_path = "test.mp4"
    # 检测视频
    results = model.predict(source=file_path, device=0, show=False, save=True)
