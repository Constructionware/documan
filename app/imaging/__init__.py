#imaging | __init__.py
import time
import urllib.request
import requests, os

import qrcode
from PIL import Image
from decimal import Decimal
from dataclasses import dataclass


@dataclass
class QRCode:
    data:any
    file_handle: str
    box_size: int = 10
    border: int = 4
    version: str = 1

    def createQR(self):
        '''Generates a Qr code form given data and save to provided 
        file location.'''
        qr = qrcode.QRCode(
            version = self.version,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = self.box_size,
            border = self.border
        )
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