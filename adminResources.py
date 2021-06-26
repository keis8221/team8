from import_export import resources
from .models import Teacher

class TeacherResources(resources.ModelResource):
    class Meta:
        model = Teacher
        skip_unchanged = True
        report_skipped = False
        # import_id_fields = ('id',)
        fields = ('id', 'subject_id', 'subject_name', 'teacher_id', 'teacher_name', 'start_time', 'finish_time', 'attend_time', 'late_time','password')
        # fields = ('講義ID','科目名','ID','教員名','開始時間','終了時間','出席限度(分)','遅刻限度(分)')
