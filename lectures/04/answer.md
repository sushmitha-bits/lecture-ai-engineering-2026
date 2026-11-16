Exercise
What I changed: the order of the judgment. I changed the output of CriterionVerdict from reason to "verdict to verdict" to reason, and updated the instruction text to match. I did not change the grading model or the rubric.
Labels used for comparison: lectures/04/reference/labels_instructor.jsonl (because my own lectures/04/labels.jsonl was not in this checkout)
Match per criterion (after the change, gemini-3.5-flash-lite, 10 items):
Criterion	Match
Grounding	8/10
Scope	10/10
Hint	10/10
Clarity	10/10
Round label (code)	10/10
Needs review (after the change): 0 items. Overall match is 10/10.
Change compared with before: I tried grading before the change several times, but the Gemini API returned 503 and the runs did not finish, so I could not get the per-criterion match or the number of items needing review. Because of this, I cannot calculate the before/after difference. After the change, grading finished.
Items where the instructor’s label and my label differed, and why I judged them that way:
Notes / questions:
Homework


Level I worked on: Basic

What I did: In app/judge.py, I changed the CriterionVerdict output order from reason to "verdict to verdict" to reason and updated the instruction text to match. I kept the grading model and rubric unchanged, then graded against the instructor labels.

Result: After the change, agreement was Grounding 8/10, Scope 10/10, Hint 10/10, Clarity 10/10, and Round label 10/10; there were 0 needs-review items. The before-change runs did not finish because the API returned 503, so I could not calculate a before/after difference.

Notes / questions: The post-change run completed, but without a completed baseline I cannot tell whether changing the output order affected agreement. A fair comparison needs completed runs under both orders with the same model and labels.

