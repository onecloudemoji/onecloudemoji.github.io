# Path to your CSV file
$csvPath = "YuGiOh_Card_List.csv"

# Import the CSV and select a random card
$cards = Import-Csv -Path $csvPath
$randomCard = $cards | Get-Random
$cardName = $randomCard.CardName

Write-Output "Randomly selected card: $cardName"

# Manually replace spaces with '%20' for URL encoding
$encodedCardName = $cardName -replace ' ', '%20'

# Retrieve the JSON data for the card
$response = Invoke-RestMethod -Uri "https://db.ygoprodeck.com/api/v7/cardinfo.php?name=$encodedCardName" -ErrorAction SilentlyContinue

# Check if data was returned
if ($response -and $response.data) {
    # Extract the image URL
    $imageUrl = $response.data[0].card_images[0].image_url
    
    # Save the image using the original card name with spaces removed as the filename
    $fileName = "$($cardName -replace ' ', '')_art.jpg"
    Invoke-WebRequest -Uri $imageUrl -OutFile $fileName

    Write-Output "Image saved as $fileName"
} else {
    Write-Output "Card not found or invalid request. Please check the card name and try again."
}
