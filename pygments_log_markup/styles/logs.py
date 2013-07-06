from __future__ import print_function;
from pygments.style import Style;
from pygments.token import *;
from pygments_log_markup import *

__author__ = 'Clint Priest';

class Colors:
	""" Aliases for common colors """
	White 		= "#FFFFFF";
	Black 		= "#000000";

	LightRed	= '#FF8888';
	Red			= '#FF0000';
	DarkRed		= '#AA0000';

	LightGreen	= '#88FF88';
	Green		= '#00FF00';
	DarkGreen	= '#00AA00';

	Cyan		= '#00FFFF';

	LightBlue	= '#8888FF';
	Blue		= '#0000FF';
	DarkBlue	= '#0000AA';

	LightYellow = '#FFFF88';
	Yellow		= '#FFFF00';
	DarkYellow	= '#BBBB00';


class LightLogsStyle(Style):
	"""
		Defines a color on white background style for logs
	"""
	default_style 		= Colors.Black;
	background_color 	= '#FFFFF3';
	highlight_color 	= Colors.Black;

	styles = {
		Token: 								' '.join(['#555555']),
		DataType.Date: 						' '.join([Colors.Black, 'bold']),
		DataType.Time: 						' '.join([Colors.Black, 'bold']),
		DataType.URL: 						' '.join([Colors.Blue]),
		DataType.Domain: 					' '.join([Colors.DarkYellow, 'bold']),
		DataType.Email: 					' '.join([Colors.Red]),
		DataType.Net.IPv4.Address:			' '.join([Colors.DarkGreen]),
		DataType.Net.IPv4.CIDR.Address:		' '.join([Colors.DarkGreen]),
		DataType.Net.IPv4.CIDR.Mask:		' '.join([Colors.DarkGreen]),
	};


class DarkLogsStyle(Style):
	"""
		Defines a color on black background style for logs
	"""
	default_style 		= '#BBBBBB';
	background_color 	= Colors.Black;
	highlight_color 	= Colors.White;

	styles = {
		Token: 								' '.join(['#BBBBBB']),
		DataType.Date: 						' '.join([Colors.White, 'bold']),
		DataType.Time: 						' '.join([Colors.White, 'bold']),
		DataType.URL: 						' '.join([Colors.LightBlue, 'underline']),
		DataType.Domain: 					' '.join([Colors.Yellow]),
		DataType.Email: 					' '.join([Colors.Red]),
		DataType.Email.From:				' '.join([Colors.Red]),
		DataType.Email.To:					' '.join([Colors.LightBlue]),
		DataType.Email.Highlight:			' '.join(['bg:#AA0000', Colors.White]),
		DataType.Net.IPv4.Address:			' '.join([Colors.Green]),
		DataType.Net.IPv4.CIDR.Address:		' '.join([Colors.Green]),
		DataType.Net.IPv4.CIDR.Mask:		' '.join([Colors.LightGreen]),
	};
