const d=require('docx'),fs=require('fs');
const {Document,Packer,Paragraph,TextRun,HeadingLevel,Table,TableRow,TableCell,WidthType,ShadingType,LevelFormat,AlignmentType,BorderStyle}=d;
const F='Calibri';
const p=(t,o={})=>new Paragraph({spacing:{after:80},...o,children:Array.isArray(t)?t:[new TextRun({text:t,font:F,size:22})]});
const b=(t)=>new TextRun({text:t,bold:true,font:F,size:22});
const r=(t)=>new TextRun({text:t,font:F,size:22});
const it=(t)=>new TextRun({text:t,italics:true,font:F,size:22,color:'555555'});
const h1=t=>new Paragraph({heading:HeadingLevel.HEADING_1,spacing:{before:260,after:100},children:[new TextRun({text:t,font:F,bold:true,size:30,color:'1F3A68'})]});
const h2=t=>new Paragraph({heading:HeadingLevel.HEADING_2,spacing:{before:160,after:60},children:[new TextRun({text:t,font:F,bold:true,size:24})]});
const bl=(t)=>new Paragraph({numbering:{reference:'bl',level:0},spacing:{after:50},children:Array.isArray(t)?t:[r(t)]});
const say=t=>new Paragraph({spacing:{after:80},indent:{left:300},border:{left:{style:BorderStyle.SINGLE,size:12,color:'1F3A68',space:8}},children:[it('Say: '),r(t)]});
const bd={style:BorderStyle.SINGLE,size:4,color:'BBBBBB'};const B={top:bd,bottom:bd,left:bd,right:bd};
const W=[1500,2900,4626];
const cell=(t,w,hd)=>new TableCell({width:{size:w,type:WidthType.DXA},borders:B,margins:{top:60,bottom:60,left:100,right:100},shading:hd?{type:ShadingType.CLEAR,fill:'1F3A68'}:undefined,children:[new Paragraph({children:[new TextRun({text:t,font:F,size:21,bold:hd,color:hd?'FFFFFF':'000000'})]})]});
const row=(a,hd)=>new TableRow({tableHeader:hd,children:a.map((t,i)=>cell(t,W[i],hd))});
const table=new Table({width:{size:9026,type:WidthType.DXA},columnWidths:W,rows:[
 row(['Time','Segment','Key message'],true),
 row(['0:00–1:00','Opening','Who I am and what I do: production GenAI and ML at Google scale']),
 row(['1:00–3:00','Expertise map','Four pillars: LLMs/RAG, embeddings & vector search, ML/NLP, deployment']),
 row(['3:00–7:00','Deep dive 1','BugSuggestion: embeddings + vector search for duplicate detection']),
 row(['7:00–10:00','Deep dive 2','AI in Dashboard: natural language to validated SQL']),
 row(['10:00–12:00','Deep dive 3','Hybrid retrieval: BM25 + dense (+18% Precision@10)']),
 row(['12:00–14:00','Lessons','What breaks in production and how I handle it']),
 row(['14:00–15:00','Close','Where I add value; questions'])]});
const kids=[
 new Paragraph({spacing:{after:40},children:[new TextRun({text:'Area of Expertise Discussion',font:F,bold:true,size:40,color:'1F3A68'})]}),
 p([it('Generative AI & Machine Learning  |  15-minute talk plan  |  Dintakurthi Achuth')]),
 h1('1. Plan at a glance'), table,
 p([r('')]),
 h1('2. Opening (1 min)'),
 say('I am a data scientist with 3+ years of experience, working at Google through Virtusa. My focus is turning LLMs, retrieval and ML models into features that real users rely on, not just demos.'),
 h1('3. Expertise map (2 min)'),
 bl([b('LLMs and RAG: '),r('prompting, retrieval, grounding answers in data, fine-tuning with LoRA/QLoRA, agents (LangChain, LangGraph).')]),
 bl([b('Embeddings and vector search: '),r('text-embedding-005, GCP Vector Search, FAISS, Pinecone, ChromaDB, KNN similarity.')]),
 bl([b('Classical ML and NLP: '),r('classification, clustering, transformers, CNNs, NER, text classification; PyTorch, TensorFlow, scikit-learn.')]),
 bl([b('Engineering and deployment: '),r('Python, SQL and Java; FastAPI, Docker, Kubernetes, CI/CD, GCP and AWS.')]),
 h1('4. Deep dive 1: BugSuggestion (4 min)'),
 p([b('Problem: '),r('with 20+ products filing bugs, duplicates waste triage time and slow resolution.')]),
 p([b('Approach: '),r('embed each bug report with Google text-embedding-005 (768 dimensions), index in GCP Vector Search, and run KNN to return the top-K similar bugs when a new one is submitted.')]),
 p([b('Why it works: '),r('embeddings capture meaning, so reports phrased differently still match, which keyword search misses.')]),
 p([b('Talking points: ')]),
 bl('Choosing K and a similarity threshold: too low floods users, too high misses duplicates.'),
 bl('Running at submission time, so the suggestion appears before triage ever sees the duplicate.'),
 bl('How I would measure it: precision of suggested duplicates and triage time saved.'),
 h1('5. Deep dive 2: AI in Dashboard (3 min)'),
 p([b('Problem: '),r('non-technical stakeholders need answers from data without writing SQL.')]),
 p([b('Approach: '),r('SVM-based intent classification routes the question, then an LLM uses schema-aware reasoning to generate SQL that is validated before it runs, with interactive visualizations on top.')]),
 p([b('Talking points: ')]),
 bl('Why a lightweight classifier first: cheap, fast and predictable before any LLM call.'),
 bl('Schema awareness and validation to reduce hallucinated tables, columns and unsafe queries.'),
 bl('Keeping the user in the loop with clear results and charts rather than raw output.'),
 h1('6. Deep dive 3: Hybrid retrieval (2 min)'),
 p([r('In my Amazon-style product listing generator, I combined BM25 (exact terms) with dense retrieval (meaning) over 50K+ records, using CLIP and FAISS for multimodal search. Hybrid retrieval improved '),b('Precision@10 by 18%'),r(', evaluated with MRR and Recall@K. The listings are generated through the Claude API.')]),
 say('Keyword search is precise but brittle; dense search is flexible but fuzzy. Combining them gives better results than either alone.'),
 h1('7. Lessons from production (2 min)'),
 bl([b('Evaluate first: '),r('define metrics (Precision@K, MRR, Recall@K) before tuning prompts or models.')]),
 bl([b('Guardrails: '),r('validate LLM output (for example SQL) before acting on it.')]),
 bl([b('Start simple: '),r('a small classifier or BM25 baseline often beats a complex setup on cost and latency.')]),
 bl([b('Monitor after launch: '),r('data and usage drift, so track quality continuously.')]),
 h1('8. Close (1 min)'),
 say('To sum up: I build end-to-end GenAI and ML systems, from data and retrieval through to deployment and monitoring. I would be glad to go deeper on any of these.'),
 h1('9. Likely questions and short answers'),
 h2('How do you reduce LLM hallucinations?'),
 p('Ground answers in retrieved data, validate outputs (such as SQL against the schema), and return sources so users can verify.'),
 h2('RAG or fine-tuning?'),
 p('RAG for fresh or private knowledge and traceability; fine-tuning (LoRA/QLoRA) for consistent style, format or domain behaviour. They can be combined.'),
 h2('How do you evaluate retrieval quality?'),
 p('Precision@K, Recall@K and MRR on labelled queries, plus spot checks on failure cases.'),
 h2('How do you choose an embedding model or vector index?'),
 p('Compare candidates on my own data using retrieval metrics, then weigh dimension size, latency, cost and managed-service fit.'),
 h2('What would you improve next?'),
 p('Reranking, stronger offline evaluation sets and automated monitoring of retrieval quality.'),
 p([it('Tip: have a number ready for each project (the +18% Precision@10 is yours). If you can add real impact figures for BugSuggestion and AI in Dashboard, add them to the deep dives above.')]),
];
const doc=new Document({numbering:{config:[{reference:'bl',levels:[{level:0,format:LevelFormat.BULLET,text:'•',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:540,hanging:270}}}}]}]},
 sections:[{properties:{page:{size:{width:11906,height:16838},margin:{top:1200,bottom:1200,left:1440,right:1440}}},children:kids}]});
Packer.toBuffer(doc).then(x=>fs.writeFileSync('../Achuth_Area_of_Expertise_15min_Talk.docx',x));
