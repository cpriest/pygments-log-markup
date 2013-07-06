# -*- coding: utf-8 -*-
"""
	This lexer will parse for basic data types such as URLs, Emails, Dates, Times, IPv4 Addresses, CIDR's, etc.  Could be used on its own but is typically used with a log parser
"""
from __future__ import print_function;

from pygments.lexer import RegexLexer, bygroups;
from pygments.token import *;
import re
from pygments_log_markup import DataType;
from pygments_log_markup.lexers import DataTypesLexer;
from pygments_log_markup.RE import RE

__all__ = ['PostfixLexer']
__author__ = 'Clint Priest';

class PostfixLexer(RegexLexer):
	"""
		Custom formatter for postfix logs
	"""
	name = 'Postfix'
	aliases = ['Postfix','postfix','pf']
	filenames = ['']
	alias_filenames = ['']
	mimetypes = ['']

	tokens = {
		'root': [
			(r'(from=<)('+RE.Email+')(>)', bygroups(Token,DataType.Email.From,Token)),
			(r'((?:orig_)?to=<)('+RE.Email+')(>)', bygroups(Token,DataType.Email.To,Token)),
			# DataTypeLexer tokens inserted here near end of file
			(r'.', Other),
		],
	}

	def __init__(self, **options):
		super(PostfixLexer, self).__init__(**options);

	# noinspection PyMethodParameters
	def analyse_text(text):
		if re.search(r'postfix/(smtpd|smtp|qmgr|anvil|cleanup|virtual)', text):
			return 1;
		return 0;

# Include DataTypesLexer tokens just before the end of our tokens
PostfixLexer.tokens['root'][-1:-1] = DataTypesLexer.tokens['root'][0:-2];
