HHU-auto-checkin(Github Action版)
=========================================
**河海大学健康打卡自动打卡脚本，请在健康状态下使用，请勿滥用！！！**
**如有身体不适等情况，请停止使用本程序，如实进行健康打卡!**

# 使用说明

**1**、Fork本仓库
![](https://raw.githubusercontent.com/asmallbit/ImageStore/master/HHUAutoCheckin/Fork.png)

**2**、点击你的仓库右上角的 Settings，找到 Secrets 这一项，添加两个秘密环境变量``USERNAME``(其值为你的学号)和``PASSWORD``(其值为你的密码)。如需为多个账户进行打卡，账号密码一行一个，一一对应
示例:
**USERNAME**
```
1234567890
0987654321
```

**PASSWORD**
```
123456
654321
```

![](https://raw.githubusercontent.com/asmallbit/ImageStore/master/HHUAutoCheckin/AddInserts.png)
![](https://raw.githubusercontent.com/asmallbit/ImageStore/master/HHUAutoCheckin/Username.png)
![](https://raw.githubusercontent.com/asmallbit/ImageStore/master/HHUAutoCheckin/Password.png)

**3**、(1)**启用Action**  点击你的仓库上方的 Actions 选项，点击 I understand...按钮。
![Enable Action](https://raw.githubusercontent.com/asmallbit/ImageStore/master/HHUAutoCheckin/EnableActions.png)
(2)**Enable Workflow**  在**Actions**中点击**Enable workflow**
![Enable Workflow](https://raw.githubusercontent.com/asmallbit/ImageStore/master/HHUAutoCheckin/EnableWorkFlows.png)
(3)**Run Workflow**  在刚才的基础上,点击**Run workflow**
![Run Workflow](https://raw.githubusercontent.com/asmallbit/ImageStore/master/HHUAutoCheckin/RunWorkflows.png)

**4**、查看运行结果
actions>HHU_Auto_Checkin>Auto_Checkin
如果显示以下类似结果,代表设置成功
![Succeed Image](https://raw.githubusercontent.com/asmallbit/ImageStore/master/HHUAutoCheckin/Result.png)
之后,将会在每天上午9:00-10:00之间和11:00-12:00之间各打卡一次
如果需要更改打卡时间，可以在``.github/workflows/action.yml``中的``cron``自行修改

**5**、（可选）可以通过和步骤二添加secrets的方式一样，添加``RAMDOMTIME``这个变量，这个变量值为你想要的最大延迟时间，比如你想让它在某个时段的25分钟内随机某一分钟进行打卡，就把这个值设置为25。同时可以和步骤三的方式一样，启动``Avoid GitHub action being suspended``workflow，这个workflow的目的是，避免仓库在两个月不活跃后workflow被关闭。详情请参见 https://docs.github.com/en/actions/managing-workflow-runs/disabling-and-enabling-a-workflow

# 参考
**Auto_healthyReport**: https://github.com/zibowang81192/Auto_healthyReport
