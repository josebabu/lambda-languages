# lambda-languages

This provides a simple example of performance of different languages in AWS Lambda.
The functions are written in Python, Node.JS, and C#.
Each funtion reads input data and prints them on console.

The performance metrics for each execution is retrieved from AWS CloudWatch Logs.

Procedure:
1. test-call function is triggered.
2. test-call invokes language Lambdas - NodeTest, PyTest, LambdaCsharpTest
3. Cold start test - Language Lambda runs 100 times and creates CloudWatch logs for each execution.
4. loggingoutputtest function monitors CloudWatch logs and retrieves report for each execution.
5. Wait for 5 minutes.
6. Warm test - Language Lambda runs 100 times and creates CloudWatch logs for each execution.
7. loggingoutputtest function monitors CloudWatch logs and retrieves report for each execution.

8.Collect data from cold and warm runs to generate final report.

Observations:
1. Cold Start - Maximum execution time:
	Highest: C# ~4600 ms
	Lowest: Python ~2018 ms
2. Cold Start - Average execution time:
	Highest: C# ~2700 ms
	Lowest: Python ~2002 ms
3. Warmed State- Maximum execution time:
	Highest: C# ~4600 ms
	Lowest: Python ~2050 ms
4. Warmed State - Average execution time:
	Highest: C# ~2125 ms
	Lowest: Python ~2003 ms
5. Spikes noticed in C# execution even during warm execution - possible creation of new containers (similar to cold start)
