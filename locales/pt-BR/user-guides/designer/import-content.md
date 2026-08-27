---
title: "Importar conteúdo existente no examina.io Designer"
description: "Importe exames de outro projeto do Designer, provas e questões de um exame exportado e questões escritas em um documento Word, RTF ou texto."
tags: [designer, import questions, import exams, docx import, question markers]
translation_source: user-guides/designer/import-content.md
translation_source_sha256: c9b2db78d897346026145e29d1812f83ea750b4e7119666b47bf640ca03d94df
---

# Importar conteúdo existente

O Designer pode importar conteúdo de outro projeto do Designer, de um exame já exportado para aplicação ou de um documento de texto em que as questões foram digitadas. Os três processos utilizam o mesmo assistente: escolha um arquivo, informe ao Designer como o documento está estruturado e marque o que deseja. O ponto de partida determina o que você pode importar.

## O que o Designer aceita

Um arquivo de projeto `.smexproj` e um exame exportado `.smex` são lidos diretamente, pois seu conteúdo já está estruturado. Um documento `.txt`, `.rtf` ou `.docx` é lido como texto, portanto o Designer precisa do marcador e das tags abaixo para identificar onde cada questão começa. O formato `.doc` não é suportado: abra-o no Word e salve como `.docx`.

!!! warning "Arquivos de uma versão mais recente não serão importados"
    Um projeto ou exame exportado salvo por uma versão mais recente do aplicativo do que a que você está executando é recusado, exibindo a mesma mensagem que apareceria ao abri-lo: *"The file version is greater than the application version"*. Peça a quem o enviou que o salve a partir de uma versão compatível.

## Iniciar uma importação

1. Escolha **Arquivo → Importar Exames de outro Projeto** para trazer exames inteiros para o projeto aberto.
2. Clique com o botão direito em um exame no **Exam Explorer** e escolha **Importar Provas de Arquivo** para adicionar provas a esse exame.
3. Clique com o botão direito em uma prova e escolha **Importar Questões de Arquivo** para adicionar questões a essa prova.

A Etapa 1 solicita o arquivo. Documentos seguem para a etapa 2; qualquer outro arquivo vai para a etapa 3.

![Etapa 1 do assistente de importação, com o seletor de arquivos e os tipos de arquivos aceitos](../../assets/images/designer/import-choose-file.png)

## Informe ao Designer onde cada questão começa

A etapa 2 aparece apenas para documentos. Escolha o marcador que inicia cada questão no seu arquivo: `1.`, `Q1.`, `Q1` em uma linha própria ou `Q.`. Nada fica pré-selecionado, portanto escolha a opção correspondente ao seu documento. Abra **O que mais posso colocar no meu documento?** para consultar as tags, cada uma no início de uma linha.

![Etapa 2 com as opções de marcador de questão e o painel de tags aberto](../../assets/images/designer/import-question-markers.png)

### Tags

**Question:**

: O texto da questão, necessário apenas quando não estiver logo após o marcador.

**Instruction:**

: A instrução para essa questão.

**Section:**

: Coloca a questão em uma seção nomeada.

**Case Study:**, **Passage:**, **Comprehension:**, **Example:**

: Um texto/passagem anexado à questão. A tag escolhida será o rótulo exibido.

**A.**, **A)**, **A:**

: Uma opção. As letras de A a J são reconhecidas.

**Ans:**, **Answer:**, **Correct Option:**

: A letra da opção correta.

**Ref:**, **Exp:**, **Explanation:**, **Reference:**

: A explicação exibida com a resposta.

### Casos que costumam causar dúvidas

Uma questão só é finalizada após uma linha de resposta ser identificada. É isso que permite que uma lista numerada dentro de um estudo de caso, como `1. First point` e `2. Second point`, permaneça no texto em vez de fazer cada linha iniciar uma nova questão. Uma questão sem linha de resposta nunca é encerrada e absorve as questões seguintes. Portanto, uma questão importada contendo o texto de várias outras geralmente indica a ausência da linha **Ans:**. Uma segunda resposta substitui a primeira; não adiciona uma nova.

Uma linha sem tag continua a linha anterior, que é como um estudo de caso com várias linhas se mantém unificado, e a razão pela qual uma anotação solta entre questões é anexada à linha acima. Textos sem tag antes de qualquer tag tornam-se o texto da questão, e uma tag **Question:** posterior o sobrescreve. Um nome de **Section:** com menos de três caracteres é ignorado e a questão vai para a seção padrão da prova. A importação de documentos sempre produz itens de múltipla escolha com resposta única, portanto preenchimento de lacunas e múltipla escolha com seleção múltipla ainda devem ser [criados manualmente](questions.md).

## Escolher o que importar

A etapa 3 mostra o que o Designer encontrou em uma árvore Exame → Prova → Questão.

1. Marque os exames, provas ou questões desejados.
2. Selecione cada um para lê-lo no painel de pré-visualização à direita.
3. Escolha **Importar**.

Apenas os níveis permitidos pelo seu ponto de entrada podem ser marcados: importar provas permite marcar provas e questões, mas não exames; importar questões permite marcar apenas questões.

![Etapa 3 com a árvore de conteúdo marcada à esquerda e a pré-visualização de uma questão à direita](../../assets/images/designer/import-select-content.png)

As imagens dentro de um arquivo `.docx` são importadas junto com suas questões; qualquer imagem grande demais ou em um formato que o Designer não consiga exibir é ignorada, contada e informada ao término da importação. O conteúdo importado torna-se conteúdo comum do Designer, portanto pré-visualize-o, defina pontuações e seções e salve o projeto.

## Baixar questões

**Baixar Questões** é um recurso independente, que não faz parte do assistente de importação. Clique com o botão direito em uma prova e escolha essa opção para puxar questões do SmartQuestions.

1. Faça login com sua conta Ratelsoft.
2. Escolha um esquema e, em seguida, até cinco disciplinas.
3. Defina quantas questões deseja obter de cada disciplina, entre 1 e 100.
4. Escolha a ordem sequencial ou aleatória e faça o download.

O login não é armazenado. O Designer solicitará o login novamente em uma nova sessão.

![A caixa de diálogo Baixar Questões solicitando login na conta Ratelsoft](../../assets/images/designer/import-download-questions.png)

Para copiar conteúdo dentro do projeto aberto, consulte [Reutilizar conteúdo do projeto](importing-questions.md).
