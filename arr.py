'''
Let us say your expense for every month are listed below,
    January - 2200
    February - 2350
    March - 2600
    April - 2130
    May - 2190

Create a list to store these monthly expenses and using that find out,
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

expense = [
    2200,2350,2600,2130,2190
]

print("In Feb extra expense compare to janurary :",(expense[1] - expense[0]))
print("First Three Months Expense :",(sum(expense[0:3])))
try:
    print("Is 2000 dollors spend in any month :",("Yes" if expense.index(2000) != -1 else "No"))
except:
    print("No")
expense.append(1980)
print("Add June Month expense :",(expense[-1]))
print("Get Refend on an Item on april expense :",(expense[3]+200))

'''
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
'''

heros=['spider man','thor','hulk','iron man','captain america']
print("Length of the list :",len(heros))
heros.append("Black Panther")
print("Add Black Panther to the end of the list :",(heros))
hulk_pos = heros.index("hulk")
heros.pop()
heros.insert(hulk_pos+1,"Black Panther")
print("Add Black Panther After Hulk :",(heros))
heros[1:3]=["Dr. Strange"]
print("Remove thor and hulk :",(heros))
print("sort heros in alphabet order :",(sorted(heros)))

'''
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''

odd_numbers = []
max_number = int(input("Enter Max Number :"))
for num in range(1,max_number+1):
    odd_numbers.append(num) if num % 2 != 0 else ""
print(odd_numbers)