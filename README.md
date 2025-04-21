# Adapting Chain of Contradiction (CoC) for Sarcasm Detection: Extending SarcasmBench with Contradiction Evaluation

**Author**: Joshua Glaspey  
**Email**: jo248954@ucf.edu  
**Institution**: University of Central Florida, Orlando, Florida, USA  

---

## 1. Project Statement

Sarcasm detection remains a significant challenge in Natural Language Processing (NLP) due to subtle linguistic cues, sentiment incongruities, and the need for contextual reasoning. Zhang et al. [25] introduced **SarcasmBench**, a benchmark that evaluates 11 LLMs and 8 PLMs across six datasets using zero-shot, few-shot, and chain-of-thought (CoT) prompting. However, CoT underperforms on this task, as sarcasm often requires non-linear, contradiction-driven understanding that CoT does not explicitly model.

This project extends SarcasmBench by implementing the **Chain of Contradiction (CoC)** prompting framework—a reasoning-based approach designed to capture sarcasm by explicitly evaluating sentiment-intent mismatches. The goal is to assess CoC's effectiveness across several datasets and models and determine whether contradiction-based reasoning improves sarcasm detection performance relative to prior prompting methods.

---

## 2. Method Overview

The **Chain of Contradiction (CoC)** method decomposes the sarcasm detection process into three structured steps:

1. **Surface Sentiment Analysis**: Identify the literal sentiment using clues such as keywords, phrases, or emojis.
2. **True Intention Deduction**: Infer the deeper meaning by analyzing tone, rhetorical devices, and language patterns.
3. **Contradiction Evaluation**: Compare sentiment and intent. If they contradict, label the sentence as sarcastic.

This project adapts the CoC framework into SarcasmBench and evaluates it across five benchmark datasets:  

- **IAC-V1**  
- **IAC-V2**  
- **Ghosh**  
- **iSarcasmEval**  
- **SemEval-2018 Task 3**  

The Riloff dataset was excluded due to unavailability. A preprocessing pipeline was implemented to normalize inputs, including emoji-to-hashtag conversion and the removal of malformed samples. Evaluation metrics include precision, recall, F1 score, and accuracy.

---

## 3. Models and Implementation

Three LLMs were selected based on accessibility and resource constraints:

- **GPT-4o-mini** (OpenAI): Used via API for cost-efficient baseline comparisons.  
- **LLaMA 3-8B** (Meta AI): Deployed locally using the oLLaMA framework.  
- **Qwen 2-7B** (Alibaba): Also run locally through oLLaMA, selected for its performance on reasoning tasks.  

Only few-shot CoC prompting was used for final evaluations, and results were directly compared against SarcasmBench’s zero-shot, few-shot, and CoT baselines.

---

## 4. Key Findings

- **Recall and F1 Improvement**: CoC consistently improved recall across most datasets, outperforming CoT and often matching zero-shot or few-shot I/O methods in F1.
- **Dataset Sensitivity**: CoC was most effective on datasets with explicit or lexical sarcasm cues (e.g., Ghosh, IAC-V2), and less so on those requiring abstract inference (e.g., iSarcasmEval).
- **Model Generalization**: Open-source models like LLaMA 3-8B and Qwen 2-7B showed notable performance gains when using CoC, suggesting that contradiction modeling helps compensate for weaker default reasoning.

---

## 5. Future Work

Possible future directions include integrating alternative strategies from the SarcasmCue framework—such as Graph of Cues (GoC), Bagging of Cues (BoC), and Tensor of Cues (ToC)—which structure or aggregate multiple cues to enhance robustness. Additional experiments with a broader set of LLMs (e.g., instruction-tuned or multilingual models) would help confirm whether the observed dataset-level trends hold across architectures. Reinforcement learning-based tuning could also be explored to optimize CoC prompting steps dynamically.

---

## 6. Running the Code

To run the sarcasm detection pipeline using CoC prompting, execute `main.py` from the command line with the appropriate parameters. This script loads the dataset, initializes the selected LLM, runs CoC prompting, and writes model predictions and evaluation metrics to an output file.

### **Usage**
```bash
python main.py --dataset_number <0–5> --llm_number <0–2> --api_key <your_openai_api_key>
```

### **Parameters**
- `--dataset_number`: Select the dataset to evaluate.
  - `0`: Ghosh  
  - `1`: IAC-V1  
  - `2`: IAC-V2 (default subset: general)  
  - `3`: iSarcasmEval  
  - `4`: SemEval-2018 Task 3  
  - `5`: Test Dataset (custom/demo use)

- `--llm_number`: Select which language model to use.
  - `0`: GPT-4o-mini (via OpenAI API)  
  - `1`: LLaMA 3-8B (via oLLaMA)  
  - `2`: Qwen 2-7B (via oLLaMA)  

- `--api_key`: Your OpenAI API key (only needed if GPT is selected)

### **Output**
A results file will be created (or appended to) in the format:

```text
results_dataset<dataset_number>_llm<llm_number>.txt
```

Each file includes:
- Dataset and LLM configuration
- Total samples evaluated
- Ground truth and model prediction for each sample
- Final classification counts (TP, TN, FP, FN)

### **Example**
```bash
python main.py --dataset_number 0 --llm_number 1 --api_key sk-...
```

This runs sarcasm detection on the Ghosh dataset using LLaMA 3-8B via oLLaMA.

### **Note for Local LLMs (LLaMA 3-8B and Qwen 2-7B)**

To run LLaMA or Qwen locally, you must:

1. Install [oLLaMA](https://ollama.com/) (macOS, Linux, or WSL required).
2. Download the model before first use:
   ```bash
   ollama run llama3:8b
   ```
   or
   ```bash
   ollama run qwen2:7b
   ```
3. Keep oLLaMA running in the background while executing `main.py`.

If oLLaMA or the selected model is not active, the script will fail to connect.

---

## References

1. Abu Farha et al. 2022. *SemEval-2022 Task 6: iSarcasmEval*. ACL.  
2. Besta et al. 2024. *Graph of Thoughts: Solving Elaborate Problems with LLMs*. AAAI.  
3. Chen et al. 2021. *Evaluating LLMs Trained on Code*. arXiv:2107.03374.  
4. Devlin et al. 2019. *BERT: Pre-training of Deep Bidirectional Transformers*. ACL.  
5. Ghosh and Veale. 2016. *Fracking Sarcasm Using Neural Networks*. ACL.  
6. Ghosh et al. 2018. *Sarcasm Analysis Using Conversation Context*. arXiv:1808.07531.  
7. Jain et al. 2020. *Sarcasm Detection in Mash-up Language*. Applied Soft Computing.  
8. Liang et al. 2022. *Multi-Modal Sarcasm Detection via Graph Convolutional Networks*. ACL.  
9. Liu et al. 2019. *RoBERTa: A Robustly Optimized BERT Pretraining Approach*. arXiv:1907.11692.  
10. Lukin and Walker. 2017. *Bootstrapping Improves Sarcasm Detection*. arXiv:1708.08572.  
11. Naveed et al. 2024. *A Comprehensive Overview of LLMs*. arXiv:2307.06435.  
12. OpenAI et al. 2024. *GPT-4 Technical Report*. arXiv:2303.08774.  
13. Oraby et al. 2017. *Creating a Diverse Corpus of Sarcasm in Dialogue*. arXiv:1709.05404.  
14. Riloff et al. 2013. *Sarcasm as Contrast Between Sentiment and Situation*. EMNLP.  
15. Touvron et al. 2023. *LLaMA: Open and Efficient Foundation Models*. arXiv:2302.13971.  
16. Van Hee et al. 2018. *SemEval-2018 Task 3: Irony Detection*. ACL.  
17. Wei et al. 2023. *Chain-of-Thought Prompting Elicits Reasoning in LLMs*. arXiv:2201.11903.  
18. Yang et al. 2024. *Qwen2 Technical Report*. arXiv:2407.10671.  
19. Yao et al. 2024. *Is Sarcasm Detection a Step-by-Step Reasoning Process in LLMs?* arXiv:2407.12725.  
20. Yao et al. 2023. *Tree of Thoughts: Deliberate Problem Solving with LLMs*. arXiv:2305.10601.  
21. Yu et al. 2023. *Prophet: Prompting LLMs for Visual Question Answering*. arXiv:2303.01903.  
22. Zhang et al. 2023. *Stance-Level Sarcasm Detection with Graph Attention Networks*. ACM TOIT.  
23. Zhang et al. 2024a. *Pushing the Limit of LLM Capacity for Text Classification*. arXiv:2402.07470.  
24. Zhang et al. 2024b. *DialogueLLM for Emotion Recognition in Conversations*. arXiv:2310.11374.  
25. Zhang et al. 2024c. *SarcasmBench: Evaluating LLMs on Sarcasm*. arXiv:2408.11319.  
26. Zhang et al. 2022. *Automatic Chain-of-Thought Prompting in LLMs*. arXiv:2210.03493.  
27. Ollama. [n.d.]. *Ollama Deployment Platform*. https://ollama.com  