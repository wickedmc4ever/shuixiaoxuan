from gradio_client import Client

client = Client("https://30c240625302dd68af.gradio.live/")
result = client.predict()
    #https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png,	# filepath  in 'input image' Image component
	#	True,	# bool  in 'resize to optimal size/自动剪裁图片尺寸' Checkbox component
	#	3,	# float  in 'number of frames' Number component
	#	3,	# float  in 'number of steps' Number component
	#	"Hello!!",	# str  in 'seed (integer or 'random')' Textbox component
	#	3,	# float  in 'number of frames decoded at a time' Number component
	#	3,	# float  in 'frames per second' Number component
	#	3,	# float  in 'motion bucket id' Number component
	#	3,	# float  in 'condition augmentation factor' Number component
	#	True,	# bool  in 'skip nsfw/watermark filter' Checkbox component api_name="/infer")
    #print(result)

client = Client("https://30c240625302dd68af.gradio.live/")
result = client.predict(
		0,	# int (index of selected example) in 'parameter_19' Dataset component
							api_name="/load_example"
)
print(result)