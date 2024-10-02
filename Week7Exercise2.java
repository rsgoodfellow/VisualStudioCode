import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main { //main class
    public static void readCsv(String fileName) { //method to read and write CVS file
        String line; //declares new String
        while ((line = br.readLine()) != null) { //while loop to read the line
            String[] values = line.split(","); //splits array index with a comma
            System.out.println("Name: " + values[0] + ", Grade: " + values[1]); //prints array index's student name and grade
        }
    }

    public static void main(String[] args) { //main method to run program
        String fileName = "students.csv";  // Specify the file name
        readCsv(fileName);  // Read and display CSV data
    }
}
