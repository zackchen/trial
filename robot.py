
path = []

def FindPath(theMap, width, height, j, i):
	# print theMap, j, i
	if j == width - 1 and i == height - 1 and theMap[i][j] == 1:
		return True
	
	if j >= width or i >= height:
		return False

	if theMap[i][j] == 0:
		return False

	if FindPath(theMap, width, height, j + 1, i):
		# print "-"
		path.append( "-")
		return True
	elif FindPath(theMap, width, height, j, i + 1):
		# print "|"
		path.append( "|")
		return True
	else:
		return False


if __name__ == "__main__":
	theMap = [[1,1,1],[0,1,0],[1,1,1],[1,0,1]]

	FindPath(theMap, 3, 4, 0, 0)
	print path
