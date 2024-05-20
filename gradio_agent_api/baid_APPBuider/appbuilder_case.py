import appbuilder
import os

# 配置密钥与应用ID
# 设置环境变量APPBUILDER_TOKEN，目前填的这个是官方的受限试用TOKEN
os.environ["APPBUILDER_TOKEN"] = "bce-v3/ALTAK-n5AYUIUJMarF7F7iFXVeK/1bf65eed7c8c7efef9b11388524fa1087f90ea58"
# 地理小达人应用ID
app_id = "42eb211a-14b9-43d2-9fae-193c8760ef26"

# 初始化应用
app = appbuilder.AppBuilderClient(app_id)
# 创建对话，这次的对话ID就是conversation_id了
conversation_id = app.create_conversation()

# 进行对话，问 地理小达人应用，"中国的首都在哪里？"
msg = app.run(conversation_id, "中国的首都在哪里？")

# 打印查看一下 地理小达人应用 的回复
print(msg.content.answer)