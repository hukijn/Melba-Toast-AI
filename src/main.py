import melbaToast
melba = melbaToast.Melba(modelPath="openhermes-2-mistral-7b.Q4_K_M.gguf",
                         databasepath="db",
                         logPath="db/0.txt") # Backup Path is optional

while True:
    userinput = input('->')
    response = melba.getMelbaResponse(userinput, "username") # message - syspromptsetting - username