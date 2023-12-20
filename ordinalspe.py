import pefile
import sys

def find_ordinal(dll_path, function_name):
    try:
        pe = pefile.PE(dll_path)
        for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            if exp.name.decode() == function_name:
                return exp.ordinal
    except Exception as e:
        print(f"Erro: {e}")
    return None

def main():
    if len(sys.argv) != 3:
        print("Uso: python script.py [caminho_da_dll] [nome_da_função]")
        sys.exit(1)

    dll_path = sys.argv[1]
    function_name = sys.argv[2]

    ordinal = find_ordinal(dll_path, function_name)
    if ordinal is not None:
        print(f"Função '{function_name}' tem ordinal: {ordinal} (Decimal)")
    else:
        print(f"Função '{function_name}' não encontrada.")

if __name__ == "__main__":
    main()
