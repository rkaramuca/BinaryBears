#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> notes = {"C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"};

int findIndex(string z);

int main() {
	int scales; cin>>scales;
	int q; cin>>q;

	const int H = 1;
	const int W = 2;
	
	string qx[scales][2];

	for( int i = 0; i < scales; i++ ) {
		cint>>qx[i][0]; cin>>qx[i][1];
	}

	vector<string> s;
	string clear;
	for( int i = 0; i < q; i++ ) {
		string x = "";
		getline(cin, x);
		s.push_back(x);
	}

	for( int i = 0; i < s.size(); i++ ) {
		string str = s[i];
	}
}	

int findIndex(string z) {
	int t;
	for( int i = 0; i < notes.size(); i++ ) {
		if(z == notes[i] || z + (notes[i + 1]) == notes[i]) {
			return 1;
		}
		t = i;
	}
	return -1;
}
