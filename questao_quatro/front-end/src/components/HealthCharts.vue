<template>
    <v-container>
        <!-- Cabeçalho -->
        <v-row class="mb-6">
            <v-col cols="12">
                <v-card>
                    <v-card-title class="text-h4">
                        Dashboard de Operadoras de Saúde
                    </v-card-title>
                    <v-card-subtitle>
                        Dados consumidos da API: http://165.22.1.202:8000/api/v1/operadoras/
                    </v-card-subtitle>
                </v-card>
            </v-col>
        </v-row>

        <!-- Filtros -->
        <v-row class="mb-4">
            <v-col cols="12" md="3">
                <v-select v-model="filters.modalidade" :items="modalidadeOptions" label="Filtrar por Modalidade"
                    clearable></v-select>
            </v-col>
            <v-col cols="12" md="2" class="d-flex align-center">
                <v-btn color="primary" @click="applyFilters" block :loading="loading">
                    <v-icon left>mdi-filter</v-icon>
                    Filtrar
                </v-btn>
            </v-col>
        </v-row>

        <!-- Gráficos -->
        <v-row>
            <!-- Distribuição por UF -->
            <v-col cols="12" md="6">
                <v-card>
                    <v-card-title>Distribuição por Estado (UF)</v-card-title>
                    <div class="chart-container">
                        <BarChart v-if="ufChartData.labels.length > 0" :chart-data="ufChartData"
                            :options="chartOptions" />
                        <v-progress-circular v-else indeterminate color="primary"></v-progress-circular>
                    </div>
                </v-card>
            </v-col>

            <!-- Distribuição por Modalidade -->
            <v-col cols="12" md="6">
                <v-card>
                    <v-card-title>Distribuição por Modalidade</v-card-title>
                    <div class="chart-container">
                        <PieChart v-if="modalidadeChartData.labels.length > 0" :chart-data="modalidadeChartData"
                            :options="chartOptions" />
                        <v-progress-circular v-else indeterminate color="primary"></v-progress-circular>
                    </div>
                </v-card>
            </v-col>
        </v-row>

        <!-- Mapa -->
        <v-row class="mt-4">
            <v-col cols="12">
                <v-card>
                    <v-card-title>Concentração Geográfica das Operadoras</v-card-title>
                    <div id="map-container" style="height: 500px; width: 100%">
                        <div id="map" style="height: 100%"></div>
                    </div>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { BarChart, PieChart } from 'vue-chart-3';
import { Chart, registerables } from 'chart.js';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

Chart.register(...registerables);

// Dados e estados
const operadoras = ref([]);
const loading = ref(true);
const filteredOperadoras = ref([]);
const dialog = ref(false);
const selectedOperadora = ref(null);
const filters = ref({
    uf: null,
    modalidade: null,
    search: ''
});

// Opções para filtros
const ufOptions = ref([]);
const modalidadeOptions = ref([]);

// Configurações dos gráficos
const chartOptions = ref({
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            position: 'top',
        },
        tooltip: {
            callbacks: {
                label: function (context) {
                    return `${context.label}: ${context.raw} (${((context.raw / context.dataset.data.reduce((a, b) => a + b, 0)) * 100).toFixed(1)}%)`;
                }
            }
        }
    }
});

// Dados para gráficos
const ufChartData = ref({
    labels: [],
    datasets: [{
        label: 'Operadoras por UF',
        data: [],
        backgroundColor: '#4e73df'
    }]
});

const modalidadeChartData = ref({
    labels: [],
    datasets: [{
        data: [],
        backgroundColor: [
            '#4e73df', '#1cc88a', '#36b9cc', '#f6c23e',
            '#e74a3b', '#858796', '#5a5c69', '#2e59d9'
        ]
    }]
});

// Cabeçalhos da tabela
const headers = ref([
    { text: 'Registro ANS', value: 'Registro_ANS' },
    { text: 'Razão Social', value: 'Razao_Social' },
    { text: 'Nome Fantasia', value: 'Nome_Fantasia' },
    { text: 'Modalidade', value: 'Modalidade' },
    { text: 'UF', value: 'UF' },
    { text: 'Cidade', value: 'Cidade' },
    { text: 'Ações', value: 'actions', sortable: false }
]);

// Funções de formatação
const formatCNPJ = (cnpj) => {
    const str = cnpj.toString().padStart(14, '0');
    return `${str.slice(0, 2)}.${str.slice(2, 5)}.${str.slice(5, 8)}/${str.slice(8, 12)}-${str.slice(12)}`;
};

const formatCEP = (cep) => {
    const str = cnpj.toString().padStart(8, '0');
    return `${str.slice(0, 5)}-${str.slice(5)}`;
};

const formatPhone = (phone) => {
    const str = phone.toString();
    return str.length === 8 ? `${str.slice(0, 4)}-${str.slice(4)}` : str;
};

// Buscar dados da API
const fetchData = async () => {
    try {
        loading.value = true;
        const response = await axios.get('http://165.22.1.202:8000/api/v1/operadoras/buscar');
        operadoras.value = response.data.data || response.data;
        filteredOperadoras.value = [...operadoras.value]; // Inicializa com todos os dados

        processChartData();
        initMap(); // Inicializa o mapa com todos os dados
    } catch (error) {
        console.error('Erro ao buscar dados:', error);
    } finally {
        loading.value = false;
    }
};

// Nova função para aplicar filtros
const applyFilters = () => {
    if (!filters.value.modalidade) {
        filteredOperadoras.value = [...operadoras.value];
    } else {
        filteredOperadoras.value = operadoras.value.filter(
            op => op.Modalidade === filters.value.modalidade
        );
    }

    processChartData();
    updateMapMarkers(); // Atualiza os marcadores do mapa
};

let map = null;
let markers = [];

// Inicializar mapa Leaflet
const initMap = () => {
    // Destruir mapa existente se houver
    if (map) {
        map.remove();
        markers = [];
    }

    // Coordenadas aproximadas do centro do Brasil
    map = L.map('map').setView([-15, -55], 4);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    updateMapMarkers();
};

// Atualizar marcadores do mapa
const updateMapMarkers = () => {
    // Limpar marcadores existentes
    markers.forEach(marker => map.removeLayer(marker));
    markers = [];

    // Adicionar novos marcadores para operadoras filtradas
    filteredOperadoras.value.forEach(op => {
        if (op.UF && op.Cidade) {
            const lat = getApproxLatitude(op.UF);
            const lng = getApproxLongitude(op.UF);

            if (lat && lng) {
                const marker = L.marker([lat, lng])
                    .addTo(map)
                    .bindPopup(`<b>${op.Razao_Social}</b><br>${op.Modalidade}<br>${op.Cidade}-${op.UF}`);
                markers.push(marker);
            }
        }
    });

    // Ajustar o zoom para mostrar todos os marcadores
    if (markers.length > 0) {
        const group = new L.featureGroup(markers);
        map.fitBounds(group.getBounds());
    }
};

// Processar dados para gráficos
// Processar dados para gráficos - ATUALIZADO para usar filteredOperadoras
const processChartData = () => {
    // Distribuição por UF - agora usa filteredOperadoras
    const ufCount = {};
    filteredOperadoras.value.forEach(op => {
        ufCount[op.UF] = (ufCount[op.UF] || 0) + 1;
    });

    ufChartData.value = {
        labels: Object.keys(ufCount).sort(),
        datasets: [{
            label: 'Operadoras por UF',
            data: Object.keys(ufCount).sort().map(uf => ufCount[uf]),
            backgroundColor: '#4e73df'
        }]
    };

    // Distribuição por Modalidade - agora usa filteredOperadoras
    const modalidadeCount = {};
    filteredOperadoras.value.forEach(op => {
        modalidadeCount[op.Modalidade] = (modalidadeCount[op.Modalidade] || 0) + 1;
    });

    modalidadeChartData.value = {
        labels: Object.keys(modalidadeCount),
        datasets: [{
            data: Object.values(modalidadeCount),
            backgroundColor: [
                '#4e73df', '#1cc88a', '#36b9cc', '#f6c23e',
                '#e74a3b', '#858796', '#5a5c69', '#2e59d9'
            ]
        }]
    };

    ufOptions.value = [...new Set(operadoras.value.map(op => op.UF))].sort();
    modalidadeOptions.value = [...new Set(operadoras.value.map(op => op.Modalidade))].sort();
};


const getApproxLatitude = (uf) => {
    const ufCoords = {
        'AC': -8.77, 'AL': -9.62, 'AM': -3.47, 'AP': 1.41, 'BA': -13.29,
        'CE': -5.20, 'DF': -15.78, 'ES': -19.19, 'GO': -15.98, 'MA': -5.42,
        'MG': -18.10, 'MS': -20.51, 'MT': -12.64, 'PA': -3.79, 'PB': -7.28,
        'PE': -8.38, 'PI': -6.60, 'PR': -24.89, 'RJ': -22.25, 'RN': -5.81,
        'RO': -10.83, 'RR': 1.99, 'RS': -30.17, 'SC': -27.45, 'SE': -10.57,
        'SP': -22.19, 'TO': -9.46
    };
    return ufCoords[uf];
};

const getApproxLongitude = (uf) => {
    const ufCoords = {
        'AC': -70.55, 'AL': -36.82, 'AM': -65.10, 'AP': -51.77, 'BA': -41.71,
        'CE': -39.53, 'DF': -47.93, 'ES': -40.34, 'GO': -49.86, 'MA': -45.44,
        'MG': -44.38, 'MS': -54.54, 'MT': -55.42, 'PA': -52.48, 'PB': -36.72,
        'PE': -37.86, 'PI': -42.28, 'PR': -51.55, 'RJ': -42.66, 'RN': -36.59,
        'RO': -63.34, 'RR': -61.33, 'RS': -53.50, 'SC': -50.95, 'SE': -37.45,
        'SP': -48.79, 'TO': -48.26
    };
    return ufCoords[uf];
};

// Mostrar detalhes da operadora
const showDetails = (operadora) => {
    selectedOperadora.value = operadora;
    dialog.value = true;
};

// Inicializar componente
onMounted(() => {
    fetchData();
});
</script>

<style scoped>
.chart-container {
    position: relative;
    height: 450px;
    padding: 16px;
}
</style>