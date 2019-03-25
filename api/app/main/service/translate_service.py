from xmlrpc.client import ServerProxy

url = "http://localhost:8080"
proxy = ServerProxy(url)


# text = u"This is my home"
# params = {"text":text, "align":"false", "report-all-factors":"false"}
#
# result = proxy.translate(params)
#
# print result['text']
#
# if 'id' in result:
#     print "Segment ID:%s" % (result['id'])
#
# if 'align' in result:
#     print "Phrase alignments:"
#     aligns = result['align']
#     for align in aligns:
#         print "%s,%s,%s" %(align['tgt-start'], align['src-start'], align['src-end'])

def translate_text(data):
    text_to_translate = data["text"]
    params = {"text": text_to_translate, "align": "false", "report-all-factors": "false"}
    result = proxy.translate(params)
    response_object = {
        'status': 'success',
        'message': 'Successfully Translated.',
        'Translation': result['text']
    }
    return response_object, 200
