class Solution {
public:
    bool isPalindrome(int x) {


        string S = to_string(x);
        int N = S.size();
        for (int i = 0 ; i < N ; i++){
            if (S[i] != S[N - 1 - i]) return false;
        }
        return true;


        
    }
};