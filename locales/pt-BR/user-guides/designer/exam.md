---
title: "A prova"
description: "Configure o título da prova, código, marca, descrição, instruções, fluxo de cadernos e visibilidade das respostas no examina.io Designer."
tags: [designer, exam settings, exam code, branding, paper flow]
translation_source: user-guides/designer/exam.md
translation_source_sha256: 08c940d21a9db0e95244f721e5db54146dfe7c47b7d4b9ec56cc739ca87bf2d8
---

# A prova

Selecione uma prova no Exam Explorer e o painel de edição mostrará tudo o que se aplica à prova como um todo. A maior parte é visível para o candidato, portanto vale a pena dedicar uma atenção cuidadosa a esta etapa, em vez de apenas preencher os campos para avançar na tela.

![Propriedades e configurações da prova](../../assets/images/designer/exam-properties.png)

## Título da prova

O nome que o candidato vê ao realizar a prova. Escreva-o da mesma forma que você imprimiria em um papel: *Northgate Entrance Examination*, e não *entrance-final-v2*.

!!! note "Sobre os exemplos"
    As capturas de tela nas páginas do Designer usam um projeto de exemplo, **Northgate Entrance Exam 2026**, contendo uma única prova chamada *Northgate Entrance Examination* com seis cadernos. Sempre que este guia citar o valor de um campo, trata-se do valor visível nesse exemplo.

## Código da prova

**Obrigatório, e o campo com maior probabilidade de causar problemas mais tarde.**

O código identifica a prova quando ela chega ao Manager, por isso ele precisa ser exclusivo em todas as provas que sua organização importar. Duas provas que compartilham o mesmo código não podem ser importadas corretamente.

Duas regras que o campo impõe:

- **Sem espaços**
- **Apenas letras e números** — sem pontuação, traços ou sublinhados

`NGCENTRY26` está correto e é o código usado no exemplo. `NGC ENTRY 26` e `NGC-ENTRY-26` não são aceitos.

!!! tip "Defina um padrão antes da sua segunda prova, não da vigésima"
    Algo como `DISCIPLINA` + `ANO` + `APLICACAO` permanece legível e exclusivo: `NGCENTRY26`, `NGCMOCK26`. Adaptar um padrão posteriormente significa ter que reimportar provas que já estão em uso.

## Banner de marca e cor

Opcional. O banner é exibido ao candidato enquanto ele realiza a prova, e a cor personaliza a interface ao redor.

Use estes recursos quando uma mesma organização realiza provas em nome de vários departamentos ou clientes, e cada um precisa ter sua própria identidade visual. O botão **Limpar** remove qualquer um dos dois sem afetar o outro.

## Descrição

Exibida ao candidato antes de ele começar, e a primeira coisa que um candidato ansioso vai ler. Explique em linguagem simples o que a prova **é** e o que ela **abrange**.

Informações úteis para incluir aqui:

- para que serve a prova — admissão, fim de módulo, simulado
- quais disciplinas ou tópicos ela abrange e quantos cadernos possui
- aproximadamente quanto tempo dura toda a aplicação
- o que significa uma aprovação, caso isso já esteja definido

O exemplo usa:

> Seis cadernos abrangendo raciocínio quantitativo, raciocínio verbal, química, bioquímica, atualidades e ensino religioso.

Evite repetir o título da prova e evite referências internas, como números de versão ou códigos de comissão. O candidato não tem o que fazer com essas informações.

## Instrução geral

Também exibida antes do início da prova. Serve para as regras da aplicação: informações que o candidato precisa saber para realizar a prova corretamente, aplicando-se a **todos** os cadernos.

Informações úteis para incluir aqui:

- se devem responder a todas as questões ou se podem escolher
- se podem navegar entre os cadernos e se podem retornar
- o que é permitido — calculadora, anotações, rascunho
- o que acontece se a conexão cair ou o navegador fechar
- como relatar um problema durante a prova
- se o progresso é salvo à medida que respondem

O exemplo usa:

> Responda a todas as questões. Você pode navegar entre os cadernos até enviar. Seu progresso é salvo à medida que você responde.

Essa última frase faz mais diferença do que parece: candidatos que não sabem que suas respostas estão sendo salvas vão evitar navegar e passarão a prova apreensivos com medo de perder o trabalho feito.

!!! tip "Informe o que acontece em caso de imprevistos"
    A instrução que mais vale a pena incluir é a que ninguém escreve: o que fazer se a conexão cair. Um candidato que sabe que pode retornar à prova voltará a fazer o teste. Aquele que não sabe pode simplesmente desistir.

Instruções específicas de cada caderno devem ficar em [o caderno](paper.md) — tempo, escolha de questões e qualquer item válido apenas para uma disciplina. Tudo o que você precisaria repetir em cada caderno deve ficar aqui.

## Fluxo de cadernos de prova

Para provas com mais de um caderno, isto define como o próximo caderno é disponibilizado.

| Configuração | Comportamento |
|---|---|
| **Server Controlled** | O servidor decide quando cada caderno abre. Todos avançam juntos |
| **Client Controlled** | O candidato avança quando termina o caderno atual |
| **Force Continuous** | Os cadernos são apresentados em sequência, sem interrupção |

Escolha **Server Controlled** para uma aplicação em que todos devem estar no mesmo caderno ao mesmo tempo. Escolha **Client Controlled** quando os candidatos puderem trabalhar no seu próprio ritmo dentro de um limite de tempo geral.

## Mostrar respostas após a prova

Define se o candidato vê quais respostas estavam certas depois de enviar a prova.

Útil para simulados e revisões. Quase sempre inadequado para uma avaliação oficial, pois entrega o gabarito a todos que realizam a prova com antecedência.

## Permitir navegação entre cadernos

Define se o candidato pode retornar a um caderno que já tenha saído.

Defina como **Não** quando cada caderno deve ser encerrado após o envio. Defina como **Sim** quando a prova inteira for na verdade um único exame longo dividido em partes e os candidatos tiverem liberdade para retornar aos conteúdos.

## Antes de continuar

O código da prova é a única configuração que realmente traz problemas para alterar depois, pois é a forma como o Manager reconhece a prova. Todo o resto pode ser editado e reexportado sem consequências.

A seguir: [O caderno](paper.md).
