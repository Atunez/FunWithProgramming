/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null){
            return null;
        }
        ListNode ret = new ListNode(head.val);
        while(head.next != null){
            head = head.next;
            ret = new ListNode(head.val, ret);
        }
        return ret;   
        
        // ListNode prev = null;
        // while (head != null) {
        //     ListNode n = head.next;
        //     head.next = prev;
        //     prev = head;
        //     head = n;
        // }
        // return prev;
        // n = head.next = prev = head = n;
    }
    
    
}
