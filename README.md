一、	目的
  
  经过调查发现，传统的考试模式中，存在着一些弊端：
    一是老师需要花费了大量的时间找试题，根据知识点拼试卷，评分，计算成绩，整个过程工作量很大；
    二是反馈信息的能力不强，对成绩的分析停留在平均分或者及格率上，很难准确地反映出学生对知识点的掌握程度。
    同时，在大学里，有些课程存在比较严重的翘课情况。
  为了解决这些问题，我们想要设计出一种即能够帮助老师出题和及时反馈信息，又能提高学生对知识的掌握程度的在线即时考试系统。


二、	思路
  用户的操作通过浏览器实现，不用安装任何软件，只需要有一台能上网的电脑或者智能手机就可以访问系统。
  系统大概有五个模块，分别是在线考试，题库管理，控制考试，成绩查询，系统管理。
  用户分为三类，分别为学生用户，教室用户，管理员用户。

  1、	用户需要经过身份认证才能进入相应用户身份的主页。学生输入学号、密码、测试码进入考试；教师输入用户名和密码进入制定试卷，控制考试以及题库管理，查看学生成绩等操作的页面；管理员输入管理员账号和密码进入系统管理的页面。

  2、	学生允许需要输入老师给予的测试码后，在线参加考试，考试类型分为即时课堂测试和期末考试两种。即时课堂测试只有选择题一种题型，在规定的时间内完成规定的题目，学生每做一题点击“OK”后再点击“Next”，进入下一题，不可后退，直到完成所有的题目，完成后即时显示得分、错题及答案。期末考试模式有选择题、分析题或者问答题等多种题型，在规定的考试时间内，学生可以点击“Back”或“Next”进行答题和检查，考试计时器为0时或者学生点击提交试卷，考试结束，不显示成绩和答案。

  3、	教师进入主页后，可以制定试卷，输入题目总数，考点，难度等参数后，选择一个组卷模式（包括优先权算法，随机抽取算法，误差补偿算法，回溯试探法，基于专家只是的框架模式的智能组卷法，遗传算法等），自动生成临时题库（每个学生登录后，自动从这个临时题库中抽取相同数目的题目，随机排序给学生，防止作弊），教师可以对生成的临时题库进行增删改查工作，在确认修改后进入选定参加考试的学生群体，点击发布，系统生成自动生成测试码。教师可以查询每一个学生的成绩。教师可以对题库进行管理，所有的教师共享题库资料，都有权限对题库进行增删改查的操作，增加题库可以单条导入或者批量导入，删除可以单条删除也可以批量删除。

  4、	管理员可以其他用户进行添加、删除和权限修改（比如随着系统功能的发展，需要添加新的角色），或者对用户资料进行添加、修改和删除（比如删除已经毕业的学生，更换了课程老师），或者对系统参数的设置（比如关闭系统，切换到其他模式等）。


三、	方法
  系统将以小组合作的形式完成，采用Django 1.5的Web应用框架，结合现有的Bootstrap 网页前端开发框架，使用Python，HTML5，CSS3，JavaScript语言进行开发。

四、	进度安排

	2013年11月11日~2013年12月11日，细化阶段1，完成及时课堂测试模式。
  2013年12月30日，提交中期报告。
  2013年12月11日~2014年1月11日，细化阶段2，拓展完成期末测试模式。
  2014年1月11日~2014年2月1日，细化阶段3，详细完成用例，进行补充拓展
……

五、程序说明

已完成：
1.教师：
-增加试卷（手动增加）
-增加问题
-删除问题
-修改问题
-登录、登出
2。管理员：
-增加、删除、修改用户
-增加、删除、修改用户组
-增加、删除、修改试卷
-增加、删除、修改问题

未完成：
1.教师
-自动组卷
2.学生
-输入学号和测试码（试卷名字）
-考试（一题一题地进行，不能后退）
-结束考试（数据存入数据库的Test类）
-考试计时（可能用到python的工具，暂时没有找到合适的；也可以考虑用javescript来解决）

注意事项：
1.对于表单信息的验证全部都在forms.py里，有些是已经写了验证的方法，但是方法可能不完全，所以没使用（必填项验证已经加入）
2.django的时间特别奇怪，用系统的自带的datetimefield生成的text类型的表单项，输入的时候必须有一定格式才能储存，非常奇怪。还需要一点时间来研究一下。（建议去看django2.0表单部分，和官方文档）
3.paper_name是唯一的，这个输入的时候必须是不重复的，这个在form里已经加入了验证方法，但是没有实现，所以输入的时候要注意，时间太紧了，以后有时间再改
4.django自带的用户认证很好用（可以去看django2.0的认证部分），所以我就没有在model里加User，用系统自带的user。但是我发现student这个类可能需要去继承user类，这里我没试过python的继承，所以有空再试试。
5.因为django还有些用法不太熟悉，花了一些时间来了解，这么久才做了这么点功能真的很抱歉了。
6.程序不包含数据库，请先在数据库建立同名数据（setting.PY里），再用models生成数据库
7.教师登录地址是127.0.0.1：8080/signin，管理员登录是127.0.0.1:8080/admin,可以直接用管理员账号登陆教师地址，但是在管理界面新建的user如果没有赋予is_STAFF权限，是不能登录的管理员界面的。
