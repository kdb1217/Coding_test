//import java.io.BufferedReader;
//import java.io.InputStreamReader;
//import java.io.IOException;
//import java.lang.reflect.Array;
//import java.util.*;
//
//public class Main {
//    private static int n;
//    private static int m;
//    private static int arr[];
//    private static int nums[];
//    private static boolean visited[];
//    private static Set<List<Integer>> set = new HashSet<>();
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//        n = Integer.parseInt(st.nextToken());
//        m = Integer.parseInt(st.nextToken());
//        st = new StringTokenizer(br.readLine());
//        nums = new int[n + 1];
//        for (int i = 0; i < n; i++) {
//            nums[i] = Integer.parseInt(st.nextToken());
//        }
//        Arrays.sort(nums);
//        br.close();
//        arr = new int[m + 1];
//        visited = new boolean[n + 1];
//        backtracking(0);
//    }
//
//    public static void backtracking(int depth) {
//        if (depth == m) {
//            List<Integer> current = new ArrayList<>();
//            for (int i = 0; i < m; i++) {
//                current.add(arr[i]);
//            }
//
//            if (!set.contains(current)) {
//                set.add(current); // 중복 방지를 위해 저장
//                for (int i = 0; i < m; i++) {
//                    System.out.print(arr[i] + " ");
//                }
//                System.out.println();
//            }
//            return;
//        }
//
//        for (int i = 1; i <= n; i++) {
//            arr[depth] = nums[i];
//            backtracking(depth + 1);
//
//        }
//    }
//}


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.ArrayDeque;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    private static int n;
    private static int m;
    private static int arr[];
    private static boolean visited[];
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        br.close();
        arr = new int[n + 1];
        backtracking(0);

        System.out.println(sb);

    }

    public static void backtracking(int depth) {
        if (depth == m) {
            for (int i = 0; i < m; i++) {
                sb.append(arr[i]).append(" ");
            }
            sb.append('\n');
            return;
        }

        for (int i = 1; i <= n; i++) {
            arr[depth] = i;
            backtracking(depth + 1);
        }
    }
}