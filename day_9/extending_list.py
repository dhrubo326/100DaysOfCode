class SuperList(list):
	def __len__(self):
		return 99;

super_list_1 = SuperList()

print(len(super_list_1))
super_list_1.append(6)
super_list_1.append(7)
print(super_list_1[1])

