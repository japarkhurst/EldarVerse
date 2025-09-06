import string

uppers = string.ascii_uppercase
lowers = string.ascii_lowercase



input = '''10
Ftq gzqjmyuzqp xurq ue zaf iadft xuhuzs
Znk cnurk oy mxkgzkx zngt znk yas ul ozy vgxzy
Je ru eh dej je ru jxqj yi jxu gkuijyed
Imagination is more important than knowledge
R jv xwln jpjrw jbtrwp oxa hxda orwjwlrju bdyyxac
Ftqdq ue za oxagp uf ue vgef eayqazq qxeqe oaybgfqd
Vhmsdq hr bnlhmf
Wvm lwma vwb aquxtg eits qvbw uwzlwz
Kyzj zj wzev
K vjkpm vjgtghqtg K ogog'''

for i,line in enumerate(input.split('\n')):
    if i == 0:
        continue
    for s in range(26):
        newUppers = uppers[s:] + uppers[:s]
        newLowers = lowers[s:] + lowers[:s]
        replaceDict = dict(zip(newUppers,uppers)) | dict(zip(newLowers,lowers))
        newline = "".join([replaceDict.get(_,_) for _ in line])
        print(newline)
        
  
