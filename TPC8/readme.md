# 🩺 Extração de Dados - Atlas da Saúde

Este projeto tem como objetivo extrair informações detalhadas sobre doenças a partir do site [Atlas da Saúde](https://www.atlasdasaude.pt/) e armazená-las num ficheiro JSON estruturado.

## 📌 O que o script faz

- Acede a páginas individuais de doenças.
- Extrai informações como:
  - Nome da doença
  - Data de publicação
  - Descrição
  - Causas
  - Sintomas
  - Tratamentos
  - Artigos relacionados
  - Notas adicionais
- Percorre todas as letras do alfabeto para recolher a lista completa de doenças disponíveis no site.
- Guarda tudo num ficheiro `doencas_completo.json`.

## 🛠️ Tecnologias usadas

- `requests` – para fazer requisições HTTP
- `BeautifulSoup` – para analisar o HTML
- `json` – para guardar os dados extraídos

## 📁 Exemplo de saída

```json
{
  "nome": "Diabetes",
  "data_publicacao": "2020-05-12",
  "descricao": "Doença crónica que afeta a forma como o corpo processa o açúcar no sangue...",
  "causas": "Fatores genéticos, sedentarismo, alimentação desequilibrada...",
  "sintomas": "Sede excessiva, cansaço, visão turva...",
  "tratamentos": "Medicação, dieta controlada, exercício físico...",
  "artigos_relacionados": ["link1", "link2"],
  "nota_adicional": "É importante o acompanhamento médico regular."
}
