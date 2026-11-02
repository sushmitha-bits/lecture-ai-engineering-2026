Model and settings : Qwen/Qwen3.5-0.8B (revision 2fc06364…, seed 42). LoRA (no quantization), r=16, alpha=32, lr=2e-4, 20 epochs, 6 warmup steps, max_seq_len 512, max_new_tokens 96, greedy generation (do_sample=False).
Did you run the training yourself (executed_training_myself)? Yes
Before training: format_rate = 0.095 (2/21) / content_rate = 0.0 (0/21)
After training: format_rate = 1.0 (21/21) / content_rate = 0.905 (19/21)
Regressed questions: None (regressed is empty).
Remaining failures after training, and their type: 2 of 21, both of the type “asserted an answer to an ungrounded question”. There are no format failures and no cases of escaping to a review request on a grounded question.
“When will grades be released?” The model answered with the assignment deadline and needs_review: false.
“Do office hours need a booking in advance?” The model repeated the Tuesday 17:00 to 18:00 line and needs_review: false. This is a near-miss, because it shares “office hours” with an FAQ item.
Knowledge questions (Section 6): before → after
Question	                                Before	        After
When is the final assignment deadline?	format_error	    asserted
Who is the instructor?	                format_error	    needs_review
What is the theme of the next lecture?	format_error	    needs_review
When is the assignment submission deadline?	format_error	asserted

What I noticed:
Before training, all 4 answers had a broken JSON format (the needs_review key was missing).
For “next lecture theme”, the untrained model gave an unrelated answer about where to submit, which sounds plausible but is wrong.
After training, the model gave a date only for the deadline questions, and asked for confirmation on the instructor name and the lecture theme.
The deadline is in the training FAQ, so giving the date is a reasonable answer.

What changed and what did not:
Changed:
Format correctness went from 9.5% to 100%.
Content correctness went from 0% to 90.5%.
The model learned the habit of asking for review when the FAQ has no answer.

Did not change:
The same 2 ungrounded questions are still answered with confidence.
The evaluation time went from 54.2 s to 45.9 s, which is about the same. This is the time to generate 21 answers, not the training time.

Homework
Level attempted: Basic
Settings or data changed:
Basic: num_train_epochs changed from 20 to 40. Everything else the same.

Results (table and numbers):
Basic
Setting	format_rate	content_rate	Final loss	Training time
20 epochs 	1.0	       0.905	        0.0140	      240 s 
40 epochs	1.0	       0.905	        0.0110	      482 s

Comment: Doubling the epochs lowered the final loss from 0.0140 to 0.0110, but format_rate was at 1.0 and content_rate stayed at 0.905 (19 of 21). Training time roughly doubled. The same two ungrounded questions failed in both runs, so more epochs did not help. The cause is the training data: only 4 of the 14 training examples were ungrounded, and none were near-miss questions like the office hours one. More varied ungrounded examples would be the better fix.

