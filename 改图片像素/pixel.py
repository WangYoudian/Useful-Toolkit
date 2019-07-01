from PIL import Image

lis = ['毕业证书', '身份证正面', '身份证反面', '毕业生接收申请表']

def getSize(x, y):
	pass


def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)
 
if __name__ == '__main__':
    # 遍历lis，获取file_in和file_out
    for filename in lis:
    	file_in = filename + '.jpg'
    	file_out = filename + '_resize.jpg'
    	# 获取图片像素 x, y
    	im = Image.open(file_in)
    	x, y = im.size

    	# 计算
    	width, height = getSize(x, y)
    	print(x, y)

    	# 修改成指定大小
    	# produceImage(file_in, width, height, file_out)

