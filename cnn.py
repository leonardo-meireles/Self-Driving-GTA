"""
RESUMO CNN

→ imgA : representa uma imagem que será convolucionada

    -1 -1 -1 -1 -1 -1 -1 -1 -1
    -1  1 -1 -1 -1 -1 -1  1 -1
    -1 -1  1 -1 -1 -1  1 -1 -1
    -1 -1 -1  1 -1  1 -1 -1 -1
    -1 -1 -1 -1  1 -1 -1 -1 -1
    -1 -1 -1  1 -1  1 -1 -1 -1
    -1 -1  1 -1 -1 -1  1 -1 -1
    -1  1 -1 -1 -1 -1 -1  1 -1
    -1 -1 -1 -1 -1 -1 -1 -1 -1

→ imgB : parte de uma imagem para realizar a convolução

     1 -1 -1
    -1  1 -1
    -1 -1  1

→ imgA ⊗ imgB = imgC
    I: conjunto de imagens à serem convolucionadas
    F: conjunto de imagens para realizar a convolução; são
        partes de imagens ∈ I
    
    imgA ∈ I
    imgB ∈ F

    imgA = mxm
    imgB = nxn, n<m
    imgC = mxm

    » Filtering:
        1. Line up the feature and the image patch
        2. Multiply each image pixel by the corresponding feature pixel
        3. Add them up
        4. Divide by the total number of pixel in the feature

        Algoritmo de convolução:
            imgC[i][j] = 1/(n*n) . ⅀ (imgA[i-1][j-1].imgB[(i%n)-1][(j%n)-1])
                (!) não está tratando as bordas

        c[1][1] = 


    S ⊆ F: stack de features para convolução, formando a CONVOLUTION LAYER.

» Pooling:
    1. Pick a window size (usually 2 or 3), no exemplo acima é 3x3
    2. Pick a stride
    3. Walk your window across your filtered images
    4. From each window, take the maximum value

    A técnica de Pooling, basicamente, reduz a imagem (inImg) para uma imagem da saída (outImg)
    com dimensões menores, mantendo as características da convolução.

» Normalization
    → Keep the mach from breaking by tweaking each of the values just a bit
    → Change everything negative to zero
    "ReLUs : Rectified Linear Units
        → ReLU Layer:
        A stack of images becomes a stack of images without negative values

→ Deep Stacking: layers repetidas várias vezes

        -----        1   2   3    1   2   3
        |   |       | | | | | |  | | | | | | 
        |   |  →    | | | | | |  | | | | | |  →  [STACK OF IMAGES]
        |   |       | | | | | |  | | | | | |
        -----
    1. Convolution
    2. ReLU (Normalization Layers)
    3. Pooling 


→ Fully Connected Layer
    Sistema de "votos" para determinar o resultado de um input

» Backpropagation
    → Erro do resultado da fully connected layer é usado para ajustar a rede
    → Na função erro em função do peso, buscar pelo gradiente descendente


"""
