import sys
from playwright.sync_api import sync_playwright

HEAD = """<html><head><meta charset="utf-8"><style>
@page{size:A4;margin:%s}
body{font-family:'Latin Modern Roman','Times New Roman',Georgia,serif;font-size:%s;line-height:%s;color:#111;margin:0}
h1{text-align:center;font-size:22pt;letter-spacing:1px;margin:0}
.sub{text-align:center;font-size:11pt;margin:1px 0 3px}
.ct{text-align:center;font-size:9.5pt;margin-bottom:2px}
.ct a{color:#1a3fb0;text-decoration:none}
h2{font-size:11.5pt;letter-spacing:.5px;text-transform:uppercase;border-bottom:1px solid #000;margin:%s 0 3px;padding-bottom:1px}
.row{display:flex;justify-content:space-between;font-weight:bold}
.row i{font-weight:normal}
.org{font-style:italic;display:flex;justify-content:space-between}
ul{margin:1px 0 3px;padding-left:17px}
li{margin:0 0 1px;text-align:justify}
p{margin:1px 0;text-align:justify}
.sk b{font-weight:bold}
.tech{font-style:italic;font-size:92%%;margin:0}
</style></head><body>"""

def build(two):
    page_m, fs, lh, h2m = ("11mm 13mm","9.6pt","1.22","6px") if not two else ("15mm 17mm","10.9pt","1.4","13px")
    h = HEAD % (page_m, fs, lh, h2m)
    h += """<h1>DINTAKURTHI ACHUTH</h1>
<div class="sub">Data Scientist &nbsp;|&nbsp; Generative AI &amp; Machine Learning Engineer</div>
<div class="ct">dintakurthiachuth@gmail.com &nbsp;•&nbsp; +919014262115 &nbsp;•&nbsp; Hyderabad, India</div>
<h2>Summary</h2>
<p>Results-driven Data Scientist with 3+ years of experience building and deploying end-to-end ML and Generative AI solutions across the full lifecycle — data engineering, modeling, deployment and monitoring — at enterprise scale for Google. Strong in Python, SQL and Java, with deep hands-on work in LLMs, RAG architectures, vector search, fine-tuning (LoRA/QLoRA) and multi-agent systems. Experienced Java developer who can ship AI features inside production-grade full-stack applications. Focused on turning complex models into measurable business impact.</p>
"""
    if two:
        h += """<h2>Core Competencies</h2>
<ul><li><b>Generative AI engineering:</b> RAG, agentic workflows, fine-tuning (LoRA/QLoRA), evaluation and guardrails for production LLM systems.</li>
<li><b>Applied ML &amp; analytics:</b> NLP, computer vision, embeddings and similarity search, statistics and experimentation, data storytelling for stakeholders.</li>
<li><b>Engineering:</b> Java/Spring Boot and Python services, REST APIs, Docker/Kubernetes, CI/CD and cloud deployment on GCP and AWS.</li></ul>"""
    h += """<h2>Professional Experience</h2>
<div class="row"><span>Data Scientist</span><span>04/2023 – Present</span></div>
<div class="org"><b>Virtusa (Deployed at Google)</b><span>Hyderabad, India</span></div><ul>
<li><b>AI in Dashboard:</b> Built an LLM-powered natural-language query interface that uses SVM-based intent classification to translate plain-English questions into validated SQL, with schema-aware reasoning and interactive visualizations for non-technical stakeholders.</li>
<li><b>BugSuggestion:</b> Developed a duplicate bug detection system across 20+ Google products using text-embedding-005 (768-dim) and GCP Vector Search; KNN similarity search surfaces top-K duplicates at submission time, automating triage and accelerating resolution.</li>
"""
    if two:
        h += """<li>Owned the full ML lifecycle on both products: data pipelines and preprocessing, embedding generation, model selection, evaluation, deployment on GCP and post-release monitoring.</li>
<li>Designed schema-aware prompting and SQL validation guardrails to reduce hallucinated queries and make LLM output safe for non-technical users.</li>
<li>Collaborated with engineering, product and triage teams to gather requirements, iterate on relevance and ship production features used across 20+ products.</li>
<li>Recognised with the <b>Time Award</b> (2025) for outstanding contributions, innovation and passion in Generative AI initiatives.</li>"""
    h += "</ul>"
    h += "<h2>Key Projects</h2>"
    # Java project
    h += """<div class="row"><span>InsightDesk — AI-Powered Support Platform (Java Full-Stack)</span><span>2025</span></div>
<p class="tech">Java 21 • Spring Boot 3 • Spring Security (JWT) • Spring Data JPA • PostgreSQL + pgvector • React • Docker • Python/FastAPI model service</p><ul>
<li>Designed and built a full-stack ticketing and knowledge platform: layered Spring Boot REST backend with JWT role-based auth, JPA/PostgreSQL persistence and a React dashboard.</li>
<li>Integrated a RAG pipeline (pgvector semantic search + LLM) via a Python microservice to auto-suggest answers and surface similar past tickets; containerised with Docker Compose.</li>"""
    if two:
        h += """<li>Applied clean architecture, DTO validation, global exception handling and JUnit/Mockito tests to keep the Java codebase production-ready.</li>"""
    h += "</ul>"
    h += """<div class="row"><span>AI-Powered Amazon-Style Product Listing Generator</span><span>2025</span></div>
<p class="tech">OpenAI CLIP • FAISS • BM25 • Claude API • Stable Diffusion / ControlNet • React • FastAPI</p><ul>
<li>Built a multimodal retrieval system with CLIP + FAISS to retrieve similar products from 50K+ records and auto-generate Amazon-style listings via the Claude API.</li>
<li>Implemented hybrid BM25 + dense retrieval (<b>Precision@10 +18%</b>), enhanced visuals with Stable Diffusion/ControlNet, deployed via React + FastAPI; evaluated with MRR and Recall@K.</li>
</ul>"""
    h += """<div class="row"><span>ResearchPilot — Multi-Agent Research &amp; Analytics Copilot</span><span>2025</span></div>
<p class="tech">LangGraph • Claude / OpenAI APIs • RAG (Pinecone + BM25 rerank) • FastAPI • Redis • Docker • GCP</p><ul>
<li>Built a LangGraph multi-agent system (planner, retriever, SQL-analyst, critic) that answers business questions over documents and warehouse tables, with cited sources and self-verification before responding.</li>
<li>Added hybrid retrieval with reranking, tool-calling for SQL/Python execution, response caching in Redis and an LLM-as-judge evaluation harness (faithfulness, answer relevance, latency) to track quality across prompt and model changes.</li>"""
    if two:
        h += """<li>Exposed the pipeline as an async FastAPI service with streaming responses, request tracing and guardrails (PII masking, prompt-injection checks), containerised for deployment on GCP.</li>"""
    h += "</ul>"
    if two:
        h += """<div class="row"><span>Domain LLM Fine-Tuning with QLoRA</span><span>2025</span></div>
<p class="tech">HuggingFace Transformers • PEFT • QLoRA • bitsandbytes • PyTorch • Weights &amp; Biases</p><ul>
<li>Fine-tuned an open-source LLM with 4-bit QLoRA on a curated instruction dataset, and benchmarked it against the base model and prompted API baselines on task accuracy, cost and latency.</li>
<li>Built the data cleaning, deduplication and train/eval split pipeline, tracked experiments, and served the adapter locally via Ollama for low-cost inference.</li></ul>"""
    if two:
        h += """<div class="row"><span>Skin Cancer Classification using Convolutional Neural Networks</span><span>Research</span></div>
<ul><li>Published research applying CNN-based image classification to skin lesion diagnosis, covering data preprocessing, model training and evaluation.</li></ul>"""
    h += """<h2>Technical Skills</h2><div class="sk">
<p><b>Programming Languages:</b> Python, Java (Core Java, Spring Boot, JPA/Hibernate, JUnit), Scala, SQL, R, JavaScript</p>
<p><b>Generative AI:</b> LLMs, SLMs, Prompt Engineering, Fine-tuning (LoRA, QLoRA), RAG, LangChain, LangGraph, AI Agents, Multi-Agent Systems, LLMOps, Ollama</p>
<p><b>Machine Learning &amp; Deep Learning:</b> Regression, Classification, Clustering, Dimensionality Reduction, CNNs, RNNs, LSTMs, GANs, Transformers, Autoencoders, Computer Vision, Object Detection, Image Segmentation, OCR, NER, Sentiment Analysis, Text Classification, PyTorch, TensorFlow, Scikit-learn, HuggingFace</p>
<p><b>Data Analysis &amp; Big Data:</b> Pandas, NumPy, SciPy, PySpark, Apache Spark (Scala), EDA, Statistics, Hypothesis Testing, A/B Testing, Feature Engineering, Matplotlib, Seaborn, Plotly, Tableau, Power BI</p>
<p><b>Databases &amp; Cloud:</b> MySQL, PostgreSQL, Redis, MongoDB, Firebase, Pinecone, ChromaDB, FAISS, Weaviate, pgvector, GCP (Vertex AI, Vector Search, DataNexus), AWS (S3, EC2, IAM)</p>
<p><b>DevOps &amp; Tools:</b> Docker, Kubernetes, Terraform, CI/CD Pipelines, RESTful APIs, FastAPI, Spring Boot, Git</p>
<p><b>3D &amp; Creative:</b> 3D Asset Design (Blender), Stable Diffusion / ControlNet pipelines</p></div>"""
    h += """<h2>Education</h2><div class="row"><span>B.Tech in Computer Science and Engineering</span><span>2019 – 2023</span></div>
<div class="org"><span>Kalasalingam Academy of Research and Education &nbsp; <b style="font-style:normal">CGPA: 8.7</b></span></div>
<h2>Certifications &amp; Achievements</h2>
<div class="row"><span>Oracle Certified Java Associate <i>— Oracle</i></span><i>2023</i></div>
<div class="row"><span>Time Award, Virtusa — outstanding contributions, innovation and passion in Generative AI</span><i>2025</i></div>
<p>Research Publication: “Skin Cancer Classification using Convolution Neural Networks”</p>
</body></html>"""
    return h

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args=['--no-sandbox'])
    for two, name in ((False,'Achuth_Dintakurthi_DS_GenAI_1page.pdf'),(True,'Achuth_Dintakurthi_DS_GenAI_2page.pdf')):
        pg = b.new_page(); pg.set_content(build(two))
        pg.pdf(path='../'+name, prefer_css_page_size=True, print_background=True)
    b.close()
