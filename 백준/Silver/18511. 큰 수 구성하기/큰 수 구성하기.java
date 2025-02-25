import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    private static String answer = ""; // 가능한 가장 큰 수 저장
    private static ArrayList<Integer> nums = new ArrayList<>(); // 사용할 수 있는 숫자들
    private static String targetNum; // 입력된 n 값 (문자열로 처리)

    // 백트래킹 메서드
    private static void backtracking(String curNum) {
        // 빈 문자열이 아니고, 현재 숫자가 목표 수보다 크면 종료
        if (!curNum.isEmpty() && Long.parseLong(curNum) > Long.parseLong(targetNum)) {
            return;
        }

        // 현재 숫자가 조건을 만족하면 정답 갱신
        if (!curNum.isEmpty()) {
            if (answer.isEmpty() || Long.parseLong(curNum) > Long.parseLong(answer)) {
                answer = curNum;
            }
        }

        // 가능한 모든 숫자 조합 시도
        for (int num : nums) {
            backtracking(curNum + num);
        }
    }

    public static void main(String[] args) throws IOException {
        // 빠른 입력 처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 입력 받기
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        targetNum = String.valueOf(n); // 목표 숫자 문자열로 저장

        // 사용할 숫자들 입력 받기
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            nums.add(Integer.parseInt(st.nextToken()));
        }

        // 숫자를 내림차순으로 정렬 (큰 숫자부터 시도하면 더 빠르게 큰 값 탐색 가능)
        Collections.sort(nums, Collections.reverseOrder());

        // 처음부터 가능한 숫자들로 시작
        for (int num : nums) {
            backtracking(String.valueOf(num)); // 빈 문자열로 시작하지 않고 첫 숫자부터 시작
        }

        // 결과 출력
        System.out.println(answer);
    }
}