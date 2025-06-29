cs=[]
def add_con():
	name=input("Enter name:")
	phone=input("Enter phone number:")
	email=input("Enter Email:")
	address=input("Enter Address:")
	cs.append({
	"name":name,
	"phone":phone,
	"email":email,
	"Address":address
	})
	 
	print("Contact Added Successfully...\n")
def view_con():
	if not cs:
		print("No Contact is found..\n")
		return
	print("\n--Contact List--")
	for i,c in enumerate(cs,start=1):
		print(f"{i}.{c['name']}-{c['phone']}")
		print()
def search_con():
	key=input("Enter name or phone number to search:").lower()
	found=False
	for c in cs:
		if key in c['name'].lower() or key in c['phone']:
			print("\nContact Found:")
			print(f"Name:{c['name']}")
			print(f"Phone:{c['phone']}")
			print(f"Email:{c['email']}")
			print(f"Address:{c['address']}\n")
			found=True
		if not found:
			print("No matching Contact is found..\n")
def updated_con():
	key=input("Enter name or phone number to update:").lower()
	for c in cs:
		if key in c['name'].lower() or key in c['phone']:
			print("Contact is found:Enter details.")
			c['name']=input("new Store name:")
			c['phone']=input("New phone Number:")
			c['email']=input("New Email:")
			c['address']=input("New Address:")
			print("Contact updated Successfully...")
			return
			print("Contact is not found...")
def delete_con():
	key=input("Enter name or phone to delete:").lower()
	for c in cs:
		if key in c['name'].lower() or key in c['phone']:
			cs.remove(c)
			print("Contact delete Successfully...")
			return
			print("Contact is not found..")
def main_me():
	while True:
		print("\nContact Book Menu:")
		print("1.Add Contact")
		print("2.View Contact")
		print("3.search Contact")
		print("4.update Contact")
		print("5.delete Contact")
		print("6.Exit")
		ch=input("Enter your Choice=")
		if ch=='1':
			add_con()
		elif ch=='2':
			view_con()
		elif ch=='3':
			search_con()
		elif ch=='4':
			updated_con()
		elif ch=='5':
			delete_con()
		elif ch=='6':
			print("Exiting Contact Book...")
			break
		else:
			print("Invalid choice..")
main_me()