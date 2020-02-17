import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class ArrayManip {

    static long arrayManipulation(int n, int[][] queries) {
    	Map<Integer, Long> ops = new TreeMap<>();
    	for (int[] q : queries) {
    		int a = q[0];
    		int b = q[1];
    		int k = q[2];
    		Long va = ops.get(a);
    		if (va == null) {
    			va = Long.valueOf(k);
    		} else {
    			va = va + k;
    		}
    		ops.put(a, va);

    		b++;
    		Long vb = ops.get(b);
    		if (vb == null) {
    			vb = Long.valueOf(-k);
    		} else {
    			vb = vb - k;
    		}
    		ops.put(b, vb);
    	}
    	long max = 0;
    	long sum = 0;
    	for (Long s : ops.values()) {
    		sum += s;
    		if (sum > max) {
    			max = sum;
    		}
    	}
    	// System.out.println(max);
    	return max;
    }
    
	
	private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nm = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nm[0]);

        int m = Integer.parseInt(nm[1]);

        int[][] queries = new int[m][3];

        for (int i = 0; i < m; i++) {
            String[] queriesRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 3; j++) {
                int queriesItem = Integer.parseInt(queriesRowItems[j]);
                queries[i][j] = queriesItem;
            }
        }

        long result = arrayManipulation(n, queries);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
