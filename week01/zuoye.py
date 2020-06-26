import re
str = "The quick brown fox junmps over the lazy dog."
str1 = str.split()
pattern = re.compile(r"(?P<macth_word>The)", re.I)
for word in str1:
	if pattern .search(word):
		print("{:s}".format(pattern.search(word).group('macth_word')))
