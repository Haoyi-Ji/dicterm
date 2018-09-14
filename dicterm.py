#! -*- coding: utf-8 -*-
import sys
import requests
from pyterm import Term


class dictionary():
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/openapi.do'
        self.t = Term()
        self.payload = {
            'keyfrom': '# your app name',
            'key': '# your key',
            'type': 'data',
            'doctype': 'json',
            'version': '1.1'
        }

    def translate(self, query):
        self.payload['q'] = query
        r = requests.get(self.url, params=self.payload)
        j = r.json()
        if j['errorCode'] == 0:
            translation = j['translation']
            for each in translation:
                _ = self.t.BOLD.MAGENTA(each + '\n')
            if 'basic' in j.keys():
                if 'us-phonetic' in j['basic'].keys():
                    _ = self.t.BOLD.RED('[' + j['basic']['us-phonetic'] + ']\n')
                elif 'uk-phonetic' in j['basic'].keys():
                    _ = self.t.BOLD.RED('[' + j['basic']['uk-phonetic'] + ']\n')
                elif 'phonetic' in j['basic'].keys():
                    _ = self.t.BOLD.RED('[' + j['basic']['phonetic'] + ']\n')

                if 'explains' in j['basic'].keys():
                    for each in j['basic']['explains']:
                        _ = self.t.BOLD.GREEN(each + '\n')

            print()
            if 'web' in j.keys():
                for each in j['web']:
                    _ = self.t.BOLD.CYAN(each['key'] + '\n')
                    for v in each['value']:
                        _ = self.t.BOLD.GREEN('    ' + v + '\n')
                    print()


def main():
    dict = dictionary()
    if len(sys.argv) == 1:
        while 1:
            query = input('> ').strip()
            if query in ['q()', 'quit()', 'exit()']:
                exit(0)
            else:
                dict.translate(query)
    else:
        query = ' '.join(sys.argv[1:])
        dict.translate(query)


if __name__ == '__main__':
    main()
