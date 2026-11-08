import datetime
import platform
import socket
import psutil


def testar_conexao(host="8.8.8.8", porta=53, timeout=3):
    try:
        socket.create_connection((host, porta), timeout=timeout)
        return "Online (conectividade OK)"
    except OSError:
        return "Offline (Sem conexão a internet)"

def gerar_diagnostico():
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sistema = f"{platform.system()} {platform.release()} {platform.version()}"
    memoria = psutil.virtual_memory()
    disco = psutil.disk_usage("/")
    conexao = testar_conexao()


    relatorio = f"""=== RELATÓRIO DE DIAGNÓSTICO DO SISTEMA ===
Data/Hora: {agora}
Sistema Operacional: {sistema}
--------------------------------------------------
MEMÓRIA RAM:
  - Total: {memoria.total / (1024**3):.2f} GB
  - Usada: {memoria.used / (1024**3):.2f} GB ({memoria.percent}%)
--------------------------------------------------
ESPAÇO EM DISCO (Raiz /):
  - Total: {disco.total / (1024**3):.2f} GB
  - Livre: {disco.free / (1024**3):.2f} GB ({disco.percent}% usado)
--------------------------------------------------
REDE:
  - Status: {conexao}
==================================================
"""

    print(relatorio)

    nome_arquivo = "diagnostico_sistema.log"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(relatorio)

    print(f"[+] Log de diagnostico  gerado com sucesso em '{nome_arquivo}'!")

    input("\nPressione ENTER para fechar a janela...")

if __name__ == "__main__":
    gerar_diagnostico()