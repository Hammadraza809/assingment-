#8-3
def make_shirt(size,meesage):
    print("Size of your shirt is "+size+ " and your meesage is " +meesage)
#calling function by positional argument
make_shirt("medium","Hello")
#calling function by keyword argument
make_shirt(meesage="Hello",size="Medium")
#8-14
def cars_info(maufacturer_name,model_no,**Add_info):
    car={}
    car["Manufacturer"]=maufacturer_name
    car["Model Name"]=model_no
    for key, value in Add_info.items():
        car[key]=value
    return car
about_cars=cars_info("Honda","civic",color="silver",gear="Automatatic",engine="1200 hourse power")
print(about_cars)