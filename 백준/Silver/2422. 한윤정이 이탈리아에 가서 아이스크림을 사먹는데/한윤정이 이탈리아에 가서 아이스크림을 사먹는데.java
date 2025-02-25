import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int cnt = 0;
        boolean[][] forbiddenArr = new boolean[n + 1][n + 1];

        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int ice1 = Integer.parseInt(st.nextToken());
            int ice2 = Integer.parseInt(st.nextToken());
            forbiddenArr[ice1][ice2] = true;
            forbiddenArr[ice2][ice1] = true;
        }


        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                for (int k = j + 1; k <= n; k++) {
                    if (!forbiddenArr[i][j] && !forbiddenArr[j][k] && !forbiddenArr[i][k]) {
                        cnt++;
                    }
                }
            }
        }

        System.out.println(cnt);
    }
}