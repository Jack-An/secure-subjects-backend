from backend.enums import SubjectType
from backend.serverless_db_sdk import database


class SubjectService:

    @classmethod
    def get_subject_by_type_with_start(cls, subject_type, start_id):
        conn = database().connection()

    @classmethod
    def get_subject_stats_with_progress(cls, course_id):
        return [
            {
                "type": SubjectType.single.value,
                "total": 100,
                "process": 11
            },
            {
                "type": SubjectType.multiple.value,
                "total": 60,
                "process": 20
            },
            {
                "type": SubjectType.judge.value,
                "total": 60,
                "process": 30
            },
            {
                "type": SubjectType.sample.value,
                "total": 30,
                "process": 20
            }
        ]









