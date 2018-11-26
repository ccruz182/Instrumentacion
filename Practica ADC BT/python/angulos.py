TABLA_ANGULOS = {
	'0': 0,
	'30': 0.28,
	'45': 0.71,
	'60': 1.17,
	'75': 1.59,
	'90': 2.05,
	'120': 3.06,
	'135': 3.57,
	'150': 4.05,
	'165': 4.53,
	'180': 4.99
}

def get_rango(voltaje):
	keys = sorted(map(int, TABLA_ANGULOS))
	lastVal = ''

	for key in keys:
		if voltaje >= TABLA_ANGULOS[str(key)]:
			lastVal = key
		else:
			return lastVal, key