import configparser

# 创建配置对象
config = configparser.ConfigParser()

config.read('junch.ini')
# 输出已读取的INI文件列表
print("Read INI files:", config.read('junch.ini'))

# 获取所有的section
sections = config.sections()
print("Sections:", sections)

# 获取每个section的键值对
for section in sections:
    print("Section:", section)
    for key, value in config.items(section):
        print(f"{key} = {value}")

# 获取数据库配置
BSC = config.get('Edu', 'BSc')
name = config.get('ID', 'name')
email = config.get('logging', 'email')
Age = config.get('ID', 'age')

print(BSC, email, name, Age)