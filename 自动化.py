import requests
from pprint import pprint

#列出课程
res = requests.get('http://localhost/api/mgr/sq_mgr/?action=list_course&pagesize=20')
#print(res.status_code,width=30)
list1 = res.json()['retlist']

#添加课程
res = requests.post('http;//localhost/api/mgr/sq_mgr/',
              data={
                  'action': 'add_course',
                  'data': '''{
                  "name":"初中化学",
                  "desc":"初中化学课程",
                  "display_idx":"4"
                  }
                  '''
              })
#print(res.status_code,width=30)

retObj = res.json()
pprint(retObj,width=30)

if retObj['retcode'] == 0:  #Python 字典
    print('检查点：返回结果retcode为0，检查通过')
else:
    print('检查点：返回结果retcode不为0，检查不通过')

#列出课程
res = requests.get('http://localhost/api/mgr/sq_mgr/?action=list_course&pagesize=20')

list2 = res.json()['retlist']

#去除，多出来的一门课程对象
newcourse = None

for one in list2:
    if one not in list1:
        newcourse = one
        break

#检查是否是刚刚添加的课程
assert newcourse!=None
assert newcourse['name']=='初中化学'
assert newcourse['desc']=='初中化学课程'
assert newcourse['display_idx']=='4'