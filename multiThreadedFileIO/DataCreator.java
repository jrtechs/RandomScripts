import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.math.*;

/**
 * Simple class to generate random data for
 * file IO tests.
 *
 * @author Jeffery Russell 1-31-19
 */
public class DataCreator
{
    /**
     * Generates an obscure random character
     * @return
     */
    private static char rndChar()
    {
        // or use Random or whatever
        int rnd = (int) (Math.random() * 52);
        char base = (rnd < 26) ? 'A' : 'a';
        return (char) (base + rnd % 26);
    }


    /**
     * Simple function to save contents to the disk
     *
     * @param s
     * @param fileName
     */
    private static void saveToDisk(String s, String fileName)
    {
        BufferedWriter writer;
        try
        {
            File file = new File(fileName);
            file.createNewFile();
            writer = new BufferedWriter(new FileWriter(file));
            writer.write(s);
            writer.flush();
            writer.close();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }


    /**
     * Creates 5MB of random test data to use
     */
    public static void main(String[] arguments)
    {
        System.out.println("Creating Test Files");
        for(int i = 0; i < 100; i++)
        {
            //10k random characters for each file
            //each file is 10kb * 500 files, total size of 5MB
            String s = "";
            for(int j = 0; j < 1000000; j++)
            {
                s = s + rndChar();
            }
            saveToDisk(s, "./testData/" + i + ".txt");
            System.out.println(s);
        }
    }
}