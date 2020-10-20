import java.util.Arrays;


class Solution{
    public static boolean valid_pillar(int x, int y, boolean[][] pillar, boolean[][] beam) {
        boolean valid = false;
        int n = pillar.length;

        if(y == n-1) {
            return valid;
        }

        if(y == 0) {
            valid = true;
        } else {
            if(pillar[x][y-1]) {
                valid = true;
            }
        }

        if(x == 0){
            if(beam[x][y]) {
                valid = true;
            }
        } else if (x == n-1) {
            if(beam[x-1][y]) {
                valid = true;
            }
        } else {
            if(beam[x][y] || beam[x-1][y]) {
                valid = true;
            }
        }

        return valid;
    }

    public static boolean valid_beam(int x, int y, boolean[][] pillar, boolean[][] beam) {
        boolean valid = false;
        int n = beam.length;

        if((y == 0) || (x == n-1)){
            return valid;
        }

        if(pillar[x][y-1] || pillar[x+1][y-1]) {
            valid = true;
        }    

        if((x > 0) && (x < n-1)){
            if(beam[x-1][y] && beam[x+1][y]) {
                valid = true;
            }
        }

        return valid;
    }

    public static void install_pillar(int x, int y, boolean[][] pillar, boolean[][] beam) {
        if(valid_pillar(x, y, pillar, beam)) {
            pillar[x][y] = true;
        }
    }
    public static void install_beam(int x, int y, boolean[][] pillar, boolean[][] beam) {
        if(valid_beam(x, y, pillar, beam)) {
            beam[x][y] = true;
        }
    }
    public static void remove_pillar(int x, int y, boolean[][] pillar, boolean[][] beam) {
        pillar[x][y] = false;
        for(int i = 0; i < pillar.length; i++) {
            for(int j = 0; j < pillar[0].length; j++) {
                if(pillar[i][j] && !valid_pillar(i, j, pillar, beam)) {
                    pillar[x][y] = true;
                    return;
                }
                if(beam[i][j] && !valid_beam(i, j, pillar, beam)) {
                    pillar[x][y] = true;
                    return;
                }
            }
        }
    }
    public static void remove_beam(int x, int y, boolean[][] pillar, boolean[][] beam) {
        beam[x][y] = false;
        for(int i = 0; i < beam.length; i++) {
            for(int j = 0; j < beam[0].length; j++) {
                if(pillar[i][j] && !valid_pillar(i, j, pillar, beam)) {
                    beam[x][y] = true;
                    return;
                }
                if(beam[i][j] && !valid_beam(i, j, pillar, beam)) {
                    beam[x][y] = true;
                    return;
                }
            }
        }
    }

    public static int[][] solution(int n, int[][] build_frame) {
        // initialize pillar and beam
        boolean[][] pillar = new boolean[n+1][n+1];
        boolean[][] beam = new boolean[n+1][n+1];
        for(int i = 0; i < n+1; i++){
            for(int j = 0; j < n+1; j++) {
                pillar[i][j] = false;
                beam[i][j] = false;
            }
        }

        for(int[] command: build_frame) {
            int x = command[0];
            int y = command[1];
            int a = command[2];
            int b = command[3];

            if(a == 0 && b == 0) {
                remove_pillar(x, y, pillar, beam);
            }
            else if(a == 0 && b == 1) {
                install_pillar(x, y, pillar, beam);
            }
            else if(a == 1 && b == 0) {
                remove_beam(x, y, pillar, beam);
            }
            else if(a == 1 && b == 1) {
                install_beam(x, y, pillar, beam);
            }

            // for(int i = 0; i < beam.length; i++) {
            //     for(int j = 0; j < beam[0].length; j++) {
            //         System.out.print(beam[i][j]);
            //         System.out.print(" ");
            //     }
            //     System.out.println();
            // }
            // System.out.println("=============");
    
        }

        int counter = 0;
        for(int i = 0; i < n+1; i++) {
            for(int j = 0; j < n+1; j++) {
                counter += pillar[i][j] ? 1 : 0;
                counter += beam[i][j] ? 1 : 0;
            }
        }

        int[][] answer = new int [counter][3];
        int index = 0;
        for(int i = 0; i < n+1; i++) {
            for(int j = 0; j < n+1; j++) {
                if(pillar[i][j]) {
                    answer[index][0] = i;
                    answer[index][1] = j;
                    answer[index][2] = 0;
                    index += 1;
                }
                if(beam[i][j]) {
                    answer[index][0] = i;
                    answer[index][1] = j;
                    answer[index][2] = 1;
                    index += 1;
                }
            }
        }

        // for(int i = 0; i < counter; i++) {
        //     for(int j = 0; j < 3; j++) {
        //         System.out.print(answer[i][j]);
        //         System.out.print(" ");
        //     }
        //     System.out.println();
        // }

        return answer;
    }

    public static void main(String[] args) {
        // int n = 5;
        // int[][] build_frame = {
        //     {1, 0, 0, 1}, {1, 1, 1, 1},
        //     {2, 1, 0, 1}, {2, 2, 1, 1},
        //     {5, 0, 0, 1}, {5, 1, 0, 1},
        //     {4, 2, 1, 1}, {3, 2, 1, 1}
        // };
        // int[][] answer = {
        //     {1, 0, 0}, {1, 1, 1},
        //     {2, 1, 0}, {2, 2, 1},
        //     {3, 2, 1}, {4, 2, 1},
        //     {5, 0, 0}, {5, 1, 0}
        // };
        // int[][] my_answer = solution(n, build_frame);
        
        int n = 5;
        int[][] build_frame = {
            {0, 0, 0, 1}, {2, 0, 0, 1},
            {4, 0, 0, 1}, {0, 1, 1, 1},
            {1, 1, 1, 1}, {2, 1, 1, 1},
            {3, 1, 1, 1}, {2, 0, 0, 0},
            {1, 1, 1, 0}, {2, 2, 0, 1}
        };
        int[][] answer = {
            {0, 0, 0}, {0, 1, 1},
            {1, 1, 1}, {2, 1, 1},
            {3, 1, 1}, {4, 0, 0}
        };
        int[][] my_answer = solution(n, build_frame);

        assert Arrays.deepEquals(my_answer, answer);
    }
}