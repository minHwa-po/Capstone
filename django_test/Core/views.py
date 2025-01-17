from django.shortcuts import render, redirect
from . import models
from . import sttService

#video list를 보여준다.
def video_list(request):
    video_list = models.Document.objects.all()
    return render(request, 'Core/video_list.html', {'video_list': video_list})

#video(file) upload
def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        # Saving the information in the database
        if request.FILES.get("uploadedFile") :
            fileTitle = request.POST["fileTitle"]
            uploadedFile = request.FILES["uploadedFile"]
            document = models.Document(
                title = fileTitle,
                uploadedFile = uploadedFile
            )
            document.save()

            #sttService로 결과 받아오기
            message = sttService.doSttService(document.uploadedFile.url)
            return render(request, "Core/success.html", context={"file" : document, "message" : message})

        # True if empty  
        else :
            return render(request, "Core/upload.html") 

    else :
        return render(request, "Core/upload.html") 