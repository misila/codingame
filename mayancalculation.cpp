/*
Mayan calculation problem 

Upon discovering a new Maya site, hundreds of mathematics, physics and astronomy books have been uncovered.

The end of the world might arrive sooner than we thought, but we need you to be sure that it doesn't!

Thus, in order to computerize the mayan scientific calculations, you're asked to develop a program capable of performing basic arithmetical operations between two mayan numbers.
 	Rules

The mayan numerical system contains 20 numerals going from 0 to 19. Here's an ASCII example of their representation:
_______________________________________________________________________
|   0	 |   1  |  2   |  3 	|  4	 |   5	|   6  | 	 7  |	  8  |	9   |
|______|______|______|______|______|______|______|______|______|______|
| .oo. | o... | oo.. | ooo. | oooo | .... | o... | oo.. | ooo. | oooo |
| o..o | .... | .... | .... | .... | ---- | ---- | ---- | ---- | ---- |
| .oo. | .... | .... | .... | .... | .... | .... | .... | .... | ---- |
| .... | .... | .... | .... | .... | .... | .... | .... | .... | ---- |
|______|______|______|______|______|______|______|______|______|______|
|  10  |	 11 |  12	 |  13	|  14	 |  15	|  16  |	17	|  18	 |  19  |
|______|______|______|______|______|______|______|______|______|______|
| .... | o... | oo.. | ooo. | oooo | .... | o... | oo.. | ooo. | oooo |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| .... | .... | .... | ---- | .... | ---- | ---- | ---- | ---- | ---- |
|______|______|______|______|______|______|______|______|______|______|

 A mayan number is divided into vertical sections. Each section contains a numeral (from 0 to 19) representing a power of 20. The lowest section corresponds to 200, the one above to 201 and so on.
Thereby, the example below is : (12 x 20 x 20) + (0 x 20) + 5 = 4805

To spice the problem up, the mayans used several dialects, and the graphical representation of the numerals could vary from one dialect to another.
The representation of the mayan numerals will be given as the input of your program in the form of ASCII characters. You will have to display the result of the operation between the two given mayan numbers. The possible operations are *, /, +, -
 	Game Input

Input
Line 1: the width L and height H of a mayan numeral.
H next lines: the ASCII representation of the 20 mayan numerals. Each line is (20 x L) characters long.
Next line: the amount of lines S1 of the first number.
S1 next lines: the first number, each line having L characters.
Next line: the amount of lines S2 of the second number.
S2 next lines: the second number, each line having L characters.
Last line: the operation to carry out: *, /, +, or -
Output
The result of the operation in mayan numeration, H lines per section, each line having L characters.
Constraints
0 < L, H < 100
0 < S1, S2 < 1000
The remainder of a division is always 0.
The mayan numbers given as input will not exceed 263.

Example
Input
4 4
.oo.o...oo..ooo.oooo....o...oo..ooo.oooo____o...oo..ooo.oooo____o...oo..ooo.oooo
o..o................____________________________________________________________
.oo.........................................____________________________________
................................................................________________
4
o...
....
....
....
4
o...
....
....
....
+

Output 
oo..
....
....
....

*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

/*
* Transforme une chaine de caractère lu en input en nombre (double, base 10)
* dict est le dictionnaire ou table de hashage ayant pour un clé, une chaine de caractère 
* correspondant à sa valeur 'entier codé en base 10 (ex: 0,1,2...)
*/
double stringToInteger(const map<string, unsigned int> &dict, int H, int L){

	int S1;
	cin >> S1; cin.ignore();

    int indice = S1/L - 1;    
    double res=0;
    
    while (indice>=0){
		string num1="";		
		for (int j=0; j<H; j++){
			string num1Line;
			cin >> num1Line; cin.ignore();
			num1+= num1Line;
		}
		int number1=0;
		number1 = dict.find(num1)->second;
		res += number1 * pow(20,indice);
		indice--;
    }	
	
	return res;
}

/*
* Transforme un nombre n (double, base 10) en chaine de caractères
* tab est le tableau de réference des chiffres 01233456789
* il a 10 cases, chaque case est formé de H*L caractères 
* /
string integerToString(double n, const vector<string> &tab){
	 
	string res="";
	
	int indice=19;
	double div = pow(20,indice);
	
	while (n/div<1) {
		indice--;
		div=pow(20,indice);
	 }
	 
	 
	while (indice>=0){
		double div=pow(20,indice);
		double entier=n/div;
		int e=(int)entier;
		double reste= n - e*div;
		string snumber=tab[e];
		res+= snumber;
		n=reste;
		indice--;
	}
	
	return res;
}

int main()
{
    unsigned int L;
    unsigned int H;
    cin >> L >> H; cin.ignore();
    vector<string> tableau;
    map<string, unsigned int> dict;
 
    
    for (unsigned int i = 0; i < H; i++) {
        string numeral;
        cin >> numeral; cin.ignore();
        unsigned int nb=numeral.size()/L;
        for (unsigned int j=0; j<nb;j++){
			unsigned int start=L*j;
			string elm=numeral.substr(start,L);
			if (tableau.size()>j){
				string elm1 = tableau.at(j);
				elm1 += elm;
				tableau[j]=elm1;
			}
			else{
				tableau.insert(tableau.end(),elm);
			}
		}
    }
    
    for (unsigned int l=0; l<tableau.size(); l++)
		dict.insert(pair<string, int>(tableau[l],l));

    
    double result1 = stringToInteger(dict, H, L);
    double result2 = stringToInteger(dict, H, L);
	
    string operation;
    cin >> operation; cin.ignore();

	double result=0;
	
	if (operation=="-")
		result=result1-result2;
	else if (operation=="+")
		result=result1+result2;
	else if (operation=="*")
		result=result1*result2;
	else if (operation=="/")
		result=result1/result2;

    
    string res="";
    if (result==0){
		res=tableau[0];
	}else 
        res=integerToString(result, tableau);
    
    cerr <<"result="<<result<<endl;
    
    for (unsigned int i=0; i<res.size()/H; i++){
		int ind=H*i;
		for (unsigned int j=0; j<L; j++){
			cout << res[ind+j];
		}
		cout <<endl;
	}
    
    return 0;
}



