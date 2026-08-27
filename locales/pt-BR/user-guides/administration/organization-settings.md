---
title: "Configurações da organização, marca e integrações"
description: "Configure domínios de incorporação aprovados, página de login do exame, logotipo, credenciais de API, webhook e integrações no examina.io."
tags: [api settings, branding, embed domains, organization settings, webhook]
translation_source: user-guides/administration/organization-settings.md
translation_source_sha256: 551087143ecc0eaf4a63a442e2ff2f2373d7c666d9cd232732c011d7788432d4
---

# Configurações da organização e marca

Contas Root e Administrator podem acessar **Início → Configurações** para gerenciar a marca de toda a organização, domínios de incorporação, credenciais de API, envio de webhooks e conexões com plataformas de aprendizagem suportadas.

![Configurações da organização para domínios, marca, chaves de API e webhook](../../assets/images/administration/organization-settings.png)

## Domínios de incorporação aprovados

A lista de permissões de domínios controla quais sites podem carregar o widget do Client.

1. Insira apenas o nome do host, sem **http://** ou **https://**.
2. Selecione **Adicionar domínio**.
3. Remova os domínios que não forem mais utilizados.

Por exemplo, insira **assessment.example.edu**, não
**https://assessment.example.edu/exams**.

Evite **Permitir todos os domínios** em produção. Se você adicionar o
**localhost** ou outro host de desenvolvimento, remova-o após os testes, pois ele
não é exclusivo da sua organização.

Veja [Incorporar o aplicativo Client](../../integrations/embedding-client-app.md).

## Logotipo da organização

O painel **Personalização do logotipo** controla o logotipo exibido nas exibições suportadas voltadas para a organização e para o candidato. Selecione **Enviar novo logotipo** e escolha um arquivo JPG, GIF ou PNG de até 512 KB.

Use um logotipo de alto contraste com espaçamento transparente ou neutro e, em seguida, verifique-o em telas de computador e celular.

## Página de login do exame

No painel **Experiência do Client**, defina a **Exibição de login do exame** como **Padrão**,
**Moderno** ou **Clássico**.
O Moderno e o Clássico podem usar uma imagem de fundo da organização. Se nenhuma for fornecida, o Client poderá exibir um plano de fundo padrão.

1. Escolha uma exibição de login e selecione **Salvar estilo**.
2. Selecione **Alterar imagem** para enviar um plano de fundo em JPG, GIF ou PNG.
3. Use uma imagem de 1920 × 1280 pixels quando possível e mantenha-a dentro do limite de tamanho exibido.
4. Selecione **Testar página de login do exame** e verifique a legibilidade, o posicionamento do logotipo e o comportamento em celular.

Veja [Personalizar a página de login do exame](../client/custom-login-page.md).

## Chaves de API

A **Chave pública da API** pode identificar integrações de navegador aprovadas, como o widget do Client. A **Chave secreta da API** autentica solicitações de servidor para servidor e nunca deve ser incluída no JavaScript do navegador, em código-fonte público, em um aplicativo de celular ou em capturas de tela de documentação.

O segredo é exibido apenas uma vez no momento da sua criação. Armazene-o imediatamente em um gerenciador de segredos aprovado. Gerar uma nova chave pode interromper integrações existentes até que todos os consumidores sejam atualizados.

Veja [Chaves de API e webhooks](../../integrations/api-keys-and-webhooks.md).

## Webhook de conclusão

Insira um URL de retorno HTTPS para receber uma notificação quando um exame for concluído. O endpoint deve validar as solicitações de acordo com o contrato atual da API, retornar uma resposta de sucesso prontamente e processar tarefas longas de forma assíncrona.

Não use uma página administrativa privada ou um URL contendo credenciais como o URL do webhook.

## Integrações com plataformas de aprendizagem

As configurações podem exibir conectores de plataformas de aprendizagem e registros LTI 1.3. A disponibilidade e os requisitos de configuração dependem do seu plano e da configuração da plataforma externa. Para fluxos completos de configuração e validação, veja [Integrar o examina.io ao Moodle](../../integrations/moodle-lms.md) e [Integrar o examina.io ao Canvas](../../integrations/canvas-lms.md) ou [Integrar o examina.io ao Blackboard Learn Ultra](../../integrations/blackboard-lms.md).

Use uma conta de integração dedicada quando apropriado, conceda apenas as permissões necessárias, documente o responsável e desconecte as integrações que não forem mais utilizadas.

## Checklist de controle de alterações

Após alterar as configurações da organização:

1. teste a página de login com um exame designado;
2. teste todos os domínios de incorporação em produção;
3. verifique os consumidores da API se alguma chave tiver mudado;
4. envie um evento de teste por meio do seu fluxo de trabalho de webhook, quando disponível; e
5. registre a alteração e o plano de reversão para ambientes de alto impacto.
