import aedsdk
import time

class Mickey(aedsdk.Paradigm):
	
	def __init__(self):
		aedsdk.Paradigm.__init__(self)
		self.sequence = []
		self.sequence_point = 0
		
		self.time_passed_experiment = 0.0
		self.time_passed_trial = 0.0

	class LeverPress(aedsdk.Action):
		def __init__(self):
			pass
		
		def detect(self):
			print 'waiting for lever press'
		
		def respond(self):
			print 'do what on lever press'
	
	class Reward(aedsdk.Event):
		def __init__(self):
			self.valve = 0

		def perform(self):
			print 'reward delivered'
		
	class Restart(aedsdk.Event):
		def __init__(self):
			pass
		
		def perform(self):
			self.sequence_point = 0
			print 'restart trial'
	
	class Wait(aedsdk.Interval):   
		def __init__(self, duration):
			aedsdk.Interval.__init__(self, duration)
			
		def on_LeverPress(self):
			print 'lever pressed'
			for act in self.events_LeverPress:
				act()
			
	class Tone(aedsdk.Interval):
		def __init__(self,duration):
			aedsdk.Interval.__init__(self, duration)
		
		def at_begin(self):
			aedsdk.Interval.at_begin(self)
			print 'tone play start'
		
		def at_end(self):
			aedsdk.Interval.at_end(self)
			print 'tone play end'
	
	class Present(aedsdk.Interval):
		def __init__(self,duration):
			aedsdk.lofty.Interval.__init__(self, duration)
		
		def on_LeverPress(self):
			print 'give reward :)'
			for act in self.events_LeverPress:
				act()
	
	class Refrain(aedsdk.Interval):
		def __init__(self,duration):
			aedsdk.lofty.Interval.__init__(self, duration)
			self.reward = True
		
		def at_end(self):
			if self.reward:
				aedsdk.Interval.at_end(self)
				print 'reward given'
			else:
				print 'reward not given'
		
		def on_LeverPress(self):
			self.reward = False
			print 'oops pressed lever no reward at the end :('
			for act in self.events_LeverPress:
				act()

	def test(self):
		"""
		self.matte = self.Wait(2.0)
		self.matte.at_begin()
		time.sleep(self.matte.duration)
		self.matte.at_end()
		"""
		#self.print_classes()
		self.bind_action_listeners()
		self.print_classes()
			
mouse = Mickey()
mouse.test()
