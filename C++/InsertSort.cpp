#include <iostream>
#include <vector>
using namespace std;

void InsertSort(vector<int> &num){
	for(int i=1; i<num.size(); ++i){
		int cur = num[i];
		int position = i;
		while(position>0 && num[position-1]>cur){
			num[position] = num[position-1];
			position--;
		}
		num[position] = cur;
	}
}

int main()
{
	int a[9] = {54,26,93,17,77,31,44,55,20};
	vector<int> num(a, a+9);
	InsertSort(num);
	for(int i=0;i<=num.size()-1;i++)
    	cout<<num[i]<<" ";
	return 0;
}