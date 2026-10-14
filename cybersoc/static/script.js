async function atualizarPainel() {
  try {
    // Solicita a criação de um evento simulado
    const geracao = await fetch("/api/gerar", {
      method: "POST",
    });

    if (!geracao.ok) {
      throw new Error("Não foi possível gerar o evento");
    }

    // Busca os dados atualizados
    const resposta = await fetch("/api/logs");

    if (!resposta.ok) {
      throw new Error("Não foi possível buscar os logs");
    }

    const dados = await resposta.json();

    // Atualiza os cartões
    document.getElementById("falha").textContent = dados.falhas;

    document.getElementById("sucesso").textContent = dados.sucessos;

    document.getElementById("total-ips").textContent = dados.ips;

    // Atualiza a tabela
    const tabela = document.getElementById("tabela-logs");
    tabela.replaceChildren();

    dados.logs.forEach((log) => {
      const linha = document.createElement("tr");

      const ip = document.createElement("td");
      ip.textContent = log.ip;

      const usuario = document.createElement("td");
      usuario.textContent = log.usuario;

      const horario = document.createElement("td");
      horario.textContent = log.horario;

      const status = document.createElement("td");
      status.textContent = log.status;
      status.className = log.status === "Falha" ? "falha" : "sucesso";

      linha.append(ip, usuario, horario, status);
      tabela.appendChild(linha);
    });
  } catch (erro) {
    console.error("Erro ao atualizar o CyberSOC:", erro);
  }
}

async function atualizarPainel() {
  try {
    // Gera um evento simulado
    await fetch("/api/gerar", {
      method: "POST",
    });

    // Busca os dados atualizados
    const resposta = await fetch("/api/logs");

    if (!resposta.ok) {
      throw new Error("Erro ao buscar eventos");
    }

    const dados = await resposta.json();

    // Atualiza os indicadores
    document.getElementById("total-falhas").textContent = dados.falhas;
    document.getElementById("total-sucessos").textContent = dados.sucessos;
    document.getElementById("total-ips").textContent = dados.ips;

    // Atualiza a tabela
    const tabela = document.getElementById("tabela-logs");
    tabela.replaceChildren();

    dados.logs.forEach((log) => {
      const linha = document.createElement("tr");

      [log.ip, log.usuario, log.horario, log.status].forEach((valor) => {
        const coluna = document.createElement("td");
        coluna.textContent = valor;
        linha.appendChild(coluna);
      });

      tabela.appendChild(linha);
    });
  } catch (erro) {
    console.error("Erro no CyberSOC:", erro);
  }
}

// Atualiza imediatamente e depois a cada 2 segundos
atualizarPainel();
setInterval(atualizarPainel, 2000);

// Atualiza ao abrir a página e depois a cada 2 segundos
atualizarPainel();
setInterval(atualizarPainel, 2000);
