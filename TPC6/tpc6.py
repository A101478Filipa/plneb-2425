from flask import Flask, request, render_template
import json
import re
app=Flask(__name__)

db_file=open("C:/Users/filip/OneDrive/Ambiente de Trabalho/Universidade/Mestrado/2ºsemestre/Processamento de Linguagem Natural/TPC6/conceitos_.json",encoding="UTF-8") 
db=json.load(db_file)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route('/conceitos')
def conceitos():
    designacoes=sorted(list(db.keys()))
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de conceitos")


@app.route("/conceitos/<designacao>")
def conceito(designacao):
    
    if designacao in db:
        return render_template("conceito.html", designacao=designacao, descricao=db[designacao])
    else :
        return render_template("conceito.html", designacao="Erro", descricao = "Descrição não encontrada")


@app.route('/api/conceitos')
def api_conceitos():
    return db

@app.route('/api/conceitos/<designacao>')
def api_conceito(designacao):

    return {"designacao":designacao, "descricao":db[designacao]}

@app.route("/pesquisar")
def exibir_pesquisa():
    return render_template("pesquisa.html", resultados={}, title="Resultados da Pesquisa")

@app.post("/conceitos")
def adicionar_conceito():
    descricao = request.form.get("descricao")
    designacao = request.form.get("designacao")
    
    db[designacao]= descricao
    f_out=open("conceitos_.json","w", encoding="UTF-8")
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()

    designacoes = sorted(list(db.keys()))
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Conceitos")

@app.post("/pesquisar")
def pesquisarconceitos():
    pesquisa = request.form.get("query")
    opcao = request.form.get("opção")
    resultados = {}
    if not pesquisa:
        return render_template("pesquisa.html", pesquisa=None, resultados=None, title="Pesquisa de Conceitos")

    # re.escape == trata a pesquisa como um texto literal, sem os caracteres especiais 
    if opcao == "Match":
        palavra_regex = rf"\b{re.escape(pesquisa)}\b"  # Palavra exata
    else:
        palavra_regex = re.escape(pesquisa)  # Qualquer parte da palavra

    for designacao, descricao in db.items():
        if re.search(palavra_regex, designacao, re.IGNORECASE) or re.search(palavra_regex, descricao, re.IGNORECASE):
            resultados[designacao] = descricao

    # Destacar e criar hiperligação nas ocorrências encontradas
    
    def destacar_texto(texto):
        return re.sub(
            palavra_regex, 
            rf'<a href="/conceitos/{designacao}" class="text-decoration-none text-warning"><u>\g<0></u></a>', 
            texto, 
            flags=re.IGNORECASE
        )
        
    resultados_negrito = {}
    for designacao, descricao in resultados.items():
        resultados_negrito[destacar_texto(designacao)] = destacar_texto(descricao)

    return render_template("pesquisa.html", pesquisa=pesquisa, resultados=resultados_negrito, title="Pesquisa de Conceitos")
    
    

@app.post("/api/conceitos")
def adicionar_conceitoapi():
    data=request.get_json()
    db[data["designacao"]]=data["descricao"]
    f_out=open("conceitos_.json","w", encoding="UTF-8")
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()

    return data


app.run(host="localhost", port=8080, debug= True)