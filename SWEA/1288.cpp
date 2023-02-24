#include<iostream>
#include<string>

using namespace std;

int test_case;
int T;

string N;
int cnt;
bool check[10];

void init() {
    cin >> N;
    cnt = 0;
    int i;
    for (i = 0; i < 10; i++) {
        check[i] = false;
    }
}

int main(int argc, char** argv)
{
    cin >> T;

	for(test_case = 1; test_case <= T; ++test_case)
	{
        init();
        int numN = std::stoi(N);
        int x = 1;
        while (cnt < 10){
            N = to_string(x*numN);
            for(int i = 0; i < N.length(); i++) {
                int digit = N[i] - '0';
                if (!check[digit]) {
                    check[digit] = true;
                    cnt++;
                }
            }
            x++;
        }
        cout << "#" << test_case << " "+ N +"\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}