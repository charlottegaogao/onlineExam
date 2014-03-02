已完成：
-添加、删除、修改试题
-添加、删除、修改试卷
-学生做题（做题库所有的题目）
-数据库建立

未完成：
-随机组卷
-优先权组卷
-其他组卷算法


关于此次修改
-setting.py
TEMPLATE_LOADERS，让所有电脑都能成功加载模板，避免不必要的错误。

-models.py
修改了Question的定义，answer增加choice属性，防止答案超出4个选项

-格式
修改部分不合法的缩进

（此次修改基于雨薇的最新分支）

操作方法：
open onlineExam/onlineTest/setting.py
search for "databases"
fill the 'Name' with the path of your database
syncdb
runserver
login to admin
edit datas of your database
login to .../instantTest to test everything
