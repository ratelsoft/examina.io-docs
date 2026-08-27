---
title: "Importar uma prova no Manager do examina.io"
description: "Exporte uma avaliação .smex do Designer, importe-a no Manager e verifique a prova antes de atribuir candidatos."
tags: [designer export, exam import, manager, smex]
translation_source: user-guides/manager/import-exams.md
translation_source_sha256: cdd0384f56afe40f416a9be4f57bf31c41f1b3b32098cafb860f785f7f9aa421
---

# Importar uma prova no Manager

O Manager aceita pacotes de provas exportados pelo Designer como arquivos `.smex`. Importe o pacote antes de adicionar atribuições ou compartilhar um link de prova.

## Antes de importar

No Designer, confirme se:

- o título e o código da prova estão corretos;
- cada caderno contém as questões desejadas;
- a duração do caderno e as configurações de questões a responder estão corretas;
- a pontuação e as respostas corretas foram revisadas;
- as instruções e regras de navegação estão completas; e
- o projeto foi salvo antes da exportação.

Mantenha o projeto de origem como seu modelo editável principal. O arquivo `.smex` exportado é o pacote de aplicação.

## Importar o arquivo

![Arquivo → Adicionar Nova Prova](../../assets/images/manager/file-menu.png)

1. Abra o **Manager**.
2. Selecione **Arquivo → Adicionar Nova Prova**.
3. Arraste o arquivo `.smex` para a área de envio ou selecione-o com o seletor de arquivos.
4. Envie o arquivo.
5. Aguarde a mensagem de sucesso contendo o código e o título da prova importada.

Se o Manager informar que o tipo de arquivo não é suportado, volte ao Designer e exporte a prova no formato `.smex` suportado. Se o arquivo exceder o tamanho permitido para seu ambiente ou plano, reduza arquivos de mídia grandes e exporte novamente.

## Verificar a prova importada

Selecione a prova e revise o painel de detalhes:

![Os detalhes da prova importada](../../assets/images/manager/exam-details.png)

- título, código e versão da prova;
- fluxo dos cadernos da prova;
- visibilidade;
- tamanho do arquivo importado; e
- o horário em que foi adicionada.

**Tamanho do Arquivo da Prova** é a verificação rápida mais eficiente para confirmar se o pacote correto foi entregue — um valor muito menor do que o esperado geralmente significa uma exportação sem os arquivos de mídia.

Abra as informações do caderno e compare-as com o projeto no Designer. Não vincule candidatos reais até que o conteúdo e a duração estejam corretos.

## Atualizar uma prova com segurança

Se o conteúdo mudar após a importação:

1. Atualize e valide o projeto de origem no Designer.
2. Exporte um novo arquivo de aplicação.
3. Importe-o de acordo com o processo de mudança da sua organização.
4. Verifique novamente os mapeamentos, a visibilidade, a fiscalização de provas e a comunicação antes da liberação.

Não presuma que um arquivo recém-exportado preservará todas as configurações do lado da aplicação. Verifique o registro no Manager e teste a jornada no Client após qualquer substituição ou alteração de versão.

## Continuar a configuração

Em seguida, [adicione ou importe candidatos](examinees.md) e, depois, [vincule pessoas e cadernos](groups-and-assignments.md).
