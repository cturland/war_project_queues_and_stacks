# War Card Game Project (Stacks & Queues)

## 🎯 Learning Goals
- Apply knowledge of **FIFO queues** and **LIFO stacks** to model a card game.
- Implement the **war tie rule** safely, handling edge cases.
- Explain why a **queue** is used for decks and a **stack** for the temporary war pile.

---

## 🃏 Game Rules
1. Two players each start with half a shuffled deck in a queue.
2. Each round:
   - Both players **dequeue** their top card.
   - The higher card wins; both cards go to the **back** of the winner’s queue.
3. If the cards are **equal**, a “war” happens:
   - Create a `Stack` (`war_pile`) **for each player** to store the cards in the tie.
   - Push both tied cards into their respective `war_piles`.
   - Each player (if possible) places:
     - **three face-down cards** (dequeue, push to their `war_pile`).
     - **one face-up card** (dequeue, push to their `war_pile`).
   - Compare the two **face-up** cards:
     - Higher card wins → winner **collects** by taking **their own `war_pile` first**, then the **opponent’s `war_pile`**, adding all collected cards to the **back** of the winner’s queue.
     - If equal again → repeat the war process with the **same** `war_piles`.
   - If a player cannot continue the war (not enough cards), the other player automatically wins the pile **and the game**.
4. The game ends when one player has **all the cards** or a **round limit** is reached.

---

## ⚙️ Part A — Setup & Dealing
- Create a deck: ranks **1..10, J, Q, K** repeated four times and **two `Jo`** (Jokers are the highest card).
- Shuffle the deck.
- Deal cards **alternately** into two `Queue` objects (`p1`, `p2`).
- **Checkpoint:** With Jokers included (54-card deck), each player should start with **27 cards**.

---

## 🕹️ Part B — Playing a Normal Round
- Create a function **`play_round(p1, p2)`** with two parameters (both are `Queue` instances).
- If either queue is empty at the start of a round, the other player has won (or the game ends if both are empty).
- Dequeue **one** card from each player: call them **`c1`** (from `p1`) and **`c2`** (from `p2`). Keep these values to return if there is a tie.
- **Compare** using a consistent rank order where **`Jo` > `K` > `Q` > `J` > `10` > … > `1`.
- If one card is higher:
  - The winner **enqueues** **their own card first**, then the opponent’s card (i.e., *winner_card then loser_card*) to the **back** of the winner’s queue.
  - **Return** the string **`"P1"`** or **`"P2"`** to indicate who won the round.
- If the cards are equal (including `Jo` vs `Jo`):
  - **Return** a value that signals war is required, along with the tied cards, e.g. **`("war", c1, c2)`** so the caller can trigger the war handler.

**Suggested helper (no code):** Define a **rank reference** or **value function** that maps each rank to a comparable order, ensuring **Joker** is the highest.

---

## ⚔️ Part C — Handling a War (3 down + 1 up; separate piles)
- Create **`resolve_war(p1, p2, c1, c2)`** that **assumes** the initial tied cards `c1` and `c2` have already been drawn.
- Create two **`Stack`** objects: one for **Player 1’s war pile** and one for **Player 2’s war pile**.
- **Push** the tied cards `c1` and `c2` onto their respective war piles.
- Repeat the following **war cycle** until there is a winner or someone cannot continue:
  1. **Availability check:** Each player must have **at least 4 cards** available (3 face-down + 1 face-up). If not, the other player immediately wins the accumulated war piles **and the game**.
  2. **Three face-down cards each:** For each player, **dequeue** three cards and **push** them onto their own war pile.
  3. **One face-up card each:** Dequeue one more from each player and **push** to the top of their war pile. Keep references to these two **face-up** values for comparison.
  4. **Compare the face-up cards** using the same rank order as Part B.
     - If **P1** is higher: **collect** by removing **all cards from P1’s war pile first**, adding them to the **back** of `p1`, then remove **all cards from P2’s war pile** and add them to the **back** of `p1`. **Return** `"P1"`.
     - If **P2** is higher: collect in the mirrored order (own pile first, then opponent’s), and **return** `"P2"`.
     - If **equal again**: **repeat** the war cycle (go back to step 1), **continuing to add** to the same war piles.
- Ensure the **order of collection** matches the rule: **winner’s pile first**, then **opponent’s pile**.

---

## 🔁 Part D — Main Game Loop
- Create **`play_game(max_rounds=… )`** that sets up the deck, shuffles, and deals into `p1` and `p2`.
- Keep a **round counter**.
- While **both** queues are **not empty** and you have **not exceeded** `max_rounds`:
  - Call **`play_round(p1, p2)`**.
  - If it returns `"P1"` or `"P2"`, continue to the next round.
  - If it signals **war**, call **`resolve_war(p1, p2, c1, c2)`** with the tied cards.
  - (Optional) Every N rounds, print or log the **round number** and **sizes** of both queues.
- End conditions:
  - If **one queue is empty**, declare the other player the **winner**.
  - If you reached the **round limit**, declare a **draw** (or print final sizes for discussion).

---

## 🧪 Part E — Testing
1. **Joker dominance:** Use a small deck that contains **Jokers vs low ranks** to confirm Jokers always win face-offs.
2. **Forced war:** Construct a mini-deck that will **tie** on the first round and verify **3 down + 1 up** behaviour and collection order (**winner’s pile first, then opponent’s**).
3. **Exhaustion during war:** Start one player with **fewer than 4 cards** and trigger a tie; confirm the opponent **wins immediately** and **collects** any accumulated war piles.
4. **Full game:** Run a complete **54-card** game and verify termination by **win** or **round limit**.

---

## 🧩 Extensions
- **War chains:** Track the **longest chain** of consecutive wars in a game.
- **Telemetry:** Record round-by-round sizes of `p1` and `p2`; plot or review later.
- **Collection variants:** Experiment with **collecting opponent’s pile first**; discuss how/why outcomes change.
- **Replayability:** Allow setting a **random seed** so specific matches can be reproduced.

---

## ❓ Reflection
1. Where do you see **FIFO** and **LIFO** behaviours in your solution?
2. Why does the rule “**winner’s pile first, then opponent’s**” matter for the final ordering of cards?
3. What edge cases did the inclusion of **Jokers** introduce?
4. If the war used **2 down + 1 up** instead of **3 down + 1 up**, which parts of your implementation would need to change?

---

## 🚀 Getting Started
- Ensure your project includes the **`Queue`** and **`Stack`** classes from class.
- Implement **`play_round`**, **`resolve_war`**, and **`play_game`** following the step-by-step guides.
- Test with **mini-decks** before running full games.
- Commit small, frequent changes and keep notes of any rule decisions you make.
