import sys
sys.path.append("..")
from ddt import data, file_data, unpack,ddt
from common import common
import unittest, requests,json

path='TestData/'
# path='../TestData/'

@ddt
class Test_DownLoadFile(unittest.TestCase):
    """docstring for TestPcloud"""
    def setUp(self):
        self.headers = {
            'accept': "application/json, text/javascript, */*; q=0.01",
            'origin': "https://my.pcloud.com",
            'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            'referer': "https://my.pcloud.com/",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.8",
            'cache-control': "no-cache",
            'postman-token': "45c3ef40-d05d-c594-df12-caac7a5e25d8"
            }

        self.url = "https://api8.pcloud.com/downloadfile"
        self.querystring = {"folderid":"0","progresshash":"upload-9087083-xhr-496","nopartial":"1","url":"http://vt.media.tumblr.com/tumblr_o97j6zzYpG1vnl0qg.mp4","auth":"mS9A7XZT5kwZOX744AA1zmhExgU2VIy63V1dsByk"}
    
    @data('http://vt.media.tumblr.com/tumblr_oaa3puzXkZ1u8q5iu.mp4')
    # @data(*common.getCsv(path+'testmp4addr.csv'))
    # @unpack
    def test(self,post_url):
        self.querystring['url']= post_url
        response = requests.request("POST", self.url, headers=self.headers, params=self.querystring)
        response = json.loads(response.text)
        self.assertEqual(response['result'],0)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
        
