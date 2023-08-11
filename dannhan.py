import pandas as pd
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

df_data = pd.read_excel("Ykita.xlsx", index_col=0)
# p = df_data.iloc[0, 0] + " " + df_data.iloc[0, 1] + " " + df_data.iloc[0, 2]
# print(p)
data_length = len(df_data)
print("Length of df_data:", data_length)
for i in range(data_length):
    print(i)
    if df_data.iloc[i, 0]:
        link = df_data.iloc[i, 0]
        p = (
            df_data.iloc[i, 1]
            + "  "
            + df_data.iloc[i, 2]
            + "  "
            + df_data.iloc[i, 3]
            + "  "
            + df_data.iloc[i, 4]
        )
        im = Image.open("Ykita_2022_02_22/" + link)

        # This method will show image in any image viewer

        I1 = ImageDraw.Draw(im)

        # Custom font style and font size
        myFont = ImageFont.truetype("arial.ttf", 40)

        # Add Text to an image
        I1.text((50, 50), p, font=myFont, fill=(0, 0, 255))

        # Display edited image

        # Save the edited image
        im.save("Ykita_2022_02_22_text/" + link)
        print(i)
