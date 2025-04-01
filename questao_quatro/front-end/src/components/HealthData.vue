<template>
    <div class="container">
        <v-card title="Operadoras" class="operadoras-container" flat>
            <template v-slot:text>
                <div class="search-fields">
                    <v-text-field v-model="filtros.registroAns" label="Registro ANS" variant="outlined" hide-details
                        class="search-field"></v-text-field>
                    <v-text-field v-model="filtros.cnpj" label="CNPJ" variant="outlined" hide-details
                        class="search-field"></v-text-field>
                    <v-text-field v-model="filtros.razaoSocial" label="Razão Social" variant="outlined" hide-details
                        class="search-field"></v-text-field>
                    <v-text-field v-model="filtros.nomeFantasia" label="Nome Fantasia" variant="outlined" hide-details
                        class="search-field"></v-text-field>
                    <v-text-field v-model="filtros.modalidade" label="Modalidade" variant="outlined" hide-details
                        class="search-field"></v-text-field>
                    <v-btn @click="buscarOperadoras" color="primary" class="search-btn">Filtrar</v-btn>
                </div>
            </template>

            <v-data-table :headers="headers" :items="operadoras" :items-per-page="10" class="elevation-1"
                no-data-text="Nenhuma operadora encontrada"></v-data-table>
        </v-card>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const filtros = ref({
    registroAns: '',
    cnpj: '',
    razaoSocial: '',
    nomeFantasia: '',
    modalidade: ''
})

const operadoras = ref([])

const headers = [
    { key: 'Registro_ANS', title: 'Registro ANS' },
    { key: 'CNPJ', title: 'CNPJ' },
    { key: 'Razao_Social', title: 'Razão Social' },
    { key: 'Nome_Fantasia', title: 'Nome Fantasia' },
    { key: 'Modalidade', title: 'Modalidade' },
    { key: 'Logradouro', title: 'Logradouro' },
    { key: 'Numero', title: 'Número' },
    { key: 'Complemento', title: 'Complemento' },
    { key: 'Bairro', title: 'Bairro' },
    { key: 'Cidade', title: 'Cidade' },
    { key: 'UF', title: 'UF' },
    { key: 'CEP', title: 'CEP' },
    { key: 'DDD', title: 'DDD' },
    { key: 'Telefone', title: 'Telefone' },
    { key: 'Fax', title: 'Fax' },
    { key: 'Endereco_eletronico', title: 'Email' },
    { key: 'Representante', title: 'Representante' },
    { key: 'Cargo_Representante', title: 'Cargo Representante' },
    { key: 'Regiao_de_Comercializacao', title: 'Região de Comercialização' },
    { key: 'Data_Registro_ANS', title: 'Data de Registro' }
]

const buscarOperadoras = async () => {
    const params = {}

    if (filtros.value.registroAns) params.registro_ans = filtros.value.registroAns
    if (filtros.value.cnpj) params.cnpj = filtros.value.cnpj
    if (filtros.value.razaoSocial) params.razao_social = filtros.value.razaoSocial
    if (filtros.value.nomeFantasia) params.nome_fantasia = filtros.value.nomeFantasia
    if (filtros.value.modalidade) params.modalidade = filtros.value.modalidade

    try {
        const response = await axios.get('https://api.iagomauricio.com/api/v1/operadoras/buscar', {
            params,
        })

        operadoras.value = response.data.data
    } catch (error) {
        console.error('Erro ao buscar dados:', error)
    }
}

// Busca inicial ao carregar o componente
buscarOperadoras()
</script>

<style scoped>
.container {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100vw;
    margin-top: 0;
}

.operadoras-container {
    width: 95%;
    border-radius: 20px;
}

.search-fields {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 20px;
}

.search-field {
    min-width: 200px;
    flex-grow: 1;
}

.search-btn {
    height: 56px;
    align-self: flex-end;
}
</style>