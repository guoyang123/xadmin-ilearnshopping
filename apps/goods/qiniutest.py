from qiniu import Auth, put_file

accessKey = "6JhwYyJs0AuaYLArQ7RxxRK_LRog-t4F2I9-s5e6"
secretKey = "J8miH3bnt2D5k2Sy66njm6rnLHsrnZzG5EyxTTOe"


# 解析结果
def parseRet(retData, respInfo):
    if retData != None:
        print("Upload file success!")
        print("Hash: " + retData["hash"])
        print("Key: " + retData["key"])

        # 检查扩展参数
        for k, v in retData.items():
            if k[:2] == "x:":
                print(k + ":" + v)

        # 检查其他参数
        for k, v in retData.items():
            if k[:2] == "x:" or k == "hash" or k == "key":
                continue
            else:
                print(k + ":" + str(v))
    else:
        print("Upload file failed!")
        print("Error: " + respInfo.text_body)


# 无key上传，http请求中不指定key参数
def upload_without_key(bucket, filePath):
    # 生成上传凭证
    auth = Auth(accessKey, secretKey)
    upToken = auth.upload_token(bucket, key=None)

    # 上传文件
    retData, respInfo = put_file(upToken, None, filePath)

    # 解析结果
    parseRet(retData, respInfo)


def main():
    bucket = "neuedu-ilearn"
    filePath = "d:/ftpfile/qr-1541422272256.png"
    upload_without_key(bucket, filePath)


if __name__ == "__main__":
    main()







