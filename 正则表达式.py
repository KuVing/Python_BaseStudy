# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 15:08:33 2021

@author: 15003
"""

import re
def main():
    s=r"jkl"
    a="sdfghjkllkjhgfds jklsdadsasdad"
    print(re.findall(s,a))
    
    
    s1=r"^jkl"
    a1="jkllkjhgfds sddfsfds"
    print(re.findall(s1,a1))
    
    s2=r"ds$"
    a2="jkllkjhgfds sddfsfds"
    print(re.findall(s2,a2))

    s3=r"\d"   #d匹配数字
    a3="asdas1231zxfas13213xfada1d6547e6r5346dasad"
    print(re.findall(s3,a3))
    
    s4=r"\D"   #D匹配非数字
    a4="asdas1231zxfas 13213xfada1d 6547e6r5346dasad"
    print(re.findall(s4,a4))
    
    s5=r"\s"  #s匹配空字符，S非空字符
    a5="asdas1231zxfas 13213xfada1d 6547e6r5346dasad"
    print(re.findall(s5,a5))

    s6=r"\W"      #w匹配字母和数字，W匹配符号和空格
    a6="asdas123$%^&!@#@!1zxfas 13213xfada1d 6547e6r5346dasad"
    print(re.findall(s6,a6))
    
    s7=r"^0510-\d{8}"    #s7=r"^\d{4}-\d{8}"
    a7="0510-85197880sadadvjkbnjkb"
    print(re.findall(s7,a7))
    
    s8=r"ab?"    #?只能找到0个或1个
    a8="a ab abb abbb abbbbb"
    print(re.findall(s8,a8))
    
    s9=r"ab{2,4}"    #?只能找到0个或1个
    a9="a ab abb abbb abbbbb"
    print(re.findall(s9,a9))
    
    s10=r"ab\d{1,2}"    #?只能找到0个或1个
    a10=" a ab ab2 ab23 ab234 ab2345"
    print(re.findall(s10,a10))
    
    s11=r"[a-zA-Z0-9]{4,20}@(163|126|gmail|qq)\.com$"   #匹配条件
    a11="Hahanihao@qq.com"
    print(re.match(s11,a11).group())    #match从头开始搜索，开头没有就结束。
                                        #findall搜索整个字符串
                                        #search搜索整个字符串
    
    s12=r"<\w*>.*</\w*>"   #匹配条件
    a12="<h1>haha</h1>"
    print(re.match(s12,a12).group())
    
    s13=r"<(\w*)>.*</\1>"   #匹配条件
    a13="asdasasdasdas<h1>haha</h1>asdasdasdad"
    print(re.search(s13,a13).group())
    
    s14=r"\d+"    #如果只写d只会有9，d+匹配一个或多个数字
    a14="阅读数：9991 887"
    print(re.search(s14,a14).group())   #加group用于截取字符串
    
    s15=r"\d+"    
    a15="阅读数：9991"
    print(re.sub(s15,"100",a15))
    
    s16=r"a.*b"    #.表示匹配任意字符一次，.*表示0次或多次
    a16="a ab abb abbb abbbbb acb afasdadsasdb"
    print(re.findall(s16,a16))
    
    s17=r"a.b"   
    a17="a ab abb abbb abbbbb acb afasdadsasdb"
    print(re.search(s17,a17).group())   #search输出找到的第一个
    
    obj=re.compile("\d{2}") 
    print(obj.search("asdasdasdasdadsd123123123").group())
    print(obj.search("123123123").group())
    
    ret=re.finditer("\d{3}","asdasdasdasd1234asd5678")
    #print(next(ret).group())  
    #print(next(ret).group()) 
    print([i.group() for i in ret])
    
    s18=r'<span class=".*?">(.*?)</span>'
    a18='<span class="bjh-p"> 俄罗斯联邦消费者权益保护和公益监督局局长波波娃20日表示，俄罗斯境内有7人确诊感染了H5N8型禽流感病毒，这是全球首次发现人感染该型禽流感病毒。</span>'
    print(re.findall(s18,a18))
    
    s19=r'<a.*?href="(.*?)".*?>.*?</a>'
    a19='<a href="https://www.baidu.com" alt="to baidu">去百度看</a>'
    print(re.findall(s19,a19))
    
    #软件match tracer

if __name__ =="__main__":
    main()