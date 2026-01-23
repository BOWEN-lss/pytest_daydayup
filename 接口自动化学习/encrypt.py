import execjs
import os
rootPath = os.path.dirname(__file__)
jsPath = os.path.join(rootPath,"md5.js")

class ExecJs(object):
    _instance = False
    def _get_js(self, name):
        js_str = ''
        with open(name, 'r', encoding="utf-8") as f:
            line = f.readline()
            while line:
                js_str = js_str + line
                line = f.readline()
        return js_str

    def get_encrypt_pwd(self, function,*args):
        ctx = execjs.compile(self._get_js(jsPath))
        return ctx.call(function, *args)

if __name__ == "__main__":
    e = ExecJs()
    print(e.get_encrypt_pwd('md5','123ABCdef*', "zx3nhqeupprmhm2f"))
