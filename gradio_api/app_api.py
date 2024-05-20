from gradio_client import Client

#client = Client("http://127.0.0.1:7860/")
#result = client.predict(
##		"Jim!!",	# str  in 'name' Textbox component
#		api_name="/predict"
#)

from gradio_client import Client

client = Client("http://127.0.0.1:7860/")
result = client.predict(
		"camerio!!",	# str  in 'Name' Textbox component
		api_name="/greet"
)
#print(result)
print(result)