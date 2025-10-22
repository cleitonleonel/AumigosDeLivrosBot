/* jshint esversion: 6 */
/* jshint strict: global */
"use strict";

document.addEventListener("DOMContentLoaded", () => {
	const botButton = document.getElementById("botButton");
	
	botButton.addEventListener("click", () => {
		const botUsername = "AumigosdeLivros_bot";
		window.open(`https://t.me/${botUsername}?start=default`, "_blank");
	});
});
