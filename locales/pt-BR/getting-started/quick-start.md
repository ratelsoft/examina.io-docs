---
title: "Início rápido do examina.io"
description: "Configure sua organização, crie ou importe um exame, adicione candidatos, atribua provas e publique seu primeiro exame no examina.io."
tags: [exam setup, getting started, online assessment, quick start]
translation_source: getting-started/quick-start.md
translation_source_sha256: 535b1a2e6b873d0f6b729817ca3c9e64db7b8931167422d03e8816351d9da894
---

# Início rápido: publique seu primeiro exame

Esta lista de verificação guia um administrador de organização desde uma conta nova até um link de exame testável. Se outra pessoa elaborar as perguntas, ela poderá concluir as etapas do Designer e enviar o arquivo `.smex` exportado para você.

## 1. Confirme o acesso da equipe

Em **Início**, verifique se as pessoas que estão preparando a avaliação possuem as [funções de conta](roles-and-permissions.md) corretas. Use **Usuários** para adicionar contas de equipe e **Círculos** se o acesso precisar ser limitado a exames ou candidatos específicos.

![A galeria de aplicativos do examina.io após fazer login](../assets/images/dashboard/apps-gallery.png)

## 2. Crie o conteúdo do exame

Abra o **Designer** e, em seguida:

1. Selecione **Arquivo → Novo projeto de exame**.
2. Crie um exame e pelo menos uma prova.
3. Adicione seções e perguntas.
4. Defina as instruções, tempo, pontuação e regras de navegação do exame e da prova.
5. Visualize o conteúdo.
6. Exporte o exame concluído como um arquivo `.smex`.

Para obter instruções detalhadas de criação, consulte [Apresentando o Designer](../user-guides/designer/introduction.md).

## 3. Importe o exame para o Manager

Abra o **Manager** e escolha **Arquivo → Adicionar novo exame**. Selecione o arquivo `.smex` exportado e aguarde a mensagem de sucesso. Revise o título, código, provas e propriedades de aplicação importados antes de fazer qualquer atribuição.

Consulte [Importar exames](../user-guides/manager/import-exams.md).

## 4. Adicione candidatos

Escolha uma destas abordagens:

- **Arquivo → Adicionar novo candidato** para uma ou poucas pessoas.
- **Arquivo → Importar candidatos do arquivo/Excel** para uma turma ou grupo.

Um candidato é a pessoa que realiza um exame, não um usuário da equipe. Mantenha o código ou ID dele exclusivo. Se você importar um arquivo, verifique o mapeamento dos campos e faça uma visualização prévia antes de iniciar a importação.

Consulte [Adicionar e importar candidatos](../user-guides/manager/examinees.md).

## 5. Crie grupos quando for útil

Os grupos são opcionais, mas reduzem o trabalho repetitivo. Crie um grupo para uma turma, grupo de alunos, departamento ou sessão e, em seguida, adicione os candidatos correspondentes.

Você pode atribuir um grupo inteiro a um exame e, ao mesmo tempo, selecionar as provas e o horário de início opcional para essa atribuição.

## 6. Atribua o exame e as provas

Selecione um exame e escolha **Mapear candidatos** ou **Mapear grupos**. Mova as pessoas ou grupos desejados para a lista selecionada, prossiga para o mapeamento de provas e escolha as provas que eles poderão realizar.

Se você definir um horário para o exame, selecione também o fuso horário correto. O horário mapeado é o momento mais cedo em que o exame fica disponível para essa atribuição.

## 7. Configure a aplicação

Antes de compartilhar o link, revise:

- a visibilidade do exame;
- se os resultados são exibidos após a conclusão;
- os requisitos de fiscalização de provas ao vivo e verificação de identidade;
- o acesso permitido por celular ou tablet;
- o comportamento em caso de desconexão da internet; e
- quaisquer isenções de fiscalização de provas.

Mantenha o exame invisível enquanto o estiver preparando. Torne-o visível apenas quando o exame e as atribuições estiverem prontos.

## 8. Teste a jornada do candidato

Abra o link do exame em uma janela anônima do navegador. Confirme se:

- o logotipo da organização e o estilo de login estão corretos;
- o candidato de teste consegue entrar;
- as provas esperadas estão disponíveis;
- as instruções e o tempo estão corretos; e
- todas as verificações de dispositivo, câmera, microfone ou identidade funcionam como esperado.

Use um candidato de teste fictício ou designado em vez de um candidato real.

## 9. Publique e comunique

Torne o exame visível e, em seguida, copie **Abrir link do exame** ou use [**Enviar e-mail para candidatos**](../user-guides/manager/email-examinees.md) no Manager. Inclua:

- a data, horário de início e fuso horário do exame;
- o link do exame;
- o código do candidato e o método de distribuição da senha;
- os requisitos de dispositivo e navegador;
- os requisitos de fiscalização de provas; e
- um contato de suporte.

Compartilhe o [guia do candidato para o dia da prova](../user-guides/client/take-an-exam.md) com os participantes.

## 10. Monitore e gere relatórios

Durante a sessão, atualize o Manager para ver os status de conexão atuais. Se a fiscalização de provas ao vivo estiver ativada, abra o exame em **Proctoring**. Depois que os candidatos terminarem, revise os resultados individuais ou gere um relatório do exame.

O [guia de aplicação, monitoramento e relatórios](../user-guides/manager/deliver-monitor-report.md) contém a lista de verificação operacional detalhada.

!!! tip "Faça um ensaio"
    Para uma avaliação de alto impacto, realize um curto ensaio com as mesmas regras de dispositivo, condições de rede e configurações de fiscalização de provas planejadas para o exame real.
