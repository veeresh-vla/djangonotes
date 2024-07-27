from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,'testapp/index.html')

def movies_view(request):
    head_msg = 'Movies Information'
    sub_msg1 = 'OG is the upcoming movie'
    sub_msg2 = 'Devara will release on next month'
    sub_msg3 = 'Planning for aashiqui-3 with Mahesh sir and Sunny Leone'
    type = 'movies'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def sports_view(request):
    head_msg = 'Sports Information'
    sub_msg1 = 'Yesterday IPL match won by SRH'
    sub_msg2 = 'Today match b/w RR & DC'
    sub_msg3 = 'Who will win IPL cup???????????'
    type = 'sports'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def politics_view(request):
    head_msg = 'Politics Information'
    sub_msg1 = 'Telangana CM was revanth reddy'
    sub_msg2 = 'India PM was Modi'
    sub_msg3 = 'Who is upcoming CM for AP????????????'
    type = 'politics'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)
