# 第1回 解答

## 演習

- 講座に固有の質問（宿題の3レベル）へのモデルの回答（要約でよい）：
- 用語集の正しい意味と比べて気づいたこと：
- 表示できたトークン数（入力 / 出力）：

## 宿題

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：

# Session 1: Answers

## Exercises

- Model answers (summaries are acceptable) to the course-specific questions (the three levels of homework): 

uv run Python -m app.ask "What is LoRA?"
[Model] gemini-3.5-flash-lite

[Question] What is LoRA?
**LoRA** stands for **Low-Rank Adaptation**. It is a popular and efficient technique used in machine learning—specifically in Natural Language Processing (NLP) and generative AI—to **fine-tune large language models (LLMs)** like GPT, LLaMA, or Stable Diffusion.

Developed by researchers at Microsoft in 2021, LoRA solves a major problem in AI: **making massive models work for specific tasks without spending a fortune on computing power.**

Here is a breakdown of how it works, why it matters, and why it has become the industry standard.

---

### 1. The Problem LoRA Solves
Modern AI models are massive, often containing billions of parameters (the internal "weights" that determine how the model responds). 

* **Full Fine-Tuning (The Old Way):** To adapt a model to a new task (e.g., teaching it to write medical reports or mimic a specific art style), you traditionally had to update *all* of its billions of parameters. This requires massive amounts of GPU memory and storage (often hundreds of gigabytes per model).
* **The Cost:** Training full models is expensive, slow, and requires data center-grade hardware.

### 2. How LoRA Works
LoRA takes a smarter, more minimalist approach. 

Instead of changing the original, massive model, **LoRA freezes the original model’s weights** so they cannot be changed. 

It then injects a tiny number of new, trainable layers—called **adapters**—alongside the existing layers. During fine-tuning, **only these new, small layers are trained.**

* **The Analogy:** Imagine you have a massive, professionally tailored suit (the base model). Instead of tearing it apart and remaking it to fit a new trend, you simply pin a small, stylish brooch to the lapel (the LoRA). You get a brand-new look with 99% less effort.

### 3. Why is LoRA so popular? (Key Benefits)
* **Massive Storage Savings:** A full fine-tuned model usually requires storing a whole new multi-gigabyte file. A LoRA file is often just **megabytes** in size (e.g., 10MB to 200MB). You can easily download dozens of LoRAs and swap them out on the fly.
* **Lower Hardware Requirements:** You can train a LoRA on consumer-grade graphics cards (like an NVIDIA RTX 3090/4090) instead of expensive enterprise clusters.
* **Fast Switching:** Because LoRA files are so tiny, a server running a base AI model can load different LoRAs instantly to serve different users or tasks.
* **No Added Latency:** Once training is done, the LoRA weights can be mathematically "merged" back into the original model. This means the model runs just as fast as the original during inference (generation).

### 4. Where is LoRA used?
* **Image Generation:** In the AI art community (like Stable Diffusion), LoRAs are used to teach models specific characters, art styles, or objects. (e.g., "Draw Batman in the style of 1990s anime").
* **Custom Chatbots:** Companies use LoRAs to take an open-source LLM and fine-tune it on their company's internal documents and customer service logs.
[Metrics] time=3.62s input=6 tokens output=720 tokens


uv run Python -m app.ask "What are the '3 List' in the AIE2026 course Homework?"
[Model] gemini-3.5-flash-lite

[Question] What are the '3 List' in the AIE2026 course Homework?
It looks like you are referring to a specific assignment from an **"AIE2026"** course. However, **"AIE2026"** is not a standardized, globally recognized course code—it typically refers to a specific university, boot camp, or online platform's course on Artificial Intelligence and Engineering (often tailored to a specific semester or year, like AI Engineering 2026). 

Because I don't have access to your specific institution's learning management system (like Canvas, Blackboard, Moodle) or the exact syllabus for your instructor's class, I cannot automatically know what the "3 Lists" are.

To help you find the answer, could you provide a little more context?
1. **What is the name of the institution or platform offering the course?** (e.g., a specific university name, Coursera, etc.)
2. **What is the topic of the current module or week?** (e.g., Python basics, Machine Learning algorithms, AI ethics, Prompt Engineering)
3. **Can you paste a snippet of the homework prompt?** 

Once you share that, I'd be happy to help you figure out what the 3 lists are or help you complete the assignment!
[Metrics] time=2.84s input=19 tokens output=265 tokens

[Question] What will we learn in Lecture 2 of AIE2026?
Just like with the homework, **"AIE2026"** is a specific, localized course code (likely for an Artificial Intelligence / AI Engineering course at a specific university, college, or organization) rather than a universal standard. 

Because I don't have access to the internal syllabus, slide decks, or portal of the specific school or program you are taking, I cannot automatically view the exact curriculum for **Lecture 2**.

To give you the correct information, could you tell me:
1. **What is the name of the school, university, or platform offering AIE2026?**
2. **What was covered in Lecture 1?** (This usually gives a big clue about what comes next in the syllabus sequence).
3. **Do you have a syllabus or course outline handy that you can paste an excerpt from?**

Once you provide a little more context, I would be happy to help you figure out what to expect in Lecture 2 or help you prepare for the material!
[Metrics] time=1.32s input=302 tokens output=213 tokens

- Observations made by comparing your answers against the correct definitions in the glossary:
        The answers were similar to glossary. 
- Token count (Input / Output):
    [Metrics] time=3.62s input=6 tokens output=720 tokens
    [Metrics] time=2.84s input=19 tokens output=265 tokens
    [Metrics] time=1.32s input=302 tokens output=213 tokens


## Homework

- Level attempted: Advanced
- Tasks performed: I was able to print the metrics with time taken, input and output tokens.
- Results: Pasted above - model, question and answer
- Insights / Questions: The model performed well - it did not hallucinate.