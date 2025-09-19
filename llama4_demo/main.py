
from llama_models.llama4.generation import Llama4
from llama_models.llama4.datatypes import LLMInput

def main():
    import sys
    import readline  # für bessere Eingabe (Pfeiltasten, History)

    ckpt_dir = "llama_models/llama4/"
    max_seq_len = 2048
    max_batch_size = 1

    llama = Llama4.build(
        ckpt_dir=ckpt_dir,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size
    )

    print("Ey, willkommen bei Llama 4! 😎 Was geht, Bruder? Tipper deine Frage ein (oder 'quit' zum Abgang):\n")
    while True:
        try:
            prompt = input("🦙 Yo, was geht? Was willst du wissen? > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nHau rein, bleib stabil! ✌️")
            break
        if prompt.lower() in {"quit", "exit", "q"}:
            print("Hau rein, bleib stabil! ✌️")
            break
        if not prompt:
            print("Ey, schreib mal was rein!")
            continue
        tokens = llama.tokenizer.encode(prompt, bos=True, eos=False)
        llm_input = LLMInput(tokens=tokens)
        print("\nLlama haut jetzt was raus für dich:")
        for result in llama.generate([llm_input]):
            print("🦙💬:", llama.tokenizer.decode(result[0].tokens))

if __name__ == "__main__":
    main()
