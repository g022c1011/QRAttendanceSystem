from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from .models import Attendance, Course
from datetime import datetime
import pytz

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
            student_username = user_info[0].replace('User Info: ', '').strip()
            student_email = user_info[1]

            try:
                course = Course.objects.get(id=course_id)
                
                # 日本時間のタイムゾーンを設定
                tokyo_tz = pytz.timezone('Asia/Tokyo')

                # 現在の日本時間を取得
                attendance_time = timezone.now().astimezone(tokyo_tz)

                # 授業開始日時の設定と日本時間のタイムゾーン付加
                course_start_datetime = datetime.combine(course.start_date, course.start_time)
                course_start_datetime = tokyo_tz.localize(course_start_datetime)

                # デバッグ情報出力
                print(f"Attendance time: {attendance_time}")
                print(f"Course start datetime: {course_start_datetime}")

                # 出席ステータスの決定
                time_diff = (attendance_time - course_start_datetime).total_seconds() / 60  # 分単位
                print(f"Time difference: {time_diff} minutes")

                if time_diff <= 10:
                    status = 'Present'
                elif time_diff <= 15:
                    status = 'Late'
                else:
                    status = 'Absent'

                # 重複チェック
                if not Attendance.objects.filter(course=course, student=student_username).exists():
                    # 出席記録の保存
                    Attendance.objects.create(
                        course=course,
                        student=student_username,
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

def attendance_list_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    attendances = Attendance.objects.filter(course=course).order_by('attendance_time')

    context = {
        'course': course,
        'attendances': attendances,
    }
    return render(request, 'attendances/attendance_list.html', context)