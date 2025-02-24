import java.io.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static int manageIndex(int idx, int a) { return idx % a;}
    public static boolean isFinished(int sign, int t, int bCount, int dCount ) {
        if (sign == 0) {
            return t == bCount;
        } else {
            return t == dCount;
        }
    }



    public static void main(String[] args) throws Exception {
        int a = Integer.parseInt(br.readLine());
        int t = Integer.parseInt(br.readLine());
        int sign = Integer.parseInt(br.readLine());
        int startIdx = 0;
        int gameRound = 0;
        int bCount = 0;
        int dcount = 0;

        while (true) {
            for (int i = 0; i < 4; i ++) {
                if (i % 2 == 0) {
                    bCount++;
                } else {
                    dcount++;
                }

                if (isFinished(sign, t, bCount, dcount)) {
                    startIdx = manageIndex(startIdx, a);
                    System.out.println(startIdx);
                    return;
                } else {
                    startIdx++;
                }
            }

            for (int i = 0; i < 2 * (gameRound + 2); i ++) {
                if (i < (2 * (gameRound + 2)) / 2) {
                    bCount++;
                } else {
                    dcount++;
                }

                if (isFinished(sign, t, bCount, dcount)) {
                    startIdx = manageIndex(startIdx, a);
                    System.out.println(startIdx);
                    return;
                } else {
                    startIdx++;
                }
            }

            gameRound++;
        }
    }
}