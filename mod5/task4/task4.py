from typing import IO
import contextlib
import sys
import traceback


class RedirectOutput:

    def __init__(self, stdout: IO = None, stderr: IO = None):
        self.new_stdout = stdout
        self.new_stderr = stderr

    def __enter__(self):
        if self.new_stdout != None:
            self.old_stdout, sys.stdout = sys.stdout, self.new_stdout
        if self.new_stderr != None:
            self.old_stderr, sys.stderr = sys.stderr, self.new_stderr
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.new_stderr != None:
            sys.stderr.write(traceback.format_exc())
        if self.new_stdout != None:
            sys.stdout = self.old_stdout
            self.new_stdout.close()
        if self.new_stderr != None:
            sys.stderr = self.old_stderr
            self.new_stderr.close()
        return True
