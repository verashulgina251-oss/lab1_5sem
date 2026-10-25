from http.server import HTTPServer, BaseHTTPRequestHandler

response_start = '''<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Магазин</title>
</head>
<body style="margin: 0; padding: 0;">
    <header style="width: 100%; 
    font-size:xxx-large;
    background-color: gray;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    margin: 0;
    text-align: center;
    ">
        МАГАЗИН ПРОДУКТОВ o_O
    </header>
</body>
</html>'''

listOfStuff = [["Молоко", "120", '''Свежесть и натуральный вкус в каждой капле! 
                  Коровье молоко средней жирности, идеально подходит для приготовления каш, 
                  соусов, напитков и выпечки. Произведено из отборного сырья, содержит кальций 
                  и витамины для крепких костей и энергии на весь день.'''],
                 ["Хлеб", "60", '''Свежий, ароматный хлеб с мягким воздушным мякишем
                  и тонкой золотистой корочкой. Подходит для бутербродов, тостов 
                  и повседневных трапез. Выпечен из отборной пшеничной муки высшего сорта,
                  сохраняет вкус и свежесть несколько дней.'''],
                 ["Чай", "99", '''Бодрящий и насыщенный напиток с глубоким вкусом и тонким ароматом. 
                  Заваривается быстро, раскрывая богатый букет с лёгкой терпкостью. 
                  Отлично подходит для утреннего пробуждения или уютного вечера.'''],
                 ["Сыр", "180", '''Натуральный сыр с богатым сливочным вкусом и плотной текстурой. 
                  Подходит для нарезки, бутербродов, салатов и горячих блюд. 
                  Источник кальция и белка, необходимого для энергии и здоровья.
                  Отлично плавится и придаёт особый вкус любым рецептам.'''],
                 ["Масло", "150", '''СНатуральное сливочное масло с насыщенным вкусом и нежной текстурой. 
                  Отлично подходит для бутербродов, выпечки, соусов и жарки. 
                  Изготовлено из свежих сливок без добавления растительных жиров. 
                  Богато витаминами A и D, а также легкоусвояемыми жирами.'''],]
    
class siteHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.main_page()
        else:
            self.stuff_page()
    def main_page(self):
        self.response(200)
        listOfStuffHtml = ''
        for i, j in enumerate(listOfStuff):
            listOfStuffHtml += f'''<div style="background: gray; 
                                    width: 150px; 
                                    height: 200px; 
                                    padding: 10px; 
                                    margin: 10px; 
                                    font-family: Verdana, Geneva, Tahoma, sans-serif;">
                                        <div style="width: auto; 
                                        height: 100px; 
                                        background-color: 
                                        antiquewhite; 
                                        margin: 0px;"></div>
                                            <a href={i}><p>{j[0]}</p></a>
                                            <p>{j[1]} рублей</p>
                                    </div>'''
        listOfStuffHtml = "<div style='display: flex; flex-wrap: wrap;'>" + listOfStuffHtml + "</div>"
        self.render(listOfStuffHtml)
    def stuff_page(self):
        stuff_index = str(self.path)[1:]
        self.response(200)
        if int(stuff_index) < len(listOfStuff):
            info_staf = f'''<div style="background: gray;  
                                        padding: 10px; 
                                        margin: 10px; 
                                        font-size: xx-large;
                                        font-family: Verdana, Geneva, Tahoma, sans-serif;">
                                                <p>Наименование товара: {listOfStuff[int(stuff_index)][0]}</p>
                                                <p>Цена товара: {listOfStuff[int(stuff_index)][1]}</p>
                                                <p>Описание товара: {listOfStuff[int(stuff_index)][2]}</p>
                                                <a href=/>Назад</a>
                                        </div>'''
            self.render(info_staf)
        else:
            self.render('''<div style="background: gray;  
                                        padding: 10px; 
                                        margin: 10px; 
                                        font-size: xx-large;
                                        font-family: Verdana, Geneva, Tahoma, sans-serif;">
                                                <p>Страницы не существует</p>
                                                <a href=/>Назад</a>
                                        </div>''')
    def response(self, code:int):
        self.send_response(code)
        self.send_header("Content-type", 'text/html')
        self.end_headers()
    def render(self, content: str):
        self.wfile.write(response_start.encode("utf-8")) 
        self.wfile.write(content.encode("utf-8")) 

def run(http_server=HTTPServer, hander=BaseHTTPRequestHandler):
    httpd = http_server(('', 3000), hander)
    httpd.serve_forever()

if __name__ == "__main__":
    run(HTTPServer, siteHandler)