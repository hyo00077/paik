from django.shortcuts import render

# Create your views here.


def input_main(request, *args, **kwargs):
    return render(request, 'frontend/input_main.html')


# def input(request, report):
#     context = {"report": report}
#     return render(request, 'frontend/input.html', context)
