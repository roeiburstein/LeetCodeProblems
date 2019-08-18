/**
 You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 
 You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 
 Example:
 
 Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 Output: 7 -> 0 -> 8
 Explanation: 342 + 465 = 807.
 */

#include <iostream>

struct ListNode{
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int remainder = 0;
        int curr_sum = l1->val + l2->val;
        
        if (curr_sum >= 10){
            curr_sum -= 10;
            remainder = 1;
        }
        
        ListNode* l3 = new ListNode(curr_sum);
        ListNode* l3_temp = l3;
        ListNode* l3_temp2 = l3_temp;
        
        do {
            curr_sum = l1->val + l2->val + remainder;
            
            if (curr_sum >= 10){
                curr_sum -= 10;
                remainder = 1;
            }
            
            l3_temp = new ListNode(curr_sum);
            l3_temp2->next = l3_temp;
            l1 = l1->next;
            l2 = l2->next;
            l3_temp2 = l3_temp2->next;
            
            remainder = 0;
            curr_sum = 0;
            
        } while(l1 != NULL && l2 != NULL);
        
        if (remainder == 1){
            l3_temp = new ListNode(remainder);
            l3_temp2->next = l3_temp;
        }
        return l3;
    }
    
int main(int argc, const char * argv[]) {
    return 0;
}

};
#include <iostream>

