"""
Class object to assist with debugging.

Author: Leong Chang Jie
Date: March 2022
"""
class Debugger(object):
    """
    Debugger class to turn on and off debug output.
    """
    def __init__(self, show_logs=True):
        self.output = show_logs
    
    def show_print(self, value):
        """Show debug output"""
        if self.output:
            print(value)
            return
        return value