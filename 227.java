import java.util.Stack;

public class Solution {
    public int calculate(String s) {

        int ans = 0;
        int n = 0;
        char op = '+';
        s += "+0";
        Stack stack = new Stack();
        for (char ch : s.toCharArray()) {
            switch (ch) {
                case '+':
                case '-':
                    if (!stack.isEmpty()) {
                        n = calc(ans, op, n);
                        ans = (int) stack.pop();
                        op = (char) stack.pop();
                    }
                    ans = calc(ans, op, n);
                    op = ch;
                    n = 0;
                    break;
                case '*':
                case '/':
                    if (!stack.isEmpty()) {
                        ans = calc(ans, op, n);
                    } else {
                        stack.push(op);
                        stack.push(ans);
                        ans = n;
                    }
                    op = ch;
                    n = 0;
                    break;
                case ' ':
                    break;
                default:
                    n *= 10;
                    n += ch - 0x30;
            }
        }
        return ans;
    }

    private int calc(int ans, char op, int n) {
        switch (op) {
            case '+':
                return ans + n;
            case '-':
                return ans - n;
            case '*':
                return ans * n;
            case '/':
                return ans / n;
        }
        return 0;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.calculate("0*0"));
        System.out.println(solution.calculate(" 1+1 "));
    }
}

