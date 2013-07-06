from setuptools import setup, find_packages

setup(
	name='pygments-log-markup',
	version='1.0.0',
	description='Log Markup Lexers, Styles, Filters & Tokens',
	author='Clint Priest',
	author_email='pygments-log-markup@dev.rxv.me',
	url='http://github.com/cpriest/pygments-log-markup',
	license='CDDL',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Programming Language :: Python',
		'Intended Audience :: Developers',
	],

	install_requires=[
		'Pygments',
	],

	packages=find_packages(exclude=['ez_setup']),

	entry_points="""
	[pygments.lexers]
		PostfixLexer = pygments_log_markup.lexers:PostfixLexer
		DataTypesLexer = pygments_log_markup.lexers:DataTypesLexer

	[pygments.styles]
		DarkLog = pygments_log_markup.styles:DarkLogsStyle
		LightLog = pygments_log_markup.styles:LightLogsStyle
	""",
)
