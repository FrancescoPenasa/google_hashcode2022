#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <set> 

using namespace std;

int main()
{
    int C; // clients
    int L; // liked ingredients
    int D; // disliked ingredients

    string ingredient;

    set<string> liked;
    set<string> disliked;

    ifstream in("input/a_an_example.in.txt");
    in >> C;

    for (int i = 0; i<C*2; i++) {
        in >> L;
        for (int j = 0; j<L; j++) {
            in >> ingredient;
            liked.insert(ingredient);
        }
        i++;
        in >> D;
        for (int j = 0; j<D; j++) {
            in >> ingredient;
            disliked.insert(ingredient);
        }
        
    }

    L = liked.size();

    ofstream out("output/a_an_example.out.txt");
    out << L << " ";
    for (set<string>::iterator it = liked.begin(); it != liked.end(); it++){
        out << *it << " ";
    }   

    return 0;
}