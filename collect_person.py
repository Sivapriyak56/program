import glob
import imagehash
from PIL import Image


me = './me/me.jpg'
me_hash = imagehash.average_hash(Image.open(me))

girls = glob.glob('./girls/*.jpg')

my_best = girls[0]
defference = 100

for girl in girls:
    girls_hash = imagehash.average_hash(Image.open(girl))
    deff = girls_hash - me_hash
    if deff < defference:
        my_best = girl
        defference = deff
print(my_best)
my_img = Image.open(me)
bestie_img = Image.open(my_best)
couple_img = Image.new('RGB',(my_img.width+bestie_img.width, my_img.height))
couple_img.paste(my_img,(0,0,))
couple_img.paste(bestie_img,(my_img.width,0))
couple_img.show()
couple_img.save('my_bestie.jpg')
