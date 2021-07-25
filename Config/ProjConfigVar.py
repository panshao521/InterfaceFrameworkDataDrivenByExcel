# -*- coding: utf-8 -*-
"""
Time:     2021/7/25 16:49
Author:   panyuangao@foxmail.com
File:     ProjConfigVar.py
Describe: 
"""
import os

proj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 项目目录路径
test_data_excel_path = os.path.join(proj_path,"TestData","接口测试数据.xlsx")# 测试文件路径

log_conf_path = os.path.join(proj_path,"config","Logger.conf") # log配置文件路径
server_address_conf_path = os.path.join(proj_path,"Config", "interface_server_address.ini") # 接口服务器地址配置
report_path = os.path.join(proj_path,"Report")


test_case_sheet = "测试用例"
test_case_row_no_clo_no = 0
test_case_test_step_sheet_name_col_no = 2
test_case_is_executed_col_no = 3
test_case_executed_result_col_no = 6
test_case_executed_time_col_no = 7

test_data_row_no_col_no = 0
test_data_interface_name_col_no = 1
test_data_request_data_col_no = 2
test_data_response_data_col_no = 3
test_data_assert_word_col_no = 4
test_data_test_result_col_no = 5
test_data_correlate_regx_col_no = 6
test_data_test_elapse_time_col_no = 7
test_data_is_executed_col_no = 8
test_data_executed_time_col_no = 9

#object_map_file_path = os.path.join(proj_path,"testdata","ObjectDeposit.ini")

mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "testworker"  # 用户名
mail_pass = "nqwnnydoxmtydgah"  # 口令


sender = 'testworker@qq.com' # 邮件发送人
receivers = ['2943301878@qq.com',"youngboss2020@126.com" ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

if __name__ =="__main__":
    print(proj_path)
    print(log_conf_path)
    print(test_data_excel_path)
    print(server_address_conf_path)
