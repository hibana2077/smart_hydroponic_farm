/*
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-04-19 11:02:07
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-04-21 21:27:02
 * @FilePath: /smart_hydroponic_farm/lab/testing.cpp
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
#include <iostream>
#include <map>
#include <string>
#include <thread>

void run_testing_file(){
    std::string sh = "python3";
    std::string sourcefile = "testing.py";
    std::string cmd = sh + " " + sourcefile;
    system(cmd.c_str());
}

int main(){

    std::cout<< "Testing..." << std::endl;
    
    return 0;
}