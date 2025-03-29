from fastapi import APIRouter, HTTPException, Depends
from typing import List
from services.operadoras_service import carregar_dados_operadoras

router = APIRouter()

@router.get("/", response_model=List[dict])
def listar_operadoras():
    try:
        dados = carregar_dados_operadoras()
        return dados
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{registro_ans}")
def buscar_operadora(registro_ans: str):
    try:
        dados = carregar_dados_operadoras()
        operadora = next((op for op in dados if str(op.get('Registro ANS', '')).strip() == registro_ans.strip()), None)
        
        if not operadora:
            raise HTTPException(status_code=404, detail="Operadora não encontrada")
        return operadora
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))