package dataStructures;

public class SampleStack {
    private static class Node {
        private final String data;
        private Node next;
        private Node(String data) {
            this.data = data;
        }
    }

    private Node top;

    public boolean isEmpty() {
        return top == null;
    }
    public String peek() {
        return top.data;
    }
    public void push(String data) {
        Node node = new Node(data);
        node.next = top;
        top = node;
    }
    public String pop() {
        String data = top.data;
        top = top.next;
        return data;
    }

    public static void main(String[] args) {
        SampleStack stack = new SampleStack();

        System.out.println("[]");
        System.out.printf("top: %s\n", stack.top);
        System.out.printf("top.next: %s\n", "NPE");
        System.out.printf("peek() : %s, isEmpty() : %s\n\n", "NPE", stack.isEmpty());

        System.out.println("[first]");
        stack.push("first");
        System.out.printf("top: %s\n", stack.top.data);
        System.out.printf("top.next: %s\n", stack.top.next);
        System.out.printf("peek() : %s, isEmpty() : %s\n\n", stack.peek(), stack.isEmpty());

        System.out.println("[first, second]");
        stack.push("second");
        System.out.printf("top: %s\n", stack.top.data);
        System.out.printf("top.next: %s\n", stack.top.next.data);
        System.out.printf("peek() : %s, isEmpty() : %s\n\n", stack.peek(), stack.isEmpty());

        System.out.println("[first, second, third]");
        stack.push("third");
        System.out.printf("top: %s\n", stack.top.data);
        System.out.printf("top.next: %s\n", stack.top.next.data);
        System.out.printf("peek() : %s, isEmpty() : %s\n\n", stack.peek(), stack.isEmpty());

        System.out.println("[second, third]");
        System.out.printf("pop \"first\" and return : %s\n", stack.pop());
        System.out.printf("top: %s\n", stack.top.data);
        System.out.printf("top.next: %s\n", stack.top.next.data);
        System.out.printf("peek() : %s, isEmpty() : %s\n\n", stack.peek(), stack.isEmpty());

        System.out.println("[third]");
        System.out.printf("pop \"second\" and return : %s\n", stack.pop());
        System.out.printf("top: %s\n", stack.top.data);
        System.out.printf("top.next: %s\n", stack.top.next);
        System.out.printf("peek() : %s, isEmpty() : %s\n\n", stack.peek(), stack.isEmpty());

        System.out.println("[]");
        System.out.printf("pop \"third\" and return : %s\n", stack.pop());
        System.out.printf("top: %s\n", stack.top);
        System.out.printf("top.next: %s\n", "NPE");
        System.out.printf("peek() : %s, isEmpty() : %s\n\n", "NPE", stack.isEmpty());
    }
}