CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    DATA DATE,
    REG_ANS BIGINT,
    CD_CONTA_CONTABIL BIGINT,
    DESCRICAO TEXT,
    VL_SALDO_INICIAL NUMERIC(18,2),
    VL_SALDO_FINAL NUMERIC(18,2)
);

\copy demonstracoes_contabeis FROM 'demonstracoes_contabeis.csv' DELIMITER ';' CSV NULL 'NULL' ENCODING 'UTF8';

CREATE TABLE IF NOT EXISTS operadoras (
  REGISTRO_OPERADORA VARCHAR(6),
  CNPJ VARCHAR(14),
  Razao_Social VARCHAR(140),
  Nome_Fantasia VARCHAR(140),
  Modalidade VARCHAR(50),
  Logradouro VARCHAR(40),
  Numero VARCHAR(20),
  Complemento VARCHAR(40),
  Bairro VARCHAR(30),
  Cidade VARCHAR(30),
  UF VARCHAR(2),
  CEP VARCHAR(8),
  DDD VARCHAR(4),
  Telefone VARCHAR(20),
  Fax VARCHAR(20),
  Endereco_eletronico VARCHAR(255),
  Representante VARCHAR(50),
  Cargo_Representante VARCHAR(40),
  Regiao_de_Comercializacao VARCHAR(1),
  Data_Registro_ANS DATE
);


\copy operadoras FROM 'dados_operadoras.csv' DELIMITER ';' CSV NULL 'NULL' ENCODING 'UTF8';
