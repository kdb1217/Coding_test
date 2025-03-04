import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.ArrayDeque;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int answer = 1;

        while (a < b) {
            if (b % 10 == 1) {
                b /= 10;
                answer += 1;
            } else if (b % 2 == 0){
                b /= 2;
                answer += 1;
            } else {
                System.out.println(-1);
                return;
            }
        }

        if (a != b) {
            System.out.println(-1);
            return;
        }

        System.out.println(answer);
    }
}