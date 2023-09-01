from PIL import Image

# img = Image.open("./burger.jpg")
# img.show()
# print(img.size)
# print(img.mode)
# print(img.format)

cf = open("demofile2.jpg", 'wb')

with open("./burger.jpg", 'rb') as f:
    for i in f:
        cf.write(i)
cf.close()

# text = open('binary.txt', 'w')
# with open("./burger.jpg", 'rb') as f:
#     for i in f:
#         text.write(str(i))
# text.close()

# cf = open("demofile2.jpg", 'wb')

# with open("./binary.txt", 'r') as f:
#     for i in f:
#         cf.write(eval(i))

# cf.close()