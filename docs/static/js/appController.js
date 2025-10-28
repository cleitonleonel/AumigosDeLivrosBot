/* jshint esversion: 8 */
/* jshint strict: global */
"use strict";

document.addEventListener("DOMContentLoaded", () => {
	const botButton = document.getElementById("botButton");
	
	botButton.addEventListener("click", () => {
		const botUsername = "AumigosdeLivros_bot";
		window.open(`https://t.me/${botUsername}?start=default`, "_blank");
	});
});

async function loadGitHubContributors() {
	const owner = 'cleitonleonel';
	const repo = 'AumigosDeLivrosBot';
	const contributorsContainer = document.querySelector('.contributors-list');
	
	//const apiUrl = `https://api.github.com/repos/${owner}/${repo}/contributors`;
	const apiUrl = "colaboradores.json";
	
	try {
		const response = await fetch(apiUrl);
		
		if (!response.ok) {
			throw new Error('Erro ao buscar colaboradores');
		}
		
		const contributors = await response.json();

		contributorsContainer.innerHTML = '';

		if (contributors.length === 0) {
			contributorsContainer.innerHTML = `
                <div class="contributor-item">
                    <span class="contributor-icon">💻</span>
                    <div class="contributor-info">
                        <strong>Cleiton Leonel Creton</strong>
                    </div>
                </div>
            `;
			return;
		}
		
		contributors.forEach((contributor, index) => {
			const contributorDiv = document.createElement('div');
			contributorDiv.className = 'contributor-item';
			contributorDiv.style.animationDelay = `${index * 0.1}s`;

			let role = 'Colaborador';
			if (index === 0) {
				role = 'Desenvolvedor';
			} else if (contributor.contributions > 50) {
				role = 'Colaborador Ativo';
			}
			
			contributorDiv.innerHTML = `
                <a href="${contributor.html_url}" target="_blank" rel="noopener noreferrer"
                   style="display: flex; align-items: center; gap: 15px; text-decoration: none; color: inherit; width: 100%;">
                    <img src="${contributor.avatar_url}"
                         alt="${contributor.login}"
                         class="contributor-avatar"
                         style="width: 50px; height: 50px; border-radius: 50%; border: 3px solid var(--amarelo); flex-shrink: 0;">
                    <div class="contributor-info">
                        <strong>${contributor.login}</strong>
                        <!--<span class="contributor-role">${role} • ${contributor.contributions} contribuições</span>-->
                    </div>
                </a>
            `;
			
			contributorsContainer.appendChild(contributorDiv);
		});
		
	} catch (error) {
		contributorsContainer.innerHTML = `
            <div class="contributor-item">
                <span class="contributor-icon">💻</span>
                <div class="contributor-info">
                    <strong>Cleiton Leonel Creton</strong>
                </div>
            </div>
        `;
	}
}

document.addEventListener('DOMContentLoaded', loadGitHubContributors);
