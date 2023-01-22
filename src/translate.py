import boto3 

client = boto3.client('translate', region_name = "us-east-1")

text = "ich liebe dich, bruder"

result = client.translate_text(Text=text, SourceLanguageCode="auto",
    TargetLanguageCode="ar")
    
print(result["TranslatedText"])