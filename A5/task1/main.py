from App import BronzeApp, SilverApp, GoldApp

 #Main uses the app to create documents

bronze = BronzeApp()
silver = SilverApp()
gold = GoldApp()


# Run tests

bronze.new_document("word")
bronze.new_document("pdf")
bronze.new_document("excel")

print("--------------------------")

silver.new_document("word")
silver.new_document("pdf")
silver.new_document("excel")

print("--------------------------")

gold.new_document("word")
gold.new_document("pdf")
gold.new_document("excel")