# Dialogue Systems & Chatbots

> [!IMPORTANT] Gist
> Dialogue systems enable natural language interaction between humans and machines. Modern systems integrate phonetic, lexical, and pragmatic levels to simulate natural conversation.

## 1. Architecture of a Chatbot
1. **Wake Word Detection**: Identifying specific phrases (e.g., "Hey Siri," "Alexa") to initiate interaction.
2. **NLU Component**: Mapping user input to intents and entities.
3. **Dialogue Manager**: Maintaining state and deciding the next action/response.
4. **NLG Component**: Generating the textual/vocal response.

## 2. Landmark Systems
- **ELIZA (1966)**: First chatbot; used pattern matching for Rogerian therapy simulation.
- **ALICE (First Gen)**: Used **AIML** (Artificial Intelligence Markup Language) for rule-based conversational logic.
- **GUS (Genial Understander System)**: A landmark frame-based dialogue system for travel planning.

## 3. Types of Dialogue Systems
- **Task-Oriented**: Goal-focused; uses **Frame-based** or **Dialogue-State** architectures.
- **Open-Domain (Chit-Chat)**:
    - **Retrieval-Based**: Choosing the best response from a predefined database.
    - **Generation-Based**: Using LLMs to synthesize a novel response.
- **Intelligent Virtual Assistants (IVA)**: Broad systems like Google Assistant, Siri, and Alexa.

## 4. Fundamentals of Conversation
Effective chatbots must adhere to the rules of social interaction (Bengfort et al., 2018):
- **Greetings & Salutations**: Establishing the "handshake" and rapport.
- **Maintaining State**: Keeping track of what was said previously to provide context-aware responses.
- **Handling Miscommunication**: Detecting when the user is confused or the bot has failed, and providing recovery strategies (e.g., "I'm sorry, I didn't quite get that. Could you rephrase?").
- **Learning to Help**: Using feedback loops to improve response quality over time.

## 5. Dependency & Constituency Parsing for Chatbots
Structure analysis is critical for understanding user intent beyond simple keyword matching:
- **Question Detection**: Using syntactic structures to identify if a sentence is a question (e.g., detecting a "Wh-" word or an inverted auxiliary verb).
- **Subject-Predicate-Object Extraction**: Parsing the sentence to identify *who* is doing *what* to *whom*, allowing for precise information retrieval from a Knowledge Base.

## 6. Deploying Chatbots (The Telegram Flow)
Practical deployment involves integrating the bot logic with a **Bot Channel** (e.g., Telegram, Facebook Messenger).
1. **The Wrapper**: Messenger platforms provide a "wrapper" (via API keys/access tokens) for your logic.
2. **The Updater**: An object that polls for new messages from the platform.
3. **The Dispatcher**: Forwards the message to the appropriate **Handler** (callback function).
4. **spaCy Integration**: Using NLP to extract **Intents** (the action) and **Entities** (the targets) from the user's utterance in real-time.

---

#applied-nlp #chatbots #dialogue #iva
