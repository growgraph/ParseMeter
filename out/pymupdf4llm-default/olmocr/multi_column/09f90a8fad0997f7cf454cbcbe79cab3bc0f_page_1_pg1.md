Exp eriments with Op en-Domain Textual Question Answering


Sanda M. Harabagiu and Marius A. Pa�sca and Steven J. Maiorano

Department of Computer Science and Engineering

Southern Metho dist University

Dallas, TX 75275-0122

fsanda,marius,steveg@renoir. seas .sm u.ed u



Abstract


This pap er describ es the integration of several

knowledge-based natural language pro cessing tech
niques into a Question Answering system, capable

of mining textual answers from large collections of

texts. Surprizing quality is achieved when several

lightweight knowledge-based NLP techniques com
plement mostly shallow, surface-based approaches.


1 Background


The last decade has witnessed great advances and

interest in the area of Information Extraction (IE)

from real-world texts. Systems that participated in

the TIPSTER MUC comp etitions have b een quite suc
cessful at extracting information from newswire mes
sages and �lling templates with information p ertain
ing to events or situations of interest. Typically, the

templates mo del queries regarding who did what to

whom, when and where, and eventually why.

Recently, a new trend in information pro cessing

from texts has emerged. Textual Question Answer
ing (Q/A) aims at identifying the answer of a ques
tion in large collections of on-line do cuments. In
stead of extracting all events of interest and their re
lated entities, a Q/A system highlights only a short

piece of text, accounting for the answer. Moreover,

questions are expressed in natural language, are not

constrained to a sp eci�c domain and are not limited

to the six question typ es sought by IE systems (i.e.



w ho1



did w hat2



, w hen



The idea of building op en-domain Q/A systems

that p erform on real-world do cument collections was

initiated by the eighth Text REtrieval Conference

(TREC-8), by organizing the �rst comp etition of an
swering fact-based questions such as \Who came up

with the name, El Nino?". Resisting the tempta
tion of merely p orting and integrating existing IE

and IR technologies into Q/A systems, the develop
ers of the TREC Q/A systems have not only shap ed

new pro cessing metho ds, but also inspired new re
search in the challenging integration of surface-text
based metho ds with knowledge-based text inference.

In particular, two clear knowledge pro cessing needs

are presented: (1) capturing the semantics of op en
domain questions and (2) justifying the correctness

of answers.

In this pap er, we present our exp eriments with

integrating knowledge-based NLP with shallow pro
cessing techniques for these two asp ects of Q/A. Our

research was motivated by the need to enhance the

precision of an implemented Q/A system and by the

requirement to prepare it for scaling to more com
plex questions than those presented in the TREC

comp etition. In the remaining of the pap er, we de
scrib e a Q/A architecture that allows the integra
tion of knowledge-based NLP pro cessing with shal
low pro cessing and we detail their interactions. Sec
tion 2 presents the functionality of several knowledge

pro cessing mo dules and describ es the NLP tech
niques for question and answer pro cessing. Section

3 explains the semantic and logical interactions of

pro cessing questions and answers whereas Section

4 highlights the inference asp ects that implement

the justi�cation option of a Q/A system. Section

5 presents the results and the evaluations whereas

Section 6 concludes the pap er.


2 The NLP Techniques


Surprising quality for op en-domain textual Q/A can

b e achieved when several lightweight knowledge
based NLP techniques complement mostly shallow,

surface-based approaches. The pro cessing imp osed

by Q/A systems must b e distinguished, on the one

hand, from IR techniques, that lo cate sets of do c


4



and w her e



5



, and



eventually w hy



6



to w hom3

).



In op en-domain Q/A systems, the �nite-state

technology and domain knowledge that made IE sys
tems successful are replaced by a combination of (1)

knowledge-based question pro cessing, (2) new forms

of text indexing and (3) lightweight ab duction of

queries. More generally, these systems combine cre
atively comp onents of the NLP basic research in
frastructure develop ed in the 80s (e.g. the compu
tational theory of Q/A rep orted in (Lehnert 1978)

and the theory of ab ductive interpretation of texts

rep orted in (Hobbs et al.1993)) with other shallow

techniques that make p ossible the op en-domain pro
cessing on real-world texts.


