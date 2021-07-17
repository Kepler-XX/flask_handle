import time
import uuid
import hashlib
import base64
import requests

# DevOps告警通知模块发送短信功能配置
url = ''  # APP接入地址+接口访问URI
APP_KEY = "8lVq29N9w77VGT4DLq5I1L3qsKr6"  # APP_Key
APP_SECRET = "qo063Sdy740185A1P77fmk03VfuF"  # APP_Secret
sender = "8820101625583"  # 国内短信签名通道号或国际/港澳台短信通道号
TEMPLATE_ID = ""  # 模板ID
signature = "Kepler"  # 签名名称


def buildWSSEHeader(appKey=APP_KEY, appSecret=APP_SECRET):
    now = time.strftime('%Y-%m-%dT%H:%M:%SZ')  # Created
    nonce = str(uuid.uuid4()).replace('-', '')  # Nonce
    digest = hashlib.sha256((nonce + now + appSecret).encode()).hexdigest()
    digestBase64 = base64.b64encode(digest.encode()).decode()  # PasswordDigest
    return 'UsernameToken Username="{}",PasswordDigest="{}",Nonce="{}",Created="{}"' \
        .format(appKey, digestBase64, nonce, now)


def send_sms(receiver, param, sender=sender, template_id=TEMPLATE_ID, signature=signature):
    """
    发送短信,其他模块如需使用该方法，需重新设定signature, template_id, sender
    @param signature: 签名名称（不同模板不一样）
    @param template_id: 模板id （不同模板不一样）
    @param sender: 签名通道 （不同模板不一样）
    @param receiver: 手机号码，多个号码用英文,隔开
    @param param: 模板参数
    @return:
    """
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'WSSE realm="SDP",profile="UsernameToken",type="Appkey"',
        'X-WSSE': buildWSSEHeader()
    }
    formData = {
        'from': sender,
        'to': receiver,
        'templateId': template_id,
        'templateParas': param,
        'signature': signature
    }
    # 为防止因HTTPS证书认证失败造成API调用失败,需要先忽略证书信任问题
    r = requests.post(url, data=formData, headers=header, verify=False)
    return r.json()


if __name__ == '__main__':
    receiver = "15050480107"
    param = '["错误","devops","测试lucianlu","2020-10-19","磁盘空间不足的房价肯定沙发考虑实际的反馈"]'
    print(send_sms(receiver, param))
