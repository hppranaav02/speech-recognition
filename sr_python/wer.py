import jiwer

with open('original.txt', mode='r') as file:
   original = file.read()

with open('result_google.txt', mode='r') as file:
   result = file.read()

wer_google = jiwer.wer(original, result)

with open('result_sphinx.txt', mode='r') as file:
   result = file.read()

wer_sphinx = jiwer.wer(original, result)


with open('../deepspeech-transcript.txt', mode='r') as file:
   result = file.read()

wer_deepspeech = jiwer.wer(original, result)

with open('result_facebook.txt', mode='r') as file:
   result = file.read()

wer_facebook = jiwer.wer(original, result)

file = open('../answers/answers.txt', mode='w+')
file.write('WER Google: %4.2f'% (wer_google))
file.write('\nWER Sphinx: %4.2f'% (wer_sphinx))
file.write('\nWER DeepSpeech: %4.2f'% (wer_deepspeech))
file.write('\nWER Facebook Wave2Vec2: %4.2f'% (wer_facebook))

print('WER Google: %4.2f'% (wer_google))
print('WER Sphinx: %4.2f'% (wer_sphinx))
print('WER DeepSpeech: %4.2f'% (wer_deepspeech))
print('WER Facebook Wave2Vec2: %4.2f'% (wer_facebook))