🕸️ Graph Intelligence Network Analyzer

📌 Overview
A graph-based analysis system that transforms interaction data (calls, transactions, and meetings) into a network graph and applies graph theory algorithms to uncover structural patterns, influential nodes, bridge entities, and community clusters.
The project is built using Python + NetworkX and focuses on network science concepts used in fraud detection, OSINT analysis, and cybersecurity investigations.

🎯 Problem Statement
Real-world interaction data often contains hidden patterns that are difficult to analyze using traditional tabular approaches.
This project addresses:
How can we model entity interactions as a graph and extract meaningful insights such as influence, connectivity, and community structure using graph theory?

⚙️ Features

📊 Graph construction from interaction datasets (CSV-based)
🔗 Relationship mapping (calls, transactions, meetings)
🧠 Degree centrality analysis (highly connected nodes)
🌉 Betweenness centrality (bridge / hidden connector detection)
👥 Community detection (network clustering)
🧭 Shortest path tracing between entities
⚠️ Risk scoring system (based on graph structure metrics)
📈 Timeline-based interaction analysis
🧾 Investigation-style insights and ranking system


🧠 Core Concepts Used
┌──────────────────────┐
                │   CSV Dataset        │
                │ (Interactions)       │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │ Graph Builder        │
                │ (NetworkX Graph)     │
                └─────────┬────────────┘
                          │
          ┌───────────────┼────────────────┐
          ▼               ▼                ▼
┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ Centrality     │ │ Community      │ │ Path Analysis  │
│ Analysis       │ │ Detection      │ │ (Shortest Path)│
└───────┬────────┘ └───────┬────────┘ └───────┬────────┘
        │                  │                  │
        └──────────┬───────┴───────┬─────────┘
                   ▼               ▼
        ┌──────────────────────────────────┐
        │     Risk Scoring Engine          │
        │ (Influence + Bridge + Activity)  │
        └──────────────────────────────────┘
                          │
                          ▼
        ┌──────────────────────────────────┐
        │      Dashboard / Reports         │
        │  (Insights + Rankings + Graph)   │
        └──────────────────────────────────┘
Graph Theory (NetworkX)
Degree Centrality
Betweenness Centrality
Connected Components
Shortest Path Algorithms
Community Detection
Temporal Interaction Analysis (basic)
