from django.shortcuts import redirect, render, HttpResponse
from PIL import Image
from django.conf import settings
from . import nft_collection
from thirdweb.types.nft import NFTMetadataInput
#from . import NST
import os
# Create your views here.
image3 = ""

def combine(one, two):
    global image3
    image1 = Image.open(one) 
    image2 = Image.open(two)

    width, height = image1.size
    left = 4
    top = height / 5
    right = 154
    bottom = 3 * height / 5
    im1 = image1.crop((left, top, right, bottom))
    newsize = (300, 300)
    im1 = im1.resize(newsize)

    width, height = image2.size
    left = 4
    top = height / 5
    right = 154
    bottom = 3 * height / 5
    im2 = image2.crop((left, top, right, bottom))
    newsize = (300, 300)
    im2 = im2.resize(newsize)
    path = settings.MEDIA_ROOT
    image3 = Image.alpha_composite(im1, im2).save(f"{path}/mypwic.png")
    print(image3)
    return image3


def home(request):
    if request.method == 'POST' and request.FILES['myfile1'] and request.FILES['myfile2']:
        file1 = request.FILES['myfile1'].file
        file2 = request.FILES['myfile2'].file
        combine(file1, file2)
        path1="/Users/razazaidi/Documents/GitHub/thirdweb/python/django/ai_minter/aiminter/ai_engine/data/content-images/"
        path2="/Users/razazaidi/Documents/GitHub/thirdweb/python/django/ai_minter/aiminter/ai_engine/data/style-images/"
        Image.open(file1).save(f"{path1}/c1.png")
        Image.open(file2).save(f"{path2}/s1.png")
        #return redirect("/")
    #exec(open(NST))
        os.system('python3 /Users/razazaidi/Documents/GitHub/thirdweb/python/django/ai_minter/aiminter/ai_engine/NST.py')
        name_nft = "AI NFT"
        description_nft = "My-Wing"
        image_nft = open('/Users/razazaidi/Documents/GitHub/thirdweb/python/django/ai_minter/aiminter/ai_engine/data/output-images/combined_c1_s1/c1_s1.jpg','rb')
        #image_nft.name = request.POST.get('name','')
        prop = {}

        nft_metadata = {
            'name': name_nft,
            'description': description_nft,
            'image': image_nft,
            'properties':prop
        }
        print(nft_metadata)
        nft_collection.nft_collection.mint(NFTMetadataInput.from_json(nft_metadata))
        return redirect("success")


    return render(request, "index.html", {'image3':image3})


def success(request):
    return HttpResponse("successfully uploaded")