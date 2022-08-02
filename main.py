import pygame
import random
import time

# colors for the project
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#creating the win, there are 750 lines total width a width of 2 so the window is 1500
#it increases by 1 each line, i added a extra 50 so there would be room for the words
win = pygame.display.set_mode((1500,800))
pygame.display.set_caption('Sorting Algorithms')

#for the font of the text on screen
pygame.init()
font = pygame.font.Font(None, 40)

#making each label to put on the win
selection_text = font.render('Selection Sort: W', True, WHITE)
quick_text = font.render('Quick Sort: E', True, WHITE)
shuffle_text = font.render('Shuffle: S', True, WHITE)

#spaming might freeze the program rare but i've experienced it
warning_text = font.render('Do not spam buttons', True, WHITE)

#making a list to loop through in the draw function
#the numbers are where they will be put in the win, the values are trial and error until if felt like it looked nice
text = [[selection_text, (20,5)], [quick_text, (280, 5)], [shuffle_text, (490, 5)], [warning_text, (1190, 5)]]

#class for the lines that will be used for the algos
class Line():
	def __init__(self, len, x):
		self.len = len
		self.color = WHITE
		self.x = x

	def draw(self):
		pygame.draw.rect(win, self.color, (self.x, 800 - self.len, 2, self.len))

#making the lines and adding them to the arry that will be used for the algorithms
main_array = []
for i in range(750):
	line = Line(i+1, i*2)
	main_array.append(line)

#draws the win, lines and text it will update the position of the lines since the .x (position) will change in later funcs
def draw():
	win.fill(BLACK)
	for i in main_array:
		i.draw()
	for i in text:
		win.blit(i[0], i[1])
	pygame.display.update()

#changes the position of 2
def exchange(p1, p2):
	main_array[p1].color = main_array[p2].color = RED
	#this draw makes it so you can see the 2 being switched before it is done
	draw()
	#switching the position in the array and changing the position for .x
	main_array[p1], main_array[p2] = main_array[p2], main_array[p1]
	main_array[p1].x, main_array[p2].x = main_array[p2].x, main_array[p1].x
	main_array[p1].color = main_array[p2].color = WHITE
	#running this extra draw makes the program run a little slower so you have more time to see the algo run
	#commenting it out or deleting it doesn't change the programs functionality just makes the animation go faster
	draw()

#used to shuffle the lines 
def shuffle():
	#steps through the main array backwards
	for i in range(len(main_array)-1,0,-1):
		#picks a random line in-between the start and the iteration
		j = random.randint(0,i)
		#exchanges the 2 lines
		exchange(i, j)

def selection_sort():
	#iterate through the array from start to finish
	for i in range(len(main_array)):
		#set i.len to the lowest len and take the index
		lowest = main_array[i].len
		index = i
		#itterate from i to the end of the array
		for j in range(i+1, len(main_array)):
			#find the lowest value
			if main_array[j].len < lowest:
				#save the index of the lowest and save the len as lowest
				index = j
				lowest = main_array[j].len
		#switch index and i
		exchange(index, i)

#apart of quicksort
def partition(low, high):
	lowest = low-1
	for i in range(low,high):
		if main_array[i].len < main_array[high].len:
			lowest += 1
			exchange(lowest, i)

	exchange(high, lowest+1)

	return lowest + 1

def quick_sort(low, high):
	if low < high:
		lo = partition(low, high)

		quick_sort(low, lo-1)
		quick_sort(lo+1, high)

#this doesn't change how it runs it just makes the all the lines flash green when it is finished
def sort_finished():
	for i in main_array:
		i.color = GREEN
	draw()
	#this is needed so you can see the green
	time.sleep(0.15)
	for i in main_array:
		i.color = WHITE
	draw()

def main():
	run = True
	#it starts sorted so shuffled is set to false
	shuffled = False
	while run:
		draw()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			#shuffle button is S
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s and not shuffled:
					#changes the shuffled value so you cna only sort after running this
					shuffled = True
					shuffle()

			#selection sort set to W
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w and shuffled:
					#changes shuffled to false so you can't sort twice
					shuffled = False
					selection_sort()
					sort_finished()

			#quick sort is E
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_e and shuffled:
					#changes shuffled to false so you can't sort twice
					shuffled = False
					quick_sort(0, len(main_array)-1)
					sort_finished()
			
			pygame.event.get()

#runs it all
main()