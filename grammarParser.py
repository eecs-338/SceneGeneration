import language_check
tool = language_check.LanguageTool('en-US')

def correctGrammar(text):
	matches = tool.check(text)
	return language_check.correct(text, matches)