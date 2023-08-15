import os
from PIL import Image

def count_image_files(directory):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # Các định dạng ảnh phổ biến
    image_count = 0
    file_paths = [os.path.join(directory_path , filename) for filename in os.listdir(directory_path ) if not filename.lower().endswith((".zip"))]
    for file_path in file_paths:
        print (file_path)
        for filename in os.listdir(file_path):
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                image_count += 1
    return image_count
directory_path = '/media/vol0/raw/video_other/webcamera_wni_0/十和田/下616.4/2018/05'  # Thay đổi đường dẫn tới thư mục của bạn
image_count = count_image_files(directory_path)
print(f"Số lượng tệp ảnh trong thư mục: {image_count}")
