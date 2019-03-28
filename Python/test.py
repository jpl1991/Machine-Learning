def calculateProfit(n, earning, cost, e):
	money = 0
	for i in range(n):
		if(i==n-1):
			money += e*earning[i]
			return money
		if(earning[i]>cost[i]):
			money += e*earning[i]
			money = money-e*cost[i]
	return money

n , earning, cost, e = 4, [1,8,6,7],[1,3,4,1], 5

money = calculateProfit(n, earning, cost,e)

print(money)

import numpy as np