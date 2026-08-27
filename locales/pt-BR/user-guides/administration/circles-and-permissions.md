---
title: "Configure Círculos e permissões de exames"
description: "Crie Círculos no examina.io que conectam usuários, exames e candidatos para aplicar acesso delimitado para a equipe."
tags: [access control, circles, exam permissions, user permissions]
translation_source: user-guides/administration/circles-and-permissions.md
translation_source_sha256: b9c946628f9fcca401d26f0faab24b32e0a5ed14d358638d8aa3202c40724276
---

# Configure Círculos e permissões

Um Círculo é um limite de permissão formado por **Usuários**, **Exames** e **Candidatos** selecionados. Um Usuário pode trabalhar com os recursos disponibilizados por meio do Círculo, sujeito à função da conta do Usuário.

![Um Círculo resume seus candidatos, usuários e exames](../../assets/images/administration/circles-permissions.png)

## Planejar o Círculo

Use um Círculo para uma área de responsabilidade estável, como:

- um curso ou departamento;
- um programa de exames;
- um cliente ou locatário;
- um local escolar; ou
- um projeto de avaliação restrito.

Escolha um nome claro e uma tag curta, por exemplo **Biology 201** e **BIO-201**. Evite colocar informações confidenciais de candidatos no nome do Círculo.

## Criar um Círculo

1. Abra **Home → Círculos**.
2. Selecione **Adicionar Novo Círculo**.
3. Insira um nome exclusivo e uma tag opcional.
4. Selecione os Usuários que precisam de acesso.
5. Selecione os Exames que eles irão administrar ou fiscalizar.
6. Selecione os Candidatos que eles precisam visualizar ou gerenciar.
7. Salve o Círculo.

Contas Root e Administrador podem criar e editar Círculos. Outros Usuários autorizados podem ver os Círculos relevantes para eles.

## Verificar o limite

A tabela de Círculos mostra a contagem de Candidatos, Usuários e Exames em cada Círculo. Após salvar:

1. compare cada contagem com os membros pretendidos;
2. edite o Círculo e faça uma verificação pontual dos nomes em todas as três listas;
3. teste com uma conta Regular ou Fiscal;
4. verifique se exames e candidatos não relacionados não estão visíveis; e
5. verifique se os espaços de trabalho necessários do Proctor aparecem para os fiscais.

## Comparação entre Círculos e Grupos

| Círculo | Grupo |
| --- | --- |
| Controla o acesso da equipe | Organiza candidatos para operações em massa |
| Contém Usuários, Exames e Candidatos | Contém Candidatos |
| Usado em verificações de permissão do Home, Manager e Proctor | Usado no Manager para trabalhos de atribuição |

É comum usar ambos. Um Círculo de curso pode restringir a equipe do curso, enquanto um Grupo pode conter os alunos mapeados para uma sessão específica.

## Manter Círculos com segurança

- Atualize os membros quando as responsabilidades da equipe mudarem.
- Remova exames concluídos e acessos desatualizados de candidatos de acordo com a política.
- Mantenha recursos exclusivos para administradores fora de Círculos amplos.
- Revise os membros do Círculo antes de ativar a fiscalização ao vivo.
- Teste as alterações de permissão com uma conta de não administrador.

Excluir um Círculo remove o agrupamento de permissões. Confirme o impacto no acesso da equipe antes de excluí-lo.
