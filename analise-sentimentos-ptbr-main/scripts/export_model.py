from pathlib import Path

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC


def main() -> None:
    texts = [
        "Adorei o atendimento, foi rapido e eficiente.",
        "Produto excelente, superou minhas expectativas.",
        "Muito bom, recomendo para todo mundo.",
        "Entrega chegou antes do prazo, fiquei feliz.",
        "Servico de qualidade, voltarei a comprar.",
        "Interface facil e intuitiva, gostei bastante.",
        "Experiencia positiva do inicio ao fim.",
        "Aplicativo otimo, funcionou sem problemas.",
        "Estou satisfeito com o resultado final.",
        "Time de suporte resolveu tudo rapidamente.",
        "Atendimento impecavel, equipe muito atenciosa.",
        "Experiencia maravilhosa, tudo deu certo.",
        "Compra tranquila e sem dor de cabeca.",
        "Recebi exatamente o que foi prometido.",
        "Qualidade excelente, valeu cada centavo.",
        "Muito satisfeito com a plataforma.",
        "Suporte respondeu rapido e resolveu meu caso.",
        "Produto muito bom e facil de usar.",
        "Gostei bastante do resultado entregue.",
        "Foi uma experiencia positiva e confiavel.",
        "Pessima experiencia, nao recomendo.",
        "Atendimento ruim e demorado.",
        "Produto veio com defeito e sem suporte.",
        "Muito frustrante, perdi meu tempo.",
        "Servico horrivel, qualidade muito baixa.",
        "Aplicativo travou varias vezes, odiei.",
        "Nao gostei, esperava muito mais.",
        "Entrega atrasou e veio item errado.",
        "Plataforma confusa e cheia de erros.",
        "Suporte ignorou meu problema completamente.",
        "Que atendimento pessimo, fiquei decepcionado.",
        "Experiencia terrivel, nada funcionou direito.",
        "Sistema instavel e cheio de falhas.",
        "Nao resolveu meu problema, fiquei irritado.",
        "Pior compra que ja fiz.",
        "Demorou demais e ainda veio incompleto.",
        "Prometeram muito e entregaram pouco.",
        "Aplicativo ruim, lento e confuso.",
        "Suporte despreparado e sem empatia.",
        "Nao vale o preco cobrado.",
    ]
    labels = [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]

    pipeline = Pipeline(
        steps=[
            ("tfidf", TfidfVectorizer(lowercase=True, ngram_range=(1, 2))),
            ("classifier", LinearSVC(random_state=42)),
        ]
    )

    pipeline.fit(texts, labels)

    output_path = Path(__file__).resolve().parent.parent / "models" / "sentiment_pipeline.joblib"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, output_path)

    print(f"Model exported successfully to: {output_path}")


if __name__ == "__main__":
    main()
