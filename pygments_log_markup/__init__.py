"""
	pygments_log_markup
"""

from pygments.token import Token, STANDARD_TYPES;

DataType = Token.DataType;

STANDARD_TYPES[DataType] = 'dt';

STANDARD_TYPES[DataType.Date] = 'dtdt';
STANDARD_TYPES[DataType.Time] = 'dttm';
STANDARD_TYPES[DataType.URL] = 'dturl';
STANDARD_TYPES[DataType.Domain] = 'dtdm';

STANDARD_TYPES[DataType.Email] = 'dtem';
STANDARD_TYPES[DataType.Email.From] = 'dtemf';
STANDARD_TYPES[DataType.Email.To] = 'dtemt';
STANDARD_TYPES[DataType.Email.To.Highlight] = 'dtemt_hi';

STANDARD_TYPES[DataType.Net] = 'dtn';
STANDARD_TYPES[DataType.Net.IPv4] = 'dtni4';
STANDARD_TYPES[DataType.Net.IPv4.Address] = 'dtni4a';
STANDARD_TYPES[DataType.Net.IPv4.CIDR] = 'dtni4c';
STANDARD_TYPES[DataType.Net.IPv4.CIDR.Address] = 'dtni4ca';
STANDARD_TYPES[DataType.Net.IPv4.CIDR.Mask] = 'dtni4cm';



__all__ = ['DataType'];
__author__ = 'Clint Priest';
