#include<iostream>
#include<vector>
using namespace std;

class leetcode
{
public:
     vector<int>traverseArray(vector<int>& nums)
     {
          vector<int>result;
          for(int i=0;i<nums.size();i++)
          {
               result.push_back(nums[i]);
          }
          return result;
     }

};
