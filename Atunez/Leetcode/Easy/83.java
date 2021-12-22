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
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        
        ListNode answer = head;
        
        while(true){
            while(head.next != null && head.val == head.next.val){
                head.next = head.next.next;
            }
            
            if(head.next == null){
                break;
            }
            
            head = head.next;
        }
        
        return answer;
    }
}
// 100% in speed lolw
