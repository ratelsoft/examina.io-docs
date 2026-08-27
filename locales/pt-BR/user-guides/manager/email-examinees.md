---
title: "Envie e-mails para seus candidatos"
description: "Envie convites e resultados de exames a partir do examina.io Manager usando marcadores de personalização, incluindo links de acesso direto para o candidato."
tags: [exam invitation, examinee email, magic link, manager, placeholders]
translation_source: user-guides/manager/email-examinees.md
translation_source_sha256: 5fc7cb4dd93fe7848375d20f62bf4c1a125a37385e6efd89d174ef4a5460b211
---

# Envie e-mails para seus candidatos

O Manager pode enviar e-mails para as pessoas vinculadas a um exame: um convite antes da realização da prova ou o resultado depois. Você escreve a mensagem uma vez e o Manager a personaliza para cada destinatário antes de enviar.

Selecione o exame e use **Enviar e-mail para candidatos** no painel de candidatos vinculados. Somente os candidatos que tiverem um endereço de e-mail em seu cadastro receberão a mensagem.

## Marcadores de personalização

Escreva `#[CODE]` na sua mensagem e cada candidato receberá o seu próprio código no lugar. Os marcadores funcionam tanto na linha de assunto quanto no corpo do e-mail.

### O candidato

| Marcador | Substituído por |
|---|---|
| `#[FNAME]` | Primeiro nome |
| `#[MNAME]` | Nome do meio ou nada |
| `#[LNAME]` | Sobrenome |
| `#[FLNAME]` | Nome completo |
| `#[TITLE]` | *Sr.* ou *Sra.*, com base no gênero cadastrado |
| `#[GEN]` | Gênero em texto |
| `#[CODE]` | Código ou ID do candidato |
| `#[PASS]` | Senha |
| `#[EMAIL]` | Endereço de e-mail |
| `#[PHONE]` | Número de telefone ou nada |
| `#[DOB]` | Data de nascimento |
| `#[PIC]` | A fotografia do candidato, como imagem |

### O exame

| Marcador | Substituído por |
|---|---|
| `#[EXAM]` | Título do exame |
| `#[ECODE]` | Código do exame |
| `#[LINK]` | O link do exame, como um link clicável |
| `#[MAGICLINK]` | Um link de login para esse candidato específico — veja abaixo |
| `#[TIME]` | O horário de início atribuído ao candidato, ou nada caso nenhum horário tenha sido definido |
| `#[PAPERS]` | As provas às quais este candidato está vinculado |

### O resultado

| Marcador | Substituído por |
|---|---|
| `#[SCORE]` | Pontuação obtida |
| `#[MAX]` | Pontuação máxima possível |
| `#[PERCENT]` | Pontuação em porcentagem |
| `#[RESULT]` | Um resumo formatado do resultado |

!!! warning "Os marcadores de resultado só devem ser usados em e-mails de resultado"
    Eles obtêm as informações de uma tentativa concluída. Em um convite enviado antes de qualquer pessoa realizar o exame, não há pontuação para substituir e eles são exibidos em branco — deixando frases incompletas. Mantenha-os fora dos convites.

## Links de login

O `#[MAGICLINK]` insere um link que faz o login direto desse candidato no exame. Ele não precisa digitar um código ou senha; o link já carrega sua identidade.

Vale a pena usar esse recurso quando a distribuição de senhas for a parte complicada do seu processo — candidatos mais jovens, turmas grandes ou qualquer pessoa com probabilidade de errar a digitação de um código na manhã da prova.

```text
Hello #[FNAME],

Your exam, #[EXAM], starts at #[TIME].

Open it here: #[MAGICLINK]

If the link does not work, sign in at #[LINK] with
code #[CODE] and passcode #[PASS].
```

### O que saber antes de usar

**Envie também o código e a senha.** O e-mail é a parte menos confiável do dia da prova — filtros, atrasos, um candidato lendo o e-mail em um celular no qual não fará o exame. Trate o link como o caminho conveniente e as credenciais como alternativa de emergência, exatamente como no exemplo acima.

**O link é pessoal e é uma credencial.** Qualquer pessoa em posse dele pode realizar o exame como aquele candidato. Oriente os candidatos a não o encaminharem. Ele não é mais compartilhável do que uma senha, mas é mais fácil de encaminhar por acidente.

**Um candidato não pode fazer a prova duas vezes ao mesmo tempo.** Se o link for aberto enquanto o candidato já estiver com o exame aberto em outro lugar, a segunda tentativa será recusada. Um candidato cujo navegador tenha travado pode reabrir o mesmo link e continuar.

**O link deixa de funcionar quando o exame é encerrado.** Ele expira três dias após ser enviado ou logo após o término do exame quando o candidato foi vinculado com um horário de início. Ele também deixa de funcionar assim que o candidato envia a prova, se você tornar o exame invisível ou se remover o vínculo do candidato.

**O reenvio é seguro.** Um e-mail de lembrete reutiliza o link que já está na caixa de entrada do candidato em vez de substituí-lo, para que o primeiro e-mail continue funcionando.

### Quando um link não funciona

O candidato é direcionado para a página de login desse exame com uma mensagem explicando o motivo, e pode fazer login com seu código e senha. Um link expirado informa isso claramente, diferentemente de um link que nunca foi válido para aquele exame, de modo que o candidato não seja informado de que suas credenciais estão incorretas quando o link simplesmente tiver expirado.

A única exceção é um exame que foi excluído. Como não resta nenhum exame para exibir uma página de login, o link leva a uma página de erro (não encontrada).

## Antes de enviar

1. Envie um teste para você mesmo primeiro, usando um candidato de teste vinculado ao exame.
2. Verifique se todos os marcadores foram resolvidos — um marcador com erro de digitação é enviado como texto literal.
3. Confirme se os destinatários correspondem à lista esperada na relação de vinculados ao exame.
4. Verifique o horário de início e o fuso horário na mensagem em comparação com o vínculo.

## Próxima etapa

Continue com [Entregar, monitorar e relatar](deliver-monitor-report.md).
