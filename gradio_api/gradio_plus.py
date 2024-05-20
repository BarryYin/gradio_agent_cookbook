import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Gradio组件演示
        （这是一个`gr.Markdown()`组件，也是一个**输入输出组件**）\n
        下面会把每个组件的python代码写成其`label`\n
        **布局组件**不会被展示出来，但是会用到: \n
        - `gr.Blocks()`: 把组件堆在一起、\n
        - `gr.Column()`: 把组件放在一列、\n
        - `gr.Row()`: 把组件放在一行、\n
        - `gr.According()`: 把组件放在一个折叠里、\n
        - `gr.Tab()`: 把组件放在一个标签页面板里
        """
    )
    # with gr.Row():
    gr.Markdown("用`gr.Column()`将下面所有内容做成一列")
    with gr.Column(variant="panel", scale=1):
        
        gr.Markdown("## 输入输出组件")
        gr.Markdown("现在，用`gr.Row()`将下面的 **`文本组件`** 和 **`滑动条组件`** 做成一行")
        with gr.Row():
            
            name = gr.Textbox(
                label="gr.Textbot()",
                placeholder="John Doe",
                value="这里是可以输入输出的",
                interactive=True,
            )
            slider1 = gr.Slider(label="gr.Slider()")
        gr.Markdown("现在，用`gr.Row()`将下面的 **`多选组件`** 和 **`单选组件`** 做成一行")
        with gr.Row():
            gr.CheckboxGroup(["A", "B", "C"], label="gr.CheckboxGroup()")
            radio = gr.Radio(
                ["A", "B", "C"],
                label="gr.Radio()",
                # info="单选组件",
            )
        gr.Markdown("下面是 **`单选下拉组件`** 和 **`多选下拉组件`**：")
        with gr.Row():
            drop = gr.Dropdown(["Option 1", "Option 2", "Option 3"], label="gr.Dropdown()", info="multiselect=False(默认)")
            drop_2 = gr.Dropdown(
                ["Option A", "Option B", "Option C"],
                multiselect=True,
                value=["Option A"],
                label="gr.Dropdown()",
                info="multiselect=True",
                interactive=True,
            )
        gr.Markdown("下面是 **`勾选组件`** 、 **`按钮组件`** 和 **`颜色选择组件`**：")
        with gr.Row():
            check = gr.Checkbox(label="gr.Checkbox()")
            go_btn = gr.Button("gr.Button()")
            gr.ColorPicker(label="gr.ColorPicker()")

        gr.Markdown("下面是 **`图像组件`**：")
        img = gr.Image(label="gr.Image()")
        gr.Markdown("下面是 **`表格组件`** 和 **`JSON格式组件`**：")
        with gr.Row():
            gr.Dataframe(value=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], label="gr.Dataframe()")
            gr.JSON(
                value={"a": 1, "b": 2, "c": {"test": "a", "test2": [1, 2, 3]}}, label="gr.JSON()"
            )
        gr.Markdown("下面是 **`标签组件`**：")
        gr.Label(label="gr.Label()", value={"cat": 0.7, "dog": 0.2, "fish": 0.1})
        gr.Markdown("下面是 **`文件组件`**和 **`视频组件`**：")
        with gr.Row():
            gr.File(label="gr.File()")
            gr.Video(label="gr.Video()")
        gr.Markdown("下面是 **`图册组件`**(gr.Gallery())：")
        gr.Gallery(
            [
                (
                    "https://linklearner.com/assets/logo-vAxrscYT.png",
                    "Datawhale",
                ),
                (
                    "https://oss.linklearner.com/learning-project/%E5%8A%A8%E6%89%8B%E5%AD%A6%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91.png",
                    "logo",
                ),
            ]
        ).style(height="200px", grid=2)
        gr.Markdown("下面是 **`对话框组件`**：")
        chatbot = gr.Chatbot([("Hello", "Hi")], label="gr.Chatbot()")
        gr.Markdown("下面是 **`折叠组件`** 和 **`标签页面板组件`**：")
        with gr.Row():
            with gr.Accordion("gr.Accordion()"):
                gr.Number(label="gr.Number()")
            with gr.Tab("gr.Tab()1"):
                gr.Number(label="gr.Number()1")
            with gr.Tab("gr.Tab()2"):
                gr.Number(label="gr.Number()2")

if __name__ == "__main__":
    demo.launch()
