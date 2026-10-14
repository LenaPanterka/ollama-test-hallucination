import sys

import ollama
import re


MODEL = "llama3.2:latest"

def normalize(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text


def get_model_answer(question: str) -> str:
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
    )

    return response["message"]["content"].strip()


def main() -> None:
    if len(sys.argv) != 3:
        print(
            'Использование: python check_hallucination.py '
            '"вопрос" "правильный ответ"'
        )
        return

    question = sys.argv[1]
    correct_answer = sys.argv[2]

    model_answer = get_model_answer(question)

    print(f"Вопрос: {question}")
    print(f"Правильный ответ: {correct_answer}")    
    print(f"Ответ модели: {model_answer}")

    if normalize(correct_answer) in normalize(model_answer):
        print("Правильный ответ")
    else:
         print("Галлюцинация")
         
if __name__ == "__main__":
    main()