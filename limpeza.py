import os
import shutil
import time
from pathlib import Path
from datetime import datetime

def tamanho_item(caminho:Path) -> int:
    try:
        if caminho.is_file() or caminho.is_symlink():
            return caminho.stat().st_size
        
        total = 0
        for item in caminho.rglob("*"):
            try:
                if item.is_file() or item.is_symlink():
                    total += item.stat().st_size
            except Exception: 
                pass
        return total
    except Exception:
        return 0
    
def formatar_tamanho(bytes_valor: int) -> str:
    mb = bytes_valor / (1024 * 1024)
    if mb >= 1024:
        return f"{mb / 1024:.2f} GB"
    return f"{mb:.2f} MB"

def limpar_pasta(caminho: Path):
    apagados = 0
    erros = 0
    bytes_liberados = 0

    if not caminho.exists():
        return apagados, erros, bytes_liberados
    
    for item in caminho.iterdir():
        try:
            bytes_liberados += tamanho_item(item)

            if item.is_file() or item.is_symlink():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item) 

            apagados += 1

        except Exception:
            erros += 1

    return apagados, erros, bytes_liberados

def executar_limpeza():
    inicio = time.time()

    print("=" * 35)
    print("=== Limpeza rápida do Pc ===")
    print("=" * 35)
    print(f"Data:{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    candidatas = [
        os.environ.get("TEMP"),
        os.environ.get("TMP"),
        r"C:\Windows\Temp",
    ]

    pastas = []
    vistas = set()

    for valor in candidatas:
        if not valor:
            continue
        pasta = Path(valor)
        chave = str(pasta).lower()
        if chave not in vistas:
            vistas.add(chave)
            pastas.append(pasta)

    total_apagados = 0
    total_erros = 0
    total_liberado = 0

    for pasta in pastas:
        print(f"\nLimpando: {pasta}")

        apagados, erros, liberado = limpar_pasta(pasta)

        total_apagados += apagados
        total_erros += erros
        total_liberado += liberado

        print(f"Apagados: {apagados}")
        print(f"Ignorados/Erros: {erros}")
        print(f"Espaço Liberado: {formatar_tamanho(liberado)}") 

        tempo = time.time() - inicio

    relatorio = f"""
================================
RELATÓRIO FINAL
================================
Total apagado: {total_apagados}
Total ignorado: {total_erros}
Espaço liberado: {formatar_tamanho(total_liberado)}
Tempo: {tempo:.2f} segundos 
Status: Finalizado
"""
        
    print(relatorio)

    with open("relatorio_limpeza.log", "a", encoding="utf-8") as log:
        log.write(f"\n{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        log.write(relatorio)