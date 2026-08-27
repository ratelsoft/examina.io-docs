---
title: "Criar questões no examina.io Designer"
description: "Crie questões de múltipla escolha e preenchimento de lacunas, defina pontuações e seções, adicione textos e mídias e visualize o conteúdo no Designer."
tags: [designer, exam questions, fill in the blank, multiple choice, question authoring]
translation_source: user-guides/designer/questions.md
translation_source_sha256: 71aabc22c0127ffc08edfbcaf9305cadb7e175e8b8f56eedc47405e4faf982f9
---

# Criar questões no Designer

As questões pertencem a uma prova e, quando existem seções, a uma seção dessa prova.

## Adicionar uma questão

1. Abra um projeto de exame e crie uma prova.
2. Clique com o botão direito na prova e escolha a ação de nova questão ou selecione **New Question** abaixo do Exam Explorer.
3. Escolha um tipo de questão.
4. Insira o enunciado, as opções de resposta ou respostas aceitas e a explicação opcional.
5. Defina as propriedades da questão.
6. Abra o **Preview** e verifique o resultado.
7. Salve o projeto.

## Tipos de questão

O Designer dá suporte a:

- **Múltipla escolha — seleção única:** uma opção está correta.
- **Múltipla escolha — seleção múltipla:** mais de uma opção pode estar correta.
- **Preenchimento de lacuna:** o candidato insere um texto que é avaliado de acordo com as regras de resposta configuradas.

Escolha o tipo que mede a habilidade pretendida. Não transforme um item de respostas múltiplas em seleção única apenas para simplificar a correção.

## Propriedades principais

**Quantidade de opções**

: Defina o número de opções de múltipla escolha. O intervalo suportado é de 2 a 10.

**Opção correta**

: Identifica a resposta correta para um item de seleção única. Itens de seleção múltipla permitem as opções corretas aplicáveis.

**Permitir embaralhar opções**

: Randomiza a ordem das opções no Client, preservando qual opção está correta. Evite embaralhar opções como “todas as anteriores” que dependem da posição.

**Seção da questão**

: Atribui a questão a uma seção. Crie as seções necessárias da prova antes de atribuir as questões.

**Pontuação/Valor da questão**

: Defina a pontuação atribuída à questão. Valores decimais, como 0,5, são suportados.

## Estudos de caso e textos de apoio

Ative **Adicionar estudo de caso/texto de apoio** quando um enunciado depender de um material de leitura compartilhado, um anexo, um cenário ou uma declaração de problema. Use **Rótulo do estudo de caso** para substituir o rótulo padrão por um nome mais claro, como **Texto de interpretação**.

Se várias questões usarem o mesmo texto de apoio, mantenha a redação e a formatação consistentes e visualize cada questão.

## Editar e visualizar conteúdo

O painel de edição suporta formatação de texto, títulos, cores, listas, alinhamento, sobrescrito, subscrito, símbolos, expressões, imagens, áudios e tabelas.

![O editor de questões, com instrução, questão, opções e explicação](../../assets/images/designer/question-editor.png)

Use a formatação para melhorar a estrutura, não para decoração. Confirme se significados importantes não são transmitidos apenas pela cor.

### Imagens

Mantenha uma imagem importada dentro dos limites exibidos pelo Designer. A orientação do editor recomenda no máximo 650 pixels de largura e 500 KB para que a imagem seja exibida de forma confiável em computadores e celulares.

Redimensione e compacte imagens grandes antes de importar. Adicione texto suficiente na questão para que o propósito da imagem permaneça compreensível.

### Áudio

Itens de áudio podem dar suporte a questões de escuta. Configure os controles de volume, pausa, parada e busca disponíveis para corresponder às regras da avaliação.

Teste com fones de ouvido e a menor largura de banda esperada no dia do exame. Forneça um caminho de adaptação aprovado quando necessário.

### Tabelas

Use a ferramenta de tabela para adicionar linhas e colunas.

Para editar ou remover uma tabela, clique com o botão direito dentro dela e abra **Propriedades da tabela**.

Mantenha as tabelas pequenas o suficiente para se ajustarem às telas suportadas sem rolagem horizontal.

## Visualização e verificação de qualidade {#preview-and-quality-check}

Selecione **Preview** para inspecionar o enunciado e as opções renderizados.

![A visualização mostra a questão como o candidato a verá](../../assets/images/designer/question-preview.png)

Antes de exportar, verifique se:

- o enunciado tem apenas uma interpretação defensável;
- a resposta correta e a pontuação estão definidas;
- os distratores são plausíveis e não revelam a resposta acidentalmente;
- a atribuição de seção está correta;
- as opções embaralhadas permanecem com sentido;
- a mídia carrega e está legível ou audível;
- a ortografia, a gramática e a notação matemática estão corretas; e
- a questão funciona no menor tamanho de tela permitido.

Para reutilizar conteúdo existente, consulte [Reutilizar conteúdo do projeto](importing-questions.md).
Para trazer questões de um documento ou de outro projeto, consulte [Importar conteúdo existente](import-content.md).
