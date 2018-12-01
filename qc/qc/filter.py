from scrapy.dupefilter import RFPDupeFilter
import hashlib
class myDupeFilter(RFPDupeFilter):
    # def request_fingerprint(self, request):
    #     url=request._url
    #     if len(url)>1:
    #         return url[0]
    #     else:
    #         return request._url
    def request_fingerprint(self, request):
        if "kw" in request.meta:
            kw=request.meta["kw"]
            #通过hash算法将生成的密码串放在set集合中,减少了内存的开销
            return (hashlib.sha1("http://www.baidu.com/?kw=")).decode("utf-8")
        else:
            return hashlib.sha1((request._url).encode("utf-8"))