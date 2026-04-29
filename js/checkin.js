const pleasant = document.getElementById('pleasant');
const stress = document.getElementById('stress');

const tagText = document.getElementById('tag-text');
const tagColor = document.getElementById('tag-color');
const tagCont = document.getElementById('tag-area');

const entry = document.getElementById('entry');

const submitBtn = document.getElementById('submit-entry');
const clearBtn = document.getElementById('clear-entry');

function addTag() {
    const text = tagText.value.trim();
    if (!text) return;

    const color = tagColor.value

    const tag = document.createElement('span');
    tag.classList.add('tag');
    tag.textContent = text;
    tag.style.backgroundColor = color;
    tag.style.color = getTextColor(tagColor.value);
    tag.addEventListener('click', () => tag.remove());

    tagCont.appendChild(tag);
    tagText.value = '';
}

function getTextColor(hex) {
    const r = parseInt(hex.slice(1, 3), 16);
    const g = parseInt(hex.slice(3, 5), 16);
    const b = parseInt(hex.slice(5, 7), 16);
    const brightness = (r * 299 + g * 587 + b * 114) / 1000;
    return brightness > 128 ? '#000000' : '#ffffff';
}

clearBtn.addEventListener('click', () => entry.value = '');

submitBtn.addEventListener('click', () => {
    const entryData = {
        mood: document.getElementById('pleasant').value,
        stress: document.getElementById('stress').value,
        text: entry.value,
        tags: [...tagCont.children].map(tag => tag.textContent)
    };

    console.log(entryData);

    entry.value = '';
    tagCont.innerHTML = '';
    tagText.value = '';
    pleasant.value = 50;
    stress.value = 50;
});