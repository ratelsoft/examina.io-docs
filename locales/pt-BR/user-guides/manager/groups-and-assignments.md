---
title: "Grupos e atribuições de exames no examina.io"
description: "Organize candidatos em Grupos e mapeie pessoas, Grupos, exames, provas, horários de início e fusos horários no examina.io Manager."
tags: [exam assignment, exam mapping, examinee groups, manager, paper mapping]
translation_source: user-guides/manager/groups-and-assignments.md
translation_source_sha256: 4c6bbfaf4fda4dda6ae0d94a03fd399b97cb5b7665f17fbe98f789618efe5c4d
---

# Grupos e atribuições de exames

O Manager usa **Grupos** para coleções reutilizáveis de candidatos e **mapeamentos** para decidir quais provas de exame cada candidato pode realizar.

## Quando usar um Grupo

Crie um Grupo para um conjunto de pessoas que você gerencia juntas regularmente, como:

- um curso ou turma;
- uma turma de ingresso ou coorte;
- um centro de avaliação;
- um departamento; ou
- uma sessão agendada.

Um Grupo não concede permissões de equipe. Use um [Circle](../administration/circles-and-permissions.md) para controle de acesso.

## Criar um Grupo

1. Abra o **Manager**.
2. Selecione **Arquivo → Criar novo Grupo**.
3. Insira um nome exclusivo e uma descrição útil.
4. Salve o Grupo.
5. Selecione o Grupo e adicione candidatos da lista pesquisável.

![Um Grupo e seus membros](../../assets/images/manager/group-details.png)

Os botões ao lado da lista de membros cobrem todas as formas de preencher um Grupo: adicionar candidatos um por um, adicionar vários de uma vez, adicionar os candidatos correspondentes a um arquivo enviado ou copiar os membros de outro Grupo.

Você também pode adicionar membros a um Grupo a partir do registro de um candidato ou atribuir candidatos importados a um Grupo durante a importação do arquivo.

## Mapear um candidato para um exame

1. Abra a aba **Candidatos** e selecione a pessoa.
2. Escolha a ação para mapear o candidato para um exame.
3. Pesquise e selecione um exame.
4. Prosiga para o mapeamento de provas.
5. Selecione as provas que o candidato pode realizar.
6. Opcionalmente, atribua o horário inicial do exame e escolha o fuso horário correto.
7. Salve o mapeamento.

Apenas um exame é selecionado em uma única operação de mapeamento, mas você pode mapear o mesmo candidato para exames adicionais em operações posteriores.

## Mapear vários candidatos a partir de um exame

1. Abra a aba **Exames** e selecione o exame.
2. Escolha **Mapear candidatos**.
3. Pesquise candidatos por nome, código ou campo adicional disponível.
4. Mova os candidatos desejados para a lista selecionada.
5. Prosiga para o mapeamento de provas.
6. Escolha as provas e o horário de início opcional.
7. Salve os mapeamentos.

## Mapear um Grupo

Você pode começar pelo exame ou pelo Grupo:

- Selecione um exame e escolha **Mapear Grupos**; ou
- selecione um Grupo e escolha **Mapear Grupo para exame**.

Ao mapear um Grupo, o Manager aplica a atribuição aos membros atuais do Grupo que ainda não foram mapeados para esse exame. Adicionar alguém ao Grupo posteriormente não significa que cada operação de mapeamento anterior seja repetida automaticamente, portanto, revise os candidatos mapeados do exame após alterações de membros.

## Escolha as provas e os horários com cuidado

As provas selecionadas são as provas que o candidato pode realizar no Client. Se um exame contiver várias provas, confirme se cada candidato possui a combinação correta.

O horário de início mapeado opcional é o horário inicial em que o exame fica disponível para essa atribuição. Sempre verifique:

- data do calendário;
- hora local;
- fuso horário;
- implicações do horário de verão; e
- se candidatos em regiões diferentes precisam de atribuições separadas.

## Verificar mapeamentos

Antes de publicar um exame:

![A lista de candidatos mapeados para um exame](../../assets/images/manager/exam-details.png)

1. Abra a lista de candidatos mapeados do exame.
2. Compare a contagem com a lista de inscritos pretendida.
3. Faça uma verificação por amostragem das atribuições de provas.
4. Verifique os horários de início e fusos horários.
5. Confirme que candidatos desistentes ou duplicados não estejam presentes.
6. Teste com uma conta de candidato que tenha o mesmo padrão de provas.

Excluir um mapeamento remove a atribuição; isso não exclui o candidato ou Grupo subjacente.

## Próxima etapa

Continue com [Entregar, monitorar e relatar](deliver-monitor-report.md).
