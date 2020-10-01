import java.util.List;
import java.util.Vector;

/**
 * A class which enables user to run a large chunk of
 * tasks in parallel efficiently.
 *
 * @author Jeffery 1-29-19
 */
public class TaskManager
{
    /** Number of threads to use at once */
    private int threadCount;

    /** Meaningless tasks to run in parallel */
    private List<ReadTask> tasks;


    public TaskManager(int threadCount)
    {
        this.threadCount = threadCount;
        //using vectors because they are thread safe
        this.tasks = new Vector<>();
    }


    public void addTask(ReadTask t)
    {
        tasks.add(t);
    }


    /**
     * This is the fun method.
     *
     * This will run all of the tasks in parallel using the
     * desired amount of threads untill all of the jobs are
     * complete.
     */
    public void runTasks()
    {
        int desiredThreads = threadCount > tasks.size() ?
                tasks.size() : threadCount;

        Thread[] runners = new Thread[desiredThreads];

        for(int i = 0; i < desiredThreads; i++)
        {
            runners[i] = new Thread(()->
            {
                ReadTask t = null;
                while(true)
                {
                    //need synchronized block to prevent
                    //race condition
                    synchronized (tasks)
                    {
                        if(!tasks.isEmpty())
                            t = tasks.remove(0);
                    }
                    if(t == null)
                    {
                        break;
                    }
                    else
                    {
                        t.runTask();
                        t = null;
                    }
                }
            });
            runners[i].start();
        }

        for(int i = 0; i < desiredThreads; i++)
        {
            try
            {
                runners[i].join();
            }
            catch (Exception e)
            {
                e.printStackTrace();
            }
        }
    }
}