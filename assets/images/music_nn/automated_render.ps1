#1) ask for inputs; how many, length, etc
$num_outputs = Read-Host -Prompt 'How many tracks to generate?'
$num_steps = Read-Host -Prompt 'How many steps should they be?'
 
 
#2) run nn generation and put them into a folder labeled not processed
polyphony_rnn_generate --run_dir="DIR_WHERE_TRAINED_MODEL_IS_GOING" --hparams="batch_size=64,rnn_layer_sizes=[128,128,128]" --output_dir="DIR_WHERE_GENERATED_FILES_ARE_GOING" --num_outputs=$num_outputs --num_steps=$num_steps --primer_melody="[20]" --condition_on_primer=true --inject_primer_during_generation=false
 
#3) get names of things in the not processed folder
 
$OFS = "`r`n"
 
#that sets the output field seperator, meaning when we collect the childitems and add them to the variable, each var has a carriage return and a new line put at the end of them. or start, i dunno and i dont care.
 
#$fileNames = Get-ChildItem -Path "DIR_WHERE_GENERATED_FILES_ARE_GOING" -Recurse | select -exp Name
 
 
#4) feed the names into the batch processing file
(Get-Content -path test.txt -Raw) -replace 'REPLACE_TEXT', $filenames | Set-Content -Path test.txt
 
#5) run the batch processing
 
               this should be somewhere on your pc from the tests the other day.
 
#6) move the midi files to a processed folder once rendering has completed
 
Get-ChildItem -Path c:/users/nhqadm/desktop/testies -Recurse -File | Move-Item -Destination c:/users/nhqadm/desktop/testing/
 
