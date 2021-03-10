HHU-auto-checkin(Github Action版)
=========================================
河海大学健康打卡自动打卡脚本，请在健康状态下使用。
如有身体不适等情况,请停止使用本程序,如实进行健康打卡!

# 使用说明

1、Fork本仓库，然后点击你的仓库右上角的 Settings，找到 Secrets 这一项，添加两个秘密环境变量USERNAME(其值为你的学号)和PASSWORD(其值为你的密码)。

2、设置好环境变量后点击你的仓库上方的 Actions 选项，点击 I understand... 按钮确认在 Fork 的仓库上启用 GitHub Actions。

３、(可选）在你这个 Fork 的仓库内修改一下.github/workflows/action.yml 文件（这个本项目的Workflow的配置文件）。默认为早上九点到十点随机某一分钟、十一点到十二点随机某一分钟进行打卡操作。

4、提示: 如果不进行一次手动触发，GitHub action似乎并不会自动执行。第一次使用时，请务必进行一次手动触发，即随便在README.md（当然本项目任意一个文件都是可以的，不一定非要README中）末尾打几个空格提交就可以。

# 参考
Auto_healthyReport: https://github.com/zibowang81192/Auto_healthyReport
