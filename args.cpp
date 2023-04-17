/*
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-04-10 18:03:04
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-04-10 18:20:05
 * @FilePath: /smart_hydroponic_farm/args.cpp
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
#include <iostream>
#include <map>
#include <string>


using ll = long long;
using ins_mp = std::map<std::string, std::string>;

ins_mp compile = {
    {"cpp","g++ %s -o out"},
    {"c","gcc %s -o out"},
    {"java","javac %s"},
};

ins_mp run = {
    {"cpp","./out "},
    {"c","./out"},
    {"py","python3 %s < %s > %s"},//python3 sourcefile < inputfile > outputfile
    {"js","nodejs %s < %s > %s"},
    {"java","java %s < %s > %s"},
    {"go","go run %s < %s > %s"},
    {"rb","ruby %s < %s > %s"},
    {"pl","perl %s < %s > %s"},
    {"rs","rustc %s && %s < %s > %s"},
    {"swift","swiftc %s && %s < %s > %s"},
    {"kt","kotlinc %s && %s < %s > %s"},
    {"lua","lua %s < %s > %s"},
};

int main(int argc, char *argv[])
{
    // std::cout << "argc = " << argc << std::endl;
    // for (int i = 0; i < argc; ++i)
    //     std::cout << "argv[" << i << "] = " << argv[i] << std::endl;
    // return 0;
    std::map<std::string, std::string> args;
    if (argc == 0){
        std::cout << "no args" << std::endl;
    }else{
        
        for (int i = 1; i < argc; ++i){
            std::string arg = argv[i];
            std::string key = arg.substr(0, arg.find("="));
            std::string value = arg.substr(arg.find("=") + 1);
            args[key] = value;
        }
    }

    return 0;
}