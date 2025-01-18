# Adapting Chain of Contradiction (CoC) for Sarcasm Detection: Extending SarcasmBench with Contradiction Evaluation

**Author**: Joshua Glaspey  
**Email**: jo248954@ucf.edu  
**Institution**: University of Central Florida, Orlando, Florida, USA  

---

## 1. Project Statement  

Sarcasm detection remains a significant challenge in Natural Language Processing (NLP) and Large Language Model (LLM) research due to subtle linguistic cues, sentiment incongruities, and the need for contextual understanding. Zhang et al. introduced **SarcasmBench**, a benchmark that evaluates 11 LLMs and 8 pre-trained language models (PLMs) across six datasets using zero-shot, few-shot, and chain-of-thought (CoT) prompting methods. However, CoT underperforms in sarcasm detection because it fails to address the non-linear and holistic nature of sarcasm.  

This project builds upon SarcasmBench by implementing the **Chain of Contradiction (CoC)** technique, a CoT-based framework tailored to sarcasm detection. CoC analyzes surface sentiment, deduces true intent, and evaluates contradictions between them to detect sarcasm more effectively. The goal is to enhance CoT’s performance on SarcasmBench benchmarks, rivaling zero-shot and few-shot prompting strategies.

---

## 2. Proposed Technique  

The **Chain of Contradiction (CoC)** method decomposes sarcasm detection into three key components:  

1. **Surface Sentiment Analysis**: Identifying literal sentiment via keywords, phrases, or emojis.  
2. **True Intention Deduction**: Analyzing rhetorical devices, tone, and commonsense reasoning to infer deeper meaning.  
3. **Contradiction Evaluation**: Comparing sentiment and intent to classify sarcasm.  

The experimental setup will follow SarcasmBench's testing procedures, utilizing the following six datasets:  

- **IAC-V1** ([1])  
- **IAC-V2** ([2])  
- **Ghosh** ([3])  
- **iSarcasmEval** ([4])  
- **Riloff** ([5])  
- **SemEval-2018 Task 3** ([6])  

Due to resource constraints, a subset of LLMs and PLMs will be used, including GPT-4, Claude 3, LLaMA 3, BERT, and DeBERTa. Performance will be evaluated using precision, recall, accuracy, and F1 score, compared against prior zero-shot and few-shot results.  

---

## 3. Expected Outcomes  

1. **Improved Performance**: CoC is expected to outperform CoT across all SarcasmBench datasets by explicitly modeling sentiment, intent, and contradictions.  
2. **Enhanced Understanding**: The results will provide insights into LLMs’ abilities to handle sentiment incongruence and tone analysis.  
3. **Competitiveness**: CoC is anticipated to rival or surpass zero-shot and few-shot results by forcing LLMs to reason about paradoxical information.  

---

## References  

1. arXiv.org. 2017. "Creating and Characterizing a Diverse Corpus of Sarcasm in Dialogue."  
2. arXiv.org. 2017. "Really? Well. Apparently Bootstrapping Improves the Performance of Sarcasm and Nastiness Classifiers for Online Dialogue."  
3. arXiv.org. 2016. "Fracking Sarcasm Using Neural Networks." In Proceedings of the 7th Workshop on Computational Approaches to Subjectivity, Sentiment, and Social Media Analysis. San Diego, California: Association for Computational Linguistics.  
4. arXiv.org. 2024. "Is Sarcasm Detection a Step-by-Step Reasoning Process in Large Language Models?"  
5. arXiv.org. 2024. "SarcasmBench: Towards Evaluating Large Language Models on Sarcasm Understanding."  
6. Proceedings of the 12th International Workshop on Semantic Evaluation. 2018. "SemEval-2018 Task 3: Irony Detection in English Tweets."  
7. Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing. 2013. "Sarcasm as Contrast Between a Positive Sentiment and a Negative Situation."  
8. The 16th International Workshop on Semantic Evaluation. 2022. "iSarcasmEval: Intended Sarcasm Detection in English and Arabic." Association for Computational Linguistics.  
