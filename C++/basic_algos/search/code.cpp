# include <string>
# include <vector>
# include <unordered_map>
#include <sstream>
# include <iostream>
# include "utils.h"

using namespace std;

unordered_map <string, int> data_dict = get_words_from_file("words_file.txt");

string get_data(string input_str){
    string result;
    vector<string> input_words = get_match(input_str);
    for (auto word: input_words){
    if (data_dict.find(word) != data_dict.end()){
            result = word + ": " + input_str;
            return result;
        }
    }
    return "None";
}

int main(){
    cout << "Enter input str";
    string inp_str;
    getline(cin, inp_str);
    cout << get_data(inp_str) << "\n";
    return 0;
}
