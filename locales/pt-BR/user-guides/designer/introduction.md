---
title: "Introdução ao examina.io Designer"
description: "Conheça o espaço de trabalho do Designer e crie projetos de exame, provas, seções e questões para aplicação via examina.io."
tags: [assessment authoring, designer, exam project, questions]
translation_source: user-guides/designer/introduction.md
translation_source_sha256: 00ffb0a122c3a4edb7cc94fbec1d25afdddeaa592ab5240604581e63c4551fbb
---

# Introdução ao Designer

O Designer é onde os exames são elaborados. Você cria um **projeto**, insere um ou mais **exames** dentro dele, divide cada exame em **provas** e preenche as provas com **questões**. Quando o exame estiver pronto, você o envia para o Manager, que é onde ele é atribuído às pessoas e aplicado.

O Designer roda no navegador e não precisa de nada instalado.

![O espaço de trabalho do Designer sem nenhum projeto aberto](../../assets/images/designer/workspace-empty.png)

## O espaço de trabalho

Quatro áreas que permanecem no mesmo lugar o tempo todo.

| Área | O que contém |
|---|---|
| **Exam Explorer** (superior esquerdo) | A árvore do projeto: exames, depois provas e depois questões |
| **Properties** (inferior esquerdo) | Configurações do item selecionado na árvore |
| **Hint** (inferior esquerdo) | Explicação em linguagem simples da propriedade selecionada |
| **Painel de edição** (direito) | O exame, prova ou questão em que você está trabalhando |

Vale a pena conhecer o painel Hint. Selecione qualquer linha em Properties e ele explicará o que essa configuração faz, o que geralmente é mais rápido do que pesquisar.

## Dois tipos de arquivo

Esta distinção causa mais confusão do que qualquer outra coisa no Designer, por isso vale a pena entendê-la bem antes de começar.

| Arquivo | Extensão | O que é |
|---|---|---|
| **Projeto** | `.smexproj` | Seu arquivo-fonte editável. Contém cada exame, prova e questão, e pode ser reaberto e alterado |
| **Exame** | `.smex` | Um único exame empacotado para aplicação. É isto que o Manager consome |

Guarde o projeto. Se você o perder e mantiver apenas o exame exportado, perderá a capacidade de editá-lo com facilidade.

## Criar um projeto

1. Escolha **File → New Exam Project**.
2. O Designer cria um **Untitled Exam** dentro dele.
3. Selecione esse exame no Exam Explorer para preencher seus detalhes.
4. Escolha **File → Save Project** e guarde o `.smexproj` em um local seguro.

![O menu File](../../assets/images/designer/file-menu.png)

Observe quais itens estão desativados (em cinza) e que eles ficam disponíveis em dois estágios. **Save Project**, **Save Project As...** e **New Exam** ficam disponíveis assim que um projeto é aberto. As duas ações de exportação permanecem desativadas até que você realmente **selecione um exame** no Exam Explorer, pois o Designer exporta um exame por vez e precisa saber qual. Um menu File cheio de texto em cinza não é um erro — geralmente significa apenas que nada foi selecionado ainda.

## Abrir um projeto existente

**File → Open Project** e, em seguida, escolha um arquivo `.smexproj`.

!!! warning "Projetos de uma versão mais recente não serão abertos"
    O Designer recusa um projeto salvo por uma versão mais recente do aplicativo do que a que você está executando, porque não pode garantir que compreenderá tudo o que há nele. Você verá *"The file version is greater than the application version"*.

    Exporte o exame a partir da versão que o criou ou peça a quem o enviou para salvá-lo em uma versão compatível.

![O projeto de exemplo aberto, com seu exame no Exam Explorer](../../assets/images/designer/project-loaded.png)

As capturas de tela nestas páginas usam um exemplo do início ao fim: um projeto chamado **Northgate Entrance Exam 2026** contendo um único exame, *Northgate Entrance Examination*, dividido em seis provas.

## A estrutura de um exame

Tudo no Designer é aninhado da mesma forma:

```
Project
└── Exam                     one or more
    └── Paper                one or more
        └── Question         one or more
            └── Section      optional grouping within a paper
```

Uma **prova** geralmente corresponde a uma matéria, curso ou módulo. Um exame com seis provas pode ser uma única aplicação abrangendo seis matérias, com sua própria duração e conjunto de questões para cada uma.

## Adicionar uma prova

Clique com o botão direito no exame no Exam Explorer e escolha **New Exam Paper**; em seguida, selecione a nova prova para definir seu título, duração e instruções. Veja [A prova](paper.md) para saber o que cada configuração faz.

## Adicionar uma questão

Clique com o botão direito em uma prova e escolha a ação de nova questão, ou use o botão abaixo do Exam Explorer. O Designer oferece suporte a:

- Múltipla escolha, seleção única
- Múltipla escolha, seleção múltipla
- Preenchimento de lacuna

Defina a resposta, a pontuação e a seção e, em seguida, use **Preview** para ver a questão exatamente como o candidato a verá. Veja [Criando questões](questions.md).

## Uma ordem de trabalho

1. Configure o [exame](exam.md) — título, código, descrição e instruções
2. Crie cada [prova](paper.md) e defina sua duração
3. Adicione seções se a prova precisar delas
4. Escreva as [questões](questions.md) ou [importe-as](import-content.md)
5. Faça a pré-visualização e a revisão
6. **Salve o projeto**
7. Exporte um exame para o [Manager](../manager/import-exams.md)

Você também pode [reutilizar provas e questões](importing-questions.md) de outros locais do projeto aberto, [importar conteúdo existente](import-content.md) de outro projeto ou documento, ou elaborar rascunhos a partir de suas próprias fontes com a [criação por IA](ai-question-authoring.md).
