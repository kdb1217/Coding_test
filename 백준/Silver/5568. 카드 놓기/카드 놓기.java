import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    private static int n, k;
    private static ArrayList<Integer> cards = new ArrayList<>();
    private static ArrayList<Boolean> visited;
    private static HashSet<String> answers = new HashSet<>();

    private static void backtracking(int depth, String currentNumber) {
        if (depth == k) {
            answers.add(currentNumber);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited.get(i)) {
                visited.set(i, true);
                backtracking(depth + 1, currentNumber + cards.get(i));
                visited.set(i, false);
            }
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());

        visited = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            cards.add(Integer.parseInt(br.readLine()));
            visited.add(false);
        }

        backtracking(0, "");
        System.out.println(answers.size());

    }
}