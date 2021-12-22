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
    public ListNode removeElements(ListNode head, int val) {
        if(head == null){
            return head;
        }
        if(head.next == null){
            if(head.val == val){
                return null;
            }
            return head;
        }
        
        ListNode answer = head;
        ListNode answer2 = answer;
        
        while(answer != null && answer.val == val){
            answer2 = answer.next;
            answer = answer.next;
        }
        
        // Fix answer so that the first digit is not an invalid number...
        // now that we are good...
        // if next is val, skip it.
        
        while(true){
            if(answer == null){ // empty or end
                return answer;
            }
            
            
            if(answer.next == null){ // end go out
                break;
            }
            
            // check if X X ... X Y, goes to 
            while(answer.next != null && answer.next.val == val){
                answer.next = answer.next.next;
            }
            
            if(answer.next == null){
                break;
            }
            
            answer = answer.next;
        }
        
        return answer2;
        
    }
}
