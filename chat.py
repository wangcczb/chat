#讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines
#轉換
def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		new.append(person + ': ' + line)
	return new
#檔案寫入
def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')
#主程式
def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()