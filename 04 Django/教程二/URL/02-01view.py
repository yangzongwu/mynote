def index(request):
    return render(request, 'index.html', {'user_dict':USER_DICT})

def detail(request,nid):
    #nid=request.GET.get('nid')
    detail_info=USER_DICT[nid]
    return render(request,'detail.html',{'detail_info':detail_info})
