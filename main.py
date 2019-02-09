import time, glob
import matplotlib.pyplot as plt
def maiorValor(path, t):
    maior = max(map(lambda l: int(l), open(path)))
    return str(maior), str((time.time()-t)*1000)
    


if __name__ == "__main__":
    datasets = []
    tempos = []
    for file in glob.glob("*.csv"):
        with open("resposta-"+file.replace("csv", "txt"), "w") as f:
            result = maiorValor(file, time.time())
            f.write("\n".join(result))
            datasets.append(file)
            tempos.append(result[1])
    
    plt.plot(datasets, tempos)
    plt.xlabel('Dataset')
    plt.ylabel("Tempo")
    plt.savefig("desempenho.png")
    plt.show()
    
            








