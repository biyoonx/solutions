package dataStructures;

public class SampleQueue {
    private static class Node {
        private final String data;
        private Node next;
        private Node(String data) {
            this.data = data;
        }
    }

    private Node head; // remove from the head
    private Node tail; // add things here

    public boolean isEmpty() {
        return head == null;
    }
    public String peek() {
        return head.data;
    }
    public void add(String data) {
        Node node = new Node(data);

        if (tail != null) {
            tail.next = node;
        }
        tail = node;

        if (head == null) {
            head = node;
        }
    }
    public String remove() {
        String data = head.data;
        head = head.next;

        if (head == null) {
            tail = null;
        }

        return data;
    }

    public static void main(String[] args) {
        SampleQueue queue = new SampleQueue();

        System.out.println("[]");
        System.out.printf("head: %s, tail: %s\n", queue.head, queue.tail);
        System.out.printf("head.next: %s, tail.next: %s\n", "NPE", "NPE");
        System.out.printf("peek() : %s, isEmpty() : %s\n\n", "NPE", queue.isEmpty());

        System.out.println("[first]");
        queue.add("first");
        System.out.printf("head: %s, tail: %s\n", queue.head.data, queue.tail.data);
        System.out.printf("head.next: %s, tail.next: %s\n", queue.head.next, queue.tail.next);
        System.out.printf("peek() : %s, isEmpty() : %s\n\n", queue.peek(), queue.isEmpty());

        System.out.println("[first, second]");
        queue.add("second");
        System.out.printf("head: %s, tail: %s\n", queue.head.data, queue.tail.data);
        System.out.printf("head.next: %s, tail.next: %s\n", queue.head.next.data, queue.tail.next);
        System.out.printf("peek() : %s, isEmpty() : %s\n\n", queue.peek(), queue.isEmpty());

        System.out.println("[first, second, third]");
        queue.add("third");
        System.out.printf("head: %s, tail: %s\n", queue.head.data, queue.tail.data);
        System.out.printf("head.next: %s, tail.next: %s\n", queue.head.next.data, queue.tail.next);
        System.out.printf("peek() : %s, isEmpty() : %s\n\n", queue.peek(), queue.isEmpty());

        System.out.println("[second, third]");
        System.out.printf("remove \"first\" and return : %s\n", queue.remove());
        System.out.printf("head: %s, tail: %s\n", queue.head.data, queue.tail.data);
        System.out.printf("head.next: %s, tail.next: %s\n", queue.head.next.data, queue.tail.next);
        System.out.printf("peek() : %s, isEmpty() : %s\n\n", queue.peek(), queue.isEmpty());

        System.out.println("[third]");
        System.out.printf("remove \"second\" and return : %s\n", queue.remove());
        System.out.printf("head: %s, tail: %s\n", queue.head.data, queue.tail.data);
        System.out.printf("head.next: %s, tail.next: %s\n", queue.head.next, queue.tail.next);
        System.out.printf("peek() : %s, isEmpty() : %s\n\n", queue.peek(), queue.isEmpty());

        System.out.println("[]");
        System.out.printf("remove \"third\" and return : %s\n", queue.remove());
        System.out.printf("head: %s, tail: %s\n", queue.head, queue.tail);
        System.out.printf("head.next: %s, tail.next: %s\n", "NPE", "NPE");
        System.out.printf("peek() : %s, isEmpty() : %s\n\n", "NPE", queue.isEmpty());
    }
}