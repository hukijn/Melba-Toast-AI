import melbaToast
melba = melbaToast.Melba("openhermes-2-mistral-7b.Q4_K_M.gguf",
                         "db",
                         "db/0.txt",
                         "Backup Path") # Backup Path is optional

input = 'who are you'#input('->')
response = melba.getMelbaResponse(input, '0', "username") # message - syspromptsetting - username
print(f'->{response}')