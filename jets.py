def jets(cube):
	latitude=(-75,-15)
	cube = cube.intersection(latitude=latitude)
	cube = cube.collapsed(['longitude'], iris.analysis.MEAN)
	print(cube)
	lats = cube.coord('latitude').points
	lat = np.array([])
	mag = np.array([])
	ind = np.where( cube.data[:] == np.max(cube.data[:]) )
	lat = np.append( lat, lats[ind]  )
	mag = np.append( mag, cube.data[ind] )
	return lat, mag


