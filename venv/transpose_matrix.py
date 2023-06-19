# matrix = [[1,5,9,7], [8,0,6,3],[9,8,6,5]]
# def mat(matrix:list):
#     matrix2 = []#новая матрица
#     for i in range(len(matrix[0])):#длинна одного списка первой матрицы
#         matrix2.append(list())#столько списков будет в результирующей матрице по длинне одного списка первой матрицы
#         for j  in range(len(matrix)):#по кол-ву списков первой матрицы(будет строк в новой)
#             matrix2[i].append(matrix[j][i])#на текущий элемент одного из списков второй матрицы добавить элемент из первой матрицы
#     return matrix2

# print(mat(matrix))

matrix = iter([[1, 5, 9, 7], [8, 0, 6, 3], [9, 8, 6, 5]])
matrix2 = zip(next(matrix), next(matrix), next(matrix))
# matrix2 = list(zip(list(next(matrix)),list(next(matrix)),list(next(matrix))))#так выдает лист кортежей,почему сразу нельзя применить и перевести так в список списков?
res_matrix = list(map(list, matrix2))
print(res_matrix)
# print(matrix2)
