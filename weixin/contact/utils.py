import time

import pystache


class Utils:
    ##mustche模板获取数据
    @classmethod
    def parse(self, template_path, dict):
        template = "".join(open(template_path).readlines())
        return pystache.render(template, dict)

    @classmethod
    def udid(self):
        return str(time.time()).replace(".", "")[0:11]