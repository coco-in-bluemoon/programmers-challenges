import java.util.ArrayDeque;

class Coordinator {
    private int rowIndex;
    private int colIndex;

    public Coordinator() {
        this.rowIndex = 0;
        this.colIndex = 0;
    }

    public Coordinator(int rowIndex, int colIndex) {
        this.rowIndex = rowIndex;
        this.colIndex = colIndex;
    }

    public void setColIndex(int colIndex) {
        this.colIndex = colIndex;
    }
    public void setRowIndex(int rowIndex) {
        this.rowIndex = rowIndex;
    }
    public int getColIndex() {
        return colIndex;
    }
    public int getRowIndex() {
        return rowIndex;
    }
}


class Solution {
    public static int[] solution(int m, int n, int[][] picture) {
        boolean[][] visited = new boolean[m][n];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                visited[r][c] = false;
            }
        }

        ArrayDeque<Coordinator> queue = new ArrayDeque<>();

        int maxSizeBlock = 0;
        int counterBlock = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (picture[r][c] == 0) {
                    visited[r][c] = true;
                } 
                if (visited[r][c]) {
                    continue;
                }
                
                queue.add(new Coordinator(r, c));
                counterBlock += 1;
                int blockId = picture[r][c];
                int sizeBlock = 0;
                while (queue.size() > 0) {
                    Coordinator coord = queue.pop();

                    int baseRowIndex = coord.getRowIndex();
                    int baseColIndex = coord.getColIndex();

                    if (visited[baseRowIndex][baseColIndex]) {
                        continue;
                    }

                    visited[baseRowIndex][baseColIndex] = true;
                    sizeBlock += 1;
                    
                    int[] deltaRow = {0, 0, 1, -1};
                    int[] deltaCol = {1, -1, 0, 0};

                    for (int deltaIndex = 0; deltaIndex < deltaRow.length; deltaIndex++) {
                        int dr = deltaRow[deltaIndex];
                        int dc = deltaCol[deltaIndex];

                        int nextRowIndex = baseRowIndex + dr;
                        int nextColIndex = baseColIndex + dc;

                        if (! (0 <= nextRowIndex && nextRowIndex < m && 0 <= nextColIndex && nextColIndex < n)) {
                            continue;
                        }

                        if (picture[nextRowIndex][nextColIndex] != blockId) {
                            continue;
                        } 

                        if (visited[nextRowIndex][nextColIndex]) {
                            continue;
                        }

                        queue.add(new Coordinator(nextRowIndex, nextColIndex));                        
                    }
                }

                if (maxSizeBlock < sizeBlock) {
                    maxSizeBlock = sizeBlock;
                }

            }
        }

        int[] answer = {counterBlock, maxSizeBlock};
        return answer;
    }

    public static void main(String[] args) {
        int m = 6;
        int n = 4;
        int[][] picture = {
            {1, 1, 1, 0},
            {1, 2, 2, 0},
            {1, 0, 0, 1},
            {0, 0, 0, 1},
            {0, 0, 0, 3},
            {0, 0, 0, 3}
        };
        int[] answer = {4, 5};
        int[] myAnswer = solution(m, n, picture);
        assert answer.equals(myAnswer);
    }
}