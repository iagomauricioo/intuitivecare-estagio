<template>
  <div class="dashboard">
    <h1>Operadoras</h1>
    <div class="search-form">
      <input v-model="registroAns" type="text" placeholder="Filtrar por Registro ANS" />
      <input v-model="cnpj" type="text" placeholder="Filtrar por CNPJ" />
      <input v-model="razaoSocial" type="text" placeholder="Filtrar por Razão Social" />
      <input v-model="nomeFantasia" type="text" placeholder="Filtrar por Nome Fantasia" />
      <input v-model="modalidade" type="text" placeholder="Filtrar por Modalidade" />
      <button @click="buscarOperadoras" class="submit-btn">Filtrar</button>
    </div>
    <table>
      <thead>
        <tr>
          <th>Registro ANS</th>
          <th>CNPJ</th>
          <th>Razão Social</th>
          <th>Nome Fantasia</th>
          <th>Modalidade</th>
          <th>Logradouro</th>
          <th>Número</th>
          <th>Complemento</th>
          <th>Bairro</th>
          <th>Cidade</th>
          <th>UF</th>
          <th>CEP</th>
          <th>DDD</th>
          <th>Telefone</th>
          <th>Fax</th>
          <th>Email</th>
          <th>Representante</th>
          <th>Cargo Representante</th>
          <th>Região de Comercialização</th>
          <th>Data de Registro</th>
        </tr>
      </thead>
      <tbody>
        <!-- Exibe os dados recebidos da API -->
        <tr v-for="operadora in operadoras" :key="operadora.Registro_ANS">
          <td>{{ operadora.Registro_ANS }}</td>
          <td>{{ operadora.CNPJ }}</td>
          <td>{{ operadora.Razao_Social }}</td>
          <td>{{ operadora.Nome_Fantasia || 'N/A' }}</td>
          <td>{{ operadora.Modalidade }}</td>
          <td>{{ operadora.Logradouro }}</td>
          <td>{{ operadora.Numero }}</td>
          <td>{{ operadora.Complemento || 'N/A' }}</td>
          <td>{{ operadora.Bairro }}</td>
          <td>{{ operadora.Cidade }}</td>
          <td>{{ operadora.UF }}</td>
          <td>{{ operadora.CEP }}</td>
          <td>{{ operadora.DDD }}</td>
          <td>{{ operadora.Telefone }}</td>
          <td>{{ operadora.Fax }}</td>
          <td>{{ operadora.Endereco_eletronico }}</td>
          <td>{{ operadora.Representante }}</td>
          <td>{{ operadora.Cargo_Representante }}</td>
          <td>{{ operadora.Regiao_de_Comercializacao }}</td>
          <td>{{ operadora.Data_Registro_ANS }}</td>
        </tr>
        <!-- Caso não haja dados -->
        <tr v-if="operadoras.length === 0">
          <td colspan="20" class="text-center">Nenhuma operadora encontrada.</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      operadoras: [],
      registroAns: '',
      cnpj: '',
      razaoSocial: '',
      nomeFantasia: '',
      modalidade: '',
    };
  },
  methods: {
    async buscarOperadoras() {
      const params = {};

      if (this.registroAns) params.registro_ans = this.registroAns;
      if (this.cnpj) params.cnpj = this.cnpj;
      if (this.razaoSocial) params.razao_social = this.razaoSocial;
      if (this.nomeFantasia) params.nome_fantasia = this.nomeFantasia;
      if (this.modalidade) params.modalidade = this.modalidade;

      try {
        const response = await axios.get('http://127.0.0.1:8000/api/v1/operadoras/buscar', { params });


        this.operadoras = response.data.data;
      } catch (error) {
        console.error("Erro ao buscar dados:", error);
      }
    }
  },
  mounted() {
    this.buscarOperadoras();
  }
};
</script>

<style scoped>
.dashboard {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.search-form {
  margin-bottom: 20px;
}

.search-form input {
  padding: 8px;
  margin-right: 8px;
  margin-bottom: 10px;
  border: 1px solid var(--color-border);
  border-radius: 4px;
}

.search-form button {
  width: 200px;
  font-size: 20px;
  padding: 8px 16px;
  background-color: rgb(65, 65, 203);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.search-form button:hover {
  background-color: rgb(59, 59, 180);
}

table {
  width: 100%;
  border-collapse: collapse;
  background-color: var(--color-background);
}

th,
td {
  border: 1px solid var(--color-border);
  padding: 8px;
  text-align: left;
}

th {
  background-color: var(--color-background-soft);
  color: var(--color-heading);
}

td {
  color: var(--color-text);
}

tr:hover {
  background-color: var(--color-background-mute);
}

th,
td {
  cursor: pointer;
}

tr:nth-child(even) {
  background-color: var(--color-background-soft);
}

tr:nth-child(odd) {
  background-color: var(--color-background);
}

tr:hover {
  background-color: var(--color-background-mute);
}

.text-center {
  text-align: center;
}
</style>
