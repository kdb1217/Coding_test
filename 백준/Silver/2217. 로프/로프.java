import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> arr = new ArrayList<Integer>();

        int n = Integer.parseInt(br.readLine());
        int answer = 0;

        for (int i = 0; i < n; i++) {
            arr.add(Integer.parseInt(br.readLine()));
        }
        arr.sort(Collections.reverseOrder());

        for (int i = 0; i < n; i++) {
            int tmpw = (i + 1) * arr.get(i);

            if (tmpw >= answer) {
                answer = tmpw;
            }
        }
        System.out.println(answer);
    }
}