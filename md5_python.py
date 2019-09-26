import hashlib

class md5Python(object):
    """MD5签名和验签"""

    @classmethod
    def data_processing(cls, data):
        """
        :param data: 需要签名的数据，字典类型
        :return: 处理后的字符串，格式为：参数名称=参数值，并用&连接
        """
        if "sign" in data:
            del data["sign"]
        dataList = []
        for key in sorted(data):
            if data[key] and key!= "imgData":
                dataList.append("%s=%s" % (key, data[key]))
        return "&".join(dataList).strip()

    @classmethod
    def md5_sign_str(cls, data, api_key):
        """
        MD5签名的完整字符串
        :param data: 需要签名的数据，字典类型
        :param api_key: MD5签名需要的字符串
        :return: 处理后的字符串，格式为：参数名称=参数值，并用&连接，最后用&连接'key=api_key'
        """
        data = cls.data_processing(data) + '&key=' + api_key.strip()
        return data

    @classmethod
    def md5_sign(cls, data, api_key):
        """
        MD5签名
        :param api_key: MD5签名需要的字符串
        :return: 签名后的字符串sign
        """
        data = cls.data_processing(data) + '&key=' + api_key.strip()
        md5 = hashlib.md5()
        md5.update(data.encode(encoding='UTF-8'))
        return md5.hexdigest()

    @classmethod
    def md5_verify(cls, data, signature):
        """
        md5验签
        :param data: 接收到的数据
        :param signature: 接收到的sign
        :return: 验签结果,布尔值
        """
        if cls.md5_sign(data) == signature:
            return True
        else:
            return False