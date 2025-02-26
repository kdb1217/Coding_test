import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int cnt = 0;

        while (n > 1) {
            if (n % 5 == 0) {
                cnt += n / 5;
                n = n % 5;
            } else {
                n -= 2;
                cnt += 1;
            }
        }

        if (n == 0) {
            System.out.println(cnt);
        } else {
            System.out.println(-1);
        }
    }
}