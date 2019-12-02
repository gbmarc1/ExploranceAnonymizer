from argparse import ArgumentParser
from pathlib import Path

import pandas as pd
import spacy
from tqdm import tqdm


def get_parser():
    parser = ArgumentParser()
    parser.add_argument("--file", type=Path)
    return parser


def replace_entities(text, ents):
    new_text = ''
    start = 0
    for e in sorted(ents, key=lambda x: x.start):
        new_text += text[start:e.start_char] + '<' + e.label_ + '>'
        start = e.end_char

    new_text += text[start:]
    return new_text


def anonymize(data):
    nlp = spacy.load("en_core_web_sm")
    anonimized_data, entities, raw_data = [], [], []
    valid_entities = ['PERSON']

    for d in tqdm(data.iloc[:, 0]):
        raw_data.append(d)
        doc = nlp(d, disable=["tagger", "parser"])
        ents = [e for e in doc.ents if e.label_ in valid_entities]
        anonimized_data.append(replace_entities(d, ents))
        entities.append(str([((e.start, e.end), e.text+'->'+e.label_) for e in ents]))

    return pd.DataFrame(
        {"Raw": raw_data, "Anonymized": anonimized_data, "Entities": entities}
    )


def main(args):

    args = get_parser().parse_args(args)
    data = pd.read_csv(args.file, header=None)
    data = anonymize(data)
    data.to_csv(args.file.parent/('anonymized_'+args.file.name), index=False)


if __name__ == "__main__":
    main(None)
