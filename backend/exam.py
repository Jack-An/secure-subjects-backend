from datetime import datetime


class Course:
    id: int
    name: str


class Subject:
    id: int
    course_id: int
    type: str
    title: str
    answer: str
    tag: str
    parent_id: int
    options: list


class Exam:
    id: int
    course_id: int
    user_id: int
    created_at: datetime
    cost: int
    score: int
    detail: dict


class CorrectBook:
    id: int
    course_id: int
    user_id: int
    subject_id: int
    count: int

