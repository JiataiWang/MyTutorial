import torch
from transformers.models.mixtral import MixtralConfig, MixtralModel
    
mixtralconfig = MixtralConfig(
    vocab_size=3200,
    hidden_size=2048,
    intermediate_size=14336//2
)
mixtral = MixtralModel(config=mixtralconfig)
inputs_ids = torch.randint(
            low=0, high=mixtralconfig.vocab_size, size=(4, 30)
        )
res = mixtral(inputs_ids)
print(res)

pass
