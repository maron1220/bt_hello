from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm


class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title': '検査数値から考える鑑別疾患',
            'result': None,
            'form': HelloForm()
        }

    def get(self, request):
        return render(request, 'bt_hello/index.html', self.params)

    def post(self, request):
        bun = ("腎不全", "心不全")
        ch = request.POST.getlist('choice')
        result = '<ol class = "list-group"><b>鑑別リスト:</b>'
        for item in ch:
            if item == "BUN上昇":
                result += '----------------BUN上昇-------------------'
                for i in bun:
                    result += '<li class="list-group-item">'+i+'</li>'
            else:
                result += '-------------------------------------------'
                result += '<li class="list-group-item">'+item+'</li>'
        result += '</ol>'
        self.params['result'] = result
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'bt_hello/index.html', self.params)


# Create your views here.
