from requests_html import HTMLSession
import pandas as pd

def CrawlIDProducts():
    session = HTMLSession()
    keyword = input("Keyword: ").replace(" ", "+")    #keyword = products keyword
    quantity = int(input("Number of Products: ")) 
    limit = 100   #limit = products per page
    limit_page = (quantity // limit) + 1
    URL_ID = "https://tiki.vn/api/v2/products?limit={limit}&q={keyword}&page{page}"
    #URL_ID = API product ID
    url_product = "https://tiki.vn/product-p{ID}.html?spid={spid}"
    index = 0
    product_list = {
            "Index":                [],
            "Product_id":           [],
            "Spid":                 [],
            "Name" :                [],
            "URL":                  [],
            "Seller":               [],
            "Price":                [],
            "Original Price":       [],
            "Discout":              [],
            "Discout Rate":         [],
            "Rating":               [],
            "Reviews":              [],
                    } 

    for i in range(1,limit_page):
        data = session.get(URL_ID.format(limit=limit, keyword=keyword, page=i)).json()
        print("Crawling page: ",i)
        print(URL_ID.format(limit=limit, keyword=keyword, page=i))
        for product in data["data"]:
            try:
                product_list["Index"].append(index)
            except:  
                product_list["Index"].append(" ")
                
            try:
                product_list["Product_id"].append(product["id"])
            except:
                product_list["Product_id"].append(" ")
                
            try:
                product_list["Spid"].append(product["seller_product_id"])
            except:
                product_list["Spid"].append(" ")
                
            try:
                product_list["Name"].append(product["name"])
            except:        
                product_list["Name"].append(" ")
                                                            
            try:
                product_list["URL"].append(url_product.format(ID=product["id"],spid=product["seller_product_id"]))
            except:
                product_list["URL"].append(" ")
                                                            
            
            try:
                product_list["Seller"].append(product["seller_name"])                                            
            except:
                product_list["Seller"].append(" ")
                
            try:
                product_list["Price"].append(product["price"])                                            
            except:
                product_list["Price"].append(" ")
            
            try:
                product_list["Original Price"].append(product["original_price"])                                            
            except:
                product_list["Original Price"].append(" ")
                    
            try:
                product_list["Discout"].append(product["discount"])                                           
            except:
                product_list["Discout"].append(" ")
                
            try:
                product_list["Discout Rate"].append(product["discount_rate"])                                           
            except:
                product_list["Discout Rate"].append(" ")           
                
            try:
                product_list["Rating"].append(product["rating_average"])                                            
            except:
                product_list["Rating"].append(" ")
                                                            
            try:
                product_list["Reviews"].append(product["review_count"])                                            
            except:
                product_list["Reviews"].append(" ")
                                              
            index += 1                                                
            if index % limit == 0 or index >= quantity-1:
                break
    print("Crawled: ",index+1)
    return product_list

def SaveData(data, filename):
    df_data = pd.DataFrame(data)
    df_data.to_csv(filename, encoding='utf-8', index=False)

product_list = CrawlIDProducts()
SaveData(product_list, input("Filename: "))