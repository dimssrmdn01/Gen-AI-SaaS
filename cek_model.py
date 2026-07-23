import google.generativeai as genai

genai.configure(api_key = "Kode_Rahasia mwehehe")
print("Daftar Model yang Bisa Dipakai:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
