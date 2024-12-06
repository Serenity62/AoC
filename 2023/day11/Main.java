import java.util.ArrayList;
import java.util.stream.Collectors;
import java.util.List;
//import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.io.BufferedReader;
import java.util.stream.Stream;
import java.io.IOException;

public class Main {
    private static ArrayList<String> readFile(String file) {
        ArrayList<String> s = new ArrayList();
        Path path = Path.of(file);
        try (BufferedReader reader = Files.newBufferedReader(path);
                Stream<String> lines = reader.lines();) {
            s = lines.collect(Collectors.toCollection(ArrayList::new));
        } catch(IOException e) {
            e.printStackTrace();
        }
        return s;
    }

    public static void main(String[] args) {
        String file = "test";

        if(args.length > 0) {
            file = args[0];
        }

        var input = readFile(file);

        System.out.println(input);
    }
}
