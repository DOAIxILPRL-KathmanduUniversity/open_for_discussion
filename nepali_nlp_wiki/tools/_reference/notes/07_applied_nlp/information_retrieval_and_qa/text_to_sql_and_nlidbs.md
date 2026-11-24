# Text-to-SQL & NL Interfaces for Databases (NLIDBs)

> [!IMPORTANT] Gist
> Natural Language Interfaces to Databases (NLIDBs) allow non-technical users to access relational data via natural language. The core task is **Text-to-SQL**, which maps an unstructured query into a structured, executable SQL statement (Katsogiannis-Meimarakis et al., 2026).

## 1. The Text-to-SQL Pipeline
A standard neural Text-to-SQL system follows these steps:
1.  **Input Pre-Processing**:
    *   **Schema Linking**: Identifying which tables and columns are referenced in the natural language question (NLQ).
    *   **Value Linking**: Mapping entities in the NLQ to specific cell values in the database.
2.  **Input Construction**: Serializing the schema (e.g., `Table1 [Col1, Col2] | Table2 [Col3]`) and the NLQ into a format suitable for a Transformer or LLM.
3.  **SQL Generation**:
    *   **Sequence-to-Sequence**: Directly generating the SQL string.
    *   **Sketch-based**: Filling in the slots of a pre-defined SQL template.
    *   **Grammar-based**: Generating an Abstract Syntax Tree (AST) to ensure the SQL is syntactically valid.
4.  **Output Post-Processing**:
    *   **Execution-guided Decoding**: Running candidate SQLs against a database to filter out those that produce errors or empty results.

## 2. Multi-turn & Conversational SQL
Modern NLIDBs handle multi-turn interactions where the user asks follow-up questions:
- **Context Management**: The system must track the state of previous queries to resolve pronouns (e.g., "What is the price of the *first one*?") or constraints (e.g., "Now show only the *red ones*").
- **Conversational Benchmarks**: **SParC** and **CoSQL** are the standard datasets for testing cross-domain conversational SQL.

## 3. Beyond Generation: SQL-to-Text & Results-to-Text
- **SQL-to-Text**: Explaining an existing SQL query in natural language to help the user verify if the system understood them correctly.
- **Data-to-Text**: Summarizing the results of a query (e.g., "The average price is $50, which is a 10% increase from last month") rather than just showing a raw table.

## 4. LLMs and In-Context Learning (ICL)
LLMs have revolutionized NLIDBs through **Few-shot Prompting**:
- **Chain of Thought (CoT)**: Prompting the model to "think step-by-step" through the logic of the SQL (e.g., "First, I need to join the 'Sales' and 'Items' tables...").
- **In-Context Learning**: Providing a few examples of (NLQ, SQL) pairs in the prompt to guide the model on specific schema patterns without fine-tuning.

---

#applied #sql #nlidb #generation #llm #schema-linking
