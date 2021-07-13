from flask import request

from api.controller.user import user_api
from api.common import response
from api.services.user.userservice import UserService


@user_api.route("/all", methods=['GET'])
def user_all():
    """
    page : 页码 默认1
    size : 每页个数   默认10
    :return:
    """
    try:
        page = request.args.get("page", 1)
        size = request.args.get("size", 10)
        user_list = UserService.user_all(page, size)
        return user_list
    except Exception as e:
        return response.fail(msg="get all user failed")
