import java.io.*;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Deque;


public class Main {
    private static StringBuilder result = new StringBuilder();
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static void solution() throws IOException {
        String n = "";
        n = br.readLine();
        int left = 0;
        int right = 0;

        for (int i = 0; i < n.length(); i++) {
            if (n.charAt(i) == '(') {
                left += 1;
            } else {
                right += 1;
            }

            if (left < right) {
                result.append("NO\n");
                return;
            }
        }

        if (left == right) {
            result.append("YES\n");
        } else {
            result.append("NO\n");
        }
        return;
    }

    public static void main(String[] args) throws Exception {
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            solution();
        }

        bw.write(result.toString());
        bw.flush();
        bw.close();
    }
}