---
title: "Crie questões de prova baseadas em fontes com IA"
description: "Elabore questões de prova editáveis e citadas a partir de PDF, DOCX, PPTX, TXT, Markdown, HTML e trechos existentes no examina.io Designer."
tags: [source-backed AI question authoring, assessment authoring, exam questions, Designer, cited questions]
translation_source: user-guides/designer/ai-question-authoring.md
translation_source_sha256: f2eee7ab06512f6877e0dc625ad4ff119520e39668d030b899bc4d144b41b991
---

# Criar e revisar questões com IA

O Designer pode transformar o material de origem em rascunhos de questões editáveis sem sair do documento atual. Ele nunca insere ou publica resultados de IA automaticamente: um autor autorizado revisa cada candidato e escolhe o que entra no documento.

## O que o seu plano inclui e quanto custam as questões extras

A elaboração de questões por IA baseada em fontes está incluída em todos os planos. Sua cota mensal conta candidatos válidos, baseados em fontes e não duplicados que chegam até a **Revisão** — não solicitações, páginas enviadas por upload ou tentativas do provedor.

| Plano | Questões baseadas em fontes por mês | Armazenamento da biblioteca de fontes | Fontes salvas | Tamanho máximo do arquivo |
| --- | ---: | ---: | ---: | ---: |
| Starter | 10 | 250 MB | 25 | 50 MB |
| Basic | 100 | 2 GB | 250 | 250 MB |
| Professional | 500 | 10 GB | 1.000 | 500 MB |
| Flexible | 100 | 5 GB | 500 | 500 MB |
| Enterprise | Personalizado | Personalizado | Personalizado | Personalizado |

A cota incluída é reiniciada no início de cada mês do calendário UTC e é compartilhada pela organização. A cota atual é exibida na janela de elaboração por IA. Uma questão apenas de texto ou uma questão que reutiliza uma imagem da fonte consome uma questão incluída. Uma questão com um recurso visual recém-gerado consome quatro questões incluídas. Por exemplo, uma cota de 100 pode produzir até 100 questões de texto ou com imagem da fonte, até 25 questões com recursos visuais recém-gerados ou uma combinação de ambos.

Após o uso da cota incluída, o preço atual para cada questão válida adicional que chega à Revisão é:

| Resultado que chega à Revisão | USD | CAD | NGN |
| --- | ---: | ---: | ---: |
| Questão apenas de texto ou com imagem da fonte | $0.15 | C$0.20 | ₦200 |
| Questão com um recurso visual recém-gerado | $0.60 | C$0.80 | ₦800 |

Não existe um produto separado de créditos de IA ou carteira de IA. O valor é reservado e deduzido do saldo pré-pago normal da sua organização. Todos os planos podem adicionar fundos em **Faturamento → Saldo Pré-pago** usando o provedor de pagamento disponível. A janela de IA mostra o preço aplicável e o saldo pré-pago disponível antes de você gerar. Se o saldo não puder cobrir a parte da solicitação além da sua cota, a geração não é iniciada e informa quanto você deve adicionar.

Por exemplo, se restarem duas questões incluídas e você solicitar cinco, o Designer reserva o valor de três questões. Se quatro candidatos válidos chegarem à Revisão, as duas questões incluídas contam primeiro, apenas duas questões pré-pagas são cobradas e a reserva não utilizada de uma questão é devolvida ao saldo pré-pago.

!!! info "Apenas candidatos válidos e baseados em fontes que chegam à Revisão contam"
    Solicitações com falha, candidatos inválidos, candidatos sem evidência de fonte verificável e duplicatas rejeitadas antes da Revisão não consomem a cota nem o saldo pré-pago.

## Fontes suportadas

Você pode gerar a partir do trecho ou estudo de caso atual, selecionar até 10 recursos salvos da organização ou fazer upload de qualquer um destes tipos de arquivo:

- PDF (`.pdf`)
- Microsoft Word (`.docx`)
- Microsoft PowerPoint (`.pptx`)
- texto simples em UTF-8 (`.txt`)
- Markdown (`.md` ou `.markdown`)
- HTML (`.html` ou `.htm`)
- Imagens PNG, JPEG, GIF ou WebP

As fontes em PDF devem conter texto selecionável. Execute o OCR antes de fazer o upload de um PDF digitalizado ou apenas com imagens. Arquivos do Office com macros ativadas e criptografados não são suportados. O Designer lê HTML como texto inerte: ele não executa scripts, não envia formulários, não carrega objetos incorporados nem busca recursos remotos.

Os recursos enviados por upload permanecem na biblioteca de fontes privada da sua organização até que um usuário os exclua. Fazer o upload do mesmo arquivo novamente reutiliza o recurso existente em vez de armazenar outra cópia.

## Gerar candidatos a questões

1. Abra um projeto de exame e selecione o documento que deve receber as questões.
2. Escolha **Elaborar questões a partir das suas fontes** na barra de ferramentas do Exam Explorer.
3. Em **Fonte**, escolha o trecho atual, selecione recursos salvos ou faça upload de um arquivo suportado. Aguarde até que todos os recursos selecionados estejam prontos.
4. Em **Questões**, adicione uma ou mais linhas de estrutura.
5. Para cada linha, escolha uma quantidade exata, tipo de questão, dificuldade, pontuação e um tópico ou resultado de aprendizagem opcional.
6. Escolha **Gerar candidatos**.

O Designer suporta estes tipos de questões geradas:

- Multiple Choice — single select
- Multiple Choice — multiple select
- Fill in the Blank

Fontes grandes usam uma seleção direcionada de seções originais da fonte em vez de um resumo de IA. Para manter as solicitações em escala de livro econômicas, o Designer exige pelo menos três questões solicitadas quando as fontes selecionadas contiverem entre 100.000 e 499.999 tokens estimados, e pelo menos cinco quando houver 500.000 tokens ou mais. Fontes mais curtas podem gerar uma questão.

## Revisar antes de inserir

Em **Revisão**, verifique e edite em cada candidato:

- o texto da questão;
- as opções de resposta ou respostas aceitas para preenchimento;
- a seleção da resposta correta;
- a explicação;
- a dificuldade e pontuação; e
- a citação da fonte.

Desmarque **Aceitar** ou escolha **Descartar** para qualquer candidato que você não desejar. Escolha **Inserir selecionados** somente após as questões restantes estarem prontas para a edição e visualização normais do Designer.

!!! important
    O resultado da IA pode ser incompleto, ambíguo ou incorreto, mesmo quando cita uma fonte. Um especialista no assunto deve verificar o enunciado, gabarito, explicação, dificuldade, acessibilidade e pontuação antes da aplicação.

## Evidências e verificação de duplicatas

Os candidatos devem citar o texto encontrado na página do PDF, seção do Word, slide do PowerPoint, intervalo de linhas do texto, cabeçalho do Markdown ou cabeçalho do HTML indicados antes de poderem chegar à Revisão.

A detecção de duplicatas compara os candidatos com:

- outros candidatos na geração atual; e
- questões já existentes no documento aberto atualmente.

O Designer intencionalmente não compara questões em outros documentos, exames ou conteúdos da organização.

## Se a geração não for concluída

- Confirme se o arquivo é de um tipo suportado e contém texto legível suficiente.
- Para texto, Markdown e HTML, salve o arquivo como UTF-8.
- Para PDF, execute o OCR se você não conseguir selecionar e copiar seu texto.
- Confirme se a quantidade de questões solicitadas atende ao mínimo exigido para fontes grandes.
- Selecione menos fontes ou fontes mais direcionadas e tente novamente.
- Verifique a cota incluída restante da organização e o saldo pré-pago.
- Se a cota estiver esgotada, abra **Faturamento → Saldo Pré-pago** e adicione pelo menos o valor restante indicado na janela de elaboração por IA.

Após a inserção, use a [visualização e verificação de qualidade da questão](questions.md#preview-and-quality-check) normal antes de salvar e exportar o projeto.

## Criar questões que usam recursos visuais

Quando uma fonte selecionada contém uma imagem suportada, cada linha de estrutura oferece estas opções visuais:

| Escolha | O que o Designer faz | Uso de questões incluídas |
| --- | --- | ---: |
| Sem recurso visual | Gera uma questão apenas de texto. | 1 |
| Reutilizar imagem da fonte | Usa uma imagem relevante extraída do local da fonte citado. | 1 |
| Gerar novo recurso visual | Cria um recurso visual distinto em 1K que testa um conceito semelhante. | 4 |
| Automático | Escolhe texto, reutilização da fonte ou um novo recurso visual de acordo com a fonte e devolve as questões reservadas não utilizadas após o ajuste. | 1 ou 4 |

Uma questão visual deve citar texto de origem legível da mesma página de PDF, slide de PowerPoint, seção de documento ou outro local de origem de sua imagem de referência. O Designer evita capas, logotipos, imagens decorativas e pré-textuais não relacionados. Recursos visuais recém-gerados mantêm sua linhagem de fonte, modelo e tarefa, e permanecem pendentes de revisão humana.

Antes de inserir um candidato visual, verifique se a imagem é relevante, não revela a resposta e possui um texto alternativo preciso e uma descrição longa útil. Uma imagem com falha ou rejeitada não consome a cota da organização nem o saldo pré-pago.
