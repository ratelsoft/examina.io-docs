---
title: "Visão geral da plataforma examina.io"
description: "Entenda como Designer, Manager, Proctor, Client, usuários, grupos e Circles trabalham juntos no ciclo de vida de avaliação do examina.io."
tags: [assessment platform, client, designer, examinees, exams, manager, proctoring]
translation_source: getting-started/overview.md
translation_source_sha256: 3758552e04cfd298de85e07c2a290dd7c4675706cab28137e1fb9cf0b0dae7ca
---

# Entenda a plataforma examina.io

O examina.io separa o trabalho de avaliação em aplicações focadas. Autores de questões podem criar conteúdos sem acesso aos registros de candidatos, administradores podem agendar e aplicar exames, fiscais de prova podem supervisionar apenas os exames aos quais foram atribuídos, e os candidatos usam um aplicativo Client dedicado.

![A galeria de aplicativos do examina.io mostra o Designer, o Manager e o Client](../assets/images/dashboard/apps-gallery.png)

## Fluxo de trabalho de avaliação

1. **Crie** um projeto de exame, provas, seções e questões no Designer.
2. **Exporte** o exame concluído como um arquivo `.smex`.
3. **Importe** esse arquivo no Manager.
4. **Adicione candidatos** individualmente ou importe-os do Excel, CSV ou texto.
5. **Organize e atribua** candidatos com Groups, mapeamentos de exames e mapeamentos de provas.
6. **Configure opções de aplicação** como visibilidade, horário de início, exibição de resultados, dispositivos suportados, verificação de identidade e fiscalização de provas ao vivo.
7. **Compartilhe o link do exame** ou envie um e-mail do Manager.
8. **Monitore e gere relatórios** enquanto o exame estiver ativo e após a sua conclusão.

A mesma pessoa pode realizar várias etapas em uma organização pequena. Organizações maiores podem separar responsabilidades com [funções de conta e Circles](roles-and-permissions.md).

## Designer

O Designer é o aplicativo de autoria de exames. Use-o para criar projetos de exame, organizar uma ou mais provas, adicionar seções, escrever questões, definir regras de pontuação e tempo, e importar conteúdos de questões existentes.

![A mesma questão no painel de edição e no painel de visualização do Designer](../assets/images/general/designer-edit-preview.png)

Quando a autoria estiver concluída, exporte o exame como um arquivo `.smex` criptografado para aplicação através do Manager. Comece com a [Introdução ao Designer](../user-guides/designer/introduction.md).

## Manager

O Manager conecta o conteúdo do exame às pessoas que o realizam. Administradores e equipe autorizada usam o Manager para:

- importar arquivos de exame `.smex`;
- criar ou importar registros de candidatos;
- organizar candidatos em Groups;
- mapear candidatos ou Groups para um exame e suas provas;
- controlar a visibilidade do exame e as configurações de aplicação;
- abrir ou distribuir um link de exame; e
- monitorar o progresso e gerar resultados ou relatórios.

![Um exame no Manager, com seus candidatos mapeados](../assets/images/manager/exam-details.png)

Consulte a [Visão geral do Manager](../user-guides/manager/overview.md) para ver a navegação principal e a sequência operacional recomendada.

## Proctor

O Proctor é o espaço de trabalho para fiscalização ao vivo. Quando a fiscalização de provas ao vivo está ativada para um exame, fiscais autorizados podem revisar as transmissões disponíveis de áudio, webcam e tela, comunicar-se com um candidato e aprovar o início do exame quando o fluxo de trabalho configurado exigir.

![O espaço de trabalho do Proctor, com um bloco por candidato](../assets/images/general/proctoring-view.png)

Cada candidato conectado aparece como um bloco com exibições de Detalhes, Webcam e Tela, controles de gravação e mudo, e uma caixa de mensagem direta.

Ative apenas os recursos de fiscalização de provas que sua organização tem autorização para usar e informe os candidatos sobre os dados que serão coletados.

## Client

O Client é o aplicativo voltado para o candidato. Os candidatos abrem o link do exame, inserem suas credenciais atribuídas, concluem todas as verificações de sistema ou identidade necessárias e realizam as provas mapeadas.

![O aplicativo Client voltado para o candidato](../assets/images/client/question.png)

O Client salva periodicamente o estado do exame enquanto houver uma conexão disponível. O [guia do dia da prova](../user-guides/client/take-an-exam.md) explica como os candidatos devem se preparar e o que fazer se a conexão for interrompida.

## Users, Groups, and Circles

Esses conceitos parecidos resolvem problemas diferentes:

| Conceito | Finalidade |
| --- | --- |
| **User** | Uma conta de equipe que faz login no examina.io, como um administrador, coordenador de exame ou fiscal de prova. |
| **Examinee** | Um candidato ou estudante que entra por meio de um link de exame para realizar uma avaliação. |
| **Group** | Uma coleção reutilizável de candidatos, usada para atribuições em massa de exames e provas. |
| **Circle** | Um limite de permissão que conecta usuários selecionados a exames e candidatos selecionados. |

Use Groups para reduzir o trabalho repetitivo de atribuição. Use Circles para restringir o que a equipe pode ver e gerenciar. Saiba mais em [Groups e atribuições de exames](../user-guides/manager/groups-and-assignments.md) e [Circles e permissões](../user-guides/administration/circles-and-permissions.md).

## Integrações

As organizações podem conectar o examina.io a outros sistemas com:

- chaves de API públicas e secretas;
- um webhook de conclusão;
- o widget incorporável do Client;
- a API REST; e
- integrações com plataformas de aprendizagem suportadas exibidas em Configurações.

Comece com [Chaves de API e webhooks](../integrations/api-keys-and-webhooks.md) ou vá diretamente para a [Referência da API](../api/index.md).

## Próximo passo

Siga o [início rápido](quick-start.md) para obter um checklist prático para o seu primeiro exame.
