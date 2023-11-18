import melbaToast
melba = melbaToast.Melba(modelPath="openhermes-2-mistral-7b.Q4_K_M.gguf",
                         databasepath="db",
                         logPath="db/0.txt") # Backup Path is optional

while True:
    input = input('->')
    response = melba.getMelbaResponse(input, "username") # message - syspromptsetting - username