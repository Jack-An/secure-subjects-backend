import json
import os

from backend.serverless_db_sdk import database


class SubjectImporter:

    def __init__(self, filename, s_type, course_id):
        self.filename = filename
        self.s_type = s_type
        self.course_id = course_id

    def json_to_df(self):
        with open(self.filename, encoding='utf-8') as f:
            data = json.load(f)

        conn = database('secure_subjects').connection(autocommit=False)
        cursor = conn.cursor()
        count = 0
        for item in data:
            if self.s_type == "multiple":
                answer = "".join(item["answer"])
            else:
                answer = item["answer"]
            options = json.dumps(item["options"], ensure_ascii=False)
            sql = f"""insert into `subject`(`course_id`, `type`, `title`, `answer`, `tag`, `options`) values ({self.course_id}, '{self.s_type}', '{item['title']}', '{answer}', '{item['tag']}', '{options}')"""
            cursor.execute(sql)
            count += 1

            if count % 100 == 0:
                conn.commit()

        conn.commit()

    def sample_to_db(self):
        with open(self.filename, encoding='utf-8') as f:
            data = json.load(f)

        conn = database('secure_subjects').connection(autocommit=False)

        conn = conn._conn
        cursor = conn.cursor()
        for item in data:
            sql = f"""insert into `subject`(`course_id`, `type`, `title`, `answer`, `tag`) values ({self.course_id}, '{self.s_type}', '{item['title']}', '', '{item['tag']}')"""
            cursor.execute(sql)
            parent_id = cursor.lastrowid
            subs = item["subs"]
            for sub in subs:
                if sub["type"] == "multiple":
                    answer = "".join(sub["answer"])
                else:
                    answer = sub["answer"]
                options = json.dumps(sub["options"], ensure_ascii=False)
                sub_sql = f"""insert into `subject`(`course_id`, `type`, `title`, `answer`, `tag`, `options`, `parent_id`) values ({self.course_id}, '{sub["type"]}', '{sub['title']}', '{answer}', '', '{options}', {parent_id})"""
                cursor.execute(sub_sql)

            conn.commit()


if __name__ == '__main__':
    count = 0
    for ff in os.listdir("./lib"):
        with open(f'./lib/{ff}') as f:
            d = json.load(f)
            count += len(d)

    print(count)

    # s = SubjectImporter(filename="./lib/single_法规.json", s_type="single", course_id=2)
    # s.json_to_df()
    # s = SubjectImporter(filename="./lib/judge_法规.json", s_type="judge", course_id=2)
    # s.json_to_df()
    # s = SubjectImporter(filename="./lib/multiple_法规.json", s_type="multiple", course_id=2)
    # s.json_to_df()
    # s = SubjectImporter(filename="./lib/sample_法规.json", s_type="sample", course_id=2)
    # s.sample_to_db()
