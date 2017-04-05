# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        if(cur == None):
            return None
        if(cur.next == None):
            return head
        else:
            length = 1
            while(cur.next != None):
                cur = cur.next
                length = length+1
            oldtail = cur
            cur = head
            k = k%length
            counter = 1
            while(counter<length-k):
                cur = cur.next
                counter = counter+1
            
            oldtail.next = head
            head = cur.next
            cur.next = None
        return head
        
#         class Solution {
# public:
#     ListNode* rotateRight(ListNode* head, int k) {
#         if(!head) return head;
        
#         int len=1; // number of nodes
#         ListNode *newH, *tail;
#         newH=tail=head;
        
#         while(tail->next)  // get the number of nodes in the list
#         {
#             tail = tail->next;
#             len++;
#         }
#         tail->next = head; // circle the link

#         if(k %= len) 
#         {
#             for(auto i=0; i<len-k; i++) tail = tail->next; // the tail node is the (len-k)-th node (1st node is head)
#         }
#         newH = tail->next; 
#         tail->next = NULL;
#         return newH;
#     }
# };