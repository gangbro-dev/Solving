#include<iostream>
#include<string>

#define MAX_VALUE 1000000007

using namespace std;
int test_case;
int T;
int ans = 0;
string str;

int to_bitID(char a){
    if (a == 'A') return 0b1000;
    else if (a == 'B') return 0b100;
    else if (a == 'C') return 0b10;
    else if (a == 'D') return 0b1;
}

void DFS(int key, int depth) {
    if (depth >= str.length()) {
        ans++;
        if (ans == MAX_VALUE) ans = 0; 
        return;
    }
    for(int i = 1; i < 16; i++) {
        if ((i & to_bitID(str[depth])) & key) {
            DFS(i, depth++);
        }
    }
}

int main(int argc, char** argv) {
    cin >> T;

	for(test_case = 1; test_case <= T; ++test_case) {
        cin >> str;
        DFS(0b1000, 0);
        cout << "#" << test_case << " " << ans << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}