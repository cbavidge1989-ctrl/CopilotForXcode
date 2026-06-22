import threading
import time

def createAndRunTask(name: str, delay: float, action):
	"""Create a background task that waits `delay` seconds then runs `action`.

	Returns the Thread object.
	"""

	def wrapper():
		time.sleep(delay)
		try:
			action()
		except Exception as e:
			print(f"Task '{name}' raised: {e}")

	t = threading.Thread(target=wrapper, name=name, daemon=True)
	t.start()
	return t

if __name__ == '__main__':
	# example usage
	def my_action():
		print('Task executed')

	task = createAndRunTask('example', 1.0, my_action)
	task.join(timeout=2.0)
