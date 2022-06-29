from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.forms import ImageForm
from app.models import Image
from tensorflow import keras
import cv2
import numpy as np


def success(request):
    obj = Image.objects.latest('id')
    # im = imd.open(obj.image_url)
    print(0)
    img = cv2.imread('D:\HPE Project\Detecting-Dyslexia-at-an-early-stage\data\Test\Reversal\g-52.R0dfD.png')
    face = cv2.resize(img, (28, 28))
    (b, g, r) = cv2.split(face)
    img = cv2.merge([r, g, b])
    img = img.astype(np.float32)
    img = img / 255
    model = keras.models.load_model('D:\HPE Project\djangoProject\models\main_model.h5')
    x = []
    x.append(img)
    img = img.reshape(-1, 28, 28, 3)
    result = model.predict(img)
    return HttpResponse(str(result))


def homepage(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        return render(request, 'app/home.html', context={'form': ImageForm})
