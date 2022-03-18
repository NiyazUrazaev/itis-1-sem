from docxtpl import DocxTemplate


class DiaryDocx:

    def __init__(self, student, teacher, practice, diary_days):
        self.doc = DocxTemplate(
            "./diary_template.docx"
        )
        self.context = {}
        self.student = student
        self.teacher = teacher
        self.practice = practice
        self.diary_days = diary_days

    def create_docx(self):
        self.context.update(self.create_header())
        self.context.update(self.create_teacher_info())
        self.context.update(self.create_user_info())
        self.context.update(self.create_table_info())

        self.doc.render(self.context)
        self.doc.save("./generated_diary.docx")

    def create_header(self):
        data = {
            "practice_type": self.practice["practice_type"],
            "date_start_day": self.practice["date_start_day"],
            "date_start_month": self.practice["date_start_month"],
            "date_start_year": self.practice["date_start_year"],
            "date_end_day": self.practice["date_end_day"],
            "date_end_month": self.practice["date_end_month"],
            "date_end_year": self.practice["date_end_year"],
            "practice_address": self.practice["practice_address"],
        }
        return data

    def create_user_info(self):
        return {
            "user_full_name": self.student["user_full_name"],
            "user_group": self.student["user_group"],
        }

    def create_teacher_info(self):
        return {
            "teacher_position": self.teacher["teacher_position"],
            "teacher_short_name": self.teacher["teacher_short_name"],
        }

    def create_table_info(self):
        table_data = [
            {"date": day["date"], "work_info": day["work_info"]}
                for day in self.diary_days
        ]
        return {
            "table": table_data
        }


student = {
    "user_full_name": "Иванов Иван Иванович",
    "user_group": "11-705"
}

teacher = {
    "teacher_position": "Старший преподаватель",
    "teacher_short_name": "Иванов И.И.",
}

practice = {
    "practice_type": "Учебная",
    "date_start_day": "18",
    "date_start_month": "3",
    "date_start_year": "2022",
    "date_end_day": "15",
    "date_end_month": "4",
    "date_end_year": "2022",
    "practice_address": "г. Казань, ул. Кремлевская 35",
}

diary_days = [
    {"date": "18.3.22", "work_info": "Что-то делаю"},
    {"date": "20.3.22", "work_info": "Что-то делаю"},
    {"date": "23.3.22", "work_info": "Что-то делаю"},
    {"date": "25.3.22", "work_info": "Что-то делаю"},
    {"date": "27.3.22", "work_info": "Что-то делаю"},
    {"date": "29.3.22", "work_info": "Что-то делаю"},
    {"date": "1.4.22", "work_info": "Что-то делаю"},
    {"date": "10.4.22", "work_info": "Что-то делаю"},
    {"date": "15.4.22", "work_info": "Что-то делаю"},
]

docx_diary = DiaryDocx(
    student,
    teacher,
    practice,
    diary_days,
)

docx_diary.create_docx()