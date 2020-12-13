package step3;

public class Step3 {
    char[] alpha = {'B', 'W', 'O', 'G', 'Y', 'R'};
    char arr[][][] = new char[6][3][3];

    // 큐브 상태 출력
    void printcube(){
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < alpha.length; j++) {
                for (int k = 0; k < 3; k++) {
                    System.out.print(alpha[j]+"\t");
                }
                if (j==5) {
                    System.out.println("");
                }else{
                    System.out.print("\t\t");
                }
            }
        }
    }
    //  3차원 배열에 큐브상태 저장
    void savecube(){
        for(int i=0; i<alpha.length; i++){
            for(int j=0; j<3; j++){
                for(int k=0; k<3; k++){
                    arr[i][j][k] = alpha[i];
                }
            }
        }
    }
    public static void main(String[] args) {
        Step3 s = new Step3();
        s.savecube();
        s.printcube();
    }
}
