

class Convert:
    def __init__(self):
        pass
    def convert_image_to_base64(self,img_path):
        """This function creates binary file for the image
        stores as a .bin file"""
        with open(img_path, "rb") as image2string:
            conv_str = base64.b64encode(image2string.read())
            print(conv_str)
  
        with open('encode.bin', "wb") as file:
            file.write(conv_str)

        return 1            
        
    def convert_base64_to_image(self,binfile_path):
        """By using this funtion we can convert binary file of 
        the image to actual image file"""
        file = open('binfile_path', 'rb')
        byte = file.read()
        file.close()
  
        decodeit = open('hello_level.jpeg', 'wb')
        decodeit.write(base64.b64decode((byte)))
        decodeit.close()
        return 1