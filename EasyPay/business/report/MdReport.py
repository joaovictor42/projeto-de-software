from business.report.BaseReport import BaseReport


class MdReport(BaseReport):
    
    format = '.md'

    def header(self) -> None:
        self.arq.write('# Relatório de Acessos\n')

    def body(self, data) -> None:
        self.arq.write(data.to_markdown())

    def footer(self) -> None:
        self.arq.write('\n### Propriedade EasyPay')