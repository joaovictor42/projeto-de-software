from business.report.BaseReport import BaseReport


open_structure = '''
<!DOCTYPE html>
    <html>
        <head>
        </head>
        <body>
'''

close_structure = '''
        </body>
    </html>
'''

class HtmlReport(BaseReport):

    format = '.html'

    def hook1(self) -> None:
        self.arq.write(open_structure)
        
    def header(self) -> None:
        self.arq.write('<h1>Relatório de Acessos</h1>')

    def body(self, data) -> None:
        self.arq.write(data.to_html())

    def footer(self) -> None:
        self.arq.write('<h3>Propriedade EasyPay<h3>')

    def hook2(self) -> None:
        self.arq.write(close_structure)
