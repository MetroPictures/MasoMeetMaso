import os, json, logging
from sys import argv, exit
from time import sleep

from core.vars import BASE_DIR
from core.api import MPServerAPI

SUITORS = [
	'Leopold',
	'Job',
	'M',
	'Andre',
	'Sebastian',
	'Edward',
	'Lou',
	'Stephen',
	'JeanJacques',
	'Jesus',
	'Pierre',
	'TE',
	'Sol',
	'Ryan',
	'Timur'	
]

class MasoMeetMaso(MPServerAPI):
	def __init__(self):
		MPServerAPI.__init__(self)
		logging.basicConfig(filename=self.conf['d_files']['module']['log'], level=logging.DEBUG)

	def hear_main_menu(self):
		choice = self.prompt(os.path.join("prompts", "1_MasoMenu.wav"), release_keys=range(len(SUITORS) + 1))
		return self.play_suitor_menu(SUITORS[choice])

	def play_suitor_menu(self, suitor):
		choice = self.prompt(os.path.join("prompts", "Menu-%s.wav" % suitor), release_keys=[0,1])
		
		if choice == 0:
			return self.say(os.path.join("prompts", "End-%s.wav" % suitor))

		return self.hear_main_menu()

	def map_key_to_tone(self, key):
		return 2

	def run_script(self):
		super(MasoMeetMaso, self).run_script()
		self.hear_main_menu()

if __name__ == "__main__":
	res = False
	mmm = MasoMeetMaso()

	if argv[1] in ['--stop', '--restart']:
		res = mmm.stop()
		sleep(5)

	if argv[1] in ['--start', '--restart']:
		res = mmm.start()

	exit(0 if res else -1)