# -*- coding: utf-8 -*-
"""
	This lexer will parse for basic data types such as URLs, Emails, Dates, Times, IPv4 Addresses, CIDR's, etc.  Could be used on its own but is typically used with a log parser
"""

from pygments.lexer import RegexLexer, bygroups;
from pygments.token import *;
from pygments_log_markup import *;
from pygments_log_markup.RE import RE

__all__ = ['DataTypesLexer']
__author__ = 'Clint Priest';

class DataTypesLexer(RegexLexer):
	"""
		Custom formatter for postfix-reject-log by Clint Priest
	"""
	name = 'DataTypes'
	aliases = ['DataTypes','datatypes']
	filenames = []
	mimetypes = ['text/x-datatypes-lexer']

	tokens = {
		'root': [
			(RE.URL, DataType.URL),
			(RE.Email, DataType.Email),
			(RE.Domain, DataType.Domain),
			(RE.IPv4_CIDR, bygroups(DataType.Net.IPv4.CIDR.Address,Operator,DataType.Net.IPv4.CIDR.Mask)),
			(RE.IPv4_Address, DataType.Net.IPv4.Address),
			(RE.Time, DataType.Time),
			(RE.Dates[0], bygroups(DataType.Date, DataType.Date, Literal)),
			(RE.Dates[1], DataType.Date),
			(RE.Dates[2], DataType.Date),
			(r'.', Other),
		],
	}

	def __init__(self, **options):
#		print('DataTypesLexer Loaded');
		super(DataTypesLexer, self).__init__(**options);

	# noinspection PyMethodParameters
	def analyse_text(text):
		return .3;
