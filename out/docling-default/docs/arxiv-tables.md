## Beyond Text: LLM-Based Dimensional Emotion Evaluation in Multimodal Dialogue

Yutong Hu and Jinho Choi

Emory University Atlanta, GA

yutong.hu@emory.edu, jinho.choi@emory.edu

## Abstract

Emotion recognition in conversation has been widely studied, but applying Large Language Models (LLMs) to continuous dimensional emotion evaluation in multimodal dialogue remains largely unexplored. We propose an LLM-based framework that performs discrete emotion recognition and Valence-Arousal-Dominance (VAD) dimensional evaluation on IEMOCAP, incorporating acoustic cues as natural language descriptions following the SpeechCueLLM approach. We evaluate six models spanning the LLaMA, GPT, and Qwen families under zero-shot prompting, fewshot prompting, and LoRA fine-tuning. LoRA fine-tuned LLaMA models substantially outperform prompt-engineered GPT models on both tasks despite GPT's larger scale, a gap we attribute to domain adaptation rather than model capacity. Our best model achieves a Valence CCC of 0.7822, a new state-of-the-art on IEMOCAP. Ablation studies confirm that textual audio descriptions meaningfully improve smaller models (+3.5-3.6 weighted F1) while contributing little for the largest model, suggesting audio cues are most valuable when linguistic capacity is limited. The performance asymmetry across VAD dimensions closely mirrors the annotator agreement hierarchy in IEMOCAP's own annotations.

## 1 Introduction

Emotion recognition in conversation (ERC) has gained attention for the past two decades. Unlike isolated utterance-level analysis, ERC requires the contextual understanding of utterances across multiple conversational turns with dynamic emotions (Wu et al., 2025a). This conversational dependency makes the problem substantially more challenging and more consequential for real-world applications such as mental health support and human-computer interaction.

There are two common ways for emotion representation. The first way is a discrete emotion label, which assigns a single categorical label(e.g. happiness, frustration, etc.) to an utterance. The second one is continuous dimensional emotions, which quantify emotional experience along continuous scales. And among the continuous dimensions, the Valence-Arousal-Dominance (VAD) system (Russell and Mehrabian, 1977) is the most widely adopted, measuring how positive, activated, and dominant a person feels. While discrete ERC has received the bulk of the attention (Lei et al., 2023; Wu et al., 2025b), dimensional evaluation has grown more recently, driven by the demand for richer emotional characterization.

Because emotions are not conveyed only by words alone, the incorporation of multimodal information is critical for both tasks: tone, pitch, rhythm, and speaking rate all carry affective signals that text transcriptions discard. The involvement of multimodality is therefore essential not only for the accuracy but also for the diverse potential downstream applications, such as emotion-conditioned speech generation.

Currently, for multimodal ERC on VAD systems, Large Language Models (LLM) are barely used in this regime; instead, most dimensional work on multimodal dataset still relies on Deep Learning(DL) models, including LSTM and CNN-1D (Atmaja and Akagi, 2021; Messaoudi et al., 2024), or pre-trained models such as HuBERT or DeBERTa, limiting the contextual reasoning capacity to exploit (Srinivasan et al., 2022; Ispas et al., 2023). To address this gap, we make the following contributions:

- We propose the first systematic LLM-based framework for continuous VAD dimensional emotion evaluation in multimodal dialogue, extending the SpeechCueLLM approach of incorporating acoustic cues as natural language descriptions from discrete ER to the dimensional setting.

- We conduct a comprehensive comparison across six models spanning the LLaMA, GPT, and Qwen families under prompt engineering and LoRA fine-tuning, showing that parameter-efficient fine-tuning substantially outperforms prompting-based approaches for both discrete and dimensional emotion tasks, despite the larger scale of the prompted models.
- Through error analysis and ablation studies, we identify the sources of the performance gap between fine-tuned and prompted models, the contribution of acoustic descriptions to performance, and the effect of past VAD context on prediction quality.

## 2 Background and RelatedWork

## 2.1 Discrete Emotion Recognition in Dialogue

Early DL approaches to Emotion Recognition (ER) employed CNNs for end-to-end speech representations (Trigeorgis et al., 2016), LSTMs for sequential dialogue modeling (Poria et al., 2017), and graph-based architectures (Ghosal et al., 2019). DialogueRNN (Majumder et al., 2019), which models speaker state, emotion state, and global context via an attentive RNN, remains one of the most influential baselines for ERC on IEMOCAP and MELD. More recently, InstructERC (Lei et al., 2023) reformulates ERC as an instruction-following task using multi-task retrieval-augmented prompting. SpeechCueLLM (Wu et al., 2025b) extends this LLM-based approach to the multimodal setting by incorporating vocal information as natural language descriptions of acoustic features. This work directly adopted that framework for acoustic information incorporation.

## 2.2 Dimensional Emotion Evaluation

The Valence-Arousal-Dominance (VAD) framework (Russell and Mehrabian, 1977) provides a richer characterization of emotional state than discrete labels, capturing the positive-negative, activation-deactivation, and power axes respectively. Multimodal approaches combining audio and text for VAD prediction on IEMOCAP, using architectures such as LSTM/CNN-1D (Atmaja and Akagi, 2021; Awatef et al., 2025), have advanced performance substantially. However, LLMs remain largely absent from this regime; the contextual reasoning capacity that drives gains in discrete ERC

has not been systematically evaluated for continuous VAD prediction in multimodal dialogue, which is the gap this work addresses.

## 2.3 Available Multimodal Models for Audio and Text Data

Models capable of jointly processing audio and text fall into two broad categories: audio-language foundation models (e.g., Wav2Vec 2.0 (Baevski et al., 2020), CLAP (Elizalde et al., 2022), and SpeechT5 (Ao et al., 2022)), which learn generalpurpose audio representations; end-to-end conversational multimodal LLMs (e.g., Qwen3-Omni, GPT-5.1, and Gemini 3 Pro), which map speech directly into semantic representations within unified dialogue frameworks. This work does not adopt the latter due to their substantial computational requirements and uncertain impact on specialized ER tasks, leaving their exploration to future work.

## 3 Methods

## 3.1 Framework Overview

This work proposes an LLM-based framework for performing discrete ER and continuous VAD dimensional evaluation on utterances in multimodal dialogues. While those two tasks share the same input construction strategy, they are treated as independent tasks, each with its own prompt formulation, and in the case of the LoRA fine-tuning, its own separately trained model instance adapted to the corresponding annotation type. The framework takes three sources of information as input: the conversation history, the target utterance, and the audio feature descriptions. A discrete emotion label will be output for the discrete ER, while a set of VAD scores (the representation the emotional state along Valence, Arousal, and Dominance dimensions) will be output for the continuous emotion evaluation.

Figure 1 and the algorithm 1 illustrate the overall pipeline. Given a target utterance from IEMOCAP, the framework retrieves the preceding structured conversation (up to 12 utterances in this study) to provide dialogue context. Simultaneously, acoustic features are extracted from the audio recording of the target utterance and converted to natural language descriptions following SpeechCueLLM approach (Wu et al., 2025b). Based on the required task and passed structured text prompts with all required inputs, the models will output either the discrete emotion category selected from a predefined label set (happy, sad, neutral, angry, excited, Input Construction and frustrated) or numerical integer VAD scores on a 1-5 scale. The framework is designed to allow direct comparison across models of different scales and training paradigms. In this work, we evaluate the framework mainly under two strategies: prompt engineering (zero-shot and few-shot) and LoRA fine-tuning.

<!-- image -->

Figure 1: Overall Pipeline

## 3.2 Audio Feature Extraction and Textual Description

A central design choice of this framework is to incorporate acoustic information in natural language descriptions rather than raw audio features or learned audio embeddings. This approach, adopted from SpeechCueLLM (Wu et al., 2025b), enables LLMs to access audio information that is included in the input without requiring architectural modification to handle the multimodal input directly.

For each utterance in this dataset, three acoustic features are extracted from the raw audio recording: the perceived volume, pitch, and speaking rate. For each of the features, both the central tendency and the degree of variation within the utterances are computed, yielding six descriptive values in total for each utterance.

To convert these acoustic measurements into natural language descriptions, a quantile-based scheme is utilized to assign one of the categorical labels to acoustic feature values and variation measurements: very low, low, moderate, high, or very high. This produces a concise and interpretable description of each utterance's acoustic information as in Figure 5.

This textual audio description provide models with non-lexical cues that are not recoverable from the transcribed text alone. And the contribution of the audio description to model performance is evaluated through an ablation study comparing models with or without them, the results of which are discussed in Section 11.1.

## 3.3 Fine-Tuning Strategy (LoRA)

While LLMs possess strong general language understanding capabilities, adaption to the target domain and annotation conventions is often required for their effective application to specialized tasks. Full fine-tuning of LLMs is computationally expensive given the scale of the modern models, as it requires updating all model parameters simultaneously. To address this, we adopt Low-Rank Adaptation(LoRA), a parameter-efficient fine-tuning method that introduces a small number of trainable parameters while keeping the original model weights frozen (Hu et al., 2021).

The IEMOCAP dataset, while the most appropriate available resource for this task, provides a limited number of training samples compared to the scale of the datasets those LLMs were originally trained on. LoRA's constrained parameterization reduces the risk of overfitting under the data-limited situation.

## 4 Experiment Setup

## 4.1 Dataset

This study requires the dataset to satisfy: (I) multimodal, containing at least audio and text modalities; (II) conversational; (III) annotated with both discrete and continuous emotion. While textual emotion datasets with discrete labels are relatively common, datasets meeting all three criteria are rare. After reviewing 19 emotion datasets in total (see Table 8 in Appendix B), we chose IEMOCAP (Busso et al., 2008), one of the most widely used datasets for multimodal emotion research.

## 4.1.1 IEMOCAP Dataset

The Interactive Emotional Dyadic Motion Capture (IEMOCAP) (Busso et al., 2008) dataset is a multimodal corpus designed for the study of expressive human communication in dyadic interaction. The dataset consists of 151 dyadic dialogues performed by 10 actors arranged in five sessions, each pairing one male and one female actor. The recordings include both scripted scenarios and improvised interactions elicited through emotional prompts, yielding a total of 10,086 utterances with an average of approximately 66 utterances per dialogue.

The dataset captures four modalities for each utterance: audio recordings, video recordings, text transcriptions, and motion capture data tracking facial and hand movements. The total duration of all audio recordings is approximately 12 hours. In this work, we only utilized the audio recordings and text transcriptions, as these modalities are most directly relevant to the proposed framework and align with the SpeechCueLLM approach adopted for audio feature extraction.

Each utterance in IEMOCAP is annotated by multiple evaluators with a discrete emotion category. The final label is determined by majority voting across annotators. The original label set covers nine categories: anger, sadness, frustration, happiness, excitement, neutral state, surprise, fear, and other. In addition to categorical labels, annotators provided VAD ratings on a scale of 1 to 5, where higher values indicate more positive valence, higher arousal, and greater dominance respectively. The aggregated annotator VAD scores were used as the ground truth for each utterance in this work.

For the discrete ER task, we followed common practice in the literature (Wu et al., 2025b; Lei et al., 2023), excluding low-frequency categories Surprise, Fear, and Others from the label set and arriving at six discrete emotion categories and a total of 7,433 utterances.

## 4.1.2 Data Splitting

To evaluate model generalization across speakers, we adopted a Leave-One-Subject-Out (LOSO) splitting strategy. Specifically, the fifth session of IEMOCAP was held out as the test set, as it contains unseen speakers not present in the training data, ensuring the model is evaluated on its ability to generalize to new speakers. The remaining four sessions were used for training and validation, split at a 90/10 ratio respectively. This splitting strategy is consistent with prior work on IEMOCAP.

## 4.2 Models

We evaluated the proposed framework across six language models spanning three families (the Qwen model was only used for discrete ER evaluation), enabling comparison between open-source and closed-source systems as well as across different parameter scales.

Within the open-source models, we selected three models from the LLaMA series: LLaMA-2-7B, LLaMA-3.1-8B, and LLaMA-3.370B. LLaMA-2-7B and LLaMA-3.1-8B represent smaller, more computationally accessible configurations, while LLaMA-3.3-70B represents a largescale model. To evaluate more comprehensively, we also included the Qwen3.5-35B-A3B model for the discrete ER task. All three LLaMA models were evaluated under zero-shot prompting, fewshot prompting, and LoRA fine-tuning conditions for discrete ER, and only LoRA fine-tuning for VAD evaluation.

For closed-source comparison, we included two OpenAI models: GPT-4o-mini and GPT-5-mini. GPT models are evaluated under zero-shot and fewshot prompting conditions only.

## 4.3 Implementation Details

For LoRA fine-tuning, we used the AdamW optimizer with a learning rate of 0.0003. The LoRA rank is set to r = 16 with the scaling parameter α set equal to r, following standard practice. All models are trained for 15 epochs.

For the LLaMA-3.3-70B model, training was conducted using DeepSpeed to handle the memory requirement of the 70-billion-parameters configurations across two GPUs. Smaller models were trained on a single GPU configuration.

For prompt engineering conditions, zero-shot prompts follow the templates described in Appendix C Few-shot prompts prepend a fixed set of annotated examples to the same template.

## 5 EvaluationMetrics

## 5.1 Discrete ER

The discrete emotion recognition task was evaluated using the weighted F1 score, defined as:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where wi is the proportion of samples belonging to class i and F1i is the F1 score for that class. The weighted F1 score is chosen over macro F1 because it accounts for class imbalance in the IEMOCAP dataset, where emotion categories are not uniformly distributed.

## 5.2 VAD Evaluation

The VAD evaluation task was assessed using the Concordance Correlation Coefficient (CCC), which jointly captures both the correlation and the agreement between predicted and ground truth values by penalizing mean offset in addition to variance differences:

<!-- formula-not-decoded -->

where r is the Pearson correlation, σx and σy are the standard deviations, and µx and µy are the means of the predicted and ground truth distributions respectively. CCC ranges from -1 to 1, where 1 indicates perfect agreement.

## 6 Emotion Recognition Results

Table 1 reports weighted F1 scores for discrete ER across all six models and training/prompting conditions, including comparison with SpeechCueLLM (Wu et al., 2025b) baseline.

The most prominent finding is the LoRA finetuned open-source models consistently outperform the prompt-engineered ones. With all three LoRA fine-tuned LLaMA models achieving scores between 71.8 and 73.2 along with the fine-tuned Qwen3.5 model of 68.493, there is a large gap between prompt engineering and LoRA fine-tuning for open-source models used here. Among prompt engineering conditions, LLaMA-3.3-70B zero-shot (60.299) performs comparably to GPT-4o-mini fewshot (56.8), suggesting that scale partially compensates for the absence of task-specific adaptation. Fine-tuned models uniformly surpass all prompting-based approaches, including GPT-5mini few-shot (59.6).

## 7 VAD Evaluation Results

Table 2 reports VAD evaluation performance for prompt-engineered GPT models and LoRA finetuned LLaMA models. Due to the huge gap between the performance of LLaMA models with LoRA fine-tuning and with the prompt engineering, we only applied LoRA fine-tuning for LLaMA models within the experiment for VAD evaluation.

Among GPT models, GPT-5-mini outperforms GPT-4o-mini across most conditions. The most pronounced difference appears on the Dominance dimension, where GPT-5-mini zero-shot achieves a CCC of 0.299 versus 0.146 for GPT-4o-mini zero-shot. Valence is the best-predicted dimension across all prompt engineering conditions (CCC 0.60-0.67), while Arousal and Dominance remain substantially lower (CCC 0.13-0.39).

LoRA fine-tuned LLaMA models substantially outperform all prompt-engineered approaches. On Valence, LLaMA-3.3-70B achieves a CCC of 0.7822, leading the best GPT-5-mini prompting result of 0.6697 by around 0.11. LLaMA-2-7B and LLaMA-3.1-8B also achieve strong Valence CCC values of 0.7672 and 0.7433 respectively, demonstrating that the gain is not primarily attributable to model scale. On Arousal and Dominance, LoRA fine-tuned models also outperform GPT prompting (CCC values from 0.44 to 0.48 vs. from 0.34 to 0.39 for Arousal and around 0.44 vs. from 0.12 to 0.30 for Dominance), though absolute values remain substantially lower than Valence.

Table 3 compares our best model against prior works on VAD evaluation on IEMOCAP; our approach achieves state-of-the-art performance on the Valence dimension, surpassing all baselines by a substantial margin, while Arousal and Dominance remain competitive but below the best reported results.

Among those previous works, the one by Awatef et al. (Awatef et al., 2025), even though it has a lower Valence CCC, outperforms our model on both Arousal (0.736 vs. 0.465) and Dominance

Table 1: Discrete ER Performance of All Models (Weighted F1 score)

|           |   LLaMA-2-7B |   LLaMA-3.1-8B |   LLaMA-3.3-70B |   Qwen3.5-35B-A3B | GPT 4o mini   | GPT 5 mini   | SpeechCueLLM (Wu et al., 2025b)   |
|-----------|--------------|----------------|-----------------|-------------------|---------------|--------------|-----------------------------------|
| Zero-shot |        9.058 |         31.293 |          60.299 |            14.317 | 54.700        | 58.490       | -                                 |
| Few-shot  |       25.675 |         38.762 |          58.280 |            21.832 | 56.822        | 59.600       | -                                 |
| LoRA      |       73.196 |         71.818 |          72.122 |            68.493 | -             | -            | 72.021                            |

Table 2: VAD Evaluation Performance Comparison Across Different Models

| Metric    |   GPT-4o mini - Zero-shot |   GPT-4o mini - Few-shot |   GPT-5 mini - Zero-shot |   GPT-5 mini - Few-shot |   LoRA Fine-tuned LLaMA Model - 2-7B |   LoRA Fine-tuned LLaMA Model - 3.1-8B |   LoRA Fine-tuned LLaMA Model - 3.370B |
|-----------|---------------------------|--------------------------|--------------------------|-------------------------|--------------------------------------|----------------------------------------|----------------------------------------|
| Valence   |                    0.6024 |                   0.6311 |                   0.6630 |                  0.6697 |                               0.7672 |                                 0.7433 |                                 0.7822 |
| Arousal   |                    0.3393 |                   0.3589 |                   0.3926 |                  0.3416 |                               0.4406 |                                 0.4778 |                                 0.4653 |
| Dominance |                    0.1458 |                   0.1235 |                   0.2990 |                  0.3046 |                               0.4388 |                                 0.4400 |                                 0.4413 |
| Overall   |                    0.3625 |                   0.3712 |                   0.4515 |                  0.4386 |                               0.5489 |                                 0.5537 |                                 0.5629 |

(0.604 vs. 0.441) by a notable gap. Their work utilized LSTM and CNN-1D models with a late fusion by Neural Network. While their architecture was trained end-to-end on acoustic features, our approach used discretized textual audio descriptions. The Valence gain suggests LLMs bring complementary contextual reasoning that compensates on the dimension with highest annotator agreement.

## 8 Error Analysis for Discrete ER

While the substantial performance gap between LoRA fine-tuned LLaMA models and promptengineered GPT models is somewhat unexpected given the latter's considerably larger scale, a closer examination of per-emotion F1 scores and confusion patterns helps explain this discrepancy. Tables 4 and 5 present the per-emotion F1 scores and key bidirectional confusion rates respectively.

Based on Table 4, all models (despite LLaMA2-7B and LLaMA-3.1-8B with few-shot) have the best performance for Sad emotion. The promptengineered GPT models are outperformed by finetuned LLaMA models under every emotion category. For GPT models, Happy and Angry are the two discrete emotions where they have the lowest F1 scores. Few-shot prompting generally slightly improved GPT models' performance over zero-shot prompting. GPT-4o-mini gets similar scores to GPT-5-mini for Frustrated and Sad, slightly outperforms it in Happy, and underperforms for Neutral, Angry, and Excited. Table 5 implies the potential reason for GPT models not meeting our expectations. GPT models have high confusion rates on angry and frustrated. The confusion rates of 46.5-75.3 for GPT models on misinterpreting anger as frustration show they are less sensitive to aggressiveness. One interesting difference between GPT-4o-mini and GPT-5-mini models is that GPT-5-mini tends to overestimate the energy of positive emotions (confusion rate of 29.2-30.6 on Happy→Excite vs. 18.4-22.1 for Excite→Happy), while GPT4o-mini, in contrast, is more conservative about the positive levels (confusion rate of 7.6-12.5 on Happy→Excite vs. 22.7-29.8 for Excite→Happy). That explains why LoRA fine-tuned LLaMA models outperform GPT models here.

The poor performance of LLaMA-2-7B and LLaMA-3.1-8B models with prompt engineering can also be explained now. They tend to collapse most emotions into a single label, as presented by the extremely high ratio of excitement instances misclassified as happiness and the low confusion rate over other emotion label pairs.

## 9 VAD Evaluation Performance Analysis

A consistent hierarchy emerges across all model families and training conditions: Valence is predicted substantially better than Arousal, which is predicted at roughly the same level as Dominance. This pattern holds both for GPT prompt-engineered models (Valence CCC 0.60-0.67 vs. Arousal CCC 0.34-0.39) and for LoRA fine-tuned LLaMA models (Valence CCC 0.74-0.78 vs. Arousal CCC 0.44-0.48). The gap is particularly striking given that all three dimensions share the same scale, annotation protocols, and model architecture.

This performance hierarchy directly mirrors the annotator agreement hierarchy reported in Table 6. Valence has the highest inter-annotator agreement (Krippendorff's α = 0.680), while Dominance has the lowest (α = 0.271) and Arousal is intermediate (α = 0.304). When annotators themselves disagree substantially, the annotation ground truth is inherently noisy, imposing a natural ceiling on achiev-

|                                           | Modalities   |   Valence CCC |   Arousal CCC |   Dominance CCC |
|-------------------------------------------|--------------|---------------|---------------|-----------------|
| Atmaja et al. (Atmaja and Akagi, 2021)    | Audio, Text  |         0.553 |         0.579 |           0.456 |
| Messaoudi et al. (Messaoudi et al., 2024) | Audio        |         0.236 |         0.571 |           0.408 |
| Awatef et al. (Awatef et al., 2025)       | Audio, Text  |         0.603 |         0.736 |           0.604 |
| The Proposed                              | Audio, Text  |         0.782 |         0.465 |           0.441 |

The proposed here is LLaMA-3.3-70B with LoRA fine-tuning

Table 3: Comparison with Prior Work on VAD Evaluation on IEMOCAP

Table 4: Per-emotion F1 score (%)

| Model            |   Happy |   Sad |   Neutral |   Angry |   Excited |   Frustrated |
|------------------|---------|-------|-----------|---------|-----------|--------------|
| GPT-4o-mini ZS   |      49 |    70 |        53 |      32 |        53 |           60 |
| GPT-4o-mini FS   |      46 |    74 |        55 |      40 |        56 |           60 |
| GPT-5-mini ZS    |      42 |    70 |        57 |      45 |        63 |           61 |
| GPT-5-mini FS    |      43 |    70 |        60 |      53 |        61 |           61 |
| LLaMA-2-7B ZS    |      28 |     2 |         4 |       3 |         5 |            8 |
| LLaMA-2-7B FS    |      40 |     3 |         5 |       4 |         9 |            7 |
| LLaMA-3.1-8B ZS  |      41 |    55 |        52 |      22 |         6 |           15 |
| LLaMA-3.1-8B FS  |      44 |    42 |        54 |      38 |        24 |           37 |
| LLaMA-3.3-70B ZS |      50 |    78 |        31 |      70 |        67 |           40 |
| LLaMA-3.3-70B FS |      42 |    74 |        58 |      44 |        57 |           56 |
| FT LLaMA-2-7B    |      63 |    83 |        75 |      69 |        72 |           72 |
| FT LLaMA-3.1-8B  |      66 |    84 |        74 |      61 |        71 |           69 |
| FT LLaMA-3.3-70B |      61 |    80 |        73 |      65 |        78 |           69 |

ZS: zero-shot; FS: few-shot; FT: fine-tuned.

able model performance. The agreement hierarchyValence, Arousal, Dominance- is consistent with the VAD evaluation performance.

## 10 Annotator Reliability

Because emotions are subjective, annotators are likely to have different answers for the same target sentence. We conducted an inter-agreement measurement with Krippendorff's α and Fleiss' κ to test the reliability of data. Table 6 reports the test results for each annotation type in IEMOCAP.

Discrete emotion labels achieve only fair agreement (α = 0.279 and κ = 0.273), reflecting inherent ambiguity in emotion assignment. Valence shows substantially higher agreement (α = 0.680). Arousal shows intermediate agreement (α = 0.304 and κ = 0.085), comparable to discrete labels. Dominance shows near-floor alpha and also near-zero Kappa (α = 0.271 and κ = 0.014), suggesting that while annotators show some ordinal agreement on dominance, they diverge substantially on absolute scores. These reliability statistics contextualize the model performance results for VAD evaluation.

## 11 Ablation Studies

## 11.1 The Impact of Acoustic Feature Descriptions

Natural language audio description is part of the input to LLMs. We also conducted experiments to reveal the contribution of audio feature description to final performance by removing audio feature descriptions in discrete ER performance for LoRA fine-tuned LLaMA models. Table 7 reports this impact driven by the removal.

Removing audio descriptions reduces weighted F1 by 3.5 for LLaMA-2-7B (73.2 vs. 69.7) and 3.6 for LLaMA-3.1-8B (71.8 vs. 68.2), while having negligible effect on LLaMA-3.3-70B (72.1 vs. 72.1). This suggests that audio information provides useful signal for smaller models but that the larger model can partially recover prosodic context from linguistic patterns.

## 11.2 The Impact of Past VADContext

Another interesting question here is whether LLMs provided with the VAD scores for utterances in conversation history will improve their performance. Here the VAD scores for previous utterances are the outputs predicted by models themselves rather than the ground truth VAD values.

## 11.2.1 GPTModels with Prompting

Table 10 reports VAD evaluation performance for GPT models when past VAD scores are provided in the context window (12 and 3 utterances respectively). Adding past VAD context yields modest improvements for GPT-5-mini on Valence (CCC of 0.663 to 0.689 with window =12) but has minimal or negative effects on Arousal and Dominance. The window size makes little difference overall.

## 11.2.2 LoRA Fine-tuned LLaMAModels

Table 11 reports the effect of past VAD context conditioning on LoRA fine-tuned LLaMA models. Unlike the GPT results, providing past VAD context generally degrades performance for fine-tuned models. For LLaMA-3.3-70B, including estimated past VAD with a 12-utterance window reduces Valence CCC from 0.7822 to 0.5368.

Importantly, this degradation does not imply that past VAD information is inherently uninformative. An oracle experiment in which ground-truth VAD

Table 5: Key Bidirectional Confusion Rates (%)

| Model            |   Happy↔Excited - Hap→Exc |   Happy↔Excited - Exc→Hap |   Angry↔Frustrated - Ang→Fru |   Angry↔Frustrated - Fru→Ang |   Sad ↔ Frustrated - Sad→Fru |   Sad ↔ Frustrated - Fru→Sad |
|------------------|---------------------------|---------------------------|------------------------------|------------------------------|------------------------------|------------------------------|
| GPT-4o-mini ZS   |                       7.6 |                      29.8 |                         75.3 |                          3.1 |                         22.0 |                          3.4 |
| GPT-4o-mini FS   |                      12.5 |                      22.7 |                         65.9 |                          6.3 |                         15.1 |                          6.0 |
| GPT-5-mini ZS    |                      30.6 |                      18.4 |                         60.0 |                          6.3 |                         18.8 |                          4.5 |
| GPT-5-mini FS    |                      29.2 |                      22.1 |                         46.5 |                         12.1 |                         11.0 |                          8.7 |
| LLaMA-2-7B ZS    |                       1.1 |                      81.5 |                         10.2 |                          3.3 |                          2.5 |                         10.4 |
| LLaMA-2-7B FS    |                       5.1 |                      86.7 |                         18.4 |                          5.1 |                          6.5 |                          5.7 |
| LLaMA-3.1-8B ZS  |                       1.4 |                      67.2 |                          9.4 |                          1.0 |                          1.8 |                         12.6 |
| LLaMA-3.1-8B FS  |                       4.9 |                      52.8 |                         22.4 |                          5.2 |                          6.1 |                          6.8 |
| LLaMA-3.3-70B ZS |                      34.2 |                      17.8 |                         16.7 |                         17.6 |                          4.2 |                         36.5 |
| LLaMA-3.3-70B FS |                      18.7 |                      17.0 |                         56.8 |                          5.8 |                         15.6 |                          5.5 |
| FT LLaMA-2-7B    |                      21.5 |                      17.7 |                         27.6 |                         12.1 |                         13.1 |                          1.8 |
| FT LLaMA-3.1-8B  |                      11.8 |                      20.7 |                         37.1 |                         10.0 |                          9.4 |                          3.9 |
| FT LLaMA-3.3-70B |                      34.0 |                      10.7 |                         30.0 |                         14.7 |                         12.2 |                          2.1 |

ZS: zero-shot; FS: few-shot; FT: fine-tuned.

Impact of Past VAD Context on CCC — GPT Models

Figure 2: The Impact of Past VAD on GPT Models in Emotion Dimensional Evaluation

<!-- image -->

Table 6: Reliability Measurements of IEMOCAP

|                         |   Reliability Measurements - Krippendorff's alpha |   Reliability Measurements - Fleiss' Kappa |
|-------------------------|---------------------------------------------------|--------------------------------------------|
| Discrete Emotion Labels |                                             0.279 |                                      0.273 |
| Valence Score           |                                             0.680 |                                      0.316 |
| Arousal Score           |                                             0.304 |                                      0.085 |
| Dominance Score         |                                             0.271 |                                      0.014 |

scores from prior utterances are provided as context yields substantially higher performance than experiments without past VAD scores, demonstrating that temporal VAD context carries meaningful signal. The observed degradation in the estimatedVAD condition is therefore better attributed to error accumulation: when model-predicted VAD values from earlier utterances are fed back as context, any prediction errors propagate forward and corrupt the conditioning signal for subsequent utterances.

## 12 Conclusion

This thesis investigated the application of Large Language Models to two independent tasks in multimodal dialogue: discrete emotion recognition (ER) and dimensional emotion evaluation along the VAD continuum. Both tasks were applied to IEMOCAP using a shared input construction strategy, which combines conversation history, target utterance, and textual audio feature descriptions following the SpeechCueLLM approach.

Our results yield four principal findings. First, LoRA fine-tuning dramatically outperforms prompt engineering for both tasks. Fine-tuned LLaMA models achieve weighted F1 scores of Impact of Past VAD Context on CCC — LoRA Fine-tuned LLaMA Models

Table 7: The Impact of Audio Description on Discrete ER Performance of LLaMA Models(Weighted F1 score)

|                               |   LLaMA-2-7B |   LLaMA-3.1-8B |   LLaMA-3.3-70B |
|-------------------------------|--------------|----------------|-----------------|
| LoRA                          |       73.196 |         71.818 |          72.122 |
| LoRAwithout audio description |       69.672 |          68.23 |          72.108 |

Figure 3: The Impact of Past VAD on LoRA Fine-tuned LLaMA Models in Emotion Dimensional Evaluation

<!-- image -->

71.8-73.2 for discrete ER, compared to 54.7-59.6 for the best GPT prompting conditions. For VAD evaluation, fine-tuned LLaMA-3.3-70B achieves a Valence CCC of 0.7822, establishing a new stateof-the-art on the IEMOCAP dataset and outperforming the best prompt-engineered GPT result by approximately 0.11. These gains indicate that domain adaptation through parameter-efficient finetuning is more impactful than general instructionfollowing capacity for specialized emotion tasks.

Second, audio feature descriptions contribute meaningfully to performance, especially for smaller models. In the task of discrete ERC, removing audio descriptions from LoRA fine-tuned models reduces weighted F1 by 3.5-3.6 for LLaMA-27B and LLaMA-3.1-8B, with negligible effect on LLaMA-3.3-70B. This suggests that larger models can partially recover prosodic context from linguistic patterns, but audio information remains a cost-effective signal for smaller architectures.

Third, performance asymmetry across VAD is explained by annotator agreement. The high CCC score on Valence along the much lower scores for Arousal and Dominance mirrors their interannotator agreement scores hierarchy, directly linking annotation noise to model performance ceilings.

Fourth, providing explicit past VAD values estimated by models as context helps promptengineered models marginally but degrades performance for LoRA fine-tuned models. This degradation is attributed to error accumulation instead of the incorporation of past VAD scores itself.

## 13 Limitation

Limitations of this work include the restriction to a single dataset (IEMOCAP), which lacks solid reliability due to its low inter-annotator agreement on the annotation of discrete emotion labels, Arousal, and Dominance. While IEMOCAP was the only available dataset satisfying all requirements after reviewing 19 candidates, the noisy data set a ceiling on the models' performance; future work should prioritize the development of additional multimodal dialogue datasets with continuous dimensional annotations. Moreover, rather than directly using a multimodal large model, we turned the raw audio recordings into textual audio feature descriptions and fed them into LLMs. Although features like volume, pitch, and speed are kept, some acoustic information is inevitably lost in this process. This might be another underlying reason for models gaining much better results in Valence than in Arousal and Dominance, for the latter two might be more acoustic information dependent.

In the future, we intend to use multimodal large models to directly process the raw audio recordings so that the acoustic information can be preserved more completely. Moreover, realizing the shortage of available data sources, we aim to establish more reliable multimodal dialogue emotion datasets. Furthermore, we hope to extend this study to text-tospeech generation with emotional control.

## Acknowledgments

We thank SAIL Lab at USC for giving us permission to IEMOCAP dataset.

## References

[CUEMPATHY: A Counseling Speech Dataset for Psychotherapy Research.](https://arxiv.org/html/2409.02466v1)

Junyi Ao, Rui Wang, Long Zhou, Chengyi Wang, Shuo Ren, Yu Wu, Shujie Liu, Tom Ko, Qing Li, Yu Zhang, Zhihua Wei, Yao Qian, Jinyu Li, and Furu Wei. 2022. SpeechT5: Unified-Modal Encoder-Decoder Pre-Training for Spoken Language Processing. arXiv preprint. ArXiv:2110.07205 [eess].

- Bagus Tris Atmaja and Masato Akagi. 2021. Twostage dimensional emotion recognition by fusing predictions of acoustic and text networks using SVM. Speech Communication, 126:9-21. ArXiv:2210.14495 [cs].

Messaoudi Awatef, Boughrara Hayet, and Lachiri Zied. 2025. Multimodal emotion recognition: integrating speech and text for improved valence, arousal, and dominance prediction. Annals of Telecommunications, 80(5):401-415.

Alexei Baevski, Henry Zhou, Abdelrahman Mohamed, and Michael Auli. 2020. wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations. arXiv preprint. ArXiv:2006.11477 [cs].

AmirAli Bagher Zadeh, Paul Pu Liang, Soujanya Poria, Erik Cambria, and Louis-Philippe Morency. 2018. Multimodal Language Analysis in the Wild: CMUMOSEI Dataset and Interpretable Dynamic Fusion Graph. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 2236-2246, Melbourne, Australia. Association for Computational Linguistics.

- Carlos Busso, Murtaza Bulut, Chi-Chun Lee, Abe Kazemzadeh, Emily Mower, Samuel Kim, Jeannette N. Chang, Sungbok Lee, and Shrikanth S. Narayanan. 2008. IEMOCAP: interactive emotional dyadic motion capture database. Language Resources and Evaluation, 42(4):335-359.
- Carlos Busso, Srinivas Parthasarathy, Alec Burmania, Mohammed AbdelWahab, Najmeh Sadoughi, and Emily Mower Provost. 2017. MSP-IMPROV: An Acted Corpus of Dyadic Interactions to Study Emotion Perception. IEEE Transactions on Affective Computing, 8(1):67-80.
- Houwei Cao, David G. Cooper, Michael K. Keutmann, Ruben C. Gur, Ani Nenkova, and Ragini Verma. 2014. CREMA-D: Crowd-Sourced Emotional Multimodal Actors Dataset. IEEE Transactions on Affective Computing, 5(4):377-390.
- Sheng-Yeh Chen, Chao-Chun Hsu, Chuan-Chun Kuo, Ting-Hao, Huang, and Lun-Wei Ku. 2018. EmotionLines: An Emotion Corpus of Multi-Party Conversations. arXiv preprint. ArXiv:1802.08379 [cs].
- Dorottya Demszky, Dana Movshovitz-Attias, Jeongwoo Ko, Alan Cowen, Gaurav Nemade, and Sujith Ravi. 2020. GoEmotions: A Dataset of Fine-Grained Emotions. arXiv preprint. ArXiv:2005.00547 [cs].
- Benjamin Elizalde, Soham Deshmukh, Mahmoud Al Ismail, and Huaming Wang. 2022. CLAP: Learning Audio Concepts From Natural Language Supervision. arXiv preprint. ArXiv:2206.04769 [cs].

Mauajama Firdaus, Hardik Chauhan, Asif Ekbal, and Pushpak Bhattacharyya. 2020. MEISD: A Multimodal Multi-Label Emotion, Intensity and Sentiment Dialogue Dataset for Emotion Recognition and Sentiment Analysis in Conversations. In Proceedings of the 28th International Conference on Computational Linguistics, pages 4441-4453, Barcelona, Spain (Online). International Committee on Computational Linguistics.

- Deepanway Ghosal, Navonil Majumder, Soujanya Poria, Niyati Chhaya, and Alexander Gelbukh. 2019. DialogueGCN: A Graph Convolutional Neural Network for Emotion Recognition in Conversation. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 154-164, Hong Kong, China. Association for Computational Linguistics.
- Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. 2021. LoRA: Low-Rank Adaptation of Large Language Models. arXiv preprint. ArXiv:2106.09685 [cs].

Alex-R˘azvan Ispas, Théo Deschamps-Berger, and Laurence Devillers. 2023. A Multi-Task, MultiModal Approach for Predicting Categorical and Dimensional Emotions. In International Cconference on Multimodal Interaction, pages 311-317. ArXiv:2401.00536 [cs].

- Dimitrios Kollias and Stefanos Zafeiriou. 2019. AffWild2: Extending the Aff-Wild Database for Affect Recognition. arXiv preprint. ArXiv:1811.07770 [cs].
- Alkis Koudounas, Moreno La Quatra, and Elena Baralis. 2025. DeepDialogue: A Multi-Turn EmotionallyRich Spoken Dialogue Dataset. arXiv preprint. ArXiv:2505.19978 [cs].

Shanglin Lei, Guanting Dong, Xiaoping Wang, Keheng Wang, Runqi Qiao, and Sirui Wang. 2023. InstructERC: Reforming Emotion Recognition in Conversation with Multi-task Retrieval-Augmented Large Language Models.

Yanran Li, Hui Su, Xiaoyu Shen, Wenjie Li, Ziqiang Cao, and Shuzi Niu. 2017. DailyDialog: A Manually Labelled Multi-turn Dialogue Dataset. arXiv preprint. ArXiv:1710.03957 [cs].

- Navonil Majumder, Soujanya Poria, Devamanyu Hazarika, Rada Mihalcea, Alexander Gelbukh, and Erik Cambria. 2019. DialogueRNN: An Attentive RNN for Emotion Detection in Conversations. arXiv preprint. ArXiv:1811.00405 [cs].

Awatef Messaoudi, Hayet Boughrara, and Zied Lachiri. 2024. Speech Emotion Recognition In Continuous Space Using IEMOCAP Database. In 2024 IEEE 12th International Symposium on Signal, Image, Video and Communications (ISIVC), pages 1-6.

Tu Anh Nguyen, Wei-Ning Hsu, Antony D'Avirro, Bowen Shi, Itai Gat, Maryam Fazel-Zarani, Tal Remez, Jade Copet, Gabriel Synnaeve, Michael Hassid, Felix Kreuk, Yossi Adi, and Emmanuel Dupoux. 2023. EXPRESSO: A Benchmark and Analysis of Discrete Expressive Speech Resynthesis. arXiv preprint. ArXiv:2308.05725 [cs].

Soujanya Poria, Erik Cambria, Devamanyu Hazarika, Navonil Majumder, Amir Zadeh, and Louis-Philippe Morency. 2017. Context-Dependent Sentiment Analysis in User-Generated Videos. In Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 873-883, Vancouver, Canada. Association for Computational Linguistics.

Soujanya Poria, Devamanyu Hazarika, Navonil Majumder, Gautam Naik, Erik Cambria, and Rada Mihalcea. 2019. MELD: A Multimodal Multi-Party Dataset for Emotion Recognition in Conversations. arXiv preprint. ArXiv:1810.02508 [cs].

Hannah Rashkin, Eric Michael Smith, Margaret Li, and Y.-Lan Boureau. 2019. Towards Empathetic Opendomain Conversation Models: a New Benchmark and Dataset. arXiv preprint. ArXiv:1811.00207 [cs].

James A Russell and Albert Mehrabian. 1977. Evidence for a three-factor theory of emotions. Journal of Research in Personality, 11(3):273-294.

Vandana Singh and Swati Prasad. 2023. Speech Emotion Recognition using Fully Convolutional Network and Augmented RAVDESS Dataset. In 2023 International Conference on Advanced Computing Technologies and Applications (ICACTA), pages 1-7.

Sundararajan Srinivasan, Zhaocheng Huang, and Katrin Kirchhoff. 2022. Representation learning through cross-modal conditional teacher-student training for speech emotion recognition. arXiv preprint. ArXiv:2112.00158 [eess].

Haoqin Sun, Xuechen Wang, Jinghua Zhao, Shiwan Zhao, Jiaming Zhou, Hui Wang, Jiabei He, Aobo Kong, Xi Yang, Yequan Wang, Yonghua Lin, and Yong Qin. 2025. EmotionTalk: An Interactive Chinese Multimodal Emotion Dataset With Rich Annotations. arXiv preprint. ArXiv:2505.23018 [cs].

George Trigeorgis, Fabien Ringeval, Raymond Brueckner, Erik Marchi, Mihalis A. Nicolaou, Björn Schuller, and Stefanos Zafeiriou. 2016. Adieu features? End-to-end speech emotion recognition using a deep convolutional recurrent network. In 2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 5200-5204.

Kaisiyuan Wang, Qianyi Wu, Linsen Song, Zhuoqian Yang, Wayne Wu, Chen Qian, Ran He, Yu Qiao, and Chen Change Loy. 2020. MEAD: A Large-Scale Audio-Visual Dataset for Emotional Talking-Face Generation. In Computer Vision - ECCV 2020: 16th European Conference, Glasgow, UK, August 23-28, 2020, Proceedings, Part XXI, pages 700-717, Berlin, Heidelberg. Springer-Verlag.

ChengYan Wu, Yiqiang Cai, Yang Liu, Pengxu Zhu, Yun Xue, Ziwei Gong, Julia Hirschberg, and Bolei Ma. 2025a. Multimodal Emotion Recognition in Conversations: A Survey of Methods, Trends, Challenges and Prospects. In Findings of the Association for Computational Linguistics: EMNLP 2025, pages 6257-6274, Suzhou, China. Association for Computational Linguistics.

Zichen Wu, Hsiu-Yuan Huang, and Yunfang Wu. 2025b. Beyond Spurious Signals: Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing. In Findings of the Association for Computational Linguistics: EMNLP 2025, pages 3805-3825, Suzhou, China. Association for Computational Linguistics.

Han Zhang, Zixiang Meng, Meng Luo, Hong Han, Lizi Liao, Erik Cambria, and Hao Fei. 2025. Towards Multimodal Empathetic Response Generation: A Rich Text-Speech-Vision Avatar-based Benchmark. arXiv preprint. ArXiv:2502.04976 [cs].

Kun Zhou, Berrak Sisman, Rui Liu, and Haizhou Li. 2022. Emotional Voice Conversion: Theory, Databases and ESD. arXiv preprint. ArXiv:2105.14762 [cs].

## A Methodology Pipeline Algorithm, Details, and Examples

Figure 4 gives an example of how the proposed pipeline will work with emotion data, and the Algorithm 1 includes more details of the pipeline. Furthermore, Fig 5 visualizes the entire process of converting audio information from IEMOCAP dataset to textual audio feature description.

## B Multimodal Emotion Dataset

Current multimodal emotion datasets vary significantly in their modality coverage, text types and annotation content for intensity-focused research.

## B.1 Dataset Coverage byModality

Text-only datasets like GoEmotions (58k Reddit comments, 28 emotions) and DailyDialog (13k dialogues) provide broad emotional coverage but lack multimodal context. Pure audio-visual datasets such as MEAD (40 hours) and RAVDESS (7,462

```
Input: Target utterance ut, audio recording at, conversation history H = {(si, ui)}t-1 i=t-W Output: Emotion label ˆ y ∈ E or VAD scores (ˆ v, ˆa, ˆ d) ∈ [1, 5]3 // Step 1: Audio Feature Extraction for each feature f ∈ {volume, pitch, speaking rate} do µf , σf ← EXTRACTSTATS(at, f); ℓf ← QUANTIZE(µf , {q0.25, q0.50, q0.75}); ℓσf ← QUANTIZE(σf , {q0.25, q0.50, q0.75}); end daudio ← TOTEXT({ℓf , ℓσf }f ) ; // e.g., "moderate volume with high variation" // Step 2: Prompt Construction chistory ← FORMAT(H) ; // prefix each turn with speaker ID p ← ASSEMBLEPROMPT(chistory, ut, daudio, τ) ; // τ: task-specific template // Step 3: Independent Task Inference if task = DISCRETEER then ˆ y ←LLMER(p), ˆ y ∈ E = {happy, sad, neutral, angry, excited, frustrated}; else(ˆ v, ˆa, ˆ d) ←LLMVAD(p), ˆ v, ˆa, ˆ d ∈ {1, 2, 3, 4, 5}; end // Step 4: (LoRA only) Model is separately fine-tuned per task if mode = LORA then LLMER ← LORAFINETUNE(LLMbase, DER, r=16, α=16); LLMVAD ← LORAFINETUNE(LLMbase, DVAD, r=16, α=16); end
```

Algorithm 1: Multimodal LLM-based Emotion Evaluation

Figure 4: Example of The Proposed Pipeline

<!-- image -->

clips) include emotion intensity levels but consist primarily of acted performances. Comprehensive multimodal datasets like IEMOCAP (12 hours audiovisual data) and CMU-MOSEI (23.5k utterances) combine text, audio, and visual modalities with both categorical and dimensional annotations.

## B.2 Emotion Continuous Dimensional Annotations

Few datasets explicitly model emotion on continuous dimensions, which is crucial for quantitative evaluation. IEMOCAP provides VAD system ratings (valence, arousal, dominance), while MEAD categorizes intensity as neutral, weak, medium, and strong. MEISD offers explicit intensity levels (1-3) across eight emotion categories. However, most datasets including MELD, EmotionLines, and GoEmotions provide only categorical emotion labels without dimensional emotion measures.

## B.3 Conversational Versus Non-Conversational Context

Datasets vary in their contextual structure. Conversational datasets like MELD, IEMOCAP, and T: Text, A: Audio, V: Vision; VAD: Valence-Arousal-Dominance MEISD preserve turn-taking dynamics and contextual emotion flow. Non-conversational datasets such as CMU-MOSEI (YouTube monologues) and actor-based datasets (MEAD, RAVDESS, CREMA-D) focus on isolated emotional expressions without interactive context.

Figure 5: Example of the Audio Feature Description Generation

<!-- image -->

Table 8: Existing Emotion Datasets

| Dataset                                     | Modalities   |   # Emotions | Continuous Measurements   | Dimensional Metric   | Dialogue   |
|---------------------------------------------|--------------|--------------|---------------------------|----------------------|------------|
| IEMOCAP                                     | T, A, V      |            9 | ✓                         | VAD                  | ✓          |
| MELD (Poria et al., 2019)                   | T, A, V      |            7 | ×                         | -                    | ✓          |
| EmotionLines (Chen et al., 2018)            | T            |            6 | ×                         | -                    | ✓          |
| DailyDialog (Li et al., 2017)               | T            |            7 | ×                         | -                    | ✓          |
| CMU-MOSEI (Bagher Zadeh et al., 2018)       | T, A, V      |            6 | ✓                         | 0-3 Likert scale     | ×          |
| MEISD (Firdaus et al., 2020)                | T, A, V      |            8 | ✓                         | 1-3 Likert scale     | ✓          |
| MSP-IMPROV (Busso et al., 2017)             | T, A, V      |            4 | ×                         | -                    | ✓          |
| RAVDESS (Singh and Prasad, 2023)            | T, A, V      |            6 | ✓                         | 2 levels             | ×          |
| CREMA-D (Cao et al., 2014)                  | T, A, V      |            6 | ✓                         | 3 levels             | ×          |
| MEAD (Wang et al., 2020)                    | A, V         |            7 | ✓                         | 3 levels             | ✓          |
| Aff-Wild2 (Kollias and Zafeiriou, 2019)     | A, V         |            7 | ✓                         | VAD                  | ×          |
| GoEmotions (Demszky et al., 2020)           | T            |           28 | ×                         | -                    | ×          |
| Empathetic Dialogues (Rashkin et al., 2019) | T            |           32 | ×                         | -                    | ✓          |
| DeepDialogue (Koudounas et al., 2025)       | T            |           20 | ×                         | -                    | ✓          |
| EmotionTalk (Sun et al., 2025)              | T, A, V      |            7 | ×                         | -                    | ✓          |
| ESD (Zhou et al., 2022)                     | T, A         |            5 | ×                         | -                    | ×          |
| Expresso (Nguyen et al., 2023)              | T, A         |           19 | ×                         | -                    | ✓          |
| AvaMERG (Zhang et al., 2025)                | T, A, V      |            7 | ×                         | -                    | ×          |
| Counselling Transcripts (noa)               | T            |           11 | ×                         | -                    | ✓          |

Figure 6: Example of IEMOCAP Dataset

<!-- image -->

The predominance of categorical over continuous dimensional annotations limits research in emotion quantitative evaluation. For multimodal emotion dimensional evaluation research, IEMOCAP and MEISD represent the most suitable resources. However, due to the unavailability of MEISD dataset, our final and only available choice is IEMOCAP dataset.

## C Prompt Templates

Reasoning was required for prompts for both tasks to boost the performance.

## C.1 Discrete ER Prompt

The zero-shot prompt for discrete ER follows this structure:

[System] You are an expert in emotional analysis for dialogues. Select one emotion label from {happy, sad, neutral, angry, excited, frustrated} and respond in strict JSON format.

```
[User] Conversation history: {{conversation_history}} Target utterance: {{target_utterance}} Audio features: {{audio_features}} Select the single emotion that
```

```
best represents the dominant emotion of the target utterance. Respond in JSON: {"emotion_label": "...", "reasoning": "..."}
```

Few-shot prompts prepend a fixed set of annotated examples (with input-output pairs) before the target utterance. The examples are selected to cover all six emotion categories and to represent cases where audio features are diagnostic.

## C.2 VAD Evaluation Prompt

The zero-shot prompt for VAD evaluation follows the same structure, with the output format modified to return three integer scores:

[System] You are an expert in dimensional emotion analysis. Rate the target utterance on Valence (V), Arousal (A), and Dominance (D), each on a scale of 1 to 5, where higher values indicate more positive, more activated, and more dominant respectively. Respond in strict JSON format.

```
[User] Conversation history: {{conversation_history}} Target utterance: {{target_utterance}} Audio features: {{audio_features}} Respond in JSON: {"valence": <1-5>, "arousal": <1-5>, "dominance": <1-5>, "reasoning": "..."}
```

## C.3 Detailed Results for the Impact of Past VAD Values on VAD Evaluation Performance

Table 10 and Table 11 provide detailed results of the ablation study for the impact of past VAD values on VAD evaluation performance.

Table 9: Summary Statistics of the IEMOCAP Dataset

| Property                         | Value                                               |
|----------------------------------|-----------------------------------------------------|
| Number of sessions               | 5 dyadic sessions                                   |
| Total dialogues                  | 151                                                 |
| Total utterances                 | 10,086                                              |
| Avg. utterances per dialogue     | ≈ 66                                                |
| Total audio duration             | ≈ 12 hours                                          |
| Available modalities             | Audio, Video, Text, Motion Capture                  |
| Discrete emotion categories used | 6 (happy, sad, neutral, angry, excited, frustrated) |
| Utterances after filtering       | 7,433                                               |

Table 10: VAD Evaluation Performance Comparison Across OpenAI Models and Prompting Strategies with Past VAD Values

| Dimension   |   Context Window = 12 - GPT-4o mini - Zero-shot |   Context Window = 12 - GPT-4o mini - Few-shot |   Context Window = 12 - GPT-5 mini - Zero-shot |   Context Window = 12 - GPT-5 mini - Few-shot |   Context Window = 3 - GPT-4o mini - Zero-shot |   Context Window = 3 - GPT-4o mini - Few-shot |   Context Window = 3 - GPT-5 mini - Zero-shot |   Context Window = 3 - GPT-5 mini - Few-shot |
|-------------|-------------------------------------------------|------------------------------------------------|------------------------------------------------|-----------------------------------------------|------------------------------------------------|-----------------------------------------------|-----------------------------------------------|----------------------------------------------|
| Valence     |                                          0.5795 |                                         0.6193 |                                         0.6892 |                                        0.6861 |                                         0.6132 |                                        0.6329 |                                        0.6806 |                                       0.6857 |
| Arousal     |                                          0.3787 |                                         0.3720 |                                         0.3959 |                                        0.3460 |                                         0.3481 |                                        0.3462 |                                        0.3710 |                                       0.3415 |
| Dominance   |                                          0.1487 |                                         0.1504 |                                         0.3396 |                                        0.3424 |                                         0.1555 |                                        0.1340 |                                        0.3343 |                                       0.3333 |
| Overall     |                                          0.3690 |                                         0.3806 |                                         0.4749 |                                        0.4582 |                                         0.3723 |                                        0.3710 |                                        0.4620 |                                       0.4535 |

Table 11: VAD Evaluation Performance Comparison Across LLaMA Models with LoRA Finetuning With Past VAD

| Dimension   |   Context Window = 12 - 2-7B |   Context Window = 12 - 3.1-8B |   Context Window = 12 - 3.3-70B |   Context Window = 3 - 2-7B |   Context Window = 3 - 3.1-8B |   Context Window = 3 - 3.3-70B |
|-------------|------------------------------|--------------------------------|---------------------------------|-----------------------------|-------------------------------|--------------------------------|
| Valence     |                       0.6647 |                         0.7677 |                          0.5368 |                      0.6291 |                        0.7160 |                         0.4626 |
| Arousal     |                       0.3033 |                         0.4411 |                          0.3046 |                      0.3412 |                        0.3968 |                         0.2034 |
| Dominance   |                       0.2662 |                         0.4252 |                          0.3585 |                      0.3166 |                        0.3719 |                         0.2412 |
| Overall     |                       0.4114 |                         0.5447 |                          0.4000 |                      0.5489 |                        0.4949 |                         0.3024 |