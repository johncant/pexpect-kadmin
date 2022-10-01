
class MITUtils:
    def remove_prompt(self, text):
        if len(text) == 0:
            return text
        elif text[-1].strip() == "kadmin.local:":
            return text[:-1]
        elif text[-1].strip() == "kadmin:":
            return text[:-1]
        else:
            return text
