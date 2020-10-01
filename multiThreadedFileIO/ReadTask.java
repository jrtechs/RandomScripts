/**
 * Simple method to be used by the task manager to do
 * file io.
 *
 * @author Jeffery Russell
 */
public class ReadTask
{
    private String fileName;

    public ReadTask(String fileName)
    {
        this.fileName = fileName;
    }

    public void runTask()
    {
        FileReader.readFile(fileName);
    }
}