# 🕸️ Graph Intelligence Network Analyzer

A graph-based network analysis platform that transforms interaction data into an interactive network and applies graph theory to uncover **influential entities, critical connections, communities, and relationship paths**.

Built with **Python, NetworkX, Pandas, and Streamlit**.

---

## 📌 Overview

Interaction data is often stored as rows and tables:

```text
A → B
B → C
C → D
```

Individually, these records may not reveal much.

This project converts those interactions into a **graph**, where:

* **Nodes** represent entities
* **Edges** represent relationships between entities

The resulting network can then be analyzed using graph algorithms to identify structural patterns that are difficult to see in raw tabular data.

The platform is designed as a general-purpose **Network Intelligence** tool and can be applied to domains such as:

* Fraud and financial networks
* Cybersecurity
* OSINT and investigation analysis
* Communication networks
* Social networks
* Supply-chain relationships

---

## 🎯 Problem Statement

Given a dataset containing relationships between entities:

> **How can graph theory be used to identify important entities, hidden communities, critical connectors, and relationships within the network?**

The system addresses this by converting interaction records into a graph and applying multiple network analysis techniques.

---

## ⚙️ Features

### 📊 Network Construction

* Import interaction data from CSV
* Automatically construct a graph from source-target relationships
* Support relationship types such as calls, transactions, and meetings

### 🧠 Centrality Analysis

Identify structurally important entities using:

* **Degree Centrality** — identifies highly connected entities
* **Betweenness Centrality** — identifies entities that act as bridges between different parts of the network

### 👥 Community Detection

Identify groups of closely connected entities within the network.

### 🧭 Shortest Path Analysis

Find the shortest connection path between any two entities.

Example:

```text
A → B → D → E → F
```

### 🔗 Connectivity Analysis

Analyze connected components to determine which entities belong to the same network.

### 📈 Network Statistics

View structural information such as:

* Number of entities
* Number of relationships
* Network connectivity
* Centrality rankings
* Community structure

### 🕸️ Interactive Visualization

Explore the generated network visually and inspect relationships between entities.

---

## 🧠 Core Concepts

The system follows this pipeline:

```text
┌──────────────────────┐
│     CSV Dataset      │
│    (Interactions)    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Data Processing   │
│       Pandas         │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     Graph Builder    │
│      NetworkX        │
└──────────┬───────────┘
           │
           ▼
┌─────────────────────────────────────┐
│          Network Analysis           │
│                                     │
│  • Degree Centrality                │
│  • Betweenness Centrality           │
│  • Community Detection              │
│  • Connected Components             │
│  • Shortest Path Analysis           │
└──────────┬──────────────────────────┘
           │
           ▼
┌──────────────────────┐
│ Interactive Dashboard│
│   & Visualizations   │
└──────────────────────┘
```

---

## 📂 Input Data

The platform accepts CSV-based interaction data.

Example:

```csv
source,target,type
A,B,call
A,C,call
B,D,transaction
D,E,meeting
E,F,call
G,H,call
H,I,transaction
```

Where:

| Column   | Description          |
| -------- | -------------------- |
| `source` | Starting entity      |
| `target` | Connected entity     |
| `type`   | Type of relationship |

The same structure can represent different types of networks depending on the dataset.

---

## 🔍 How the Analysis Works

### 1. Degree Centrality

Measures how connected an entity is to the rest of the network.

A highly connected node may represent an important or highly active entity.

```text
       B
       |
C ──── A ──── D
       |
       E
```

Here, `A` has several direct connections and therefore has high degree centrality.

---

### 2. Betweenness Centrality

Measures how frequently a node lies on the shortest paths between other nodes.

Example:

```text
Group A

A ─ B ─ C
      |
      D
      |
      E ─ F ─ G

Group B
```

If many paths between two parts of the network pass through `D`, it becomes a structurally important bridge.

This helps identify **critical connectors** within a network.

---

### 3. Community Detection

Networks often contain groups where nodes have stronger connections with members of their own group.

The system identifies these clusters to reveal the underlying community structure.

```text
Community 1          Community 2

A ─ B ─ C             X ─ Y
|     |                \ /
D ─── E                 Z
```

---

### 4. Shortest Path

Given two entities, the system determines the shortest route connecting them through the network.

```text
A → B → D → E → F
```

This can help understand how entities are connected and how many relationships separate them.

---

### 5. Connected Components

Connected-component analysis identifies separate networks within the dataset.

For example:

```text
A ─ B ─ C ─ D

X ─ Y ─ Z
```

The system recognizes these as two independent connected components.

---

## 🛠️ Tech Stack

### Backend / Analysis

* **Python**
* **NetworkX**
* **Pandas**

### Interface

* **Streamlit**

### Visualization

* Network graph visualization through Python graph/plotting libraries

---

## 📁 Project Structure

```text
network-intelligence/
│
├── app.py
│
├── data/
│   └── interactions.csv
│
├── src/
│   ├── data_loader.py
│   ├── graph_builder.py
│   ├── analytics.py
│   └── visualizer.py
│
├── requirements.txt
│
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd network-intelligence
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 Example Workflow

```text
Upload CSV
     ↓
Validate interaction data
     ↓
Construct network graph
     ↓
Calculate network statistics
     ↓
Run graph analysis
     ↓
Identify important entities
     ↓
Detect communities
     ↓
Explore connection paths
     ↓
Visualize results
```

---

## 💡 Why Graph Analysis?

Traditional tabular analysis focuses on individual records.

Graph analysis focuses on **relationships**.

For example:

```text
A → B
B → C
C → D
```

A table shows three separate interactions.

A graph reveals a **chain of connected entities**.

As networks become larger, graph-based methods can reveal structural properties that are difficult to identify by inspecting rows individually.

---

## 🔐 Responsible Use

This project is intended for **network analysis and research/educational purposes**.

Graph metrics identify structural patterns in a network. They do **not** establish criminal activity, intent, or wrongdoing.

For example:

> A node with high betweenness centrality is a structurally important connector.

It does **not** automatically mean:

> The person represented by that node is suspicious or guilty.

Any real-world investigative application would require appropriate data validation, context, legal processes, and human review.

---

## 🔮 Future Improvements

Potential extensions include:

* [ ] Temporal network analysis
* [ ] Weighted relationship analysis
* [ ] Interactive node-level exploration
* [ ] Advanced community detection
* [ ] Custom network scoring
* [ ] Network evolution over time
* [ ] Larger-scale graph processing
* [ ] Exportable analysis reports
* [ ] Domain-specific analysis modules for fraud or cybersecurity

---

## 📚 Key Concepts Demonstrated

This project provides practical experience with:

* Graph data structures
* Graph traversal
* Breadth-First Search
* Shortest path algorithms
* Centrality measures
* Community detection
* Connected components
* Network visualization
* Data processing
* Interactive data applications

---

## 👩‍💻 Author

**Nidhii Warankar**

Built as an exploration of **graph algorithms, network science, and data-driven problem solving**.

Temporal Interaction Analysis (basic)
