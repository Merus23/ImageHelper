import codes.moveToFolder as mtf
import codes.resize as rsz
import codes.dataAugmentation as da

print("Informe o que você deseja fazer:")
opcao = -1
while(opcao != 0):
    opcao = int(input("\n\n\n1 - Data Augmentation\n2 - Redimensionar imagens\n3 - Mover arquivos de uma pasta para outra\n0 - Sair\n"))
    
    if(opcao == 1):
        augmentation = da.dataAugmentation()
        augmentation.inputs()
        augmentation.execute()

    elif(opcao == 2):
        redimensionar = rsz.Resize()
        redimensionar.inputs()
        redimensionar.ler_imagens()
        redimensionar.redimensionar_imagens()

    elif(opcao == 3):
        mover = mtf.moveToFolder()
        mover.inputs()
        mover.moveFiles()

    elif(opcao == 0):
        print('Saindo...')
        break
