
def cost_of_sales(oi, p, ci):
    oi = input("Enter Opening Inventories: ")
    p = input("Enter Purchases: ")
    ci = input("Enter Closing Inventories: ")

    result_cos = oi + p - ci

    if result_cos < 0:
        result_cos = -result_cos
        
    print result_cos
    
cost_of_sales(0, 0, 0)

