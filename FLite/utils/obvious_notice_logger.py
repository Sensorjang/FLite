import logging
import os

class noticelogger(object):
    def __init__(self):
        # 获取当前目录下的banner.txt文件
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                            filename='./test.log', filemode='a')

    #获取单例
    @staticmethod
    def get_instance():
        if not hasattr(noticelogger, "_instance"):
            noticelogger._instance = noticelogger()
        return noticelogger._instance

    def red(self, message):
        logging.info("\033[1;31m{msg} \033[0m".format(msg=message))

    def green(self, message):
        logging.info("\033[1;32m{msg} \033[0m".format(msg=message))

    def yellow(self, message):
        logging.info("\033[1;33m{msg} \033[0m".format(msg=message))

    def blue(self, message):
        logging.info("\033[1;34m{msg} \033[0m".format(msg=message))

    def purple(self, message):
        logging.info("\033[1;35m{msg} \033[0m".format(msg=message))

    def cyan(self, message):
        logging.info("\033[1;36m{msg} \033[0m".format(msg=message))

    def white(self, message):
        logging.info("\033[1;37m{msg} \033[0m".format(msg=message))

    def black(self, message):
        logging.info("\033[1;30m{msg} \033[0m".format(msg=message))

    def FLiteTitle(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        banner_path = os.path.join(current_path, "banner.txt")
        with open(banner_path, "r") as f:
            txt = None
            for i, line in enumerate(f.readlines()):
                if i < 1:
                    self.red(line.strip())
                else:
                    if txt is None:
                        txt = line
                    else:
                        txt = txt + line
            self.blue(txt)


if __name__ == "__main__":
    logger = noticelogger()
    logger.FLiteTitle()