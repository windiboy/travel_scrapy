import re
from wang.model.kashi_comment import KashiComment

if __name__ == '__main__':
    rows = KashiComment.select().order_by(KashiComment.id.desc())
    for row in rows:
        pattern = re.compile(r'\s+')
        new_content = re.sub(pattern, '', row.content)
        row.content = new_content
        row.save()
        print("format content success, id = {}".format(row.id))