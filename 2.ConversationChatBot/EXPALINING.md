### Create_history_aware_retriver
<br>
- smart retriver, retrive the user question based on chat history.
<br>
<Strong>Example</Strong> <br>
Q1. what is LLM? <br>
Q2. what is use of it? <br>
<br>
Result : what is the use of LLM?

---

### Create_retrieval_chain

it is connects

- Question -> Retriver -> Documents -> LLM -> Answer
---
### Create Stuff Document Chain

1. Takes retriver documents
2. Stuff them into promt
3. send everythnig to LLM

---
### Chat_Message_history
Stores: user messages, Assistant messages.
- used to maintain conversation memory

---
### ChatPromptTemplate

Defines structured chat prompts

Supports:

1. System message
2. User message
3. Context injection
---
### MessagesPlaceholder

Placeholder for chat history

Injects past messages dynamically

 Critical for conversational RAG

---
### RunnableWithMessageHistory
What it does

Wraps your chain

Automatically:

Reads chat history

Updates chat history

---

## PATH
### PDF-> LOADER -> sPLITTER -> EMBEDDING -> vECTORDB
### USER QUESTION



