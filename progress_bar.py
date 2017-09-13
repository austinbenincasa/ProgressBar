import sys
import time


class ProgressBar:
    def __init__(self, count=0, bar_size=None):
        self.progress_bar_size = bar_size
        self.process_count = count
        self.processed_count = 0
        self._start_progress()

    def _start_progress(self):
        '''
        Called by the init function to create the progress bar
        '''
        if self.progress_bar_size is not None and bar_size > 2:
            self.progress_bar_size -= 2
        else:
            self.progress_bar_size = 98
        sys.stdout.write("\r[")
        sys.stdout.write("-" * self.progress_bar_size)
        sys.stdout.write("] 00.00%")
           
    def progress(self):
        '''
        Function the user will call to progress the 
        progress bar
        '''
        self.processed_count += 1
        res = self.calc_percentage()
        self.print_progress(res[0], res[1])        

    def _calc_percentage(self):
        '''
        Calculates the percentage of processing done
        and number of '#' to print given the percentage
        '''
        if self.processed_count == 0:
            return 0
        else:
            per = (self.processed_count / self.process_count)
            count = (self.progress_bar_size * per)
            return (count, (per * 100))

    def _print_progress(self, count, per):
        '''
        Prints the given progress to the console 
        '''
        sys.stdout.flush()
        sys.stdout.write("\r[")
        sys.stdout.write("#" * int(round(count)))
        sys.stdout.write("-" * (self.progress_bar_size - int(round(count))))
        sys.stdout.write("] " + str("%.2f" % per) + "%")
        if per == 100.00:
            print("\n")
