# encoding: utf-8

from scrapy import cmdline


def main():
    cmdline.execute("scrapy crawl superspider".split())


if __name__ == '__main__':
    main()