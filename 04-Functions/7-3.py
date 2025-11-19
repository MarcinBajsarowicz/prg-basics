def month(n):
    months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    
    
    for i in range(len(months)):
        if (i == n  - 1):
            return months[i]
       

print(month(8))