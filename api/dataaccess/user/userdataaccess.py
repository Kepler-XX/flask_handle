from pymysql import cursors
import math
from api.common.db import get_db


class UserAccess:
    def __init__(self):
        self.db = get_db()

    def user_all(self, page, size):
        cursor = self.db.cursor(cursor=cursors.DictCursor)
        query_sql = ' where 1=1 '
        query_param_limit = []
        query_param_limit.append((int(page) - 1) * int(size))
        query_param_limit.append(int(size))
        cursor.execute("select *  from  user_people"
                       + format(query_sql) +
                       " limit %s,%s", query_param_limit)
        info = cursor.fetchall()
        data = {'data': info, 'totalCount': len(info), 'totalPage': math.ceil(len(info) / 10),
                'pageNo': page, 'pageSize': size}
        return data
