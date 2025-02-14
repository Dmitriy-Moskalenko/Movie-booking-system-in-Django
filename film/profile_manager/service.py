import io
import qrcode
from django.core.files.base import ContentFile


def qrcode_create(data):
    """Создание QR кода билета"""

    # Создание QR кода и сохранение её в памяти
    qr = qrcode.make(data)
    buffer = io.BytesIO()

    qr.save(buffer, format='PNG')
    qr_image = buffer.getvalue()
    return ContentFile(qr_image, name='ticket.png')


