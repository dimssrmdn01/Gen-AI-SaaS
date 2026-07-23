import google.generativeai as genai

# Masukkan API Key kamu di sini
genai.configure(api_key = "KODE_RAHASIA")

print("Daftar Model yang Bisa Dipakai:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)