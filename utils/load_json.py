"""Arquivo de funções de utilidade"""
import json

def load_json(file_name: str) -> dict[str, str]:
    """ Lê um arquivo .json e retorna um dicionário equivalente """
    f = open(file_name, "r", encoding="utf-8")
    cmd_map = json.load(f)
    f.close()
    return cmd_map
