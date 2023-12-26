import sys
import pytest

tags = "testui"

if __name__ == '__main__':
    sys.exit(pytest.main(["-m", tags, "--capture=tee-sys", "--browser=chrome", "-s", "--html=report/report.html"]))
