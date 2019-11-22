import csv
import matplotlib.pyplot as plt

# pie chart for men's hockey medal colors (gold, silver, bronze)
# arrays for each color

golds = []
silvers = []
bronzes = []

categories = []

with open('menshockey.csv') as csvfile:
		reader = csv.reader(csvfile)

		line_count = 0

		for row in reader:
			if line_count is 0:
				#parse that first row of text data out of the file
				categories.append(row)
				line_count += 1
			else:
				if row [7] == "Gold":
					print("won gold!")
					golds.append(row[7])

				elif row [7] == "Silver":
					print("won silver!")
					silvers.append(row[7])

				if row [7] == "Bronze":
					print("won bronze!")
					bronzes.append(row[7])

					line_count += 1

print("gold medals: ", len(golds))
print("silver medals: ", len(silvers))
print("bronze medals: ", len(bronzes))

# plot a pie chart!
labels = ("Gold", "Silver", "Bronze")
#Sizes are how many and how large t he slices of the pie chart will be
sizes = [len(golds), len(silvers), len(bronzes)]
colors = ['gold', 'silver', 'darkgoldenrod']
explode = (0.1, 0, 0)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Medals for Men's Hockey")
plt.xlabel("Medals Since 1924")
plt.show()