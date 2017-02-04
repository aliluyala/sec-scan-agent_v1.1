#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2016-12-21 11:39:45
# Description:  coding 

import tornado.ioloop,os
import tornado.web,json
from tornado.web import HTTPError
from configure.setting import allowip
from libraries.common import  PocHashId,ModelHashId

def blocks(func):
    def decorator(self,*args,**kwargs):
        remote_ip = self.request.remote_ip
        if str(remote_ip) in allowip:
            return func(self,*args, **kwargs)
        else:
            raise HTTPError(403)
    return decorator

class MainHandler(tornado.web.RequestHandler):
    @blocks
    def get(self):
        self.current_user = "Hello ! Welcome to SEC API "
        name = tornado.escape.xhtml_escape(self.current_user)	
        #tornado.escape.json_encode(self.current_user)
        self.write(name)

class SubSaveHandler(tornado.web.RequestHandler):
    "save result into mysql and no repeat"
    def get(self):
        self.current_user = "Subdomain API"
        name = tornado.escape.xhtml_escape(self.current_user) 
        self.write(name)

    #@blocks
    def post(self):
    	res = self.get_body_arguments('result_info')[0].encode("gbk")
    	taskid = self.get_body_arguments('taskid')[0].encode("gbk")
    	model = self.get_body_arguments('model')[0].encode("gbk")
    	poc = self.get_body_arguments('poc')[0].encode("gbk")
    	target = self.get_body_arguments('target')[0].encode("gbk")

    	# res = tornado.escape.json_encode('result_info')
    	# taskid = tornado.escape.json_encode('taskid')
    	# model = tornado.escape.json_encode('model')
    	# poc = tornado.escape.json_encode('poc')
    	# target = tornado.escape.json_encode('target')
    	if res:
    		status = {"status":1,"taskid" : taskid , "target" : target , "model" : model , "poc" : poc}

    	self.write(json.dumps(status))
   
class UploadFileHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('''
<html>
<head><title>Upload File</title></head>
<body>
    <div>
        <form action='uploadfile' enctype="multipart/form-data" method='post'>
        <select name='types'>
            <option>web</option>
            <option>brute</option>
            <option>dddd</option>
            <option>eeee</option>
            <option>ffff</option>
        </select><br/>
        <input type='text' name='title'/><br/>
        <input type='file' name='file'/><br/>
        <input type='submit' value='submit'/>
        </form>
    </div>
</body>
</html>
''')

    def post(self):
        #文件的暂存路径
        upload_path = os.path.join(os.path.dirname(__file__),'models/web/')
        upload_path2 = os.path.join(os.path.dirname(__file__),'models/brute/') 
        print upload_path2
        #提取表单中‘name’为‘file’的文件元数据
        file_metas = self.request.files['file']                                                  
        title = self.get_body_arguments('title')[0].encode("gbk")
        types = self.get_body_arguments('types')[0].encode("gbk")

        for meta in file_metas:
            filename=meta['filename']
            file_type=meta['filename'].split(".")[-1].encode("gbk")
            if file_type == "py" :
                if str(types) == "web":
                    name = "web-"+str(title)
                    file_name = ModelHashId(name)+".py"
                    filepath=os.path.join(upload_path2,file_name)
                    #insert_db(table,types,title,file_name) 有数据库时写入
                    #有些文件需要已二进制的形式存储，实际中可以更改
                    with open(filepath,'wb') as up:      
                        up.write(meta['body'])
                elif str(types) == "brute":
                    name = "brute-"+str(title)
                    file_name = ModelHashId(name)+".py"
                    filepath=os.path.join(upload_path2,file_name)
                    #insert_db(table,types,title,file_name) 有数据库时写入
                    #有些文件需要已二进制的形式存储，实际中可以更改
                    with open(filepath,'wb') as up:      
                        up.write(meta['body'])
                else:
                    pass
                self.write('finished!')
            else:
                self.write('upload error!')


settings = dict(
            # template_path=TEMPLATE_PATH,
            # static_path=STATIC_PATH,
            # cookie_secret=str(uuid.uuid1()),
            #cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            #login_url="/login",
            # gzip=True,
            # xheaders=True,
            # 'xsrf_cookies': True,          # 防止跨站伪造
            # 'ui_methods': mt,              # 自定义UIMethod函数
            # 'ui_modules': md,              # 自定义UIModule类
            debug=True
        )



application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/sec/uploadfile",UploadFileHandler),
    (r"/sec/domain/save", SubSaveHandler)
], **settings)


if __name__ == "__main__":
    application.listen(3333)
    tornado.ioloop.IOLoop.current().start()





