from docx.document import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph
import docx
import openpyxl
import xlsxwriter
 
def iter_block_items(parent):
    """
    Yield each paragraph and table child within *parent*, in document order.
    Each returned value is an instance of either Table or Paragraph. *parent*
    would most commonly be a reference to a main Document object, but
    also works for a _Cell object, which itself can contain paragraphs and tables.
    """
    data_list = []
    if isinstance(parent, Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    m = 0
    for child in parent_elm.iterchildren():
        
        if isinstance(child, CT_P):
            p = Paragraph(child, parent)
            block_obj = {}
            block_obj['no'] = m
            block_obj['content'] = p.text
            data_list.append(block_obj)
        elif isinstance(child, CT_Tbl):
            table = Table(child, parent)
            i = 1
            for row in table.rows:
                j = 1
                for cell in row.cells:
                    block_obj = {}
                    block_obj['no'] = m
                    block_obj['content'] = cell.text
                    block_obj['row_no'] = i
                    block_obj['column_no'] = j
                    j += 1
                    data_list.append(block_obj)
                i += 1
        m += 1
    return data_list
	
    
if __name__ == "__main__":
    import urllib.request as r
    #导入联网工具包，命名为r
    url= 'http://api.openweathermap.org/data/2.5/weather?q=Dalian&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
    data =r.urlopen(url).read().decode('utf-8')
    #将str类型转换为dict
    import json
    data =json.loads(data)
    print(data)