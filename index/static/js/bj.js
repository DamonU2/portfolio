// Blackjack
let bjGame = {
    'you': {'scoreSpan': '#your-bj-result', 'div': 'your-box', 'score': 0, 'bet': 20, 'result': 'none','aceCount': 0},
    'split': {'scoreSpan': '#split-bj-result', 'div': 'split-box', 'score': 0, 'bet': 0, 'result': 'none', 'aceCount': 0},
    'dealer': {'scoreSpan': '#dealer-bj-result', 'div': 'dealer-box', 'score': 0, 'aceCount': 0},
    'suits': ['C', 'D', 'H', 'S'],
    'cards': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
    'cardsMap': {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7':7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11},
    'decks': 2,
    'discardCount': 104,
    'money': 230,
    'bet': 20,
};

const YOU = bjGame['you'];
const SPLIT = bjGame['split'];
const DEALER = bjGame['dealer'];
let hearts = [], clubs = [], diamonds = [], spades = [];
let activePlayer = YOU;
let holeCard = [];
let lastCard = [];
let firstCard = [];
let secondCard = [];
let initialBet = 0;
let split = false;

const hitSound = new Audio('../static/sounds/swish.m4a');
const winSound = new Audio('../static/sounds/cash.mp3');
const lossSound = new Audio('../static/sounds/aww.mp3');
const shuffleSound = new Audio('../static/sounds/shuffling-cards-1.wav');

document.querySelector('#bj-hit-btn').addEventListener('click', bjHit);
document.querySelector('#bj-DD-btn').addEventListener('click', bjDD);
document.querySelector('#bj-split-btn').addEventListener('click', bjSplit);
document.querySelector('#bj-deal-btn').addEventListener('click', bjDeal);
document.querySelector('#bj-stand-btn').addEventListener('click', bjStand);

document.querySelector('#add-bet').addEventListener('click', addFive);
document.querySelector('#reduce-bet').addEventListener('click', reduceFive);
document.querySelector('#max-bet').addEventListener('click', maxBet);
document.querySelector('#restart').addEventListener('click', restartGame);

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function randomCard() {
    var suit = bjGame['suits'][Math.floor(Math.random() * 4)]
    if (suit === 'C'){
        if (clubs.length > 0) {
            let randNum = Math.floor(Math.random() * clubs.length);
            let cardChoice = clubs[randNum];
            clubs.splice(randNum, 1);
            bjGame['discardCount']++;
            return [suit, cardChoice];
        }
        else {
            return randomCard();
        }
    }
    else if (suit === 'D'){
        if (diamonds.length > 0) {
            let randNum = Math.floor(Math.random() * diamonds.length);
            let cardChoice = diamonds[randNum];
            diamonds.splice(randNum, 1);
            bjGame['discardCount']++;
            return [suit, cardChoice];
        }
        else {
            return randomCard();
        }
    }
    else if (suit === 'H'){
        if (hearts.length > 0) {
            let randNum = Math.floor(Math.random() * hearts.length);
            let cardChoice = hearts[randNum];
            hearts.splice(randNum, 1);
            bjGame['discardCount']++;
            return [suit, cardChoice];
        }
        else {
            return randomCard();
        }
    }
    else if (suit === 'S'){
        if (spades.length > 0) {
            let randNum = Math.floor(Math.random() * spades.length);
            let cardChoice = spades[randNum];
            spades.splice(randNum, 1);
            bjGame['discardCount']++;
            return [suit, cardChoice];
        }
        else {
            return randomCard();
        }
    }
}

function betButtonCheck() {
    if (bjGame['bet'] > 45 || bjGame['money'] < 5) {
        document.getElementById("add-bet").disabled = true;
    }
    else {
        document.getElementById("add-bet").disabled = false;
    }
    if (bjGame['bet'] > 49 || bjGame['money'] < (50 - bjGame['bet'])) {
        document.getElementById("max-bet").disabled = true;
    }
    else {
        document.getElementById("max-bet").disabled = false;
    }
    if (bjGame['bet'] < 6) {
        document.getElementById("reduce-bet").disabled = true;
    }
    else {
        document.getElementById("reduce-bet").disabled = false;
    }
}

function updateMoney() {
    bjGame['bet'] = YOU['bet'] + SPLIT['bet'];
    document.getElementById("money").textContent = '$' + bjGame['money'];
    document.getElementById("bet").textContent = '$' + bjGame['bet'];
}

function hideBet() {
    document.getElementById("add-bet").disabled = true;
    document.getElementById("reduce-bet").disabled = true;
    document.getElementById("max-bet").disabled = true;
}

function clearCards() {
    let yourImages = document.querySelector('#your-box').querySelectorAll('img');
    let dealerImages = document.querySelector('#dealer-box').querySelectorAll('img');
    for (i=0; i < yourImages.length; i++) {
        yourImages[i].remove();
    }
    for (i=0; i < dealerImages.length; i++) {
        dealerImages[i].remove();
    }
}

function showCard(activePlayer, card, suit) {
    let cardImage = document.createElement('img');
    cardImage.src = `../static/images/${suit}/${card}.png`;
    document.getElementById(activePlayer['div']).appendChild(cardImage);
    hitSound.play();
}

function shuffle() {
    hearts = [], clubs = [], diamonds = [], spades = [];
    for (i = 0; i < bjGame['decks']; i++) {
        clubs = clubs.concat(bjGame['cards']);
        diamonds = diamonds.concat(bjGame['cards']);
        hearts = hearts.concat(bjGame['cards']);
        spades = spades.concat(bjGame['cards']);
    }
    bjGame['discardCount'] = 0;
}

function hideBtns() {
    document.getElementById("bj-stand-btn").disabled = true;
    document.getElementById("bj-hit-btn").disabled = true;
    document.getElementById("bj-DD-btn").disabled = true;
    document.getElementById("bj-split-btn").disabled = true;
}

function addFive() {
    YOU['bet'] += 5;
    bjGame['money'] -= 5;
    updateMoney();
    betButtonCheck();
}

function reduceFive() {
    YOU['bet'] -= 5;
    bjGame['money'] += 5;
    updateMoney();
    betButtonCheck();
}

function maxBet() {
    bjGame['money'] -= 50 - bjGame['bet'];
    YOU['bet'] = 50;
    updateMoney();
    betButtonCheck();
}

async function bjDeal() {
    document.getElementById("bj-deal-btn").disabled = true;
    clearCards();
    hideBet();

    initialBet = bjGame['bet'];
    YOU['bet'] = initialBet;
    SPLIT['bet'] = 0;

    split = false;

    if (SPLIT['score'] != 0) {
        document.getElementById(SPLIT['div']).remove();
    }

    if (bjGame['discardCount'] > 70) {
        shuffle();
        shuffleSound.play();
        await sleep(700);
    }

    document.getElementById("bj-result").style.visibility = "hidden";
    document.getElementById("your-box").style.visibility = "visible";
    document.getElementById("dealer-box").style.visibility = "visible";

    YOU['score'] = 0;
    YOU['result'] = 'none';
    YOU['acesCount'] = 0;
    SPLIT['score'] = 0;
    SPLIT['result'] = 'bust';
    SPLIT['acesCount'] = 0;
    DEALER['score'] = 0;
    DEALER['acesCount'] = 0;
    showScore(YOU);
    showScore(DEALER);

    activePlayer = YOU;
    bjHit();
    firstCard = lastCard;
    
    activePlayer = DEALER;
    await sleep(500);
    let cardBack = document.createElement('img');
    cardBack.src = `../static/images/back.png`;
    cardBack.id = 'back';
    holeCard = randomCard();
    document.getElementById(activePlayer['div']).appendChild(cardBack);
    hitSound.play();

    activePlayer = YOU;
    await sleep(500);
    bjHit();
    secondCard = lastCard;

    activePlayer = DEALER;
    await sleep(500);
    bjHit();
    activePlayer = YOU;

    await sleep(500);
    if (YOU['score'] === 21) {
        if (DEALER['score'] === 11 && bjGame['cardsMap'][holeCard[1]] === 10) {
            bjStand();
        }
        else {
            showResult('bj', YOU);
            resetBet();
        }
    }
    else if (DEALER['score'] === 11 && bjGame['cardsMap'][holeCard[1]] === 10) {
        bjStand();
    }
    else {
        document.getElementById("bj-stand-btn").disabled = false;
        document.getElementById("bj-hit-btn").disabled = false;
        if (bjGame['money'] >= initialBet) {
            document.getElementById("bj-DD-btn").disabled = false;
        }

        if (bjGame['money'] >= initialBet && bjGame['cardsMap'][firstCard[1]] === bjGame['cardsMap'][secondCard[1]]) {
            document.getElementById("bj-split-btn").disabled = false;
        }
    }
}

function bjHit() {
    document.getElementById("bj-DD-btn").disabled = true;
    document.getElementById("bj-split-btn").disabled = true;
    lastCard = randomCard();
    showCard(activePlayer, lastCard[1], lastCard[0]);
    updateScore(lastCard[1], activePlayer);
}

async function bjDD() {
    hideBtns();
    bjGame['money'] -= initialBet;
    activePlayer['bet'] += initialBet;
    updateMoney();
    bjHit();
    await sleep(500);
    bjStand();
}

async function bjSplit() {
    hideBtns();
    split = true;
    SPLIT['result'] = 'none';
    SPLIT['bet'] += initialBet;
    bjGame['money'] -= initialBet;
    updateMoney();
    activePlayer = SPLIT;
    let splitDiv = document.createElement('div');
    splitDiv.id = SPLIT['div'];
    splitDiv.innerHTML = '<h2><span id="split-bj-result">0</span></h2>';
    var flexBox = document.getElementById('bj-row-1');
    flexBox.insertBefore(splitDiv, flexBox.firstChild);
    showCard(activePlayer, firstCard[1], firstCard[0]);
    document.getElementById(YOU['div']).getElementsByTagName('img')[0].remove();
    updateScore(firstCard[1], activePlayer);
    YOU['score'] = 0;
    updateScore(secondCard[1], YOU);
    showScore(YOU);
    await sleep(500);
    bjHit();
    document.getElementById("bj-stand-btn").disabled = false;
    document.getElementById("bj-hit-btn").disabled = false;
    if (bjGame['money'] >= initialBet) {
        document.getElementById("bj-DD-btn").disabled = false;
    }
}

async function bjStand() {
    hideBtns();
    if (split === true){
        split = false;
        activePlayer = YOU;
        await sleep(500);
        bjHit();
        document.getElementById("bj-stand-btn").disabled = false;
        document.getElementById("bj-hit-btn").disabled = false;
        if (bjGame['money'] >= initialBet) {
            document.getElementById("bj-DD-btn").disabled = false;
        }
    }
    else if (SPLIT['result'] === 'bust' && YOU['result'] === 'bust') {
        if (SPLIT['score'] != 0) {
            computeWinner(SPLIT);
        }
        computeWinner(YOU);
        resetBet();
    }
    else {
        activePlayer = DEALER;
        document.getElementById("back").src = `../static/images/${holeCard[0]}/${holeCard[1]}.png`;
        updateScore(holeCard[1], activePlayer);
        hitSound.play();
        await sleep(500);
        while (activePlayer['score'] < 17) {
            bjHit();
            await sleep(500);
        }
        if (SPLIT['score'] != 0) {
            computeWinner(SPLIT);
        }
        computeWinner(YOU);
        resetBet();
    }
}

function updateScore(card, player) {
    player['score'] += bjGame['cardsMap'][card];
    if (card === 'A') {
        player['acesCount']++;
    }
    showScore(player);
}

async function showScore(player) {
    if (player['score'] > 21 && player['acesCount'] === 0) {
        hideBtns();
        document.querySelector(player['scoreSpan']).textContent = 'Bust!';
        document.querySelector(player['scoreSpan']).style.color = 'red';
        await sleep(500);
        if (player === SPLIT || player === YOU) {
            player['result'] = 'bust';
            bjStand();
        }
    }
    else if (player['score'] > 21 && player['acesCount'] > 0) {
        player['score'] -= 10;
        player['acesCount']--;
        document.querySelector(player['scoreSpan']).textContent = player['score'];
        document.querySelector(player['scoreSpan']).style.color = 'white';
    }
    else {
        document.querySelector(player['scoreSpan']).textContent = player['score'];
        document.querySelector(player['scoreSpan']).style.color = 'white';
    }
}

function computeWinner(player) {
    if (player['result'] ==='bust') {
        showResult('bust', player);
    }
    else if (player['score'] === DEALER['score'] && player['score'] < 22) {
        showResult('tied', player);
    }
    else if (player['score'] < DEALER['score'] && DEALER['score'] < 22) {
        showResult('lost', player);
    }
    else if (player['score'] > DEALER['score'] || DEALER['score'] > 21) {
        showResult('won', player);
    }
}

async function showResult(wlt, player) {
    hideBtns();
    if (wlt === 'won') {
        document.querySelector(player['scoreSpan']).textContent = 'You won!';
        document.querySelector(player['scoreSpan']).style.color = 'gold';
        winSound.play();
        player['bet'] += player['bet'];
    }
    else if (wlt === 'bj') {
        document.querySelector(player['scoreSpan']).textContent = 'Blackjack!';
        document.querySelector(player['scoreSpan']).style.color = 'gold';
        winSound.play();
        player['bet'] += player['bet'] * 1.5;
    }
    else if (wlt === 'tied') {
        document.querySelector(player['scoreSpan']).textContent = 'You tied.';
        document.querySelector(player['scoreSpan']).style.color = 'white';
    }
    else if (wlt === 'bust') {
        player['bet'] = 0;
    }
    else {
        document.querySelector(player['scoreSpan']).textContent = 'You lost.';
        document.querySelector(player['scoreSpan']).style.color = 'red';
        lossSound.play();
        player['bet'] = 0;
    }
    updateMoney();
}

function resetBet() {
    if (bjGame['money'] === 0 && bjGame['bet'] === 0){
        document.getElementById("restart").style.visibility = "visible";
    }
    else {
        if (bjGame['money'] + bjGame['bet'] < initialBet) {
            YOU['bet'] = bjGame['money'] + bjGame['bet'];
            bjGame['money'] = 0;
            updateMoney();
        }
        else {
            bjGame['money'] += bjGame['bet'] - initialBet;
            YOU['bet'] = initialBet;
            updateMoney();
        }
        SPLIT['bet'] = 0;
        document.getElementById("bj-deal-btn").disabled = false;
        document.getElementById("bj-result").style.visibility = "visible";
        updateMoney();
        betButtonCheck();
    }
}

function restartGame() {
    bjGame['money'] = 230;
    YOU['bet'] = 20;
    betButtonCheck();
    updateMoney();
    document.getElementById("restart").style.visibility = "hidden";
    let yourImages = document.querySelector('#your-box').querySelectorAll('img');
    let dealerImages = document.querySelector('#dealer-box').querySelectorAll('img');
    for (i=0; i < yourImages.length; i++) {
        yourImages[i].remove();
    }
    for (i=0; i < dealerImages.length; i++) {
        dealerImages[i].remove();
    }
    document.getElementById("bj-deal-btn").disabled = false;
    document.getElementById("bj-result").style.visibility = "hidden";
    document.getElementById("your-box").style.visibility = "hidden";
    document.getElementById("dealer-box").style.visibility = "hidden";
}