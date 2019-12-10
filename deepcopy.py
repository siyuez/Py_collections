
ex = [1, [2, [3,4], 5]]

# # 如果碰到list就新建一个list，然后把里面所有元素都深复制进去
# # 如果碰到不可变型，直接返回

# def deepcopy_naive(thing):
# 	if isinstance(thing, list):
# 		return [deepcopy(e) for e in thing]
# 	return thing


def deepcopy(something):
	dic = {}
	def helper(thing):
		if isinstance(thing, list):
			if id(thing) in dic.keys():
				return dic[id(thing)]

			temp = []
			dic[id(thing)] = temp
			for e in thing:
				temp.append(helper(e))
			return temp
		return thing
	return helper(something)

# a = deepcopy(ex)

# print(id(ex[1]))
# print(id(a[1]))

# a = [1,]
# print(id(a))
# print(id(a[0]))
# a.append(a)
# print(a)



# dic = {}
# def deepcopy(something):
# 	if isinstance(something, list):
# 		if id(something) in dic.keys():
# 			return dic[id(something)]
# 		temp = []
# 		dic[id(temp)] = temp
# 		for e in something:
# 			temp.append(deepcopy(e))
# 		return temp
# 	return something

# a = deepcopy(ex)

# print(id(a[1]))
# print(id(ex[1]))