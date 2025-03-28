-- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU
-- AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?

SELECT 
    dc.reg_ans as registro_ans,
    o.nome_fantasia as operadora,
    o.razao_social,
    dc.descricao,
    SUM(dc.vl_saldo_final) AS saldo_final_total,
    SUM(dc.vl_saldo_inicial) AS saldo_inicial_total,
    SUM(dc.vl_saldo_final) - SUM(dc.vl_saldo_inicial) AS diferenca_saldo,
    CONCAT(SUBSTRING(o.cnpj FROM 1 FOR 2), '.', SUBSTRING(o.cnpj FROM 3 FOR 3), '.', SUBSTRING(o.cnpj FROM 6 FOR 3), '/', SUBSTRING(o.cnpj FROM 9 FOR 4), '-', SUBSTRING(o.cnpj FROM 13 FOR 2)) AS cnpj_masc
	FROM demonstracoes_contabeis dc
	JOIN operadoras o ON dc.reg_ans = o.registro_operadora
	WHERE dc.data >= '2024-10-01'
	  AND dc.descricao ILIKE '%SAÚDE MEDICO HOSPITALAR%'
	GROUP BY o.cnpj, dc.reg_ans, o.nome_fantasia, dc.descricao, o.razao_social
	ORDER BY diferenca_saldo
	LIMIT 10;

-- Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

SELECT 
    dc.reg_ans as registro_ans,
    o.nome_fantasia as operadora,
    o.razao_social,
    dc.descricao,
    SUM(dc.vl_saldo_final) AS saldo_final_total,
    SUM(dc.vl_saldo_inicial) AS saldo_inicial_total,
    SUM(dc.vl_saldo_final) - SUM(dc.vl_saldo_inicial) AS diferenca_saldo,
    CONCAT(SUBSTRING(o.cnpj FROM 1 FOR 2), '.', SUBSTRING(o.cnpj FROM 3 FOR 3), '.', SUBSTRING(o.cnpj FROM 6 FOR 3), '/', SUBSTRING(o.cnpj FROM 9 FOR 4), '-', SUBSTRING(o.cnpj FROM 13 FOR 2)) AS cnpj_masc
	FROM demonstracoes_contabeis dc
	JOIN operadoras o ON dc.reg_ans = o.registro_operadora
	WHERE dc.data >= '2024-01-01'
	  AND dc.descricao ILIKE '%SAÚDE MEDICO HOSPITALAR%'
	GROUP BY o.cnpj, dc.reg_ans, o.nome_fantasia, dc.descricao, o.razao_social
	ORDER BY diferenca_saldo
	LIMIT 10;
