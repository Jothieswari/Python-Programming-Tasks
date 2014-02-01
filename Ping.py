import subprocess
def main():
    class Command(object):
      def _init_(self,command):
            self.command = command
	def run(self, shell= True):
            process = subprocess.Popen(self.command,shell = 

shell,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	    self.pid = process.pid
	    self.output, self.error = process.communicate()
	    self.failed = process.returncode
	    return self
	def returncode(self):
            return self.failed
    com = Command("ping 192.168.5.183").run()
    print com.output
    print com.error
    print com.failed
if __name__ == '__main__':
    main()
