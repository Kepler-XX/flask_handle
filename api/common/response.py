from flask import jsonify


def success(code=200, msg='success', data=''):
    if data is None:
        return jsonify({"code": code, "msg": msg})
    return jsonify({"code": code, "msg": msg, "data": data})


def fail(code=500, msg='failed', data=''):
    if data is None:
        return jsonify({"code": code, "msg": msg})
    return jsonify({"code": code, "msg": msg, "data": data})

