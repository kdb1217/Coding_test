import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Deque;


public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Deque<Integer> dec = new LinkedList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<Integer> answer = new ArrayList<>();

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int count = 0;


        for (int i = 1; i < n+1; i++) {
            dec.addLast(i);
        }

        while (!dec.isEmpty()) {
            count += 1;
            int tmp = dec.pollFirst();
            if (count == m) {
                answer.add(tmp);
                count = 0;
            } else {
                dec.addLast(tmp);
            }
        }

        bw.write("<");
        for (int i = 0; i < answer.size() - 1; i++) {
            bw.write(answer.get(i) + ", ");
        }
        bw.write(answer.get(answer.size() - 1) + ">\n");
        bw.flush();
        bw.close();
    }
}