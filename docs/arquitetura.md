# Arquitetura do Sistema

O sistema segue uma arquitetura em camadas simples, inspirada em aplicações reais.

## Camadas

- **Sensor**
  - Responsável pela leitura do peso (simulado ou real)

- **Service**
  - Orquestra o fluxo da aplicação
  - Centraliza a lógica de processamento

- **Classifier**
  - Contém as regras de negócio para classificação

- **Logger**
  - Responsável por registrar eventos do sistema

- **Utils**
  - Formatação e funções auxiliares

- **Main**
  - Ponto de entrada da aplicação

---

## Fluxo de execução

Sensor → Service → Classifier → Logger → Output

---

## Benefícios

- Separação clara de responsabilidades
- Facilidade para manutenção
- Escalabilidade para APIs e IoT
- Código mais testável

---

## Evoluções possíveis

- Substituir Logger por sistema de logs (ex: logging lib)
- Transformar Service em API (FastAPI)
- Integração com banco de dados
- Uso com hardware real (HX711)
