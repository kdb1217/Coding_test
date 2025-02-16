import java.io.*;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Deque;


public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


    public static void main(String[] args) throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Deque<Integer> dec = new LinkedList<>();

        int n = Integer.parseInt(br.readLine());

        for (int i = 1; i < n+1; i++) {
            dec.addLast(i);
        }

        while (dec.size() > 1) {
            int discard = dec.pollFirst();
            int move = dec.pollFirst();
            dec.addLast(move);
        }

        bw.write(dec.pollLast() + "\n");
        bw.flush();
        bw.close();
    }
}