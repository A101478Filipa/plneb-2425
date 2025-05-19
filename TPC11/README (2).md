# 🔎 Extrator de Artigos - Revista SPMI

Script em Python concebido para recolher e organizar dados científicos publicados na revista da Sociedade Portuguesa de Medicina Interna ([revista.spmi.pt](https://revista.spmi.pt)). O conteúdo recolhido é exportado para um ficheiro `.json` devidamente estruturado.

---

## O que faz este script?

Este programa automatiza a recolha de informações dos artigos disponíveis online na revista da SPMI. É especialmente útil para investigadores, profissionais de saúde e bibliotecários que pretendam manter uma base de dados local com os metadados das publicações.

### Dados recolhidos por artigo:

- Título do artigo  
- Lista de autores  
- Resumo (abstract)  
- DOI (caso exista)  
- Palavras-chave  
- URL directa para o artigo

Além disso, os dados são agrupados por:

- Edição (com título e link correspondente)
- Secção (nome e artigos incluídos)

---

## Estrutura do Ficheiro JSON

O resultado final é um ficheiro `.json` com a seguinte organização:

```json
{
  "titulo_arquivo": "Nome curto da edição",
  "titulo_completo": "Nome completo da edição",
  "url_edicao": "Endereço da edição no site",
  "secoes": [
    {
      "nome_secao": "Designação da secção",
      "artigos": [
        {
          "titulo": "Título completo do artigo",
          "autores": "Autores separados por vírgulas",
          "url": "Endereço do artigo",
          "resumo": "Texto do resumo",
          "doi": "Identificador DOI (se existir)",
          "palavras_chave": "Lista de palavras-chave"
        }
      ]
    }
  ]
}
```

---

## Requisitos

Certifica-te de que tens o ambiente configurado com:

- **Python 3.x**

### Bibliotecas necessárias:

```bash
pip install requests beautifulsoup4
```

Outras bibliotecas utilizadas (`json` e `datetime`) já vêm incluídas na biblioteca padrão do Python.

---

## Como personalizar

Podes ajustar o número de páginas a processar modificando o valor da variável `total_paginas` no corpo da função `main()`.

O script está preparado para lidar com lacunas de informação (ex.: ausência de resumo ou DOI), preenchendo automaticamente os campos com um valor predefinido como `"Não disponível"`.

---

## O que aparece no terminal?

Durante a execução, o script mostra mensagens informativas, como:

- Título da edição em análise  
- Secções identificadas e número de artigos por secção  
- Para cada artigo:
  - Título
  - Autores
  - URL
  - Resumo (se presente)
  - DOI (se presente)
  - Palavras-chave (se existirem)

---

## Saída

O ficheiro JSON é guardado com um nome único baseado na data e hora da execução, evitando sobreposição de dados antigos.

Exemplo:  
```bash
revista_spmi_2025-05-19_14-32-10.json
```

---

## Contacto

Para sugestões, melhorias ou relatórios de erros, entra em contacto com o autor do script ou cria um _issue_ no repositório.

---

> Utiliza este script de forma ética e em conformidade com os termos de uso da revista SPMI.
