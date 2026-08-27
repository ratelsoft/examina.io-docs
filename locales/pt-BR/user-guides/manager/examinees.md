---
title: "Adicionar e importar candidatos no examina.io"
description: "Crie registros de candidatos individualmente ou importe candidatos de arquivos Excel, CSV ou texto no examina.io Manager."
tags: [candidate import, csv import, examinees, excel import, manager]
translation_source: user-guides/manager/examinees.md
translation_source_sha256: 173ab50c30199eb9a9667889688609598592bbab3972eab3326f03082ffd9b90
---

# Adicionar e importar candidatos

Um **candidato** é quem realiza um exame por meio do aplicativo Client. Os candidatos são separados dos **Usuários** da equipe.

![A aba Candidatos](../../assets/images/manager/examinees-tab.png)

## Adicionar um candidato

1. Abra o **Manager**.
2. Selecione **Arquivo → Adicionar novo candidato**.
3. Insira o nome e o gênero do candidato.
4. Insira um código exclusivo para o candidato ou escolha a atribuição automática de código.
5. Insira uma senha ou escolha a geração de senha.
6. Adicione detalhes opcionais, como endereço de e-mail, número de telefone, data de nascimento, título ou fotografia.
7. Salve o registro.

O código identifica o candidato durante o login e deve ser exclusivo. Uma foto quadrada de cerca de 256 × 256 pixels funciona melhor quando seu fluxo de trabalho utiliza imagens dos candidatos ou verificação de identidade.

![Um registro de candidato salvo](../../assets/images/manager/examinee-details.png)

## Preparar um arquivo de importação

O Manager dá suporte a:

- Pastas de trabalho do Excel: `.xls` e `.xlsx`
- texto delimitado: `.csv` e `.txt`

Coloque um candidato em cada linha. Os campos obrigatórios são:

- nome;
- sobrenome; e
- gênero.

Os códigos e as senhas podem ser gerados quando forem omitidos. Se você incluir números de telefone, use o formato internacional, como `+14165550100`. Se incluir datas de nascimento, use o formato exibido pelo importador, como `8/7/1900`.

Para uma importação confiável, use uma linha de cabeçalho com nomes de colunas claros e salve uma cópia do arquivo de origem original.

Exemplo de CSV:

```csv
student_id,first_name,last_name,gender,email
STU-1001,Avery,Okafor,F,avery@example.edu
STU-1002,Noah,Martin,M,noah@example.edu
```

## Importar um arquivo

1. Selecione **Arquivo → Importar candidatos de arquivo/Excel**.
2. Escolha o arquivo.
3. Para um arquivo de texto, escolha ou detecte automaticamente o separador, como vírgula, tabulação, pipe, ponto e vírgula ou dois-pontos.
4. Revise a pré-visualização dos dados.
5. Escolha se a segunda linha da pré-visualização deve ser exibida e se a primeira linha é um cabeçalho a ser ignorado.
6. Mapeie cada coluna de origem para o campo de candidato apropriado.
7. Opcionalmente, escolha um Grupo para os registros importados.
8. Escolha se o processo deve parar no primeiro erro.
9. Inicie a importação e revise cada linha adicionada, ignorada ou com falha.

Se a opção **Atualizar candidatos existentes se o código/ID do candidato corresponder** estiver disponível e selecionada, os códigos correspondentes poderão atualizar os registros existentes. Use essa opção apenas quando o arquivo de origem for confiável e o mapeamento de código tiver sido verificado.

## Validar o resultado

Após a importação:

- compare a contagem de registros adicionados com o arquivo de origem;
- pesquise por vários códigos de candidatos;
- verifique os nomes, endereços de e-mail e mapeamentos de gênero;
- verifique quaisquer códigos ou senhas gerados automaticamente;
- confirme a associação opcional a Grupos; e
- exporte ou registre o log de importação de acordo com o seu procedimento operacional.

Linhas sem os campos obrigatórios são ignoradas ou causam a interrupção de acordo com a configuração de erro escolhida.

## Proteger os dados dos candidatos

- Importe apenas os dados necessários para administrar a avaliação.
- Não coloque senhas em uma planilha compartilhada publicamente.
- Use um canal seguro aprovado para distribuir credenciais.
- Remova registros de teste antigos e cópias locais de acordo com sua política de retenção.
- Confirme se sua organização tem uma base legal para quaisquer dados de foto, biometria ou fiscalização de provas que coletar.

## Próximo passo

Crie Grupos ou atribua candidatos diretamente seguindo [Grupos e atribuições de exames](groups-and-assignments.md).
