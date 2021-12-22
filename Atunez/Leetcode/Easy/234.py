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
    boolean even = false;
    
    public ListNode middleNode(ListNode head) {
        if(head.next == null){
            return head;
        }
        
        ListNode slow = head;
        ListNode fast = head.next;
        
        while(fast != slow){
            if(fast.next == null){
                even = true;
                return slow;
            }
            fast = fast.next.next;
            if(fast == null){
                return slow;
            }
            slow = slow.next;
         }
        
        return null;
    }

    
    public ListNode reverse(ListNode head){
        if(head == null){
            return null;
        }
        ListNode ret = new ListNode(head.val);
        while(head.next != null){
            head = head.next;
            ret = new ListNode(head.val, ret);
        }
        return ret;   
    }
    
    public boolean isPalindrome(ListNode head) {
        if(head.next == null){
            return true;
        }
        if(head.next.next == null){
            return head.val == head.next.val;
        }
        if(head.next.next.next == null){
            return head.val == head.next.next.val;
        }
        ListNode middle = middleNode(head);
        ListNode shifted;
        if(even){
            shifted = middle.next;
            // deal with X Y1 Y2 X, shifted is Y2, middle is Y1
        }else{
            shifted = middle.next.next;
            // deal with X1 Y X2, middle is X1, shifted is X2
        }
        middle.next = null;
        
        // This needs to be changed to satisfy the O(1) space requirement...
        ListNode reversedMiddle = reverse(shifted);
        
        while(true){
            if(reversedMiddle.val != head.val){
                return false;
            }
            head = head.next;
            reversedMiddle = reversedMiddle.next;
            if(head == null && reversedMiddle == null){
                return true;
            }
            if(head == null || reversedMiddle == null ){
                return false;
            }
        }        
    }
}
