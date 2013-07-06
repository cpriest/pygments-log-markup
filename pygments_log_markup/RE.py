__author__ = 'Clint Priest'

class RE:
	Domain = r'\b(?:[A-Za-z0-9\-\.]+){1,4}\.(?:com|net|org|biz|gov|edu|mil|aero|asia|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|[A-Za-z]{2})\b';
	Email = r'[\w\d!#$%&*_0/=?^_`{|}~\-]+@(?:[A-Za-z0-9\-\.]+){1,}\.[A-Za-z\-]{2,6}';
	IPv4_CIDR = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(/)(\d{1,2})';
	IPv4_Address = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}';
	Time = r'\d{1,2}:\d{2}(:\d{2})?(\s+(AM|PM))?';
	Dates = [
		r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct\Nov|Dec)\s+\d{1,2})(\s+\d{2,4})?(\s+)',
		r'\d{1,2}/\d{1,2}/\d{2,4}',
		r'\d{4}-\d{1,2}-\d{1,2}',
	];
	URL = '';

RE.URL = r'(https?|ftp|ssh|git|svn|file)://' + RE.Domain + r'(/\S+)?\b'
