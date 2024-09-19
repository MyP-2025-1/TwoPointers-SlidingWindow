#include <iostream>

using namespace std;

string inside_out(const string&);

int main()
{
  int t;
  string s;
  cin >> t;
  cin.ignore();
  for(int i = 0; i < t; i++){
    getline(cin, s);
    cout << inside_out(s) << endl;
  }
  return 0;
}

string inside_out(const string& s)
{
  string aux;
  int len = s.length();
  for(int i = len/2 - 1; i >= 0; i--)
    aux += s[i];
  for(int i = len-1; i >= len/2; i--)
    aux += s[i];
  return aux;
}
