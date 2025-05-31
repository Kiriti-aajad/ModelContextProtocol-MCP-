from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class GPT2Handler:
    def __init__(self, model_name="gpt2", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name).to(self.device)
        
        # GPT2 tokenizer has no pad token by default; set it to eos token for padding
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

    def generate(self, prompt, max_length=50, temperature=1.0, do_sample=True):
        inputs = self.tokenizer(prompt, return_tensors="pt", padding=True).to(self.device)
        outputs = self.model.generate(
            **inputs,
            max_length=max_length,
            temperature=temperature,
            do_sample=do_sample,
            pad_token_id=self.tokenizer.pad_token_id,
            eos_token_id=self.tokenizer.eos_token_id,
            no_repeat_ngram_size=2,
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage:
if __name__ == "__main__":
    handler = GPT2Handler()
    print(handler.generate("Write SQL query to  to display table tbl_LTV_COL_FAC_DA."))
