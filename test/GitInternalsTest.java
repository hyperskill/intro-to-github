import org.hyperskill.hstest.stage.StageTest;
import org.hyperskill.hstest.testcase.CheckResult;
import org.hyperskill.hstest.testcase.TestCase;

import java.util.Arrays;
import java.util.List;

// version 1.2
public class GitInternalsTest extends StageTest<List<String>> {

    private final String gitOnePath = "test/gitone/";

    @Override
    public List<TestCase<List<String>>> generate() {
        return Arrays.asList(
                new TestCase<List<String>>()
                        .setInput(
                                gitOnePath + "objects/61/8383db6d7ee3bd2e97b871205f113b6a3ba854\n")
                        .setAttach(Arrays.asList(
                                "Enter git object location:",
                                "blob 14",
                                "Hello world! ")),
                new TestCase<List<String>>()
                        .setInput(
                                gitOnePath + "objects/a8/7a4a0e9fcf5a8a091c54909b674ac2a051f5e8\n")
                        .setAttach(Arrays.asList(
                                "Enter git object location:",
                                "blob 24",
                                "first line",
                                "second line ")),
                new TestCase<List<String>>()
                        .setInput(
                                gitOnePath + "objects/4a/8abe7b618ddf9c55adbea359ce891775794a61\n")
                        .setAttach(Arrays.asList(
                                "Enter git object location:",
                                "blob 35",
                                "first line",
                                "second line",
                                "third line "))
        );
    }

    @Override
    public CheckResult check(String reply, List<String> expectedOutput) {
        List<String> lines = Arrays.asList(reply.split("(\\r\\n|\\r|\\n)"));

        if (lines.size() != expectedOutput.size()) {
            return CheckResult.wrong(String.format(
                    "Number of lines in your output (%d) does not match expected value(%d)",
                    lines.size(), expectedOutput.size()));
        }

        for (int i = 0; i < lines.size(); i++) {
            if (!lines.get(i).equals(expectedOutput.get(i))) {
                return CheckResult.wrong(String.format(
                        "Output text at line (%d) (%s) does not match expected (%s)",
                        i, lines.get(i), expectedOutput.get(i)));
            }
        }


        return CheckResult.correct();
    }
}
