from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from services.operadoras_service import carregar_dados_operadoras

router = APIRouter()

@router.get("/", response_model=List[dict])
def listar_operadoras():
    try:
        dados = carregar_dados_operadoras()
        return dados
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/buscar")
def buscar_operadoras(
    registro_ans: Optional[str] = Query(None, description="Filtrar por Registro ANS"),
    cnpj: Optional[str] = Query(None, description="Filtrar por CNPJ"),
    razao_social: Optional[str] = Query(None, description="Filtrar por Razão Social (contém)"),
    nome_fantasia: Optional[str] = Query(None, description="Filtrar por Nome Fantasia (contém)"),
    modalidade: Optional[str] = Query(None, description="Filtrar por Modalidade")
):
    """
    Busca operadoras com filtros opcionais.
    Todos os parâmetros são opcionais e podem ser combinados.
    Para campos textuais (Razão Social, Nome Fantasia), a busca é por CONTÉM (case insensitive).
    """
    try:
        dados = carregar_dados_operadoras()
        resultados = dados
        
        if registro_ans:
            resultados = [op for op in resultados if str(op.get('Registro_ANS', '')).strip() == registro_ans.strip()]
        
        if cnpj:
            resultados = [op for op in resultados if str(op.get('CNPJ', '')).strip() == cnpj.strip()]
        
        if razao_social:
            razao_social_lower = razao_social.lower()
            resultados = [op for op in resultados 
                         if razao_social_lower in str(op.get('Razao_Social', '')).lower()]
        
        if nome_fantasia:
            nome_fantasia_lower = nome_fantasia.lower()
            resultados = [op for op in resultados 
                         if op.get('Nome_Fantasia') and 
                         nome_fantasia_lower in str(op['Nome_Fantasia']).lower()]
        
        if modalidade:
            modalidade_lower = modalidade.lower()
            resultados = [op for op in resultados 
                         if modalidade_lower in str(op.get('Modalidade', '')).lower()]
        
        return {
            "success": True,
            "count": len(resultados),
            "data": resultados
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))