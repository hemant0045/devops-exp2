import java.util.Scanner;

public class Nqueen {

    static int[] board;
    static int n;

    // Check whether a queen can be placed at (row, col)
    static boolean isSafe(int row, int col) {
        for (int i = 0; i < row; i++) {
            // Same column
            if (board[i] == col)
                return false;

            // Same diagonal
            if (Math.abs(board[i] - col) == Math.abs(i - row))
                return false;
        }
        return true;
    }

    // Solve the N-Queens problem
    static boolean solve(int row) {
        if (row == n)
            return true;

        for (int col = 0; col < n; col++) {
            if (isSafe(row, col)) {
                board[row] = col;

                if (solve(row + 1))
                    return true;

                // Backtrack
                board[row] = -1;
            }
        }
        return false;
    }

    // Display the chessboard
    static void printBoard() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i] == j)
                    System.out.print("Q ");
                else
                    System.out.print(". ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the value of N: ");
        n = sc.nextInt();

        board = new int[n];

        for (int i = 0; i < n; i++)
            board[i] = -1;

        if (solve(0)) {
            System.out.println("\nSolution:");
            printBoard();
        } else {
            System.out.println("No solution exists for N = " + n);
        }

        sc.close();
    }
}