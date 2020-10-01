import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;


/**
 * Simple class for reading files as strings. 
 *
 * @author Jeffery Russell
 */
public class FileReader
{

    public static String readFile(String filePath)
    {
        String fileContent = new String();

        try
        {
            BufferedReader br = new BufferedReader(
                    new InputStreamReader(new FileInputStream(filePath)));
            String line;

            while ((line = br.readLine()) != null)
            {
                fileContent = fileContent.concat(line);
            }
            br.close();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        return fileContent;
    }


    public static void main(String[] args)
    {
        System.out.println("Test");
        System.out.println(FileReader.readFile("./testData/data1.txt"));
    }
}