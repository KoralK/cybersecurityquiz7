import streamlit as st

def main():
    st.title("Maintaining Access & Covering Tracks Quiz")
    st.markdown("Test your understanding of backdoors, steganography, and log manipulation tactics.")

    questions = [
        {
            "question": "What is the primary purpose of a backdoor in system hacking?",
            "options": [
                "Encrypt sensitive data",
                "Maintain persistent access to a compromised system",
                "Scan for new vulnerabilities"
            ],
            "answer": "Maintain persistent access to a compromised system",
            "explanation": "Backdoors ensure attackers can re-enter systems without re-exploiting vulnerabilities."
        },
        {
            "question": "Which tool is specifically mentioned for creating backdoors?",
            "options": ["Wireshark", "Metasploit Meterpreter", "Nmap"],
            "answer": "Metasploit Meterpreter",
            "explanation": "Metasploit’s Meterpreter is a common tool for backdoor creation."
        },
        {
            "question": "How does NTFS Alternate Data Stream (ADS) hide data?",
            "options": [
                "Encrypts files in the system BIOS",
                "Stores hidden data within existing files without altering their appearance",
                "Deletes original files after duplication"
            ],
            "answer": "Stores hidden data within existing files without altering their appearance",
            "explanation": "ADS uses NTFS metadata to hide data invisibly within files."
        },
         {
            "question": "What is steganography primarily used for?",
            "options": [
                 "Deleting event logs",
                "Hiding secret messages within ordinary files (e.g., images)",
                "Brute-forcing passwords"
            ],
            "answer": "Hiding secret messages within ordinary files (e.g., images)",
             "explanation": "Steganography embeds hidden data in media files (e.g., images, audio) to avoid detection."
        },
        {
            "question": "Which action helps attackers avoid detection after compromising a system?",
             "options": [
                 "Disabling firewalls",
                "Clearing event logs",
                "Encrypting all user data"
            ],
            "answer": "Clearing event logs",
             "explanation": "Attackers clear logs to erase evidence of their activities and avoid detection."
        },
        {
            "question": "What is a risk of clearing system logs?",
            "options": [
                 "Improved system performance",
                "Obvious evidence of tampering (missing logs)",
                "Automatic system shutdown"
            ],
            "answer": "Obvious evidence of tampering (missing logs)",
            "explanation": "Missing logs can alert administrators to unauthorized access."
        },
        {
            "question": "Which tool is used for 'covering tracks' in Windows?",
            "options": [
                 "CCleaner",
                "Wireshark",
                "Nmap"
            ],
            "answer":"CCleaner",
            "explanation": "CCleaner and similar tools erase logs and temporary files to hide attacker activity."
         },
        {
             "question": "True or False: Rootkits operate only at the application level.",
            "options": [
                 "True",
                "False"
            ],
             "answer": "False",
            "explanation":"Rootkits can operate at kernel, hardware, or hypervisor levels to hide malicious activity."
        }
    ]

    if 'score' not in st.session_state:
        st.session_state.score = 0

    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        st.write(q["question"])
        selected = st.radio("Choose an answer:", q["options"], key=f"q{i}", index=None)
        
        if st.button("Check Answer", key=f"btn{i}"):
            if selected == q["answer"]:
                st.session_state.score += 1
                st.success("Correct!")
            else:
                st.error(f"Incorrect. Correct answer: {q['answer']}")
            with st.expander("Explanation"):
                st.write(q["explanation"])
            st.write("---")

    st.header("Results")
    st.write(f"Final Score: {st.session_state.score}/{len(questions)}")

if __name__ == "__main__":
    main()