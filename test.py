import detect

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

detect.run(weights='last.pt', conf_thres=0.25, source='8.jpg', save_crop=True, imgsz=(640, 640))
