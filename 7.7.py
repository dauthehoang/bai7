print("ĐẬU THẾ HOÀNG")
print("MSSV:235752021610017")
def count_lines(filename):
  count = 0
  with open(filename, 'r') as f:
    for line in f:
      count += 1
  return count

filename = (r"C:\zalo\ktddt\accc.txt")
total_lines = count_lines(filename)
print("Số dòng trong tệp", filename, "là", total_lines)
