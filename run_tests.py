import sys
import subprocess

from ai.failure_analyzer import analyze_failure


def run_tests(test_path):

    result = subprocess.run(
        [
            "pytest",
            test_path,
            "--html=reports/report.html",
            "--self-contained-html"
        ],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:

        print("\n" + "=" * 60)
        print("🤖 AI FAILURE ANALYSIS")
        print("=" * 60)

        failure_output = result.stdout + result.stderr

        analysis = analyze_failure(failure_output)

        print(analysis)

    else:
        print("\n✅ All tests passed!")


if __name__ == "__main__":

    test_path = sys.argv[1] if len(sys.argv) > 1 else "tests"

    run_tests(test_path)