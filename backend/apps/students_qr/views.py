import qrcode
import os
from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from io import BytesIO

def generate_qr(request):
    user = request.user
    qr_content = f"User Info: {user.username}, {user.email}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_content)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    # メディアディレクトリにQRコード画像を保存
    file_name = f"qr_code_{user.username}.png"
    file_path = os.path.join('qr_codes', file_name)
    
    # デフォルトストレージを使ってファイルを保存
    content_file = ContentFile(img_io.read())
    file_path = default_storage.save(file_path, content_file)

    # htmlテンプレートに画像のURLを渡す
    qr_image_url = os.path.join(settings.MEDIA_URL, file_path)
    return render(request, 'students_qr/qr_code.html', {'qr_image_url': qr_image_url})
