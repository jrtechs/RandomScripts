import java.util.*;

/**
 * File to test the performance of multi threaded file
 * io by reading a large quantity of files in parallel
 * using a different amount of threads.
 *
 * @author Jeffery Russell 1-31-19
 */
public class MultiThreadedFileReadTest
{
    public static void main(String[] args)
    {
        List<Integer> x = new ArrayList<>();
        List<Double> y = new ArrayList<>();
        for(int i = 1; i <= 64; i++)
        {
            long threadTotal = 0;
            for(int w = 0; w < 20; w++)
            {
                TaskManager boss = new TaskManager(i);

                for(int j = 0; j < 500; j++)
                {
                    boss.addTask(new ReadTask("./testData/" + i + ".txt"));
                }
                long startTime = System.nanoTime();
                boss.runTasks();
                long endTime = System.nanoTime();
                long durationMS = (endTime - startTime)/1000000;
                threadTotal+= durationMS;
            }

            x.add(i);
            y.add(threadTotal/20.0); //finds average
        }
        System.out.println(x);
        System.out.println(y);
    }
}