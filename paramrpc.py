import argparse
import re

def add_fuzz_to_parameters(url):
    return re.sub(r'=(.*?)(?=&|$)', r'=FUZZ', url)

def process_file(file_path):
    if file_path:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        modified_lines = [add_fuzz_to_parameters(line.strip()) for line in lines]
        return modified_lines
    else:
        return []

def main():
    parser = argparse.ArgumentParser(description='Script para adicionar FUZZ nos URLs.')
    parser.add_argument('-f', '--file', required=False, help='Caminho para o arquivo contendo as URLs.')
    parser.add_argument('-s', '--silent', action='store_true', help='Não imprimir as URLs modificadas no terminal.')
    parser.add_argument('-o', '--output', help='Caminho para o arquivo de saída para salvar as URLs modificadas.')
    
    args = parser.parse_args()

    file_path = args.file

    try:
        modified_lines = process_file(file_path)

        if args.output:
            with open(args.output, 'w') as output_file:
                for modified_line in modified_lines:
                    output_file.write(f"{modified_line}\n")
        elif not args.silent:
            for modified_line in modified_lines:
                print(modified_line)

    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")

if __name__ == "__main__":
    main()
