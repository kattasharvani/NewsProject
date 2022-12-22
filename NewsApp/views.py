from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'index.html');

def india(req):
    dict={'mainmsg':'India News Page',
           'submsg1':'100+crores vaccines succesfully done!!!',
           'submsg2':'India Largest growing GDP by 2025',
           'submsg3':'India to declare lockdown due to covid-19',
           'imgs':'images/india.jpg'}
    return render(req, 'news.html',context=dict);

def tech(req):
    dict={'mainmsg':'Technology News',
          'submsg1':'Cybersecurity to reach its peak in theyear 2023',
          'submsg2':'the top technical courses to be learned in 2023',
          'submsg3':'Amazon to sell the elcetronic products at the lowest in the year end',
          'imgs':'images/tech.jpg'}
    return render(req, 'news.html',context=dict);


def sports(req):
    dict={'mainmsg':'Sports News',
         'submsg1':'India Won the World cup in the Final match of with west indies',
         'submsg2':'Pro Kabbadi League(pkl) is going to start from 29 nov of 2022',
         'submsg3':'This year FIFA annouces the opening song by Jungkook of BTS',
         'imgs':'images/sports.jpg',}
    return render(req, 'news.html', context=dict);

def hyperlinks(req):
    return render(req, 'hyperlinks.html');