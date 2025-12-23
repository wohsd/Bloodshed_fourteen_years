import os

def add_desc_simple():
    """
    简单方法：在所有段落开始后直接添加desc行
    """
    print("处理当前目录下所有.txt文件...")
    
    for filename in os.listdir('.'):
        if filename.endswith('.txt'):
            print(f"处理: {filename}")
            
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 获取所有人物名称
                import re
                characters = re.findall(r'(\w+)=\{[^}]*name\s*=\s*(\w+)', content)
                
                for char_def, char_name in characters:
                    print(f"  找到人物: {char_name}")
                    
                    # 为这个人物的每个段落添加desc
                    for section in ['country_leader', 'advisor', 'field_marshal', 'corps_commander', 'navy_leader']:
                        pattern = rf'{char_def}.*?{section}=.*?\{{'
                        match = re.search(pattern, content, re.DOTALL)
                        if match:
                            # 检查是否已有desc
                            section_start = match.end()
                            section_end = content.find('}', section_start)
                            section_content = content[section_start:section_end]
                            
                            if 'desc =' not in section_content:
                                # 在段落开始后添加desc
                                insert_pos = match.end()
                                desc_line = f'\tdesc = {char_name}_leader_desc\n'
                                content = content[:insert_pos] + desc_line + content[insert_pos:]
                
                # 写回文件
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"  ✓ 完成")
                
            except Exception as e:
                print(f"  ✗ 错误: {e}")
    
    print("处理完成!")

add_desc_simple()