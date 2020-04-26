from src.errors_handler import ErrorsHandler
from src.translations_reader import *

if __name__ == '__main__':
    translation_outputs = read_files(r"D:\lingo\examples\reference.txt", r"D:\lingo\examples\hypothesis.txt")
    # translation_outputs = read_conllu_outputs(r"D:\lingo\examples\conllu ref.txt", r"D:\lingo\examples\conllu hyp.txt")
    translation_errors = ErrorsHandler()
    errors = translation_errors.get_errors(translation_outputs)
    print(errors)
