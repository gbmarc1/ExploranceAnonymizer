from PyInstaller.utils.hooks import collect_data_files
import spacy

# add datas for spacy
datas = collect_data_files('spacy', False)

# append spacy data path
datas.append((spacy.util.get_data_path(), 'spacy/data'))
datas.extend(collect_data_files('thinc.neural', False))

hiddenimports=['cymem', 'cymem.cymem', 'thinc.linalg', 'murmurhash', 'murmurhash.mrmr', 'spacy.strings',
'spacy.morphology', 'spacy.tokens.morphanalysis', 'spacy.lexeme', 'spacy.tokens', 'spacy.tokens.underscore', 'spacy.parts_of_speech', 'spacy.tokens._retokenize', 'spacy.syntax', 'spacy.syntax.stateclass',
'spacy.syntax.transition_system', 'spacy.syntax.nonproj', 'spacy.syntax.nn_parser', 'spacy.syntax.arc_eager', 'thinc.extra.search',
'spacy.syntax._beam_utils', 'spacy.syntax.ner', 'thinc.neural._classes.difference', 'srsly.msgpack.util', 'preshed',
'preshed.maps', 'thinc.neural', 'thinc.neural._aligned_alloc', 'thinc', 'thinc.neural._custom_kernels', 'blis',
'blis.py', 'spacy.vocab', 'spacy.lemmatizer', 'spacy._align', 'spacy.util',
'spacy.lang', 'spacy.syntax._parser_model', 'spacy.matcher._schemas', 'spacy.kb', 'en_core_web_sm', 'spacy.lang.en']