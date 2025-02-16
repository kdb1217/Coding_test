import java.io.*;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Deque;


public class Main {
    private static StringBuilder result = new StringBuilder();
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static Deque<Integer> stack = new LinkedList<>();

    private static void push(int x) {
        stack.addLast(x);
    }

    private static void pop() {
        if (stack.isEmpty()) {
            result.append(-1 + "\n");
        } else {
            result.append(stack.removeLast()).append("\n");
        }
    }

    private static void size() {
        result.append(stack.size()).append("\n");
    }

    private static void empty() {
        if (stack.isEmpty()) {
            result.append(1 + "\n");
        } else {
            result.append(0 + "\n");
        }
    }

    private static void top() {
        if (stack.isEmpty()) {
            result.append(-1 + "\n");
        } else {
            result.append(stack.peekLast()).append("\n");
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();

            switch (cmd) {
                case "push":
                    int num = Integer.parseInt(st.nextToken());
                    push(num);
                    break;
                case "pop":
                    pop();
                    break;
                case "size":
                    size();
                    break;
                case "empty":
                    empty();
                    break;
                case "top":
                    top();
                    break;
            }
        }
        bw.write(result.toString());
        bw.flush();
        bw.close();

    }
}