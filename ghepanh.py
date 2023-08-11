from PIL import Image
import os


# Đường dẫn đến hai hình ảnh cần ghép
image_path1 = "c:/Users/Thanh/Desktop/ảnh/kosaka_2019_01_16_text"
image_path2 = "c:/Users/Thanh/Desktop/ảnh/kosaka_2019_01_16"


file_paths = [os.path.join(image_path1 , filename) for filename in os.listdir(image_path1 ) if filename.lower().endswith((".jpg", ".jpeg", ".png"))]
for file_path in file_paths:
# Mở hai hình ảnh sử dụng thư viện Pillow
    image1 = Image.open(file_path)
    name = os.path.basename(file_path)
    image2 = Image.open("c:/Users/Thanh/Desktop/ảnh/kosaka_2019_01_16/"+name)

# Lấy kích thước của cả hai hình ảnh
    width1, height1 = image1.size
    width2, height2 = image2.size

# Tính toán kích thước của hình ảnh mới sau khi ghép
    total_width = width1 + width2
    max_height = max(height1, height2)

# Tạo hình ảnh mới để ghép
    merged_image = Image.new("RGB", (total_width, max_height))

# Ghép hình ảnh đầu tiên vào bên trái
    merged_image.paste(image1, (0, 0))

# Ghép hình ảnh thứ hai vào bên phải
    merged_image.paste(image2, (width1, 0))

# Hiển thị hoặc lưu hình ảnh đã ghép
    # merged_image.show()
# Hoặc
    merged_image.save("ouput/"+name)
