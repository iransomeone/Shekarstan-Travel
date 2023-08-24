print("سلام.لطفا در ابتدا تعداد مناطق و تعداد سفرها  را وارد کنید.سپس نرخ سفرهای بین مناطق را وارد کنید.در آخر مبدا و مقصد سفرهایی که میخواهید هزینه اشان محاسبه شود را وارد کنید.دقت کنید که ورودی هایی که در هر خط وارد میکنید باید با یک اسپیس از هم جدا شوند. ")
print("باید تعداد مناطق بین 2 تا 10،تعداد سفرها بین 1 تا 20،هزینه هر سفر بین 1 تا 1000،مسیرهای ورودی بیه 1 تا تعداد مناطق باشند.مبدا و مقصد سفرها نمیتوانند یک عدد باشند.")
#وارد کردن تعداد منطقه و سفر

r=0
while r in range(0,1):
    NoM=str.split(input("Please enter number of zones and trips:")," ")
    N, M =int(NoM[0]),int(NoM[1])
    if 2<=N<=10 and 1<=M<=20:
        r+=1
        break
    else:
        print("تعداد مناطق باید از 2 تا 10 و تعداد سفرها باید از 1 تا 20 باشد")
    

#وارد کردن هزینه سفر از هر منطقه مشخص به منطقه دیگر(نرخ)

cost={}

for satr in range(1,N+1):
    cost_per_trip=str.split(input(f"from zone {satr}:")," ")
    cost_per_trip=map(int,cost_per_trip)
    cost_per_trip=list(cost_per_trip)
    cost.update({f"Zone{satr}":cost_per_trip})
    
print("هزینه ثابت منطقه به منطقه:",cost)

#وارد کردن مسیرسفرهای انجام شده

location={}    

for khat in range(1,M+1):
    loc=str.split(input(f"Axy{khat}")," ")
    loc=map(int,loc)
    loc=list(loc)
    location.update({f"masir{khat}":loc})
    
print ("مبدا و مقصد سفر به سفر:",location)

#محاسبه مجموع هزینه ها
s=1
Total_cost=0
while s < M+1:
    a=location[f"masir{s}"]
    print("The Origin & Destination being calculated:",a)
    a1,a2=a[0],a[1]
    b=cost[f"Zone{a1}"]
    print("Costs from the certain origin:",b)
    c=b[a2-1]
    print("Cost of the certain trip:",c)
    Total_cost+=c
    s=s+1
    
print("مجموعه هزینه پرداخت شده",Total_cost)