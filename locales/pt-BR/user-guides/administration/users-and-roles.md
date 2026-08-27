---
title: "Gerenciar usuários e funções de conta"
description: "Adicione Usuários da equipe, escolha funções de conta do examina.io, redefina o acesso e aplique permissões de menor privilégio para equipes de avaliação."
tags: [account roles, administrators, invigilators, user management]
translation_source: user-guides/administration/users-and-roles.md
translation_source_sha256: 0de577eb6227a78de5c3212ee769ac9f5df03d7870c962fa0fd9a33b2883d719
---

# Gerenciar Usuários e funções de conta

Usuários são contas de colaboradores para criação, administração ou fiscalização de provas.
Eles não são registros de candidatos.

Contas Root e Administrator podem abrir **Início → Usuários**. A tabela Usuários
mostra o nome, endereço de e-mail e tipo de conta de cada membro da equipe visível.

![A tabela Usuários com uma conta Regular de coordenador de provas](../../assets/images/administration/users-and-roles.png)

## Escolher uma função de conta

| Função | Atribuir a |
| --- | --- |
| **Root** | Um proprietário principal da organização que precisa de faturamento e administração completa da organização |
| **Administrator** | Um administrador de confiança que gerencia Usuários, Circles e Configurações |
| **Regular** | Um autor de questões, coordenador de provas ou outro membro da equipe que precisa do Designer ou Manager |
| **Invigilator** | Uma pessoa que apenas supervisiona provas ao vivo elegíveis com fiscalização de provas |

Use a função mais baixa que suporte o trabalho da pessoa. Veja [Funções e
permissões de usuário](../../getting-started/roles-and-permissions.md) para o modelo de
acesso detalhado.

## Adicionar um Usuário

1. Abra **Início → Usuários**.
2. Selecione **Adicionar Novo Usuário**.
3. Informe o nome da pessoa e o endereço de e-mail de trabalho.
4. Escolha o tipo de conta.
5. Envie o formulário.
6. Confirme se a pessoa concluiu o processo necessário de verificação de conta ou
   definição de senha.
7. Adicione o Usuário aos Circles apropriados.

Use uma conta de trabalho individual para cada pessoa. Credenciais compartilhadas de
administrador ou invigilator enfraquecem a responsabilidade e dificultam o desligamento.

## Redefinir ou remover o acesso

Os botões de ação na tabela Usuários permitem que um administrador redefina a senha
de um Usuário ou o exclua.

Antes de redefinir uma senha, verifique a identidade do solicitante por meio de um
canal aprovado. Antes de excluir um Usuário:

1. confirme a conta exata;
2. revise qualquer transição operacional;
3. remova ou reatribua responsabilidades do Circle;
4. preserve as informações de auditoria necessárias; e
5. notifique o proprietário da conta de acordo com a política.

Excluir um Usuário da equipe é diferente de excluir um candidato.

## Revisar o acesso regularmente

Pelo menos antes de cada avaliação de grande porte:

- remova contas de pessoas que não precisam mais de acesso;
- reduza contas de Administrator que não administram mais a plataforma;
- confirme se os Invigilators estão vinculados apenas às provas necessárias por meio dos Circles;
- verifique se usuários Regular não conseguem ver provas ou candidatos não relacionados; e
- proteja contas Root com credenciais fortes e exclusivas.

## Solucionar problemas de falta de acesso

Se um membro da equipe conseguir fazer login, mas não conseguir ver uma prova ou candidato:

1. confirme se a função da conta oferece suporte ao aplicativo necessário;
2. confirme se o Usuário pertence ao Circle relevante;
3. confirme se a prova e os candidatos estão nesse mesmo Circle; e
4. saia e faça login novamente após alterações de permissão, quando necessário.

Continue em [Circles e permissões](circles-and-permissions.md).
