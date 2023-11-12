import melbaToast
melba = melbaToast.Melba(modelPath="openhermes-2-mistral-7b.Q4_K_M.gguf",
                         databasepath="db",
                         logPath="db/0.txt")

input = 'who are you'#input('->')
response = melba.getMelbaResponse(input, '0', "username") # message - syspromptsetting - username
print(f'->{response}')