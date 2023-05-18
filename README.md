# awesome-remote-image-captioning
The project is currently under construction

### Templates
```markdown
Papers
| `标签` | [论文名称](论文地址) <br/>一句话概括<br/>所有作者<br/>单位<br/>所属期刊缩写 年份 | 引用数 | [[Code]](仓库地址)<br/>[[Page]](主页地址)<br/>[[Demo]](Demo地址) |

Datasets
| [数据集名称](论文地址) <br/>一句话概括<br/>单位<br/>年份 | 语言 | 图像类别数 | 图像总个数 | 最低图像分辨率 - <br/>最高图像分辨率 |

Popular Implementations
| [仓库名称](仓库地址) | 框架 |

Blogs
| [Blog标题](Blog地址) | 作者 | 一句话概括 |
```

### Papers
| Tag | Paper info | Citations | Useful links |
|---|---|---|---|
| `Contextual attention, NWPU-Captions` | [NWPU-Captions Dataset and MLCA-Net for Remote Sensing Image Captioning](https://ieeexplore.ieee.org/document/9866055/keywords)<br/>The paper propose a novel encoder–decoder architecture — multilevel and contextual attention network (MLCA-Net), which improves the flexibility and diversity of the generated captions while keeping their accuracy and conciseness.<br/>Qimin Cheng; Haiyan Huang; Yuan Xu; Yuzhuo Zhou; Huanying Li; Zhongyuan Wang<br/>School of Electronic Information and Communications, Huazhong University of Science and Technology, Wuhan, China<br/>TGRS 2022 | 4 | None |
|`Change captioning (CC), change detection (CD), Transformer`| [Remote Sensing Image Change Captioning With Dual-Branch Transformers: A New Method and a Large Scale Dataset](https://ieeexplore.ieee.org/document/9934924/keywords#full-text-header)<br/>The paper proposes a novel Transformer-based RSICC (RSICCformer) model, which consists of a CNN-based feature extractor, a dual-branch Transformer encoder (DTE) and a caption decoder.<br/>Chenyang Liu; Rui Zhao; Hao Chen; Zhengxia Zou; Zhenwei Shi<br/>Beijing Key Laboratory of Digital Media, Beihang University, Beijing, China<br/>TGRS 2022 | 3 | None |
| `joint training, multilabel attributes` | [A Joint-Training Two-Stage Method For Remote Sensing Image Captioning](https://ieeexplore.ieee.org/document/9961235/keywords#full-text-header) <br/>A novel joint-training two-stage (JTTS) method improves remote sensing image captioning by integrating multilabel classification for prior information, utilizing differentiable sampling, and employing an attribute-guided decoder.<br/>Xiutiao Ye; Shuang Wang; Yu Gu; Jihui Wang; Ruixuan Wang; Biao Hou; Fausto Giunchiglia; Licheng Jiao<br/>Key Laboratory of Intelligent Perception and Image Understanding of Ministry of Education of China, Xidian University, Xi’an, China<br/>TGRS 2022 | 2 | None |
| `Attention mechanism` | [Global Visual Feature and Linguistic State Guided Attention for Remote Sensing Image Captioning](https://ieeexplore.ieee.org/document/9632558/) <br/>This article proposes a global visual feature-guided attention mechanism for remote-sensing image captioning, which introduces global visual features, filters out redundant components.<br/>Zhengyuan Zhang;Wenkai Zhang;Menglong Yan;Xin Gao;Kun Fu;Xian Sun<br/>Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing, China<br/>TGRS 2022 | 9 | None |
| `change detection (CD), support vector machines (SVMs)` | [Change Captioning: A New Paradigm for Multitemporal Remote Sensing Image Analysis](https://ieeexplore.ieee.org/document/9847254) <br/>This article proposes change captioning systems that generate coherent sentence descriptions of occurred changes in remote sensing, which utilize convolutional neural networks to extract features and recurrent neural networks or support vector machines to generate change descriptions.<br/>Genc Hoxha;Seloua Chouaf;Farid Melgani;Youcef Smara<br/>Department of Information Engineering and Computer Science, University of Trento, Trento, Italy<br/>TGRS 2022 | 3 | None |
| `Attention mechanism, encoder-decoder` | [Recurrent Attention and Semantic Gate for Remote Sensing Image Captioning](https://ieeexplore.ieee.org/document/9515452) <br/>This article introduces a novel RASG framework for remote sensing image captioning, and it utilizes competitive visual features and a recurrent attention mechanism to generate improved context vectors and enhance word representations.<br/>Yunpeng Li;Xiangrong Zhang;Jing Gu;Chen Li;Xin Wang;Xu Tang;Licheng Jiao<br/>School of Artificial Intelligence, Xidian University, Xi’an, China<br/>TGRS 2022 | 14 | None |
| `structured attention` | [High-Resolution Remote Sensing Image Captioning Based on Structured Attention](https://ieeexplore.ieee.org/document/9400386/keywords#keywords) <br/>A fine-grained, structured attention-based method is proposed for generating language descriptions of high-resolution remote sensing images, utilizes the structural characteristics of semantic contents and can generate pixelwise segmentation masks without requiring pixelwise annotations.<br/>Rui Zhao;Zhenwei Shi;Zhengxia Zou<br/>Image Processing Center, School of Astronautics, Beihang University, Beijing, China<br/>TGRS 2022 | 35 | None |
| `support vector machines (SVMs)` | [A Novel SVM-Based Decoder for Remote Sensing Image Captioning](https://ieeexplore.ieee.org/document/9521989/) <br/>This article introduces a novel remote sensing image captioning system by using a network of support vector machines (SVMs) instead of recurrent neural networks (RNNs).<br/>Genc Hoxha;Farid Melgani<br/>Department of Information Engineering and Computer Science, University of Trento, Trento, Italy<br/>TGRS 2022 | 20 | None |
| `overfitting, truncation cross entropy (TCE) loss` | [Truncation Cross Entropy Loss for Remote Sensing Image Captioning](https://ieeexplore.ieee.org/document/9153154/keywords#keywords) <br/>This article introduces a new approach called truncation cross entropy (TCE) loss to address the overfitting problem in remote sensing image captioning (RSIC), which explores the limitations of cross entropy (CE) loss and proposes TCE loss to alleviate overfitting.<br/>Xuelong Li;Xueting Zhang;Wei Huang;Qi Wang<br/>School of Computer Science and with the Center for OPTical IMagery Analysis and Learning (OPTIMAL), Northwestern Polytechnical University, Xi’an, China<br/>TGRS 2021 | 38 | None |
| `Caption summarization` | [SD-RSIC: Summarization-Driven Deep Remote Sensing Image Captioning](https://ieeexplore.ieee.org/document/9239371) <br/>The novel SD-RSIC approach addresses the issue of redundant information in remote sensing image captioning, which utilizes summarization techniques, adaptive weighting, and a combination of CNNs and LSTM networks to improve the mapping from the image domain to the language domain.<br/>Faculty of Electrical Engineering and Computer Science, Technische Universität Berlin, Berlin, Germany<br/>TGRS 2021 | 35 | [[Code]](https://gitlab.tubit.tu-berlin.de/rsim/SD-RSIC) |
| `word–sentence framework` | [Word–Sentence Framework for Remote Sensing Image Captioning](https://ieeexplore.ieee.org/document/9308980/keywords#keywords) <br/>This article introduces a new explainable word-sentence framework for remote sensing image captioning (RSIC), consisting of a word extractor and a sentence generator.<br/>Qi Wang;Wei Huang;Xueting Zhang;Xuelong Li<br/>School of Computer Science, Northwestern Polytechnical University, Xi’an, China<br/>IRGS 2021 | 42 | None |
### Datasets
| Dataset info | Language | Categories | Total | Resolution |
|---|---|---|---|---|
| [NWPU-Captions](https://ieeexplore.ieee.org/document/9866055/keywords)<br/>The NWPU-Captions dataset is a larger and more challenging benchmark dataset for remote sensing image captioning, containing 157,500 manually annotated sentences and 31,500 images, offering a greater data volume, category variety, description richness, and wider coverage of complex scenes and vocabulary.<br/>School of Electronic Information and Communications, Huazhong University of Science and Technology, Wuhan, China<br/>2022 | English | 45 | 31500 | 30 m - <br/>0.2 m|
| [LEVIR-CC](https://ieeexplore.ieee.org/document/9934924/keywords#full-text-header)<br/>The LEVIR-CC dataset is a large-scale dataset designed for the RSICC task, consisting of 10077 pairs of RS images and 50385 corresponding sentences describing image differences.<br/>Beijing Key Laboratory of Digital Media, Beihang University, Beijing, China<br/>2022 | English | 10 | 10077 | 0.5 m - <br/>0.5 m |
### Popular Implementations
| Code | Framework |
|---|---|

### Blogs
| Title | Author | Overview |
|---|---|---|
