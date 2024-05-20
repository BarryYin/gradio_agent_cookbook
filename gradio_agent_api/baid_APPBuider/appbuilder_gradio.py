import gradio as gr
import time
import appbuilder
import os

# 配置密钥与应用ID，需要替换成自己的 密钥和应用id
os.environ["APPBUILDER_TOKEN"] =""
app_id = ""

def respond(query, chat_history):
    # 初始化应用
    builder = appbuilder.AppBuilderClient(app_id)

    # 创建会话ID
    conversation_id = builder.create_conversation()

    # 执行对话
    msg = builder.run(conversation_id, query)

    chat_history.append((query, msg.content.answer))
    time.sleep(2)
    return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()