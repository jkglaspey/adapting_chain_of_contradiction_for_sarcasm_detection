Adapting Chain of Contradiction (CoC) for Sarcasm Detection: Extending SarcasmBench with Contradiction Evaluation

Joshua Glaspey

jo248954@ucf.edu
University of Central Florida Orlando, Florida, USA

1 Project Statement

<a name="_page0_x317.96_y186.23"></a>Sarcasm detection remains a challenge in Natural Language Pro- cessing (NLP) and Large Language Model (LLM) research due to subtle linguistic cues, sentiment incongruities, and the need for contextual understanding. Zhang et al. ([4[\])](#_page0_x317.96_y218.11) introduced Sarcasm- Bench,whichevaluates11LLMsand8PLMsacrosssixbenchmarks using zero-shot, few-shot, and chain-of-thought (CoT) prompting methods. However, CoT underperforms in sarcasm detection, as it fails to address sarcasm’s non-linear, holistic nature.

ThisprojectbuildsonSarcasmBenchbyimplementingtheChain of Contradiction (CoC) technique ([[3\]),](#_page0_x317.96_y202.17) a CoT-based framework tailoredtosarcasm.CoCdetectssarcasmbyanalyzingsurfacesenti- ment, deducing true intent, and evaluating contradictions between them. The goal is to enhance CoT’s results on SarcasmBench bench- marks, rivaling zero-shot and few-shot prompting strategies.

2. arXiv.org2017.Really?Well.ApparentlyBootstrappingImprovesthePerformance <a name="_page0_x317.96_y202.17"></a>of Sarcasm and Nastiness Classifiers for Online Dialogue. (2017).
2. arXiv.org 2024. Is Sarcasm Detection A Step-by-Step Reasoning Process in Large <a name="_page0_x317.96_y218.11"></a>Language Models? (2024).
2. arXiv.org 2024. SarcasmBench: Towards Evaluating Large Language Models on <a name="_page0_x317.96_y234.05"></a>Sarcasm Understanding. (2024).
2. In Proceedings of the 7th Workshop on Computational Approaches to Subjectiv- ity, Sentiment and Social Media Analysis, pages 161–169, San Diego, California. Association for Computational Linguistics. 2016. Fracking Sarcasm using Neural <a name="_page0_x317.96_y265.93"></a>Network. (2016).
2. Proceedings of the 12th international workshop on semantic evaluation 2018. <a name="_page0_x317.96_y281.87"></a>Semeval-2018 task 3: Irony detection in english tweets. (2018).
2. Proceedings of the 2013 conference on empirical methods in natural language processing 2013. Sarcasm as contrast between a positive sentiment and negative <a name="_page0_x317.96_y305.78"></a>situation. (2013).
2. The 16th International Workshop on Semantic Evaluation 2022, Association for Computational Linguistics 2022. Semeval-2022 task 6: isarcasmeval, intended sarcasm detection in english and arabic. (2022).

2  Proposed Technique

The CoC method decomposes sarcasm detection:

- Surface Sentiment Analysis: Identifying literal sentiment via keywords, phrases, or emojis.
- True Intention Deduction: Analyzing rhetorical devices, tone, and common sense to infer deeper meaning.
- Contradiction Evaluation: Comparing sentiment and intent to classify sarcasm.

TheexperimentalsetupwillinvolverecreatingthesameSarcasm- Bench testing procedure. This involves using the same six datasets: IAC-V1 [\[2](#_page0_x317.96_y186.23)], IAC-V2 [\[1](#_page0_x53.80_y691.41)], Ghosh [[5](#_page0_x317.96_y234.05)], iSarcasmEval [\[8](#_page0_x317.96_y305.78)], Riloff [\[7](#_page0_x317.96_y281.87)], and SemEval 2018 Task 3 [\[6](#_page0_x317.96_y265.93)]. However, due to resource constraints, a smaller set of LLMs/PLMs will be used. This involves the LLMs GPT-4, Claude 3, LLaMA 3, and the PLMs BERT and DeBERT. Re- sults will be evaluated using precision, recall, accuracy, and F1 score, compared against prior results from zero-shot and few-shot methods.

3  Expected Outcomes

First, CoC will outperform CoT on all SarcasmBench datasets by explicitly modeling sentiment, intent, and contradictions.

Second, this will provide a quantifiable result to understand LLMs’ abilities to handle sentiment incongruence and tone analysis.

Third, CoC is expected to rival or surpass zero-shot and few- shot results because CoC forces the LLMs to reason out paradoxical information.

References

<a name="_page0_x53.80_y691.41"></a>[1] arXiv.org 2017. Creating and Characterizing a Diverse Corpus of Sarcasm in

Dialogue. (2017).
