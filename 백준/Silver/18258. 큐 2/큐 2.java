import java.io.*;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Deque;


public class Main {
    private static Deque<Integer> queue = new LinkedList<>();
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static void push(int x) {
        queue.addLast(x);
    }

    private static void pop() throws Exception {
        if (queue.isEmpty()) {
            bw.write(-1 + "\n");
        } else {
            bw.write(queue.pollFirst() + "\n");
        }
    }

    private static void size() throws Exception {
        bw.write(queue.size() + "\n");
    }

    private static void empty() throws Exception {
        boolean result = queue.isEmpty();

        if (result) {
            bw.write(1 + "\n");
        } else {
            bw.write(0 + "\n");
        }
    }


    private static void front() throws Exception {
        if (queue.isEmpty()) {
            bw.write(-1 + "\n");

        } else {
            bw.write(queue.peekFirst() + "\n");
        }
    }

    private static void back() throws Exception {
        if (queue.isEmpty()) {
            bw.write(-1 + "\n");

        } else {
            bw.write(queue.peekLast() + "\n");
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
                    push(Integer.parseInt(st.nextToken()));
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

                case "front":
                    front();
                    break;

                case "back":
                    back();
                    break;
            }
        }
        bw.flush();
        bw.close();
    }
}