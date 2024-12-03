# Define the API URL
$apiUrl = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

# Fetch all cards from the API
$response = Invoke-RestMethod -Uri $apiUrl

# Define the set names, including expansions, starter decks, structure decks, and special releases, up to "Light of Destruction"
$targetSets = @(
    # Main Sets
    "Legend of Blue Eyes White Dragon", "Metal Raiders", "Spell Ruler", "Pharaoh's Servant",
    "Labyrinth of Nightmare", "Legacy of Darkness", "Pharaonic Guardian", "Magician's Force",
    "Dark Crisis", "Invasion of Chaos", "Ancient Sanctuary", "Soul of the Duelist",
    "Rise of Destiny", "Flaming Eternity", "The Lost Millennium", "Cybernetic Revolution",
    "Elemental Energy", "Shadow of Infinity", "Enemy of Justice", "Power of the Duelist",
    "Cyberdark Impact", "Strike of Neos", "Force of the Breaker", "Tactical Evolution",
    "Gladiator's Assault", "Phantom Darkness", "Light of Destruction",

    # Starter Decks
    "Starter Deck: Yugi", "Starter Deck: Kaiba", "Starter Deck: Joey", "Starter Deck: Pegasus",
    "Starter Deck: Yugi Evolution", "Starter Deck: Kaiba Evolution", "Starter Deck 2006",
    "Starter Deck: Syrus Truesdale", "Starter Deck: Jaden Yuki", "Starter Deck: Yugi Reloaded",
    "Starter Deck: Kaiba Reloaded",

    # Structure Decks
    "Structure Deck: Dragon's Roar", "Structure Deck: Zombie Madness", "Structure Deck: Blaze of Destruction",
    "Structure Deck: Fury from the Deep", "Structure Deck: Warrior's Triumph", "Structure Deck: Spellcaster's Judgment",
    "Structure Deck: Invincible Fortress", "Structure Deck: Lord of the Storm", "Structure Deck: Dinosaur's Rage",
    "Structure Deck: Machine Re-Volt", "Structure Deck: Spellcasters Command", "Structure Deck: Rise of the Dragon Lords",

    # Special Releases
    "Dark Beginning 1", "Dark Beginning 2", "Dark Revelation Volume 1", "Dark Revelation Volume 2",
    "Dark Revelation Volume 3", "Dark Revelation Volume 4", "Champion Pack: Game One", "Champion Pack: Game Two",
    "Champion Pack: Game Three", "Champion Pack: Game Four", "Champion Pack: Game Five", "Champion Pack: Game Six"
)

# Filter the cards by checking each card's sets
$filteredCards = foreach ($card in $response.data) {
    foreach ($set in $card.card_sets) {
        if ($targetSets -contains $set.set_name) {
            [PSCustomObject]@{
                CardName = $card.name
                SetName = $set.set_name
                Type = $card.type
                Level = $card.level
                Attribute = $card.attribute
            }
        }
    }
}

# Check if any cards were filtered
if ($filteredCards.Count -gt 0) {
    Write-Output "Cards found: $($filteredCards.Count). Exporting to CSV."
    # Export to CSV
    $filteredCards | Export-Csv -Path "YuGiOh_Card_List.csv" -NoTypeInformation -Encoding UTF8
} else {
    Write-Output "No cards matched the specified sets. Please check the set names."
}
