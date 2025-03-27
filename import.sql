CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    DATA DATE,
    REG_ANS BIGINT,
    CD_CONTA_CONTABIL BIGINT,
    DESCRICAO TEXT,
    VL_SALDO_INICIAL NUMERIC(18,2),
    VL_SALDO_FINAL NUMERIC(18,2)
);

\copy demonstracoes_contabeis FROM 'demonstracoes_contabeis.csv' DELIMITER ';' CSV NULL 'NULL' ENCODING 'UTF8';
