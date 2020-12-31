# print("请输入一个数字:")
# str = input()
# x = int(str)
# if x % 2 == 0:
#      if x > 0:
#         print(x, "是一个正偶数")
#      elif x < 0:
#         print(x, "是一个负偶数")
#      else:
#         print(x, "为零")
# else:
#      if x > 0:
#         print(x, "是一个正奇数")
#      else:
#         print(x, "是一个负奇数")

busstop_list = ['AA', 'GG', 'FF', 'HH', 'KK', 'LL']
busstop_list.insert(busstop_list.index('AA') + 1, 'BB')
print(busstop_list)
# print("请输入开始站：")
# start = str(input())
#
# print("请输入结束站：")
# end = str(input())
#
# startIndex = busstop_list.index(start)
# endIndex = busstop_list.index(end)
#
# if startIndex > endIndex:
#     print("您需要反方向乘车")
# else:
#     print(start, "到", end, "还有", endIndex - startIndex, "站")
#     print("{}到{}还有{}站".format(start, end, endIndex - startIndex))

