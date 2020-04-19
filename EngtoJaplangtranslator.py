from translate  import Translator
translator= Translator(to_lang="zh")
try:
	with open("test.txt",mode='r') as my_file:
		text=my_file.read()
		translation = translator.translate(text)
		with open("test_zh",mode='w') as my_file2:
			my_file2.write(translation)
except FileNotFoundError as e:
	print("check your file path please")


	
