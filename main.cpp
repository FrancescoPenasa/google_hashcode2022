#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <set> 

using namespace std;

void algorithm (string input, string output);

int main()
{
    algorithm("input/a_an_example.in.txt", "output/a_an_example.out.txt" );
    algorithm("input/b_basic.in.txt", "output/b_basic.out.txt" );
    algorithm("input/c_coarse.in.txt", "output/c_coarse.out.txt" );
    algorithm("input/d_difficult.in.txt", "output/d_difficult.out.txt" );
    algorithm("input/e_elaborate.in.txt", "output/e_elaborate.out.txt" );

    return 0;
}

void algorithm(string input, string output) {
    int C; // clients
    int L; // liked ingredients
    int D; // disliked ingredients

    string ingredient;

    set<string> liked;
    set<string> disliked;

    ifstream in(input);
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

    ofstream out(output);
    out << L << " ";
    for (set<string>::iterator it = liked.begin(); it != liked.end(); it++){
        out << *it << " ";
    }  
}
