__author__ = 'TIW'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def input_command(host, port, username, enable_password, usermodtag, sysmodtag, login_prompt, password_prompt, command_output_more_tag_prompt, command_output_more_input_command, command_input, command_output_list):
    ############################输入命令并获取返回值##################################
    # 如果登录Sysmode成功，则出现类似#,使用SysmodTag来进行捕获
    tn.read_until(sysmodtag)
    # 提示输入的命令
    print('Input command:', command_input)
    # 输入命令
    tn.write((command_input + '\n').encode('utf-8'))
    # 将输入命令的返回值赋值response,命令返回值前两个输出不是期望的返回值而是空值
    response = tn.read_very_eager()
    print(response)
    # 将输入命令的返回值赋值response，如果sysmodtag在response则表示命令输出完整，否则输入命令获取完整的命令
    if sysmodtag not in response:
        n = 1
        while sysmodtag not in response:
            for i in range(2):### range(2)里面这个2是有讲究的不能少于1最好是2
                # 命令返回值未完结时，输入继续输出命令获取值的命令
                tn.write(command_output_more_input_command.encode('utf-8'))
                # 获取命令返回值并赋值给response， 用response捕获命令结束提示
                response = tn.read_until(command_output_more_tag_prompt, timeout=0.5)
                # 将获取命令返回值赋值给response_format
                response_format = response
                # 将response_format重新编码
                response_format = response_format.decode('utf-8')
                # 将response_format格式化
                response_format = re.sub(r'\x08', '', response_format)
                response_format = re.sub(r'--           ', '', response_format)
                response_format = re.split(r'\r\n', response_format)
                # 删除命令的返回值中对于的无效返回值
                for item in response_format:
                    if command_output_more_tag_prompt.decode('utf-8') in item:
                        response_format.remove(item)
                # 将输入命令的返回值添加到列表
                for item in response_format:
                    command_output_list.append(item)
                # 提示正在获取命令返回值
                #print(response)
                print('Getting command output, please wait.',  n, 'lines command output had gotten.')
                n = n + 1
        # 获取完整的命令输出后提示完成
        print('All command output had gotten!!!')
    #### 这些代码没用了，但是先留着可能有用    ###
    #else:
    #    print(2229)
    #    response_format = response
        #print(response_format)
    #    response_format = response_format.decode('utf-8')
    #    response_format = re.split(r'\r\n', response_format)
    #    for item in response_format:
    #        print(item)
    #### 这些代码没用了，但是先留着可能有用    ###
    # 删除命令的返回值中对于的无效返回值
    for item in command_output_list:
        if hostname in item:
            command_output_list.remove(item)
    for item in response_format:
        if command_output_more_tag_prompt.decode('utf-8') in item:
            response_format.remove(item)
    ############################输入命令并获取返回值##################################

