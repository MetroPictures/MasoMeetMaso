import os, json, logging
from random import sample, uniform, randint
from sys import argv, exit
from time import sleep

from core.vars import BASE_DIR
from core.api import MPServerAPI

SUITORS = range(16)

class MasoMeetMaso(MPServerAPI):
	def __init__(self):
		MPServerAPI.__init__(self)
		logging.basicConfig(filename=self.conf['d_files']['module']['log'], level=logging.DEBUG)

	def hear_main_menu(self):
		randos = list(str(uniform(1, 100)).split('.')[1])

		guest_number = sample(randos, randint(2, len(randos) - 1))
		suitors = sample(SUITORS, randint(4, len(SUITORS)/2))

		if not self.say(os.path.join(self.conf['media_dir'], "prompts", "welcome_guest.wav")) and \
			self.say_sequence(guest_number) and \
			self.say(os.path.join(self.conf['media_dir'], "prompts", "men_are_currently_waiting.wav")):
			
		return self.hear_suitor_choices(suitors)

	def hear_suitor_choices(self, suitors):
		suitor = self.prompt(os.path.join(self.conf['media_dir'], "prompts", "nada.wav"), \
			release_keys=range(len(suitors) + 3))

		for i, suitor in enumerate(suitors):
			if not self.say(os.path.join(self.conf['media_dir'], "prompts", "to_hear_type_%d.wav" % randint(0, 1))) and \
				self.say(os.path.join(self.conf['media_dir'], "prompts", "suitor_name_%d.wav" % suitors[i])) and \
				self.say(os.path.join(self.conf['media_dir'], "prompts", "numeral_%d.wav" % i)):
				return False

		return hear_suitor_message(suitor, suitors)

	def hear_suitor_message(self, suitor, suitors):
		if not self.say(os.path.join(self.conf['media_dir'], "prompts", "suitor_message_%d" % suitor)):
			return False

		choice = self.prompt(os.path.join(self.conf['media_dir'], "prompts", "suitor_choice_%d.wav" % suitor), \
			release_keys=[3, 4])
		
		if choice == 3:
			return self.connect_to_suitor(choice)
		else:
			return self.hear_suitor_choices(suitors)

	def connect_to_suitor(self, choice):
		return False

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