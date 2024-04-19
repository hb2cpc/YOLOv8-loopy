from ultralytics import YOLO

if __name__ == "__main__":
    # load a pretrained model (recommended for training)
    model = YOLO("yolov8n.pt")

    # Train the model
    model.train(
        data="dataset\loopy.yaml",
        epochs=1000,
        imgsz=640,
        device="0",
    )
