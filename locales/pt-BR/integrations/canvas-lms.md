---
title: "Integrar o examina.io ao Canvas usando LTI 1.3"
description: "Conecte o Canvas ao examina.io, escolha avaliações com LTI Deep Linking, inicie-as em um curso e envie notas com Assignment and Grade Services."
tags: [Canvas LMS, LTI 1.3, LMS integration, Deep Linking, AGS, NRPS, gradebook]
translation_source: integrations/canvas-lms.md
translation_source_sha256: a00b087c1df6149f09f18bf711a3a543691d492ce5a776d673d31fdcb8922f30
---

# Integrar o examina.io ao Canvas

Conecte o examina.io a uma conta raiz do Canvas e permita que professores adicionem avaliações publicadas a tarefas sem copiar links de exames. Os alunos abrem a avaliação dentro do Canvas sem precisar fazer login uma segunda vez, e o examina.io envia cada resultado de volta para a coluna correspondente no livro de notas do Canvas.

!!! tip "Valide antes de uma avaliação real"

    Conecte e valide todo o fluxo de trabalho em um curso de teste do Canvas com usuários fictícios antes de ativá-lo para uma avaliação real.

As capturas de tela usam um curso fictício da **Northbridge College**, **Introduction to Biology (BIO 101)**, e uma avaliação chamada **Cell Structure and Function**. A sua instituição, nome de host do Canvas, identificadores e nomes de cursos serão diferentes.

## O que a integração oferece

- **Um único login no Canvas:** os alunos não precisam fazer login no examina.io novamente quando abrem uma tarefa a partir do Canvas.
- **Seleção de avaliação publicada:** o LTI Deep Linking permite que o professor escolha o exame exato ao criar uma tarefa do tipo Ferramenta Externa.
- **Inclusão vinculada ao curso:** a publicação selecionada fica vinculada ao curso e à tarefa do Canvas que a criou.
- **Envio de notas:** o LTI Assignment and Grade Services (AGS) envia a pontuação para o usuário e coluna de notas corretos.
- **Lista de alunos do curso opcional:** o Names and Roles Provisioning Services (NRPS) pode fornecer os dados mínimos de associação ao curso exigidos por um fluxo de trabalho aprovado.

O Canvas chama esse padrão de posicionamento `assignment_selection`. A documentação oficial confirma que o posicionamento usa Deep Linking, carrega a avaliação da ferramenta escolhida para os estudantes atribuídos e pode sincronizar notas por meio dos serviços de avaliação do LTI.

## Antes de começar

Você precisa de:

- uma conta de Raiz ou Administrador no examina.io;
- um administrador da conta raiz do Canvas que possa gerenciar Chaves de Desenvolvedor e Aplicativos;
- um instrutor e um aluno fictício em um curso de teste do Canvas;
- pelo menos um exame importado e publicado no examina.io Manager;
- endereços HTTPS públicos com certificados confiáveis para ambos os sistemas; e
- um plano aprovado pela instituição para os dados de alunos que o Canvas possa divulgar.

Mantenha os relógios de ambos os sistemas precisos. As mensagens de login do LTI e as respostas assinadas expiram rapidamente, portanto, uma grande diferença de horário pode rejeitar uma configuração que, fora isso, estaria correta.

## Como o Canvas e o examina.io trocam configurações

O Canvas cria um **Client ID** e um **Deployment ID** que o examina.io precisa. O examina.io cria uma URL de chave pública específica para o registro que o Canvas precisa. Durante a visualização, a configuração tem duas etapas:

1. criar uma Chave de Desenvolvedor LTI 1.3 provisória no Canvas e instalar seu aplicativo;
2. copiar os identificadores e endpoints da plataforma do Canvas para o examina.io;
3. copiar os endpoints finais do examina.io de volta para a chave do Canvas; e
4. ativar o aplicativo, torná-lo disponível e validar todo o fluxo de trabalho.

!!! warning "Mantenha o aplicativo provisório indisponível"

    Se o Canvas exigir uma URL de chave pública durante a primeira etapa, use um endpoint HTTPS temporário do JSON Web Key Set controlado por sua instituição. Ele pode retornar um conjunto vazio (`{"keys":[]}`). Mantenha a chave desativada e o aplicativo indisponível até substituí-lo pela URL do **Conjunto de chaves públicas (JWKS)** do examina.io específica do registro na Etapa 3. Nunca use um nome de host local, Docker ou privado em uma chave de produção do Canvas.

## 1. Criar a chave provisória e o aplicativo no Canvas

Faça login com uma conta de administrador da conta raiz do Canvas. Selecione **Admin** na navegação global e escolha a conta raiz da sua instituição. Se o Canvas mostrar primeiro a lista de contas, selecione o nome da conta raiz.

![Selecione a conta raiz do Canvas da instituição](../assets/images/integrations/canvas/admin-01-accounts.png)

A navegação da conta deve incluir **Chaves de desenvolvedor** e **Aplicativos**. Se algum desses itens estiver ausente, sua função no Canvas não tem a permissão necessária na conta raiz; peça ao administrador do Canvas da instituição para realizar essa configuração.

![Abra as Chaves de desenvolvedor na navegação da conta raiz do Canvas](../assets/images/integrations/canvas/admin-02-root-account.png)

Abra **Chaves de desenvolvedor** e selecione **+ Chave de desenvolvedor**.

![Abra a página Chaves de desenvolvedor do Canvas](../assets/images/integrations/canvas/admin-03-developer-keys.png)

Escolha **Chave LTI**. O Canvas também pode mostrar **Registro LTI**; use essa opção apenas quando o examina.io fornecer uma URL de Registro Dinâmico de uso único.

![Escolha Chave LTI no menu Chave de desenvolvedor do Canvas](../assets/images/integrations/canvas/admin-04-create-lti-key.png)

Escolha **Entrada manual** e conclua as configurações da chave:

1. Digite **examina.io Assessments** como o nome e o título da chave.
2. Adicione o endereço de e-mail do administrador responsável por esta integração.
3. Adicione `https://www.examina.io/lti/launch` e `https://www.examina.io/lti/deep-link` como URIs de redirecionamento separados.
4. Insira `https://www.examina.io/lti/launch` como a **URI do link de destino**.
5. Insira `https://www.examina.io/lti/login` como a **URL de inicialização do OpenID Connect**.
6. Defina **Método JWK** como **URL do JWK público** e insira a URL do conjunto de chaves provisório descrita acima.

![Insira as URLs públicas do examina.io em uma chave LTI do Canvas](../assets/images/integrations/canvas/admin-05-lti-key-settings.png)

!!! warning "O valor do JWKS é específico para o registro"

    Se você usar `https://www.examina.io/lti/jwks/your-registration-id` durante a etapa provisória, `your-registration-id` é apenas um marcador de posição. A Etapa 3 substitui todo o valor pela URL exata do **Conjunto de chaves públicas (JWKS)** exibida pelo examina.io.

Em **Serviços LTI Advantage**, ative apenas os cinco escopos necessários para os serviços deste guia:

- criar e visualizar dados de tarefas;
- visualizar dados de tarefas;
- visualizar dados de envios;
- criar e atualizar resultados de envios; e
- recuperar dados de usuários associados ao contexto.

Os quatro primeiros oferecem suporte ao envio de notas por meio do AGS. O escopo final oferece suporte à lista de alunos do curso opcional do NRPS; mantenha-o desativado quando não precisar do acesso à lista.

![Selecione os escopos de AGS e NRPS opcional do Canvas](../assets/images/integrations/canvas/admin-06-lti-services.png)

Em **Posicionamentos**, adicione **Seleção de tarefas**. Adicione **Navegação do curso** apenas se a sua instituição também desejar um ponto de entrada do examina.io no nível do curso.

![Adicione os posicionamentos Seleção de tarefas e Navegação do curso opcional](../assets/images/integrations/canvas/admin-07-placements.png)

Salve a chave, copie seu **Client ID** e mantenha a chave **Desativada**. Abra **Admin → sua conta raiz → Aplicativos → Gerenciar**, instale o aplicativo usando o Client ID e copie seu **Deployment ID**.

O Canvas também suporta Registro Dinâmico, mas suas APIs de registro estão atualmente marcadas como beta. Use uma URL de Registro Dinâmico de uso único apenas quando ela for explicitamente fornecida pelo examina.io para a sua visualização; caso contrário, use o fluxo manual de duas etapas acima.

## 2. Adicionar o registro do Canvas no examina.io

Como um usuário Raiz ou Administrador no examina.io:

1. Abra **Início → Configurações**.
2. Localize **Traga o Examina para o seu LMS** e selecione **Adicionar registro**.
3. Escolha **Canvas** e insira um nome descritivo, como **Canvas do Northbridge College**.
4. Insira os valores do Canvas mostrados abaixo.

| Campo do examina.io | Valor do Canvas |
| --- | --- |
| URL do emissor | `https://<your-canvas-host>` |
| Client ID | O Client ID da chave de desenvolvedor LTI |
| Deployment ID | O Deployment ID do aplicativo instalado |
| Endpoint de autorização | `https://<your-canvas-host>/api/lti/authorize_redirect` |
| Endpoint de token | `https://<your-canvas-host>/login/oauth2/token` |
| URL das chaves públicas do LMS (JWKS) | `https://<your-canvas-host>/api/lti/security/jwks` |

Para o Canvas hospedado, substitua `<your-canvas-host>` pelo nome de host exato onde seus usuários fazem login. Não adicione um caminho final na URL do emissor e não use o endpoint genérico de JWKS do OAuth do Canvas no campo de chaves públicas do LMS.

5. Ative **Seleção de avaliação (Deep Linking)** e **Envio de notas (AGS)**.
6. Ative **Lista de alunos do curso (NRPS)** apenas se o escopo correspondente do Canvas foi aprovado e concedido.
7. Selecione **Salvar registro**.

![Adicione um registro do Canvas LTI 1.3 no examina.io](../assets/images/integrations/canvas/01-examina-add-canvas-registration.png)

O cartão salvo exibe as URLs exatas de **Inicialização do login OIDC**, **Inicialização do LTI**, **Deep Linking** e do **Conjunto de chaves públicas (JWKS)** específico do registro. Mantenha esse cartão aberto para a próxima etapa.

## 3. Concluir e ativar o aplicativo do Canvas

Edite a Chave de Desenvolvedor LTI do Canvas e substitua cada valor provisório da ferramenta pelo valor exato mostrado pelo examina.io:

| Campo da chave LTI do Canvas | Valor do examina.io |
| --- | --- |
| URL de inicialização do OpenID Connect | Inicialização do login OIDC |
| URI do link de destino | Inicialização do LTI |
| URI de redirecionamento | URLs de inicialização do LTI e Deep Linking, uma por linha |
| Link de destino da seleção de tarefas | Deep Linking |
| URL do JWK público | Conjunto de chaves públicas (JWKS) |
| URL do ícone da ferramenta | `https://www.examina.io/img/logo128.png` |

As rotas de produção voltadas para o navegador começam com `https://www.examina.io`.
Por exemplo, a URL de inicialização é `https://www.examina.io/lti/launch`. Sempre copie os valores completos do cartão de registro porque a URL do JWKS inclui o identificador do registro.

Salve a chave e **Ative-a**. Em **Aplicativos → Gerenciar**, abra **examina.io assessments**, confirme que o aplicativo está ativo e torne-o disponível para a conta raiz ou para as subcontas e cursos aprovados.

A **URL do ícone da ferramenta** fornece aos instrutores e administradores um logotipo reconhecível do examina.io no Canvas. Se uma instalação existente ainda exibir o ícone genérico de ferramenta externa do Canvas, atualize a Chave de Desenvolvedor com este valor e atualize ou reinstale o aplicativo para que o Canvas recarregue seus metadados de registro.

![Confirme se o examina.io Assessments está ativo e atualizado nos Aplicativos do Canvas](../assets/images/integrations/canvas/admin-08-apps-manage.png)

Se o aplicativo mostrar **Indisponível**, abra a configuração de disponibilidade, escolha a conta raiz ou uma subconta aprovada, selecione **Disponível** e salve. Limite a disponibilidade às instituições, subcontas ou cursos aprovados para a integração.

![Torne o aplicativo do Canvas disponível para a conta aprovada](../assets/images/integrations/canvas/admin-09-availability.png)

Retorne ao examina.io e ative o registro. Um registro suspenso ou revogado não pode aceitar novas inicializações.

## 4. Adicionar uma avaliação publicada a uma tarefa do Canvas

Como instrutor no curso de destino:

1. Abra **Tarefas → + Tarefa**.
2. Insira o nome da tarefa voltado para o aluno e os pontos máximos.
3. Defina **Tipo de envio** como **Ferramenta externa**.
4. Selecione **Localizar** e escolha **Adicionar uma avaliação do examina.io**.
5. Selecione o exame publicado pretendido e escolha **Adicionar exame selecionado**.

![Escolha uma avaliação publicada do examina.io no Canvas](../assets/images/integrations/canvas/04-canvas-select-published-exam.png)

O Canvas retorna ao formulário de tarefa com a URL de inicialização selecionada. Confirme o nome da tarefa, pontos, acesso à tarefa, datas e política de tentativas.

![Uma tarefa de Ferramenta Externa do Canvas usando a URL de inicialização de produção do examina.io](../assets/images/integrations/canvas/05-canvas-assignment-settings.png)

Escolha **Salvar e publicar** e abra a tarefa uma vez como instrutor. Confirme se a avaliação esperada aparece e se o Canvas não solicita um login separado no examina.io.

## 5. Verificar a experiência do aluno

Use um aluno fictício matriculado no curso:

1. Faça login no Canvas como o aluno.
2. Abra **BIO 101 → Tarefas → Cell Structure and Function**.
3. Confirme se o exame esperado abre dentro da tarefa do Canvas.
4. Inicie, conclua e envie a avaliação.

![Uma avaliação publicada do examina.io incorporada em uma tarefa do Canvas](../assets/images/integrations/canvas/06-canvas-learner-assessment.png)

A inicialização do LTI verifica a plataforma do Canvas, a implantação, o curso, a tarefa, o aluno e a publicação selecionada. Uma URL de inicialização copiada não substitui a abertura da tarefa a partir do Canvas.

## 6. Verificar a nota enviada

Após o envio, abra a visualização de notas no Canvas como aluno ou o Livro de Notas como instrutor. Confirme se o resultado aparece para a tarefa e usuário corretos.

![A avaliação concluída do examina.io enviada de volta ao livro de notas do Canvas](../assets/images/integrations/canvas/07-canvas-grade-return.png)

A entrega de notas é enfileirada separadamente do envio do exame, portanto, uma interrupção temporária do Canvas não transforma uma avaliação concluída em um envio com falha. A pontuação pode levar um curto período para aparecer. Atualize a visualização de notas antes de investigar um resultado ausente.

## Lista de verificação de validação de produção

Antes de ativar o aplicativo para um curso real, verifique tudo o que se segue com um curso de teste e usuários fictícios:

- A chave do Canvas e o aplicativo estão ativos e disponíveis apenas onde pretendido.
- O registro do examina.io está ativo na organização e no ambiente corretos.
- O Canvas usa a URL do JWKS do examina.io específica do registro.
- O examina.io usa o endpoint `/api/lti/security/jwks` do Canvas.
- O Deep Linking lista apenas as avaliações que o instrutor pode selecionar.
- A tarefa inicia a avaliação publicada pretendida dentro do Canvas.
- O aluno inicia o exame sem precisar fazer login uma segunda vez.
- A pontuação concluída chega ao aluno e à coluna do livro de notas corretos.
- Reabrir ou atualizar a tarefa não duplica um item de linha.
- O NRPS está desativado quando o acesso à lista de alunos do curso não for necessário.
- Todas as URLs voltadas para a produção usam HTTPS público e um certificado confiável.

## Solução de problemas

| Sintoma | O que verificar |
| --- | --- |
| **examina.io assessments** está ausente em **Localizar** | Confirme se a chave está ativa, se o aplicativo está disponível para este curso e se a chave inclui o posicionamento Seleção de tarefas com `LtiDeepLinkingRequest`. |
| O seletor abre, mas o Canvas rejeita o exame selecionado | Confirme se o Canvas consegue buscar a URL exata do JWKS do examina.io específica do registro a partir da sua rede de servidores. O alcance apenas pelo navegador não é suficiente. Verifique também a precisão do Client ID, Deployment ID, emissor e do relógio. |
| A tarefa abre um quadro em branco ou recusa a inicialização | Verifique a URL de inicialização do OIDC, a URL de inicialização, as URIs de redirecionamento, o certificado HTTPS confiável, a política de iframe e as configurações de cookies de terceiros do navegador. Remova todos os nomes de host locais, Docker e privados da configuração de produção. |
| A avaliação errada abre | Edite a tarefa e selecione a publicação novamente. Não copie uma tarefa entre ambientes sem selecionar novamente seu conteúdo. |
| A nota não aparece | Confirme se os escopos do AGS e o **Envio de notas** estão ativados, se a tarefa possui pontos e se o aplicativo ainda está disponível. Aguarde um curto período para a entrega enfileirada. |
| A lista de alunos do curso está indisponível | Confirme se o escopo do NRPS e a **Lista de alunos do curso** estão ativados. A inicialização e o envio de notas podem continuar sem acesso à lista de alunos. |
| O Canvas relata um erro de chave de assinatura | O Canvas deve usar a URL do JWKS do examina.io específica do registro, e o examina.io deve usar `https://<your-canvas-host>/api/lti/security/jwks`. Confirme que nenhum dos endpoints redireciona para uma página de login. |

Para obter o comportamento e a terminologia atuais da plataforma Canvas, consulte a documentação oficial da Instructure sobre [registro LTI](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.registration), [posicionamento de Seleção de tarefas](https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.assignment_selection_placement), [Deep Linking](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.content_item) e [avaliação](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.assignment_tools).
