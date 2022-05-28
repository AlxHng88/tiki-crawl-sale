import os
import pandas as pd
import json

def CrawlSale():
    URL_Sale = "https://tiki.vn/api/v2/widget/deals/collection?page=1&tag_id=best_deals&per_page={page}"
    print(URL_Sale.format(page = 24))
    quantity = int(input("SoLuong: "))
    print(URL_Sale.format(page = quantity))
    data_input = input("Copy All Data: ")
    
    try:
        os.remove("data.txt")
    except:
        print("File does not exist. ")
    jsondata = open("data.txt", "w")
    jsondata.write(data_input)
    jsondata.close()
    
    url_product = "https://tiki.vn/product-p{ID}.html?spid={spid}"
    index = 0
    product_list = {
            "Index":                [],
            "Product_id":           [],
            "Spid":                 [],
            "Name" :                [],
            "URL":                  [],
            "Price":                [],
            "Original Price":       [],
            "Discout":              [],
            "Discout Rate":         [],
            "Rating":               [],
            "Status":               [],
                    }
    data = json.load(open('data.txt'))
    for product in data["data"]:
        try:
            product_list["Index"].append(index)
        except:  
            product_list["Index"].append("null")
                
        try:
            product_list["Product_id"].append(product["product"]["id"])
        except:
            product_list["Product_id"].append("null")
                
        try:
            product_list["Spid"].append(product["product"]["seller_product_id"])
        except:
            product_list["Spid"].append("null")
                
        try:
            product_list["Name"].append(product["name"])
        except:        
            product_list["Name"].append("null")
                                                            
        try:
            product_list["URL"].append(url_product.format(ID=product["product"]["id"],spid=product["product"]["seller_product_id"]))
        except:
            product_list["URL"].append("null")
                                                            
        try:
            product_list["Price"].append(product["special_price"])                                            
        except:
            product_list["Price"].append("null")
            
        try:
            product_list["Original Price"].append(product["product"]["original_price"])                                            
        except:
            product_list["Original Price"].append("null")
                    
        try:
            product_list["Discout"].append(product["product"]["discount"])                                           
        except:
            product_list["Discout"].append("null")
                
        try:
            product_list["Discout Rate"].append(product["discount_percent"])                                           
        except:
            product_list["Discout Rate"].append("null")           
                
        try:
            product_list["Rating"].append(product["product"]["rating_average"])                                            
        except:
            product_list["Rating"].append("null")
                                                            
        try:
            product_list["Status"].append(product["deal_status"])                                            
        except:
            product_list["Status"].append("null")
                                              
        index += 1                                                
        if index >= quantity-1:
            break
                
    return product_list

def SaveData(data, filename):
    df_data = pd.DataFrame(data)
    df_data.to_csv(filename, encoding='utf-8', index=False)
    df_data.head(10)

product_list = CrawlSale()
SaveData(product_list, input("Filename: "))