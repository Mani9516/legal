import streamlit as st
import pyttsx3

# Function to recognize speech input
# Function to speak response
def speak_response(response):
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()

# Define a function to get response from ChatGPT API
def get_chatgpt_response(user_input):
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Define a dictionary of questions and answers
question_answer_pairs = {
 "What is your name?": "I am a chatbot.",
    "Hii": "Hii I am LegalEase.",
    "Hello": "Hi! How can I help you?",
    "What can you do?": "I can answer your questions and chat with you.",
    "I want to create a legal contract": """Creating a legally-binding contract involves several key steps:
1. Agreement: Ensure that all parties involved agree to the terms and conditions of the contract.
2. Identification of Parties: Clearly identify the parties entering into the contract, including their legal names and roles.
3. Definitions: Define any terms or concepts used in the contract to avoid ambiguity.
4. Description of Services or Goods: Clearly outline the services to be provided or the goods to be exchanged.
5. Terms and Conditions: Detail the rights, obligations, and responsibilities of each party, including payment terms, delivery schedules, and dispute resolution mechanisms.
6. Consideration: Specify what each party will receive in exchange for fulfilling their obligations under the contract.
7. Duration and Termination: If applicable, include provisions regarding the duration of the contract and circumstances under which it can be terminated.
8. Confidentiality and Non-Disclosure: If necessary, include clauses to protect sensitive information shared between the parties.
9. Governing Law and Jurisdiction: Specify the governing law and jurisdiction in case of disputes.
10. Signature and Date: Ensure that all parties sign and date the contract to indicate their agreement and commitment.""",
    "What is LegalEase?": "LegalEase is an online platform that helps users create various legal documents quickly and easily.",
    "How does LegalEase work?": "LegalEase guides users through a step-by-step process to create customized legal documents tailored to their specific needs.",
    "Is LegalEase suitable for individuals or businesses?": "LegalEase caters to both individuals and businesses seeking to create legally binding documents.",
    "What types of legal documents can I create with LegalEase?": "LegalEase offers a wide range of legal document templates, including contracts, agreements, leases, wills, and more.",
    "Are the documents created by LegalEase legally valid?": "Yes, the documents generated by LegalEase are legally valid when completed accurately and signed by the relevant parties.",
    "Do I need legal knowledge to use LegalEase?": "No, LegalEase is designed to be user-friendly and does not require legal expertise to create documents.",
    "Can I customize the documents created by LegalEase?": "Yes, LegalEase allows users to customize document templates to fit their specific requirements.",
    "Are the documents created by LegalEase legally binding?": "Yes, once properly completed and signed, the documents created through LegalEase are legally binding.",
    "How secure is my information on LegalEase?": "LegalEase takes data security seriously and employs industry-standard encryption to protect user information.",
    "Can I access my documents at any time after creation?": "Yes, users can access and download their documents from LegalEase at any time for future reference.",
    "Are there any hidden fees associated with using LegalEase?": "No, LegalEase operates on a transparent pricing model with no hidden fees.",
    "Can I preview my document before finalizing it?": "Yes, LegalEase allows users to preview their documents before finalizing them for download.",
    "What payment methods does LegalEase accept?": "LegalEase accepts various payment methods, including credit/debit cards and online payment gateways.",
    "Can I get legal advice through LegalEase?": "LegalEase does not provide legal advice but offers resources and guidance for document creation.",
    "Is LegalEase available in multiple languages?": "Yes, LegalEase supports document creation in multiple languages for user convenience.",
    "How quickly can I create a legal document with LegalEase?": "The time taken to create a legal document with LegalEase depends on the complexity of the document and user input.",
    "Can I make changes to my document after creation?": "Yes, users can make changes to their documents within LegalEase before finalizing them.",
    "Does LegalEase provide customer support?": "Yes, LegalEase offers customer support to assist users with any questions or issues they may encounter.",
    "Can I create documents for international use with LegalEase?": "Yes, LegalEase offers templates suitable for international use, with options to customize based on jurisdictional requirements.",
    "How does LegalEase ensure document accuracy?": "LegalEase uses intelligent algorithms and checks to ensure document accuracy based on user input.",
    "Is my personal information shared with third parties when using LegalEase?": "LegalEase respects user privacy and does not share personal information with third parties without consent.",
    "Can I create documents for specific industries with LegalEase?": "Yes, LegalEase offers industry-specific document templates tailored to the needs of different sectors.",
    "Does LegalEase offer a satisfaction guarantee?": "Yes, LegalEase stands behind the quality of its services and offers a satisfaction guarantee to users.",
    "Can I create documents for real estate transactions with LegalEase?": "Yes, LegalEase provides templates for real estate transactions, such as leases, purchase agreements, and rental agreements.",
    "Can I create non-disclosure agreements (NDAs) with LegalEase?": "Yes, LegalEase offers templates for NDAs and other confidentiality agreements.",
    "Can I create employment contracts with LegalEase?": "Yes, LegalEase provides templates for employment contracts, including terms of employment, job descriptions, and compensation details.",
    "Are there any restrictions on the use of documents created by LegalEase?": "Users must adhere to legal and ethical standards when using documents created by LegalEase, including compliance with relevant laws and regulations.",
    "Does LegalEase offer document storage services?": "Yes, LegalEase provides document storage options for users to securely store and access their documents online.",
    "Can I collaborate with others on document creation through LegalEase?": "LegalEase offers collaboration features, allowing multiple users to work on the same document simultaneously.",
    "Can I create documents for small claims court with LegalEase?": "Yes, LegalEase offers templates for small claims court documents, such as demand letters and settlement agreements.",
    "Does LegalEase offer document review services?": "While LegalEase does not provide legal review services, users can seek independent legal advice if required.",
    "Can I create business formation documents with LegalEase?": "Yes, LegalEase offers templates for business formation documents, including articles of incorporation, operating agreements, and partnership agreements.",
    "Does LegalEase offer templates for intellectual property agreements?": "Yes, LegalEase provides templates for intellectual property agreements, such as licensing agreements, assignment agreements, and non-compete agreements.",
    "Can I create documents for family law matters with LegalEase?": "Yes, LegalEase offers templates for family law matters, including prenuptial agreements, divorce agreements, and child custody agreements.",
    "Does LegalEase offer templates for immigration-related documents?": "Yes, LegalEase provides templates for immigration-related documents, such as visa applications, sponsorship agreements, and immigration petitions.",
    "Can I create documents for debt collection with LegalEase?": "Yes, LegalEase offers templates for debt collection documents, including demand letters, promissory notes, and debt settlement agreements.",
    "Does LegalEase offer templates for dispute resolution agreements?": "Yes, LegalEase provides templates for dispute resolution agreements, such as arbitration agreements and mediation agreements.",
    "Can I create documents for healthcare-related matters with LegalEase?": "Yes, LegalEase offers templates for healthcare-related matters, including medical consent forms, healthcare directives, and patient agreements.",
    "Does LegalEase offer templates for insurance-related documents?": "Yes, LegalEase provides templates for insurance-related documents, such as insurance policies, claim forms, and release of liability agreements.",
    "Can I create documents for intellectual property protection with LegalEase?": "Yes, LegalEase offers templates for intellectual property protection, including copyright notices, trademark applications, and patent assignments.",
    "Does LegalEase offer templates for compliance-related documents?": "Yes, LegalEase provides templates for compliance-related documents, such as privacy policies, terms of service agreements, and regulatory filings.",
    "Can I create documents for investment agreements with LegalEase?": "Yes, LegalEase offers templates for investment agreements, including shareholder agreements, venture capital agreements, and term sheets.",
    "Does LegalEase offer templates for partnership agreements?": "Yes, LegalEase provides templates for partnership agreements, including general partnerships, limited partnerships, and joint venture agreements.",
    "Can I create documents for mergers and acquisitions with LegalEase?": "Yes, LegalEase offers templates for mergers and acquisitions, including asset purchase agreements, stock purchase agreements, and merger agreements.",
    "Does LegalEase offer templates for franchise agreements?": "Yes, LegalEase provides templates for franchise agreements, including franchise disclosure documents, franchise agreements, and franchisee agreements.",
    "Can I create documents for construction projects with LegalEase?": "Yes, LegalEase offers templates for construction-related documents, including construction contracts, subcontractor agreements, and lien waivers.",
    "Does LegalEase offer templates for lease agreements?": "Yes, LegalEase provides templates for lease agreements, including residential leases, commercial leases, and rental agreements.",
    "Can I create documents for technology-related agreements with LegalEase?": "Yes, LegalEase offers templates for technology-related agreements, including software licenses, service level agreements, and software development agreements.",
    "Does LegalEase offer templates for employment policies and handbooks?": "Yes, LegalEase provides templates for employment policies and handbooks, including employee manuals, workplace policies, and code of conduct documents.",
    "Can I create documents for corporate governance with LegalEase?": "Yes, LegalEase offers templates for corporate governance documents, including bylaws, board resolutions, and meeting minutes.",
    "What are the key provisions of the Indian Penal Code (IPC)?": "The IPC contains provisions related to crimes and punishments in India, covering offenses such as theft, assault, murder, and fraud.",
    "How do I draft a legal contract under Indian law?": "Drafting a legal contract in India requires understanding the essential elements of a contract, such as offer, acceptance, consideration, and lawful object. It's also crucial to ensure compliance with Indian contract law principles.",
    "What are the requirements for a valid will in India?": "To create a valid will in India, the testator must be of sound mind, the will must be in writing, signed by the testator, and witnessed by at least two competent witnesses.",
    "How can I protect my intellectual property rights in India?": "Intellectual property rights in India can be protected through trademarks, copyrights, patents, and designs. Each type of intellectual property has specific registration requirements and procedures.",
    "What are the legal requirements for forming a company in India?": "Forming a company in India involves compliance with the Companies Act, which includes steps such as company name reservation, drafting the memorandum and articles of association, and filing incorporation documents with the Registrar of Companies.",
    "What are the legal implications of non-compliance with labor laws in India?": "Non-compliance with labor laws in India can result in penalties, fines, legal disputes, and reputational damage for businesses. It's essential to adhere to employment laws related to wages, working hours, safety standards, and employee benefits.",
    "How do I create a non-disclosure agreement (NDA) under Indian law?": "Creating an NDA in India involves specifying the confidential information to be protected, defining the parties' obligations regarding confidentiality, and outlining the consequences of breach.",
    "What are the legal requirements for leasing property in India?": "Leasing property in India requires drafting a lease agreement that includes details such as the parties involved, lease term, rent amount, security deposit, and terms of renewal and termination.",
    "How do I comply with data protection laws when collecting personal information in India?": "Compliance with data protection laws in India, such as the Personal Data Protection Bill, involves obtaining consent for data collection, ensuring data security measures, and providing individuals with rights regarding their personal data.",
    "What are the legal considerations for drafting employment contracts in India?": "Drafting employment contracts in India requires addressing key terms such as job responsibilities, compensation, benefits, termination clauses, non-compete clauses, and dispute resolution mechanisms in compliance with Indian labor laws."
}


# Set title and header
st.title("LegalEase")
st.header("Chat with LegalEase")

# Text field for entering messages
new_message = st.text_input("Enter your message:", "")

# If the user sends a text message, display the bot's response
if st.button("Send"):
    if new_message in question_answer_pairs:
        bot_response = question_answer_pairs[new_message]
    else:
        bot_response = "I'm sorry, I don't know the answer to that question."

    st.text("⚖ LegalEase: " + bot_response)
    speak_response(bot_response)

# Button for voice input with spoken prompt
if st.button("Speak"):
    user_input = recognize_speech()
    if user_input:
        speak_response("Hi! How can I help you?")  # Speak prompt
        st.write("How can I help you?")
        response = get_chatgpt_response(user_input)
        st.text("⚖ LegalEase: " + response)
        speak_response(response)
