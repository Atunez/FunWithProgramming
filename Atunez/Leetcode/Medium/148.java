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
    public ListNode middleNode(ListNode head) {
        if(head.next == null){
            return head;
        }
        
        ListNode slow = head;
        ListNode fast = head.next;
        
        while(fast != slow){
            if(fast.next == null){
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
    
    public ListNode mergeLists(ListNode h, ListNode t){
        if(t == null){
            return h;
        }
        if(h == null){
            return t;
        }
        
        if(h.val > t.val){
            t.next = mergeLists(h, t.next);
            return t;
        }else{
            h.next = mergeLists(h.next, t);
            return h;
        }
    }
    
    public void getLen(ListNode head){
        int i = 0;
        while(true){
            if(head == null){
                break;
            }
            i++;
            head = head.next;
        }
        System.out.println(i);
    }
    
    public ListNode sortList(ListNode head) {
        if(head == null){
            return null;
        }
        if(head.next == null){
            return head;
        }
        ListNode middle = middleNode(head);
        ListNode shifted = middle.next;
        middle.next = null;
        ListNode recur1 = sortList(head);
        ListNode recur2 = sortList(shifted);
        return mergeLists(recur1, recur2);
    }
}

// Fuck leetcode wanting me to do this in O(1) space as "bonus" that is a dumb way to write it
