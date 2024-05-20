# gradio_agent_cookbook
A cookbook for connecting AI agent platforms using gradio


### 启动
#### 先启动  gradio_app_block.py 将gradio在本地运行起来
cd gardio_api 
python gradio_app_block.py 

### 体验grdio api
#### 运行app_api.py 
pip install --upgrade gradio_client
python app_api.py
#### 或者 运行app_api.js
npm i @gradio/client
node app_api.js

### 体验html嵌入grdio
#### 进入html_gradio文件夹
#### 可以打开html文件体验
open index_app.html
#### 或者
open index_js.html

### 体验web服务调用gradio的api（没有成功）
##### fastapi
pip install gradio_client fastapi uvicorn
uvicorn main:app


### 与baiduAPPbuild进行SDK对接

#### 安装 AppBuilder-SDK
!pip install appbuilder-sdk


''''''
#### 补充你的APPBUILDER_TOKEN 和 app_id
#### 设置环境变量APPBUILDER_TOKEN，目前填的这个是官方的受限试用TOKEN
os.environ["APPBUILDER_TOKEN"] = "bce-v3/ALTAK-n5AYUIUJMarF7F7iFXVeK/1bf65eed7c8c7efef9b11388524fa1087f90ea58"
#### 地理小达人应用ID
app_id = "42eb211a-14b9-43d2-9fae-193c8760ef26"
''''''







