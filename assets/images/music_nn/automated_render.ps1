#1) ask for inputs; how many, length, etc
$num_outputs = Read-Host -Prompt 'How many tracks to generate?'
$num_steps = Read-Host -Prompt 'How many steps should they be?'


#2) run nn generation and put them into a folder labeled not processed
polyphony_rnn_generate --run_dir="E:\SNES MIDIS\NN\polyphony_rnn\logdir\run3" --hparams="batch_size=64,rnn_layer_sizes=[128,128,128]" --output_dir="E:\SNES MIDIS\Generated Midi" --num_outputs=$num_outputs --num_steps=$num_steps --primer_melody="[20]" --condition_on_primer=true --inject_primer_during_generation=false

#3) get names of things in the not processed folder 

$OFS = "`r`n"

#that sets the output field seperator, meaning when we collect the childitems and add them to the variable, each var has a carriage return and a new line put at the end of them. or start, i dunno and i dont care.

$fileNames = Get-ChildItem -Path "E:\SNES MIDIS\Generated Midi" -Recurse | select -exp fullName


#4) feed the names into the batch processing file

$original = Get-Content -path "C:\Program Files\REAPER (x64)\batch.txt"

(Get-Content -path "C:\Program Files\REAPER (x64)\batch.txt" -Raw) -replace 'REPLACE_TEXT', $filenames | Set-Content -Path "C:\Program Files\REAPER (x64)\batch.txt"

#5) run the batch processing and sleep for $num_outputs x 2.5 seconds

cd "C:\Program Files\REAPER (x64)"
.\reaper -batchconvert batch.txt
$num_outputs = [int]$num_outputs
Start-Sleep -s ((($num_steps/128) * 1.5) * $num_outputs)
#6) move the midi files to a processed folder once rendering has completed

Get-ChildItem -Path "E:\SNES MIDIS\Generated Midi" -Recurse -File | Move-Item -Destination "E:\SNES MIDIS\Rendered Midi"

#7 paste original to file

$original | out-file "C:\Program Files\REAPER (x64)\batch.txt"
