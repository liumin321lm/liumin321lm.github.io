import unittest
from HTMLTestRunner import HTMLTestRunner
import time

test_dir='./'

discover=unittest.defaultTestLoader.discover(test_dir,pattern="test.py")
if __name__ == '__main__':
    report_dir='./testreport'

    now=time.strftime("%Y-%m-%d %H_%M_%S")
    report_name=report_dir+'/'+now+'result.html'
    print("start write report..")
    with open(report_name,'wb') as f:
        runner=HTMLTestRunner(stream=f,title="Test Report",description="localhost login test")
        runner.run(discover)
        f.close()