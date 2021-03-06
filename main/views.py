# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView, FormView
from Driver import driver
from django.core.files.storage import FileSystemStorage
import os
# import numpy as np
# from PIL import ImageFile, Image
# ImageFile.LOAD_TRUNCATED_IMAGES = True

# Create your views here.

def main_page(request):

    base_repo=os.path.join('static','repo')

    if request.method=='POST':
        img=request.FILES['img']
        fs = FileSystemStorage()
        file = fs.save(os.path.join(base_repo,img.name), img)
        img_name=img.name
        img_path=os.path.join(base_repo,img_name)
        mat=driver.Solve_Sudoku(img_path)
        return render(request,'main/prediction.html',{'results':mat})

    # On getting Get Request delete all saved images!!!
    fs = FileSystemStorage()
    all_files=os.listdir(base_repo)
    for file in all_files:
        fs.delete(os.path.join(base_repo,file))
    return render(request,'main/index.html')
