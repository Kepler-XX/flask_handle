import uuid
import random


def is_none_or_empty(obj):
    """
      判断对象是否为空
    """
    if obj is None:
        return True
    elif isinstance(obj, int):
        return obj <= 0
    elif isinstance(obj, str):
        return len(obj.strip()) == 0


def get_str_uuid4():
    """
    uuid4生成
    """
    return str(uuid.uuid4())


def generate_code():
    """
    随机生成6位数字验证码
    """
    ret = ""
    for i in range(6):
        num = random.randint(0,9)
        s = str(random.choice([num,]))
        ret += s
    return ret


