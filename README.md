# Cálculo do IMC

Este programa realiza o cálculo do Índice de Massa Corporal (IMC) de uma pessoa e exibe as informações de forma formatada utilizando f-strings. O IMC é uma medida usada para avaliar o peso em relação à altura de uma pessoa.

## Objetivo

O objetivo deste exercício é calcular o IMC de uma pessoa com base no peso e na altura, e exibir as informações de forma legível utilizando f-strings no Python.

## Como Funciona

1. O programa define as variáveis `nome`, `altura` e `peso` com valores predefinidos.
2. Calcula o IMC utilizando a fórmula:  
   \[
   \text{IMC} = \frac{\text{peso}}{\text{altura}^2}
   \]
3. Utiliza f-strings para formatar as saídas de forma amigável, com 2 casas decimais para a altura e o IMC.
4. Exibe o nome, altura, peso e IMC da pessoa no formato solicitado.

## Exemplo de Execução

```
Pedro tem 1.86 de altura, pesa
94 quilos e seu IMC é
27.18
```

## Como Funciona o Código

1. **Definição de Variáveis**:
   - A variável `nome` armazena o nome da pessoa.
   - A variável `altura` armazena a altura da pessoa em metros.
   - A variável `peso` armazena o peso da pessoa em quilos.

2. **Cálculo do IMC**:
   - O IMC é calculado dividindo o peso pela altura elevada ao quadrado:  
     \[
     \text{IMC} = \frac{94}{1.86^2} \approx 27.18
     \]

3. **Exibição com f-strings**:
   - A f-string `linha_1` formata e exibe o nome e a altura da pessoa com 2 casas decimais.
   - A f-string `linha_2` exibe o peso da pessoa.
   - A f-string `linha_3` exibe o IMC da pessoa com 2 casas decimais.

## Requisitos

- Python 3.x ou superior.

## Como Usar

1. Clone ou baixe este repositório.
2. Abra o arquivo Python no seu editor de código favorito.
3. Execute o programa.
4. O programa exibirá o nome, altura, peso e IMC da pessoa.

## Possíveis Melhorias

- Permitir que o usuário insira os valores para `nome`, `peso` e `altura` ao invés de ter valores fixos no código.
- Adicionar validação de entrada para garantir que o peso e a altura sejam números positivos.

## Licença

Este projeto é de código aberto e pode ser modificado ou compartilhado conforme necessário.

---

Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato! 😄
