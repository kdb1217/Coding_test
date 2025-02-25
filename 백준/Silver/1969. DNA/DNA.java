import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        String[] dnaArr = new String[n];
        for (int i = 0; i < n; i++) {
            dnaArr[i] = br.readLine();
        }

        String[] dnaInfo = {"A", "C", "G", "T"};
        String dnaName = "";
        int hammingDistance = 0;

        for (int i = 0; i < m; i++) {
            String curDna = "";
            int minDiff = n + 1;

            for (String dna : dnaInfo) {
                int diffCount = 0;

                for (int j = 0; j < n; j++) {
                    if (dnaArr[j].charAt(i) != dna.charAt(0)) {
                        diffCount++;
                    }
                }

                if (diffCount < minDiff) {
                    minDiff = diffCount;
                    curDna = dna;
                }
            }

            dnaName += curDna;
            hammingDistance += minDiff;
        }
        System.out.println(dnaName);
        System.out.println(hammingDistance);
    }
}