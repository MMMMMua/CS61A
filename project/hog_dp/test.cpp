#include <cstdio>
#include <gmpxx.h>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <sstream>
using namespace std;
typedef long double ld;
const int maxn = 200;

int number[20][15][maxn];
int dice[02][maxn][maxn];

mpf_class f[maxn][maxn][5][5];

int g[maxn][maxn][5][5];
bool visit[maxn][maxn][5][5];
bool prime[10010];
int nxt_prime[10010];
int flipp_dice[10010];
int cnt = 0;

int is_prime(int x) { return prime[x];}
int next_prime(int x) { if (is_prime(x)) return nxt_prime[x]; else return x; }
int free_bacon(int opscore) { return next_prime(max(opscore / 10, opscore % 10) + 1); }
int is_swap(int myscore, int opscore) { return opscore * 2 == myscore || myscore * 2 == opscore; }
void get_next(int &myscore, int mturn, int &opscore, int oturn) {
	myscore += mturn, opscore += oturn;
	if (is_swap(myscore, opscore)) swap(myscore, opscore);
}


mpf_class dfs(int myscore, int opscore, int turn, int flip) {
	if (myscore >= 100 || opscore >= 100)
		return mpf_class((myscore >= 100 && turn == 0) || (opscore >= 100 && turn == 1), 500);

	mpf_class &F = f[myscore][opscore][turn][flip];
	int &G = g[myscore][opscore][turn][flip];
	bool &V = visit[myscore][opscore][turn][flip];
	
	if (V)
		return F;
	V = 1;
	F = mpf_class(0, 500);
	if (myscore < 5 && opscore > 95) {
		int x;
		x++;
	}
	if (turn == 0) { //myturn
		int turn_score = free_bacon(opscore);
		int myscore_t = myscore, opscore_t = opscore;
		get_next(myscore_t, turn_score, opscore_t, 0);
		
		mpf_class tmp = mpf_class(1.0, 500) - dfs(myscore_t, opscore_t, turn^1, flip ^ flipp_dice[turn_score]);
		F = tmp, G = 0;
			
		for (int i = 1; i <= 10; ++i) {
			mpf_class total = 0;
			for (int j = 1; j <= number[flip][i][0]; ++j) {
				turn_score = number[flip][i][j];
				myscore_t = myscore, opscore_t = opscore;
				get_next(myscore_t, turn_score, opscore_t, 0);
				tmp = mpf_class(1.0) - dfs(myscore_t, opscore_t, turn^1, flip ^ flipp_dice[turn_score]);
				
				mpf_class prob = tmp * mpf_class(1.0, 500) * dice[flip][i][turn_score] / mpf_class(pow(flip ? 4 : 6, i), 500);
				total += prob;
			}
			if (F < total)
				F = total, G = i;
		}
	}
	else {
		mpf_class total = mpf_class(0, 500);
		for (int j = 1; j <= number[flip][4][0]; ++j) {
			int turn_score = number[flip][4][j];
			int myscore_t = myscore, opscore_t = opscore;
			get_next(myscore_t, 0, opscore_t, turn_score);
			mpf_class tmp = mpf_class(1.0, 500) - dfs(myscore_t, opscore_t, turn^1, flip ^ flipp_dice[turn_score]);
			
			mpf_class prob = tmp * mpf_class(1.0, 500) * dice[flip][4][turn_score] / mpf_class(pow(flip ? 4 : 6, 4), 500);
			total += prob;
		}			
		F = total, G = 4;		
	}
	cerr << ++cnt << endl;
				   
	return F;	
}
int GG[2];	
void get_dice(int d, int n, int t) {
	if (d > 10) return;
	if (d >= 1) {
		int N = n;
		N = next_prime(N);;
		dice[t == 4][d][N]++; //dice[type][rolls][number];
		GG[t == 4]++;
	}
	get_dice(d+1, 1, t);
	for (int i = 2; i <= t; ++i)
		get_dice(d+1, n == 1 ? 1 : n+i, t);
	
}
		
mpf_class fin[maxn][maxn][11];		
int main() {
	freopen("out.txt","w", stdout);
	memset(prime, 1, sizeof(prime));

	prime[1] =0;
	int last = 0;
	for (int i = 2; i <= 150; ++i)
		if(prime[i]) {
			nxt_prime[last] = i;
			last = i;
			for (int j = i+i; j <= 150; j += i)
				prime[j] = 0;
		}
	for (int i = 2; i <= 10; ++i)
	 	flipp_dice[i*i] = flipp_dice[i*i*i] = 1;
	
	get_dice(0, 0, 4);
	get_dice(0, 0, 6);
	cerr << GG[0] << " " << GG[1] << endl;
	
	for (int i = 1; i <= 10; ++i)
		for (int j = 1; j <= 70; ++j) {
			if (dice[0][i][j] != 0)
				number[0][i][++number[0][i][0]] = j;

			if (dice[1][i][j] != 0)
				number[1][i][++number[1][i][0]] = j;
		}

	for (int i = 0; i <= 99; ++i)
		for (int j = 0; j <= 99; ++j)
			for (int a = 0; a <= 1; ++a)
				for (int b = 0; b <= 1; ++b)
					dfs(i, j, a, b);
	// dfs(0, 0, 0, 0);
	// dfs(0, 0, 1, 0);
	

	for (int i = 0; i < 100; ++i)
		for (int j = 0; j < 100; ++j)
				for (int b = 0; b <= 1; ++b)
					fin[i][j][g[i][j][0][b]] += f[i][j][0][b];
	cerr << fin[0][0][7] << endl;
	string s = "[";
	for (int i = 0; i < 100; ++i) {
		s += "[";
		for (int j = 0; j < 100; ++j) {
			// cout << i << ": " << j << "  " << max_element(fin[i][j], fin[i][j]+11) - fin[i][j] << endl;
			//printf("    if score == %d and opponent_score == %d: return %d\n", i, j, max_element(fin[i][j], fin[i][j]+11) - fin[i][j]);
			stringstream s1;
			s1 << (max_element(fin[i][j], fin[i][j]+11) - fin[i][j]);
			//s1 << 10;
			
			string t;
			s1 >> t;
			s += t;
			if (j != 99) s += ",";
		}
		s += "]";
		if (i != 99) s += ",";
	}
	s += "]";
	cout << s;
}
