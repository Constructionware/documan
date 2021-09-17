#reports.py
# Pdf Report Creator

import time
from aspire.core.security_service import GenerateId
from pdfme import build_pdf
from dataclasses import dataclass


class Document:
    _id:str 
    title: str
    doc_home:str = ""
    document:dict = {
            "style": {
            "margin_bottom": 15, 
            "text_align": "j",
            "page_size": "letter", 
            "margin": [60, 50]
        },
        "formats": {
            "url": {"c": "tomato", "u": 1},
            "title": {"b": 1, "s": 16, "c": "darkslategray"},
            "text-xs": {"b": 0, "s": 5},
            "text-sm": {"b": 0, "s": 8},
            "text-md": {"b": 0, "s": 12},
            "text-lg": {"b": 0, "s": 14},
            "h1": {"b": 1, "s": 24, "c": "chocolate"} 
        },
        "running_sections": {
            "header": {
                "x": "left", "y": 20, "height": "top", "style": {"text_align": "r"},
                "content": [{".b": f"Vera Document {time.ctime()}"}]
            },
            "footer": {
                
                "x": "left", "y": 740, "height": "bottom", "style": {"text_align": "c"},
                "content": [
                    {".": f"Vera Document Generator |"},
                    {".": ["Page ", {"var": "$page"}]}
                    ]
            }
        },
        "sections": [],
    }

    def __init__(self, title:str=None):
        self.title = title
        self._id = self.generateid

    @property
    def generateid(self):
        gen = GenerateId()
        return gen.gen_id('doc') 

    def content( self, content:list=None ) -> list:
        return content

    def add_top_section(self, style:dict=None, content:dict=None):
        if style:
            section = {"style": style}
        else: 
            section = {
            "style":{
                'page_numbering_style': 'roman'
            },
            "running_sections": ['header', 'footer'],
            "content": []
            }
        if content:
            section['content'].append(content)
        self.document['sections'].append(section)

    def add_main_section(self, style:dict=None, content:dict=None):
        if style:
            section = {"style": style}
        else: 
            section = {
                'style': {
                'page_numbering_reset': True, 'page_numbering_style': 'arabic'
            },
            "running_sections": ['header', 'footer'],
            "content": []
            }
        if content:
            section['content'].append(content)
        self.document['sections'].append(section)

    def save(self, filename:str=None) -> None:
        with open(f'{self.doc_home}/{filename}.pdf', 'wb') as f:
            build_pdf(self.document, f)
    
    def __repr__(self) -> str:
        return f"Vera Document {self.__dict__}"

    
doc = Document()
doc.title='Employment Report'
print(doc)