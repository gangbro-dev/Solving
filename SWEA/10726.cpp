#include<iostream>
#include<string>
#include <typeinfo>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int N, M;
        cin >> N >> M;
        int bitN = (1 << N) - 1;
        cout << N << "\n" << M << "\n";
        string ans;
        if (bitN == (M&bitN)) ans = "ON";
        else ans = "OFF";
        cout << typeid(bitN).name() << "\n" << typeid(M&bitN).name() << "\n";
        cout << "#" << test_case << " "+ ans +"\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}