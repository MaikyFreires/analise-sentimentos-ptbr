# Sprint 3 - MVP API REST (Analise de Sentimentos)

## Objetivo do MVP
Entregar um MVP academico funcional para analise de sentimentos em PT-BR como API REST.
O modelo servido usa pipeline TF-IDF + LinearSVC e conecta os resultados das Sprints 1/2 com uma API da Sprint 3.

## Estrutura do projeto
```text
app/
  main.py
  schemas.py
  services/
    model_loader.py
    predictor.py
models/
  sentiment_pipeline.joblib
scripts/
  export_model.py
  test_api.py
requirements.txt
README.md
```

## Como instalar (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Como gerar o modelo
```powershell
python scripts/export_model.py
```
Saida esperada (exemplo):
```text
Model exported successfully to: C:\...\models\sentiment_pipeline.joblib
```

## Como rodar a API
```powershell
uvicorn app.main:app --reload
```

Endpoints:
- `GET /health` -> `{"status":"ok"}`
- `POST /predict` -> recebe JSON `{"text":"..."}`

Swagger:
- `http://127.0.0.1:8000/docs`

## Como testar
### Script Python
Com a API rodando em outro terminal:
```powershell
python scripts/test_api.py
```

### Exemplo curl
```powershell
curl -X POST "http://127.0.0.1:8000/predict" ^
  -H "Content-Type: application/json" ^
  -d "{\"text\":\"Gostei muito do servico\"}"
```

## Exemplos de request/response
Request:
```json
{
  "text": "Atendimento rapido e produto excelente"
}
```

Response (exemplo):
```json
{
  "label": 1,
  "label_name": "positivo",
  "input_text": "Atendimento rapido e produto excelente"
}
```

Response para validacao (texto vazio/curto):
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "text"],
      "msg": "String should have at least 3 characters",
      "input": "",
      "ctx": {"min_length": 3}
    }
  ]
}
```

## Evidencias para o relatorio
Tirar prints dos itens abaixo:
- Planejamento: board no Trello/Notion com tarefas da Sprint 3 (REQ-10, REQ-11, REQ-12).
- Execucao REQ-10: terminal com `uvicorn app.main:app --reload`, tela do Swagger `/docs`, e trechos do codigo da API (`app/main.py`).
- Execucao REQ-11: execucao de `python scripts/test_api.py` mostrando respostas JSON de 3 chamadas.
- Execucao REQ-12: `README.md` aberto com instrucoes e exemplos.
- Resultados: evidencia de conexao Sprint 1/2/3 (modelo treinado e exportado na Sprint 3, servindo predicoes via API).
- Progresso: breve comparacao da evolucao do projeto (EDA -> modelagem -> servico REST).

## Fluxo rapido (resumo)
1. Criar/ativar venv e instalar dependencias.
2. Gerar o pipeline com `python scripts/export_model.py`.
3. Subir API com `uvicorn app.main:app --reload`.
4. Testar com `python scripts/test_api.py` e/ou curl.
