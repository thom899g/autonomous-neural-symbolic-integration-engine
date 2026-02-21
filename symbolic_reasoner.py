class SymbolicReasoner:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def extract_symbols(self, data):
        try:
            symbols = []
            for item in data:
                if isinstance(item, tuple) and len(item) == 2:
                    symbols.append((item[0].lower(), item[1]))
            return symbols
        except Exception as e:
            raise ValueError(f"Symbol extraction failed: {str(e)}")

    def reason(self, neural_output):
        try:
            # Mock reasoning logic; replace with actual symbolic reasoning
            if neural_output is not None and all(v > 0.5 for v in neural_output):
                return "Positive inference"
            else:
                return "Negative inference"
        except Exception as e:
            raise ValueError(f"Reasoning failed: {str(e)}")