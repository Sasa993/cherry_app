const realFileBtn = document.getElementsByClassName("real_file");
const customBtn = document.getElementsByClassName("custom_button");
const customText = document.getElementsByClassName("custom_text");
const customText2 = document.getElementsByClassName("custom_text2");

for(let i = 0; i < customBtn.length; i++){
		  customBtn[i].addEventListener('click', function() {
		   realFileBtn[i].click();
	});
}

for(let i = 0; i < realFileBtn.length; i++){
	realFileBtn[i].addEventListener('change', function() {
		if (realFileBtn[i].value) {
			if (realFileBtn[i].value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1].length > 15) {
				customText[i].innerHTML = realFileBtn[i].value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1].substring(0, 15) + '...';
				} 
			else {
			    customText[i].innerHTML = realFileBtn[i].value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
				}
			}
		else {
			customText[i].innerHTML = "No file choosen, yet.";
		}
	});
}
for(let i = 0; i < realFileBtn.length; i++){
	realFileBtn[i].addEventListener('change', function() {
		if (realFileBtn[i].value) {
			if (realFileBtn[i].value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1].length > 15) {
				customText2[i].innerHTML = realFileBtn[i].value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1].substring(0, 15) + '...';
				} 
			else {
			    customText2[i].innerHTML = realFileBtn[i].value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
				}
			}
		else {
			customText2[i].innerHTML = "No file choosen, yet.";
		}
	});
}