from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from .models import Attendance, Course
from datetime import datetime
from django.utils.timezone import make_aware

def qr_reader_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    context = {
        'course': course,
    }
    return render(request, 'attendances/qr_reader.html', context)


def save_attendance(request):
    if request.method == 'POST':
        qr_data = request.POST.get('qr_data', '')
        course_id = request.POST.get('course_id', '')

        # QRコードのデータを解析
        user_info = qr_data.split(',')
        if len(user_info) == 2:
            student_username = user_info[0]
            student_email = user_info[1]  # 現在のコードでは使用していませんが、必要に応じて利用できます

            try:
                course = Course.objects.get(id=course_id)
                
                # 出席時間の取得
                attendance_time = timezone.now()
                course_start_datetime = datetime.combine(course.start_date, course.start_time)

                # タイムゾーン情報を付加
                course_start_datetime = make_aware(course_start_datetime, timezone.get_current_timezone())

                # 出席ステータスの決定
                time_diff = (attendance_time - course_start_datetime).total_seconds() / 60  # 分単位
                if time_diff <= 10:
                    status = 'Present'  # モデルのchoicesに合わせて大文字
                elif time_diff <= 15:
                    status = 'Late'
                else:
                    status = 'Absent'

                # 重複チェック
                if not Attendance.objects.filter(course=course, student=student_username).exists():
                    # 出席記録の保存
                    Attendance.objects.create(
                        course=course,
                        student=student_username,  # モデルのフィールドに合わせてusernameを直接保存
                        attendance_time=attendance_time,
                        attendance=status
                    )

                    return JsonResponse({'status': 'success'})
                else:
                    return JsonResponse({'status': 'error', 'message': '既に出席が記録されています'})
            except Course.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'コースが見つかりません'})
        else:
            return JsonResponse({'status': 'error', 'message': 'QRコードのデータが無効です'})
    else:
        return JsonResponse({'status': 'error', 'message': 'POSTメソッドのみ対応しています'})
