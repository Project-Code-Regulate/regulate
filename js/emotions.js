const emotionCategories = [
    {
        name: 'Happy',
        color: '#cbce76',
        emotions: [
            { word: 'Joyful', definition: 'Feeling great happiness and delight.' },
            { word: 'Content', definition: 'Peacefully satisfied with how things are.' },
            { word: 'Proud', definition: 'Pleased about something you or someone close to you did.' },
            { word: 'Grateful', definition: 'Thankful for something or someone in your life.' },
            { word: 'Hopeful', definition: 'Expecting that something good will happen.' },
        ],
    },
    {
        name: 'Calm',
        color: '#427c89',
        emotions: [
            { word: 'Relaxed', definition: 'Free from tension and worry.' },
            { word: 'Peaceful', definition: 'Quiet and undisturbed inside.' },
            { word: 'Safe', definition: 'Protected and free from danger or harm.' },
            { word: 'Centered', definition: 'Balanced and focused, not pulled in many directions.' },
        ],
    },
    {
        name: 'Sad',
        color: '#7f5582',
        emotions: [
            { word: 'Lonely', definition: 'Wanting connection with others and not feeling it.' },
            { word: 'Disappointed', definition: 'Let down because something did not go as hoped.' },
            { word: 'Hurt', definition: 'Emotionally wounded by something someone said or did.' },
            { word: 'Discouraged', definition: 'Losing confidence or motivation to keep trying.' },
            { word: 'Grieving', definition: 'Deep sorrow, usually after a loss.' },
        ],
    },
    {
        name: 'Anxious',
        color: '#8ecc6a',
        emotions: [
            { word: 'Worried', definition: 'Thinking about problems or what could go wrong.' },
            { word: 'Nervous', definition: 'Uneasy or jittery about something coming up.' },
            { word: 'Overwhelmed', definition: 'Feeling like there is too much to handle at once.' },
            { word: 'Insecure', definition: 'Unsure of yourself or your worth.' },
            { word: 'Restless', definition: 'Unable to relax or stay still.' },
        ],
    },
    {
        name: 'Angry',
        color: '#be6040',
        emotions: [
            { word: 'Frustrated', definition: 'Upset because something is blocking what you want.' },
            { word: 'Irritated', definition: 'Mildly annoyed by small things.' },
            { word: 'Resentful', definition: 'Bitter about being hurt or betrayed.' },
            { word: 'Jealous', definition: 'Upset that someone has something you want.' },
        ],
    },
];

const categories = document.getElementById('categories');

emotionCategories.forEach(category => {
    const section = document.createElement('section');
    const heading = document.createElement('h3');
    heading.textContent = category.name;
    heading.style.color = category.color;
    section.appendChild(heading);
    category.emotions.forEach(emotion => {
        const card = document.createElement('div');
        card.classList.add('emotion-card');
        card.style.background = `linear-gradient(135deg, ${category.color}55, ${category.color}10)`;
        
        const word = document.createElement('strong');
        word.textContent = emotion.word;
        word.style.color = 'gray';

        const definition = document.createElement('p');
        definition.textContent = emotion.definition;

        card.appendChild(word);
        card.appendChild(definition);
        section.appendChild(card);
    })
    categories.appendChild(section);

})