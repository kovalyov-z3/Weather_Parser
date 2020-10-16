import requests, bs4 

def parser():

    s=requests.get('https://sinoptik.com.ru/погода-москва')

    b=bs4.BeautifulSoup(s.text, "html.parser") 

    p3=b.select('.temperature .p3')

    pogoda1=p3[0].getText()

    p4=b.select('.temperature .p4')

    pogoda2=p4[0].getText()

    p5=b.select('.temperature .p5')

    pogoda3=p5[0].getText()

    p6=b.select('.temperature .p6')


    pogoda4=p6[0].getText()

    p7=b.select('.temperature .p7') 

    pogoda5=p7[0].getText()

    p8=b.select('.temperature .p8') 

    pogoda6 = p8[0].getText()

    print('Утром :' + pogoda1 + ' ' + pogoda2)

    print('Днём :' + pogoda3 + ' ' + pogoda4)

    print('Ночью:' + pogoda5 + ' ' + pogoda6) 

    p=b.select('.rSide .description')

    

    pogoda=p[0].getText()

    print(pogoda.strip()) 

parser() 
