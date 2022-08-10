---
title: "Yu-Gi-Oh! GOAT Format Campaign"
date: 2022-08-03
categories:
  - mods
  - games
  
tags:
  - games
---

There are, according to wikipedia, [over 50 different yugioh games out there](https://en.wikipedia.org/wiki/List_of_Yu-Gi-Oh!_video_games). Yet not a single one has a dedicated mode for GOAT format.

GOAT format, called so for both being the greatest of all time and for the proliferation of scapegoat within a lot of decks, is a special era in the game. It runs for a single format in 2005, yet has managed to live on for the past 15 years + since its small reign ended. The objectively best player in the game, Patrick Hoban, says GOAT is the perfect way to practice yugioh; its technical, there are combo trees, its about resource control. It is essentially, the essence of the game. 

Because of this, I decided to take it upon myself (whilst standing on the shoulders of giants whom have done ~~a lot~~ literally all of the work in this field) to create this; a series of custom matches to replace the pendulum campaign with a wild variety of GOAT format decks. In essence, creating my own GOAT campaign.

The steps to do this are rather simple and contrived. I was going to put together a .ps1 script to do this automatically, but if anyone cares enough to actually go down this path, theres a good chance you wont be using the deck lists I set up anyway. There are matches in here that are complete blowouts, and the corresponding reverse duel is nigh on impossible. Still, I thought it was a cool thing to work on in some downtiem I had between pentests.

- Copy your YGO_2020.dat and YGO_2020.toc to a working directory
- Use `yugi_extract.py` to dump resources (found here https://www.moddb.com/mods/requiem-link-evolution/downloads/packing-scripts)
- Inside the folder called ``decks.zip`` are a bunch of ydc files
- [Copy the files from here](https://github.com/onecloudemoji/onecloudemoji.github.io/blob/master/assets/images/yugioh/arcv%20decks.zip) and overwrite all the arcv decks.
- Run `yugi_compress.py` to generate new .dat and .toc
- Rename the files to YGO_2020
- Make a backup of the original .toc and .dat files incase you stuffed it up
- Chuck them into your game directory 
- TADA

Alternatively, if you are unhappy to use my decks:
- Once you have extracted the files, use https://github.com/nzxth2/YGO_LOTD_LE_YDC_Converter to turn these ydc files to text
- Modify the files according to the format within the GitHub readme 
- Use the converter again to turn the txt back into a ydc once you have finished
- Run `yugi_compress.py` to generate new .dat and .toc
- Rename the files to YGO_2020
- Make a backup of the original .toc and .dat files incase you stuffed it up
- Chuck them into your game directory 
- TADA

Why, one might ask, did I replace the fifth campaign? Isn’t that a bit arbitrary? The answer is very simple; I do not like the pendulum mechanic. Not one little bit. "Oh thats because you’re stuck in caveman yugioh and just cant understand the new mechanics and blah blah blah" cries the denizens of the internet whom happily pay their waifu tax and think playing fucking solitaire is the sign of a healthy game. It is not, its bullshit.

The game peaked with the introduction of the XYZ mechanic. This to me was a healthy, natural progression. It encourages you to normal summon, the way the bloody game is supposed to be played. "You mean if I put two of these on the board, I can turn them into something else??" In all honesty it reminds me a lot of the way evolutions were handled in the early days of the Pokémon tcg. 

I say were because I have not played the TCG in so long. I found the most busted way to abuse the TCG GBC game, taking advantage of its mulligan rules and the overwhelming power of the colourless cards. But shit that came out over TWO DECADES AGO, and I just didn’t keep up after that, because **announcement trumpet noises** yugioh came out.

One would probably think they are very clever by making the point "you just like it cause that format was your childhood!" and that smarmy fucko would be wrong. I didn’t know it existed until 5 or so years ago. I have this strange memory of being at my MSP job with my [hacking homie](https://kymb0.github.io/) and just going on an insane diatribe to him about the format whilst sitting on an obtusely high chair and ignoring the tickets in our queue, after we had come back from sinking an obscene number of pints at lunch. He is an MTG man, I think that game stinks.

Its slower. Its interactive. Its turn based. What the fuck do these things mean you ask? The modern game state (2017-202X) is typically done in 3 or 4 moves. Not each, in total. Its a combination of insanely long run on combos that give you an end state board in a single turn (albeit with 30/40 combos sprinkled in to get there) and that the game is mostly reliant on you topdecking the necessary pieces to interrupt these combos. If you do not, you cannot play the game anymore. Boss monsters that block every single action you can take are not healthy. You cannot perform any sort of "comeback" from a game like that.

And that I think sums up in short why I like the GOAT format; its interactive. If I have a board lock with a relinquished and a envoy of the beginning, both of these powerhouses WILL die if I do any of the following
- drop raigeki
- nuke with dark hole
- flip a mirror force (assuming you are using the envoy as spot removal)
- combo a tsuki and a nobleman of crossout
- put down their own envoy

BUT BUTBUT this isn’t any different to the type of format you were just complaining about! It is incredibly different, and if you cant see why then you don’t understand the game well enough. Nothing in GOAT is an omni negate. In fact, negates in general basically don’t exist this far back.

“But hang on”, cries the shithead running trip ulti desires, “didn’t you say you dislike the state from 17 onwards? Pends were introduced in 14!” Yes I know this, and I actively tuned out of the game until MR4 because of their introduction, so I cannot realistically say what the state was like then. Probably hot garbage, but we don’t say untrue things here.

Here is a list of each deck I put into this mod if you are interested in simply dropping in my files. Rest assured if I find a way to get RCE out of this game there will be a massive blog post, but what a waste of time and energy. These are the deck files I am using, nothing more and nothing less.

- 01a deckout
- 01b clown control
- 1a machine otk
- 1b cat control
- 02a ninja aggro
- 02b aitsu koitsu
- 03a strike ninja
- 03b asura otk
- 04a ultimate insect
- 04b aggro bomb
- 05a burn
- 05b coin toss
- 06a pacman "pure advantage camels munch all noobs"
- 06b destiny board
- 07a silent swordsman
- 07b doriado
- 08a hand assault
- 08b dimension fusion turbo
- 09a emissary aggro
- 09b spatial collapse
- 10a flute dragon
- 10b creator
- 11a insect
- 11b pyramid of light
- 12a vanilla aggro
- 12b beatdown
- 13a wall stall
- 13b dragon aggro
- 14a heavy slump
- 14b master monk
- 15a exodia
- 15b direct attack
- 16a flip control
- 16b guardian control
- 17a ben kai otk
- 17b necromancer otk
- 18a lockdown burn
- 18b earth control
- 19a bugroth otk
- 19b empty jar
- 20a chaos recruiter
- 20b library ftk
- 21a water aggro
- 21b fire aggro
- 22a spell economics ftk
- 22b necrovalley monarch
- 23a gravekeeper
- 23b chaos aggro
- 24a ectoplasmer control
- 24b spell counter control
- 25a banish turbo
- 25b chaos turbo
- 26a horus
- 26b chaos return
- 27a plant aggro
- 27b Neo-Daedalus
- 28a bazoo return
- 28b thunder dragon reasoning gate
- 29a rescue cat
- 29b last turn
- 30a drain aggro
- 30b sealmaster
- 31a beastdown
- 31b maha vailo
- 32a spell canceller aggro
- 32b sacred phoenix
- 33a warrior
- 33b pixie control

These all came from https://www.goatformat.com/decks.html

Eagle eyed readers may notice the list does NOT contain a goat control. This is because I have a different match in campaign 1 set up to have a classic goat control. This is a personal, selfish choice because I also wanted the ability to take my goat deck and verse all these different specimens without a mirror match. 

I have been having enormous amounts of fun taking my dedicated GOAT control deck against this list. The AI really gets how to play these decks; I’ve given it the [Feb 2020 DragonLink](https://www.youtube.com/watch?v=xBX-dOaNA-g) and it’s unable to pilot it, same as peak [Sky Striker](https://www.youtube.com/watch?v=f3qzP3xZbX0). That video in particular, is of note to me. I was listening to it whilst I was driving to the DHL collection place to get my OSCP cert. 

I have zero interest in ever taking this shit online. Years ago I wiped a YGOPRO public arena with a degenerate mystic mine burn deck; the fact that people like that can exist without penalty means online isn’t for me.   

Anyway I hope you enjoy this rant/showcase. Stay tuned for any future projects on this game, but I am unsure what else I wish to do with it. A lot of the ideas I had have already been implemented [like this one which allows cpu vs cpu duels](https://github.com/pixeltris/Lotd)!

![yugioh](/assets/images/yugioh/yugioh.png)
