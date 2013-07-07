pygments-log-markup
==================
A plugin for [Pygments](http://pygments.org/) which provides for some logfile markup and coloring.

At the moment it provides:
* A general DataTypesLexer which looks for general data types:
  * URL, Email, Domains, Date, Time
  * IPv4: CIDR and IP Addresses
* A postfix log markup lexer PostfixLexer
* Two styles
  * LightLog
  * DarkLog

Because this plugin defines new Token types for DataTypes the new styles are the only ones that will presently work with these lexers.
