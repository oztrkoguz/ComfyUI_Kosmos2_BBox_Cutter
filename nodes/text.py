class Write:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
        "required": {
                "input_text": ("STRING",{"multiline": True,"default": "",},),
            },
        }
    RETURN_TYPES = ("STRING",)

    FUNCTION = "simple_text"

    CATEGORY = "Kosmos2 Nodes/Write"

    def simple_text(self, input_text):

        return (input_text, )

NODE_CLASS_MAPPINGS = {
    "Write": Write
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Write": "Simple Text"
}