async function setbackground()
{
  let currentDate = new Date();
  let starttime = currentDate.getHours()
  console.log(starttime)

  if(starttime<=18 && starttime>=6)
  {
    const html = document.getElementById("html");
    html.style.setProperty("background-image", "url(background2.jpg)");
    console.log("Background: Day")
  }
  else
  {
    const html = document.getElementById("html");
    html.style.setProperty("background-image", "url(background.jpg)");
    document.getElementById("helloword").textContent = "Good evening!";
  }
}




const card1overlay = document.getElementById("tencodes-overlay");
const card1 = document.getElementById("tencodes");

function showTencodes() {
	card1.style.display = "block";
  card1overlay.style.display = "block";
}
 
function hideTencodes() {
  card1.style.display = "none";
	card1overlay.style.display = "none";
}

card1overlay.addEventListener("click", hideTencodes);





const card2overlay = document.getElementById("urisdicia-overlay");
const card2 = document.getElementById("urisdicia");

function showUrisdicia() {
  card2.style.display = "block";
  card2overlay.style.display = "block";
}
function hideUrisdicia() {
  card2.style.display = "none";
	card2overlay.style.display = "none";
}

card2overlay.addEventListener("click", hideUrisdicia);




const card3overlay = document.getElementById("sila-overlay");
const card3 = document.getElementById("sila");

function showSila() {
  card3.style.display = "block";
  card3overlay.style.display = "block";
}
function hideSila() {
  card3.style.display = "none";
	card3overlay.style.display = "none";
}

card3overlay.addEventListener("click", hideSila);





const card4overlay = document.getElementById("process-overlay");
const card4 = document.getElementById("process");

function showProcess() {
  card4.style.display = "block";
  card4overlay.style.display = "block";
}
function hideProcess() {
  card4.style.display = "none";
	card4overlay.style.display = "none";
}

card4overlay.addEventListener("click", hideProcess);




const card5overlay = document.getElementById("yasvoboden-overlay");
const card5 = document.getElementById("yasvoboden");

function showYaSvoboden() {
  card5.style.display = "block";
  card5overlay.style.display = "block";
}
function hideYaSvoboden() {
  card5.style.display = "none";
	card5overlay.style.display = "none";
}

card5overlay.addEventListener("click", hideYaSvoboden);



async function find_button() {
    let input = document.getElementById('finder-input').value;

    let results = await eel.choice(input)();

    document.getElementById("article").innerHTML = '';

    if (results.length > 0) {
        results.forEach(result => {
            let articleDiv = document.createElement('div');
            articleDiv.innerHTML = `
                <p>
                    <center><h3>${result.key} ${result.wanted}</h3></center>
                    ${result.text}<br>
                    <font color='#ff3300'>Punishment:</font> ${result.punishment}
                </p>
            `;
            document.getElementById("article").appendChild(articleDiv);
        });
    } else {
        document.getElementById("article").innerHTML = '<p>No articles found</p>';
    }

    document.getElementById("ansver").style.display = "block";
}

const card6overlay = document.getElementById("update-overlay");
const card6 = document.getElementById("update");

function showUpdate() {
  card6.style.display = "block";
  card6overlay.style.display = "block";
}
function hideUpdate() {
  card6.style.display = "none";
  card6overlay.style.display = "none";
}
card6overlay.addEventListener("click", hideUpdate);

async function check_for_updates() {
    let result = await eel.check_for_updates()();
    if( result == 0 ) {
        pass;
    }
    else {
        let showVersion = document.getElementById('version');
        let showInfo = document.getElementById('updateInfo');
        showVersion.textContent = await eel.get_version()();
        showInfo.textContent = await eel.get_update_info()();
        showUpdate();
    }
}

check_for_updates()
setbackground()
