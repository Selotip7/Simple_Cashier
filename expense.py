def add_expense(expense,items):
    choice='y'
   
    while(choice!='n'):
        no=int(input("Masukkan pilihan"))
        if no in items:
            # no1=1
            # item1="Pangsit"
            items[no]["amount"]+=1;
            if no==1:
                items[no]["price"]+=5000;
            else:
                items[no]["price"]+=7000;    
                
        else :
            print("Pilih sesuai menu");
        
        choice = input("Tambah lagi? (y/n): ").strip().lower()
    expense.clear()
    for no, data in items.items():
        if data['amount']>0:
            expense.append({"no":no,"Name":data["name"],"Amount":data["amount"],"price":data['price'],"price_stat":data["price_sta"]})

def total_out(expenses):
     return sum(map(lambda expense: expense['price'], expenses))   


def print_expense(expense):
    print("\nDaftar Pengeluaran:")
    print("=" * 40)
    print(f"{'Nama':10} | {'Qty':3} x {'Harga':6} = {'Total':8}")
    print("-" * 40)

    for exp in expense:
        print(f"{exp['Name']:10} | {exp['Amount']:3} x {exp['price_stat']:6} = {exp['price']:8}")

    print("=" * 40)
    print(f"{'TOTAL':10} | {'':3}   {'':6} = {total_out(expense):8}")

def main():
    expense=[]
    items={
        1:{
            "no":1,
            "name":'Pangsit',
            "amount":0,
            "price_sta":5000,
            "price":0

        },
        2:{
            "no":2,
            "name":'Bihun',
            "amount":0,
            "price_sta":7000,
            "price":0
        }
    }
    pil=''
    while(pil!='n'):
        if pil=='1':
            print('ldd')
            add_expense(expense,items)
            
        elif pil=='2':
            print_expense(expense)
            print("\nTotal : ",total_out(expense))
        pil=input("Pilih")

main()