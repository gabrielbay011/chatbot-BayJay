import subprocess
import json

repo_url = "https://github.com/usuario/repositorio.git"

command = [
    "docker", "run", "--rm",
    "sandbox-scraper",  # nome da imagem já criada
    repo_url
]

try:
    result = subprocess.run(command, capture_output=True, text=True, check=True)

    print("Resultado bruto:")
    print(result.stdout)  # esse stdout é o que vem do print(json.dumps(...)) da sandbox

    # exemplo de parsing (caso venha um JSON por linha)
    resultados = []
    for linha in result.stdout.strip().splitlines():
        try:
            resultados.append(json.loads(linha))
        except json.JSONDecodeError as e:
            print("Erro ao decodificar uma linha:", linha)

    print("Dados extraídos:")
    print(json.dumps(resultados, indent=2))

except subprocess.CalledProcessError as e:
    print("Erro ao executar sandbox:")
    print(e.stderr)
