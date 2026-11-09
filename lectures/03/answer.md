# Lecture 3 Answers

## Exercises

- Difference between the answer from Lecture 1 (plain LLM) and the agent's answer:
- Tool calls seen with `--trace` (tool names and arguments):
- Number of LLM calls for one question (`requests`):
- The tool you added, and the description you wrote in its docstring:

## Homework

- Level you worked on: Basic
- What you did: 
    The new version says: when asked about the difference between 2 or more terms, call search_glossary once for each term, then compare. The old version had no such rule.
    Old: “use get_lecture_summary”. New: use it with the number of the relevant lecture.
    Old: always show the lecture (第N回). New: show the lecture the answer is based on, and if you don’t know which one, say so.
    Old: say it is “not in the glossary” (用語集にはない). New: say exactly「用語集にはありません」.
- Result:
    Before changing: 

を学習するPEFT手法。学習するパラ…
[tool return] search_glossary -> [{"term": "QLoRA", "lecture": 2, "definition": "ベースモデルの重みを4ビットなどに量子化してメモリを節約したうえで、LoRAで学習する手法。より大きなモデルを小さなGPUで扱える。本講座の第2…
[usage] RunUsage(cost=Decimal('0.0008138'), details={'text_prompt_tokens': 1196}, input_text_tokens=1196, input_tokens=1196, output_tokens=182, requests=2, tool_calls=2)


************************************************************************
Different question:

uv run python -m app.agent --trace "第2回の要点とLoRAの関係は？"
[model] gemini-3.5-flash-lite
第2回の要点とLoRAの関係についてご説明します。

### 第2回の要点
第2回は「ファインチューニングとLoRA」をテーマに、以下の内容を学習します。
- **事前学習とファインチューニングの違い**：事前学習で汎用的な能力を身につけたモデルを、目的に合うデータで追加学習させる仕組み。
- **SFT（教師あり微調整）**：入力と望ましい出力のペアでモデルを学習させ、出力形式や口調を整える方法。
- **PEFTとLoRAの導入**：全パラメータを更新する従来のファインチューニングに代わり、GPUメモリや保存容量を大幅に削減する効率的な学習手法。
- **演習の体験**：小さなモデル（Qwen3.5-0.8B）を用い、架空FAQデータを使って実際にLoRA学習を行い、学習前後での変化を確かめる。

### LoRAとの関係
第2回において、**LoRAは中心的な学習手法**として位置づけられています。

講座の中では、全パラメータを更新するコストの高さ（GPUメモリ不足など）を解決する技術（PEFT）の一つとしてLoRAが取り上げられています。事前学習済みの重みを固定したまま、小さな低ランク行列（アダプタ）だけを学習させる仕組みや、その主なハイパーパラメータ（ランク $r$ や学習率など）を学びます。さらに、関連する手法として、4bit量子化と組み合わせたQLoRAについても触れられます。

根拠となる講義の回：第2回

--- trace ---
[tool call]   get_lecture_summary({'lecture': 2})
[tool call]   search_glossary({'query': 'LoRA'})
[tool return] get_lecture_summary -> # 第2回 ファインチューニングとLoRA

## この回のねらい

- 事前学習とファインチューニングの違い、ファインチューニングが向く場面と向かない場面を理解する
- LoRAの考え方を理解し、Google Colab上で小さなモデルを…
[tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…
[usage] RunUsage(cost=Decimal('0.0014495'), details={'text_prompt_tokens': 1665}, input_text_tokens=1665, input_tokens=1665, output_tokens=380, requests=2, tool_calls=2)




- Insights / questions:

Result: “Tool calls did not change (2 calls, one per term). Tokens and cost went up about 22% because the prompt got longer.”
Insight: “For a simple comparison question, the model already called the tool once per term, so the clearer instructions did not change the tool use. They only made the prompt longer.”

For your LoRA vs QLoRA question, the model already called the tool once per term, even with the old version. So the new comparison rule (change 1) had nothing to fix. The other changes only made the prompt longer, so the tokens and cost went up.

*************************************************************************

Different question:

For a question that mixed a lecture summary and a term, the model called get_lecture_summary(2) and search_glossary('LoRA') in one step. Requests: 2. Cost: about 0.00145.
Insight: “Clear docstrings helped the model pick the right tool for each part of the question, and pass the right type of input (an integer for the lecture, one term for the query).”
