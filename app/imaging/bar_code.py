#imaging | __init__.py
import time
import os
from dataclasses import dataclass


@dataclass
class QRCode:
    data:any
    file_handle: str
    box_size: int = 10
    border: int = 4
    version: str = 1

    def create(self):
        '''Generates a Qr code form given data and save to provided 
        file location.'''
        try:
            import qrcode
        except ImportError as e:
            return str(e)
        qr = qrcode.QRCode(
            version = self.version,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = self.box_size,
            border = self.border
        )
        self.data['time'] = time.asctime()
        qr.add_data(self.data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        if '.png' in self.file_handle:
            img.save(self.file_handle)
            return {
                "status": "Success",
                "message": "File Saved",
                "result": self.file_handle
                }
        else:
            return {
                "status": "Failed",
                "message": "File Not Saved",
                "result": "Only .png file extensions accepted at this time."
                }

    
    def create_jpg(self):
        '''Generates a Barcode code form given data and save to provided 
        file location.'''
        self.create()
        try:                     
            from PIL import Image 
            try:
                file_handle =  self.file_handle
                self.file_handle = self.file_handle[:-4]
                with Image.open(file_handle) as im:   
                    self.file_handle = f"{self.file_handle}.jpg"                 
                    im.save(self.file_handle, "JPEG")            
            finally: os.remove(file_handle)
            return {
                "status": "Success",
                "message": "File Saved",
                "result": self.file_handle
                }
        except Exception as e:
            return {
                "status": "Failed",
                "message": "File Not Saved",
                "result": str(e)
                }   


import barcode

@dataclass
class BarCode:
    data:str
    file_handle: str
    barcode_class: str = 'ean13'    

    @property
    def providers(self) -> list:
        return barcode.PROVIDED_BARCODES

    def create_svg(self):
        '''Generates a Barcode code form given data and save to provided 
        file location.'''
        try:
            provider = barcode.get(self.barcode_class, self.data)
            provider.save(self.file_handle)
            return {
                "status": "Success",
                "message": "File Saved",
                "result": self.file_handle
                }
        except Exception as e:
            return {
                "status": "Failed",
                "message": "File Not Saved",
                "result": str(e)
                }


    def create_png(self):
        '''Generates a Barcode code form given data and save to provided 
        file location.'''
        try:
            from barcode.writer import ImageWriter
            provider = barcode.get(self.barcode_class, self.data, writer=ImageWriter())
            provider.save(self.file_handle)
            return {
                "status": "Success",
                "message": "File Saved",
                "result": self.file_handle
                }
        except Exception as e:
            return {
                "status": "Failed",
                "message": "File Not Saved",
                "result": str(e)
                }


    def create_jpg(self):
        '''Generates a Barcode code form given data and save to provided 
        file location.'''
        try:
            from barcode.writer import ImageWriter            
            from PIL import Image 

            provider = barcode.get(self.barcode_class, self.data, writer=ImageWriter())
            file_handle = provider.save(self.file_handle)
            try:
                self.file_handle = f"{self.file_handle}.jpg"
                with Image.open(file_handle) as im:                    
                    im.save(self.file_handle, "JPEG")            
            finally: os.remove(file_handle)
            return {
                "status": "Success",
                "message": "File Saved",
                "result": self.file_handle
                }
        except Exception as e:
            return {
                "status": "Failed",
                "message": "File Not Saved",
                "result": str(e)
                }   

    


                              