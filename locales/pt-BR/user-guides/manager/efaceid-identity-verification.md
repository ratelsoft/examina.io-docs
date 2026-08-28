---
title: Configurar e usar a verificação de identidade eFaceID
description: Ative o eFaceID, cadastre a foto do candidato, proteja uma prova e trate a análise biométrica ou não biométrica.
tags: [eFaceID, verificação de identidade, prova de vida, segurança de provas]
translation_source: user-guides/manager/efaceid-identity-verification.md
translation_source_sha256: b57baa79e7123322f1bfeb125b841a120d0e2a3728779ef9713fd580395f8872
---

# Configurar e usar o eFaceID

O eFaceID ajuda a confirmar que a pessoa que inicia uma prova protegida está
presente e corresponde à foto fornecida por um administrador autorizado. A
decisão fica vinculada ao candidato, à prova e àquela tentativa.

Este passo a passo usa a organização fictícia **Cedar Valley University**, a
candidata **Amina Hassan** e **BIO 201 — Human Genetics Midterm**.

!!! important "Mantenha uma alternativa humana"

    A biometria não deve ser a única forma de acesso. Publique um canal de
    suporte e use a análise não biométrica para quem não consentir, não puder
    usar a câmera ou precisar de adaptação.

## Antes de começar

Você precisa de um plano compatível, das permissões necessárias, de uma foto
atual por candidato, câmera compatível e um processo de análise não biométrica.

## 1. Ativar o eFaceID

Abra **Faturamento** e confirme que **Verificação eFaceID** está **Ativada**.
O cartão também mostra o local de processamento e os períodos de retenção.

![eFaceID ativado para Cedar Valley University](../../assets/images/identity-proctoring/organization-efaceid-enabled.png)

O local aparece como cidade ou região e país, por exemplo, **Norte da Virgínia,
Estados Unidos**. Sua organização pode usar outros valores.

## 2. Cadastrar a foto do candidato

No **Manager**, abra **Candidatos**, selecione a pessoa, escolha **Alterar
imagem** e envie um retrato recente, nítido, frontal e bem iluminado. Confirme
nome, código e vínculo com a prova.

![Cadastro de Amina Hassan com foto clara](../../assets/images/identity-proctoring/manager-enroll-candidate-photo.png)

Não use foto em grupo, página digitalizada, selfie com filtro ou imagem com
mais de um rosto.

## 3. Proteger a prova

Abra as configurações da prova e ative **Verificação eFaceID**. Ative também
**Fiscalização ao vivo** quando um fiscal precisar acompanhar a sessão.
Confirme candidatos, cadernos, retenção e procedimento alternativo.

![eFaceID e fiscalização habilitados para BIO 201](../../assets/images/identity-proctoring/exam-protection-controls.png)

## 4. Jornada do candidato

O candidato abre o link oficial e informa código e senha.

![Amina entrando em BIO 201](../../assets/images/identity-proctoring/candidate-sign-in.png)

## 5. Revisar o consentimento

Em seguida, revisa o consentimento: finalidade, local, retenção, pessoas
autorizadas, aviso de fotossensibilidade e opção de análise não biométrica.

![Consentimento para verificação de identidade](../../assets/images/identity-proctoring/candidate-identity-consent.png)

## 6. Concluir a prova de vida

Após consentir, libera a câmera, centraliza o rosto e segue as instruções de
cor e movimento. Somente um rosto deve aparecer, com boa iluminação frontal.

![Posicionamento do candidato para a prova de vida](../../assets/images/identity-proctoring/candidate-liveness-positioning.png)

A captura publicada usa um retrato fictício para preservar a privacidade; os
controles correspondem ao fluxo testado ao vivo.

## 7. Entender o resultado

**Aprovado**: o candidato segue para a configuração do dispositivo ou resumo
da prova.

**Análise necessária**: a tentativa é pausada e um administrador autorizado
avalia um caminho não biométrico documentado.

**Falha técnica**: verifique câmera, iluminação, navegador e rede antes de
tentar novamente.

**Consentimento recusado ou retirado**: não há aprovação biométrica. O
candidato seleciona **Solicitar análise não biométrica**.

Somente uma decisão biométrica de segurança concluída é cobrada. Erros de
permissão, abandonos e falhas de rede ou serviço não são decisões bem-sucedidas.
Consulte **Faturamento** para preço e franquia.

## 8. Retenção e auditoria

Administradores autorizados podem ver a decisão e a foto cadastrada, mas o
vídeo da câmera não fica disponível para eles no examina.io. Decisões aprovadas
e casos analisados podem ter retenções diferentes. Não envie imagens
biométricas por e-mail, chat ou chamado de suporte.

## Solução de problemas

**A câmera não abre**: permita a câmera para o site exato, feche outros apps
que a usem e recarregue. O sistema operacional pode exigir que o navegador
seja reiniciado após uma nova permissão.

**O rosto não é detectado**: melhore a luz frontal, centralize o rosto e retire
outras pessoas do enquadramento.

**Mudança de navegador**: a aprovação é vinculada à sessão da tentativa e pode
ser necessário verificar novamente.

Para uma prova fiscalizada, continue em
[Fiscalizar uma prova ao vivo](live-exam-proctoring.md).
